#!/usr/bin/env python3

import sys,os,getopt,glob
import locale
import numpy as np
import math
from tqdm import tqdm
import csv
import h5py
import tables

def usage():
  print("Usage: python hdf52raw.py " \
        " --indir=? -outdir=?\n" \
        " --width=? -height=?\n" \
        " --file=?\n" \
        "   indir: a directory containing input files to be processed\n" \
        "   outdir: a directory containing output files\n" \
        "   width: horiz. gaze coord extents\n" \
        "   height: vert. gaze coord extents\n" \
        "   file: a single file to process\n")

def gettimings(infile):

  infile = infile.replace('\\','/')

  base = os.path.basename(infile)
  dname = os.path.dirname(infile)
  print("Processing: ", infile, "[", base, "]", "<", dname, ">")

  # strip out extension
  filename, ext = os.path.splitext(base)
  print('Processing: ' + filename)

  # csvfile (expected)
  incsvfile = dname + '/' + filename + '.csv'

  if os.path.isfile(incsvfile):
    print('csv file: ' + incsvfile + ' exists')
    # utf-8-sig encoding removes leading '\ufeff'
    csvfile = open(incsvfile,newline='',encoding='utf-8-sig')
    # get number of rows, skipping header
    nrows = sum(1 for _ in csvfile) - 1
    print("nrows: ",nrows)
    csvfile.seek(0)
    csvrows = csv.DictReader(csvfile,delimiter=',')
    # print header
#   print("header: ",csvrows.fieldnames)
  else:
    print('csv file: ' + incsvfile + ' does NOT exist')

  stim = 'None'
  st = 0.0
  et = math.inf

# row = next(csvrows)
# for i, row in enumerate(csvrows):
  csvlist = list(csvrows)
  for i, row in enumerate(csvlist):

#   print("row[%d]" % (i))

#   if i > 0:
#     print("previous row: ",csvlist[i-1])

#   if row['stim'] is '':
#     print("row['stim']:",row['stim']," empty")
#   else:
#     print("row['stim']:",row['stim'])

#     if int(row['stimulus_loop.thisTrialN']) == 0:
#       st = row['image.started']
#     if int(row['stimulus_loop.thisTrialN']) > 0:
#       et = row['image.started']

#   if row['stimulus_loop.thisTrialN'] is not '' and \
#   if row['stimulus_loop.thisTrialN'].isdigit():

    if 0 < i and i < len(csvlist)-1:
      stim = row['stim']
      st = row['image.started']
      et = csvlist[i+1]['image.started']
    elif i == len(csvlist)-1:
      stim = row['stim']
      st = row['image.started']
      et = math.inf

    if 0 < i:
      print("[",i,"]: ",stim,st,et)

  csvfile.close()

# convert csv file to raw
def hdf52raw(infile,outdir,width,height,dist,outstruct):

  try:
    h5file = tables.open_file(infile,mode='r')
  except IOError:
    print("Can't open file with tables.open_file: " + infile)
    return

  infile = infile.replace('\\','/')

  # parse the subject name from the file name
# base = infile[:infile.rfind('.')]
  base = os.path.basename(infile)
  dname = os.path.dirname(infile)
  print("Processing: ", infile, "[", base, "]", "<", dname, ">")

  # strip out extension
  filename, ext = os.path.splitext(base)
  print('Processing: ' + filename)

  # subj id from filename
  subj = filename.split('_')[0]
  print('subj: ', subj)

  ################ open csv file

  # csvfile (expected)
  incsvfile = dname + '/' + filename + '.csv'

  if os.path.isfile(incsvfile):
    print('csv file: ' + incsvfile + ' exists')
    # utf-8-sig encoding removes leading '\ufeff'
    csvfile = open(incsvfile,newline='',encoding='utf-8-sig')
    # get number of rows, skipping header
#   nrows = sum(1 for _ in csvfile) - 1
#   print("nrows: ",nrows)
    csvfile.seek(0)
    csvrows = csv.DictReader(csvfile,delimiter=',')
    csvlist = list(csvrows)
    # print header
#   print("header: ",csvrows.fieldnames)
  else:
    print('csv file: ' + incsvfile + ' does NOT exist')

  outfile = None


  ################ open HDF5 file

  # processing hdf5 file using pytables
