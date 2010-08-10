#!/usr/bin/env python
"""
USAGE:
    ./upload.py file.json

NOTE:
    This doesn't work, never has.
"""

import sys

import common.hyperparameters, common.options
HYPERPARAMETERS = common.hyperparameters.read("crowdflower")
HYPERPARAMETERS, options, args, newkeystr = common.options.reparse(HYPERPARAMETERS)

assert len(args) == 1       # Must pass one filename (JSON file) as arg

file_to_upload = args[0]

print >> sys.stderr, "Uploading file: %s" % file_to_upload


import urllib2_file
import urllib2
data = { 'form_name':    open(file_to_upload) }

u = urllib2.urlopen('http://api.crowdflower.com/v1/jobs/upload.json?key=%s' % HYPERPARAMETERS["API key"], data)
print u

