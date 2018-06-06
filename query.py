#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys,getopt,subprocess


def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h,v,p,q", ["help","version","path"])
    # parse command line options
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
     

    for o, a in opts:
      if o in ("-h", "--help"):
            print "        this is software that how can use it    "
            print "-v for display the version of this software"
            print "-p for display the information of this path"
            print "-q 查找最大目录或文件"
            sys.exit(0)
      elif o in ("-v","--version"):
            print "version 1.0.0.0"
            sys.exit(0)
      elif o in ("-p","--path"):
             p = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE)
             out = p.stdout.readlines()
             print out.pop()
             sys.exit(0)
      elif o in ("-q"):
             os.system("ncdu /")
             sys.exit(0)
    # process arguments
    for arg in args:
        process(arg) # process() is defined elsewhere

if __name__ == "__main__":
    main()
