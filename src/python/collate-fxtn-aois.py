#!/usr/bin/env python3

import sys, os, getopt

def usage():
  print(f"Usage: python {os.path.basename(__file__)} " \
        " --outstruct=?\n" \
        "   outstructt: The structure of the output file")

def catCSVFile(infile,df,ct,outstruct):
  try:
    f = open(infile,'r')
  except IOError:
    print("Can't open file: " + infile)
    return

  path, base = os.path.split(infile)

  print("Processing: ", infile, "[", base, "]")

  # split filename from extension
  filename, ext = os.path.splitext(base)

  print("path, base, filename, ext: ", path, base, filename, ext)

  # extract stimulus name and subj id
  # filename now has the form 'date-rest_of_it', extract just the second part
  filename = filename.split("-")
  outfile = {}
  for i in range(len(outstruct)):
    outfile[outstruct[i]] = filename[i]
  
  dStrOne = ""
  dStrTwo = ""
  for k,v in outfile.items():
    dStrOne += f"{k},"
    dStrTwo += f"{v},"
  dStrOne = dStrOne[:-1]
  dStrTwo = dStrTwo[:-1]
  print(f"{dStrOne}: {dStrTwo}")

  # read lines, throwing away first one (header)
# linelist = f.readlines()
# linelist = f.read().split('\r')
  linelist = f.read().splitlines()
  header = linelist[0].split(',')
  linelist = linelist[1:]

  # timestamp,x,y,duration,prev_sacc_amplitude,aoi_label
  for idx, label in enumerate(header):
    if label.strip() == "timestamp":
      TIMESTAMP = idx
    if label.strip() == "x":
      X = idx
    if label.strip() == "y":
      Y = idx
    if label.strip() == "duration":
      DURATION = idx
    if label.strip() == "prev_sacc_amplitude":
      PREV_SACC_AMPLITUDE = idx
    if label.strip() == "aoi_span":
      AOI_SPAN = idx
    if label.strip() == "aoi_label":
      AOI_LABEL = idx
    if label.strip() == "aoi_order":
      AOI_ORDER = idx

  for line in linelist:
    entry = line.split(',')

    # get line elements
    timestamp = entry[TIMESTAMP]
    x  = entry[X]
    y  = entry[Y]
    duration  = entry[DURATION]
    prev_sacc_amplitude  = entry[PREV_SACC_AMPLITUDE]
    aoi_span  = entry[AOI_SPAN]
    aoi_label  = entry[AOI_LABEL]
    aoi_order  = entry[AOI_ORDER]

    # str = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % ( \
    #                      subj, \
    #                      exp_id, \
    #                      ses_id, \
    #                      marker, \
    #                      object, \
    #                      timestamp,\
    #                      x,y,\
    #                      duration,\
    #                      prev_sacc_amplitude,\
    #                      aoi_span,\
    #                      aoi_label,\
    #                      aoi_order,\
    #                      ct)
    str = ""
    for _,v in outfile.items():
      str += f"{v},"
    str = f"{str[:-1]},{timestamp},{x},{y},{duration}," \
          f"{prev_sacc_amplitude},{aoi_span},{aoi_label},{aoi_order},{ct}"
    print(str, file=df)
    ct += 1

  return ct

###############################################################################

# clear out output file
def main(argv):
  try:
    opts, args = getopt.getopt(argv, '', \
                 ['outstruct='])
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
    if(opt != '--file' and opt != '--indir'):
      arg = arg.lower()

    if opt == '--outstruct':
      outstruct = arg
    else:
      sys.argv[1:]
    
  outstruct = outstruct.split("-")

  df = open("fxtn-aois.csv",'w')
  header = ""
  for item in outstruct:
    header += f"{item},"
  header += "timestamp,x,y,duration,prev_sacc_amplitude,aoi_span,aoi_label,aoi_order,order"
  print(header, file=df)

  dir = './data/'

  # find all files in dir with .csv extension
  lst = [a for a in os.listdir(dir) if a.endswith('-fxtn-aoi.csv')]

  lineno = 1

  for item in lst:

    file = dir + item
    print('Processing ', file)

    # cat csv files into one
    lineno = catCSVFile(file,df,lineno,outstruct)

  df.close()

if __name__ == "__main__":
  main(sys.argv[1:])