# print("h5file: ", h5file)

  # find session_data_data...
  metatable = h5file.root.data_collection.session_meta_data
  # print("metatable: ", metatable)

  # first use class_table_mapping to get at paths to various datasets
  pathtable = h5file.root.class_table_mapping
# print("pathtable: ",pathtable)
# for rec in pathtable.iterrows():
#   print("rec['table_path']: ", rec['table_path'].decode('utf-8'))
# bespath = [rec['table_path'] for rec in \
#           pathtable.where("""(class_name == 'BinocularEyeSampleEvent')""")]
# print("bespath: ", bespath)

  # from https://www.pytables.org/usersguide/tutorials.html
  # rows in class_table_mapping table give us path to other data objects

  # find gaze data...
  # in theory there may be more than one such node but not likely in practice
# for record in pathtable.where('(class_name == b"BinocularEyeSampleEvent")'):
  for record in pathtable.where('(class_name == b"GazepointSampleEvent")'):
    # pull out row from class_table_mapping to GazepointSampleEvent node 
    bespath = record['table_path'].decode('utf-8')
    # get table
    bestable = h5file.get_node(bespath)
#   print("bestable: ", bestable)

  # this is if we manually add in code to issue messages in PsychoPy
  # find message data...
  # in theory there may be more than one such node but not likely in practice
  for record in pathtable.where('(class_name == b"MessageEvent")'):
    # pull out row from class_table_mapping to MessageEvent node 
    mespath = record['table_path'].decode('utf-8')
    # get table
    mestable = h5file.get_node(mespath)
#   print("mestable: ", mestable)

  # init vars
  stim = []
  st = []
  et = []
  conditions = {}
  units = "height"

  # this is if we manually add in code to issue messages in PsychoPy
  # process each pair of rows in message table: they contain start/end times
  for row in mestable.where('(category == "units")'):
    units = row["text"].decode("utf-8")
  
  # Changed this since I think would overwrite the start and end times for each trial
  for row in mestable.where('(category == "trial")'):
    # Couldn't find a way to check a substring for start in the text column. 
    # Could probably append start and end times here, rather than do two loops
    if ("start" not in str(row["text"])):
      continue
    st.append(row['time'])
    exp_id = row['experiment_id']
    ses_id = row['session_id']
  for row in mestable.where('(category == "trial")'):
    if ("stop" not in str(row["text"])):
      continue
    et.append(row['time'])
    exp_id = row['experiment_id']
    ses_id = row['session_id']

  # UNIQUE TO THIS PROJECT
  for row in mestable.where('(category == "original")'):
    img = row["text"].decode("utf-8")
    img = img.split("/")[3]
    img = img[:5]
    stim.append(img)
  
  
  # Assumes that all instances of cond have an equal amount of instances (e.g. once per trial)
  for cond in outstruct[2:]:
    for row in mestable.where('category == cond'):
      val = row["text"].decode("utf-8")
      
      conditions.setdefault(cond, []).append(val)
      # conditions[cond].append(row["text"].decode("utf-8"))

  # pull out date string from session_meta_data table with matching
  # experiment_id and session_id
  for row in metatable.where('(experiment_id == exp_id) & \
                                 (session_id == ses_id)' \
                            ):
    date = row['code'].decode('utf-8')
 
  print("exp_id: ", exp_id)
  print("ses_id: ", ses_id)
  print("st: ", st)
  print("et: ", et)
  print("date: ", date)

  # for number of trials here
  for i in range(len(stim)):
    print("stim, st, et: ",stim[i],st[i],et[i])

    if outfile is not None:
      outfile.close()

    # If there are conditions in our data we want to add those to the file name
    outfilename = f"{subj}-{stim[i]}"
    if conditions != {}:
      for _,cond in conditions.items():
        outfilename += f"-{cond[i]}"
    outfilename += ".raw"
    outfile = open(outdir + outfilename,'w+')
    print('Outfile: %s' % (outfilename))

    startTime = st[i]
    endTime = et[i]
    for row in bestable.where('(startTime <= time)  &  (time <= endTime)'):

      # see:
      # https://www.psychopy.org/api/iohub/device/eyetracker_interface/GazePoint_Implementation_Notes.html#psychopy.iohub.devices.eyetracker.BinocularEyeSampleEvent
      t = row['time']
      # gaze position in psychopy window in the window coord unit being used
      # (e.g., norm, height, pix, etc.)
      x_l = row['left_gaze_x']
      y_l = row['left_gaze_y']
      x_r = row['right_gaze_x']
      y_r = row['right_gaze_y']
      d_l = row['left_pupil_measure2']
      d_r = row['right_pupil_measure2']
      v = row['status']

      # height unit mapping [0,w,0,h] -> [-.5*(w/h),.5*(w/h),-.5,.5]
      # x' = ( (x - 0)/w -.5 )*(w/h)
      # y' = ( (y - 0)/h -.5 )*(h/h)

      # convert height units to normalized coords
      # [-.5*(h/w), .5*(h/w)] -> [0,1]
      if units == "height":
        x_l = (x_l * height/width + 0.5)
        x_r = (x_r * height/width + 0.5)

        # [-.5, .5] -> [0,1]
        y_l = (y_l * 1.0 + 0.5)
        y_r = (y_r * 1.0 + 0.5)

        # y-flip
        y_l = 1.0 - y_l
        y_r = 1.0 - y_r
      # pix unit mapping
      # x range [-width/2, width/2]
      # y range [-height/2, height/2] 
      elif units == "pix":
        x_l = (x_l / width) + 0.5
        x_r = (x_r / width) + 0.5
        # Normalize and flip in one line
        y_l = 1 - ((y_l / height) + 0.5) 
        y_r = 1 - ((y_r / height) + 0.5)

      x = (x_l + x_r)/2.0
      y = (y_l + y_r)/2.0
      d = (d_l + d_r)/2.0

      if(v < 6):
        strout = "%f %f %f %f" % (x,y,d,t)
        outfile.write(strout + '\n')

    if outfile is not None:
      outfile.close()

  h5file.close()

  return

