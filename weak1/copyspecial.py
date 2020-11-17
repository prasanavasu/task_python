#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def extract_path(dirname):
  result = []
  paths = os.listdir(dirname)  # list of paths in that dir
  for fname in paths:

    match = re.search(r'__(\w+)__', fname)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, fname)))
  return result

def copy_dir(paths, to_dir):
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    fname = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, fname))

def zip(paths, zipfile):
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print ("Command I'm going to do:" + cmd)
  (status, output) = subprocess.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  try:
    paths = []
    for dirname in args:
      paths.extend(extract_path(dirname))

    if todir:
      copy_dir(paths, todir)
    elif tozip:
      zip(paths, tozip)
    else:
      print ('\n'.join(paths))
  except IOError:
    for dirname in args:
      sys.stderr.write(f'No such zip or directory : {dirname} \n ')  
if __name__ == "__main__":
  main()
