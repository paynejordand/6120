#!/usr/bin/env python3

import sys, os, getopt

def usage():
  print(f"Usage: python {os.path.basename(__file__)} " \
        " --outstruct=?\n" \
        "   outstructt: The structure of the output file")

def catDATFile(infile,df,ct,outstruct):
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

  for line in linelist:
    entry = line.split(' ')

    # get line elements
    t = entry[0]
    x = entry[1]
    y = entry[2]
    mag = entry[6]
    amp = entry[7]
    dur = entry[8]

    # str = "%s,%s,%s,%s,%s,%s" % ( \
    #                      subj, \
    #                      shot, \
    #                      mag, \
    #                      amp, \
    #                      dur, \
    #                      t)
    str = ""
    for _,v in outfile.items():
      str += f"{v},"
    str = f"{str[:-1]},{mag},{amp},{dur},{t}"
    print(str, file=df)
    ct += 1

  return ct

###############################################################################
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
  # clear out output file
  df = open("sacc.csv",'w')
  header = ""
  for item in outstruct:
    header += f"{item},"
  header += "mag,amp,dur,timestamp"
  print(header, file=df)

  dir = './data/'

  # find all files in dir with .csv extension
  lst = [a for a in os.listdir(dir) if a.endswith('-sacc.dat')]

  lineno = 1

  for item in lst:

    if "VALIDATION" in item:
      continue

    file = dir + item
    print('Processing ', file)

    if os.path.getsize(file) == 0:
      continue

    # cat csv files into one
    lineno = catDATFile(file,df,lineno,outstruct)

  df.close()

if __name__ == "__main__":
  main(sys.argv[1:])