def main(argv):
# if not len(argv):
#   usage()
  try:
    opts, args = getopt.getopt(argv, '', \
                 ['indir=','outdir=','file=',\
                  'width=','height=','dist=',\
                  'hertz=','sfdegree=','sfcutoff=',
                  'outstruct='])
  except getopt.GetoptError as err:
    usage()
    exit()

  file = None
  files = []
  indir = './'
  outdir = './'
  outstruct = 'subj-stim'

  for opt,arg in opts:
    opt = opt.lower()
    if(opt != '--file' and opt != '--indir' and opt != '--outstruct'):
      arg = arg.lower()

    if opt == '--indir':
      indir = arg
    elif opt == '--outdir':
      outdir = arg
    elif opt == '--width':
      width = float(arg)
    elif opt == '--height':
      height = float(arg)
    elif opt == '--dist':
      # convert distance to cm and then to mm
      dist = float(arg) * 2.54 * 10.0
    elif opt == '--outstruct':
      outstruct = arg
    else:
      sys.argv[1:]

  outstruct = outstruct.split("-")
  # get .hdf5 input files to process
  if os.path.isdir(indir):
#   files = glob.glob('%s/*.hdf5' % (indir))
    for top, dirs, listing in os.walk(indir):

#     print("top: %s" % (top))
#     print("dirs: %s" % (dirs))
#     print("listing: %s" % (listing))

      for file in listing:
        path = os.path.join(top,file)
        # get second-to-last path entry
        dname = path.split('/')[-2]
        base = os.path.basename(path)

#       print("path: %s" % (path))
#       print("dname: %s" % (dname))
#       print("base: %s" % (base))

        if base.endswith('.hdf5'):
          basename = base[:base.rfind('.hdf5')]
#         print path, top, dname, base, "[",basename,"]","[",file,"]"
          files.extend([path])

  # if user specified --file="..." then we use that as the only one to process
  if(file != None and os.path.isfile(file)):
    files = [file]

  # set up progress bar
# pbar = tqdm(total=len(files))

  for file in files:
#   gettimings(file)
    hdf52raw(file,outdir,width,height,dist,outstruct)
    # update progress bar
#   pbar.update(1)


#######################
#locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

if __name__ == "__main__":
  main(sys.argv[1:])
