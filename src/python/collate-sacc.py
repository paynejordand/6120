#!/usr/bin/env python3

import sys, os, math

def catDATFile(infile,df,ct):
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
  subj = filename.split('-')[0]
  shot = filename.split('-')[1]
  print("subj, shot: ", \
         subj, shot)

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

    str = "%s,%s,%s,%s,%s,%s" % ( \
                         subj, \
                         shot, \
                         mag, \
                         amp, \
                         dur, \
                         t)
    print(str, file=df)
    ct += 1

  return ct

###############################################################################

# clear out output file
df = open("sacc.csv",'w')
print("subj,shot,mag,amp,dur,timestamp", file=df)


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
  lineno = catDATFile(file,df,lineno)

df.close()
