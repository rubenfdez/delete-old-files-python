#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from sys import argv
from os import path
import os, time, re, glob, fnmatch

if path.exists('script.conf') is False:
    print ('No existe el fichero script.conf donde se guardan las directivas')

with open('script.conf') as f:
	content = f.readlines()
	# Read the file and part the fields in strings by commas (Folder, Name file log, days, recursive)
	for section in content:
		section = section.strip()
		args_conf = section.split(',')
		folder = args_conf[0].strip()
		name_file = args_conf[1].strip()
		days = int(args_conf[2].strip())
		recursive = False
		# Conditional if the field "R" is in the configuration file
		if len(args_conf) > 3:
			recursive = args_conf[3].strip()
			# List dirs, subdirs and files
			for dirname, dirnames, filenames in os.walk(folder):
				for filename in filenames:
					# Test whether the filename string matches the name_file string
					if fnmatch.fnmatch(filename, name_file):	
						m = "%s/%s" % (dirname, filename)						
						age = int(days)*86400
						now = time.time()
						modified = os.stat(m).st_mtime
						if modified < now - age:
							#os.remove(m)
							print 'Deleted: %s' % m
		else:
			for dirname1, dirnames1, filenames1 in os.walk(folder):
				# List files
				for filename1 in filenames1:
					# Test whether the filename string matches the name_file string
					if fnmatch.fnmatch(filename1, name_file):
						n = "%s/%s" % (folder, filename1)
						age = int(days)*86400
						now = time.time()
						modified = os.stat(n).st_mtime
						if modified < now - age:
							#os.remove(n)
							print 'Deleted: %s' % n
