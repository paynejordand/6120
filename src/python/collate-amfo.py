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
# header = linelist[0].split(',')
# linelist = linelist[1:]

  # timestamp,x,y,duration,prev_sacc_amplitude
  TIMESTAMP = 0
  K = 1

  for line in linelist:
    entry = line.split(' ')

    # get line elements
    timestamp = entry[TIMESTAMP]
    k  = entry[K]

    # str = "%s,%s,%s,%s" % ( \
    #                      subj, \
    #                      shot, \
    #                      timestamp,\
    #                      k)
    str = ""
    for _,v in outfile.items():
      str += f"{v},"
    str = f"{str[:-1]},{timestamp},{k}"
    
    print(str, file=df)
    ct += 1

  return ct

###############################################################################

def main(argv):
  # clear out output file
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

  df = open("amfo.csv",'w')
  header = ""
  for item in outstruct:
    header += f"{item},"
  header += "timestamp,K"
  print(header, file=df)

  dir = './data/'

  # find all files in dir with .csv extension
  lst = [a for a in os.listdir(dir) if a.endswith('-amfo.dat')]

  lineno = 1

  for item in lst:

    file = dir + item
    print('Processing ', file)

    # cat csv files into one
    lineno = catCSVFile(file,df,lineno,outstruct)

  df.close()

if __name__ == "__main__":
  main(sys.argv[1:])