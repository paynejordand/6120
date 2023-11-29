#!/usr/bin/env python3

import sys, os, math

def catCSVFile(infile,df,ct):
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

  # timestamp,x,y,duration,prev_sacc_amplitude
  TIMESTAMP = 0
  K = 1

  for line in linelist:
    entry = line.split(' ')

    # get line elements
    timestamp = entry[TIMESTAMP]
    k  = entry[K]

    str = "%s,%s,%s,%s" % ( \
                         subj, \
                         shot, \
                         timestamp,\
                         k)
    print(str, file=df)
    ct += 1

  return ct

###############################################################################

# clear out output file
df = open("amfo.csv",'w')
print("subj,shot,timestamp,K", file=df)

dir = './data/'

# find all files in dir with .csv extension
lst = [a for a in os.listdir(dir) if a.endswith('-amfo.dat')]

lineno = 1

for item in lst:

  file = dir + item
  print('Processing ', file)

  # cat csv files into one
  lineno = catCSVFile(file,df,lineno)

df.close()
