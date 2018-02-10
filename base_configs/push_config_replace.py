#!/usr/bin/env python2.7

import napalm_base
from napalm import get_network_driver
import os
import sys

conf_files = []

# Usage: ./push_config_replace.py <labname>
# Labname is DC_LAB, BB_LAB, etc

# Get list of config files
conf_path = '%s/CONFIGS' % sys.argv[1]

for dirname, dirnames, filenames in os.walk(conf_path):
  for filename in filenames:
    conf_files.append(filename)

print "Will apply new configs to the following devices:"
for c in conf_files:
  print "  %s" % c

for conf in conf_files:
  try:
    print "Applying config to %s..." % conf
    hostname = conf.replace('.conf', '')
    if conf[:4] == 'eos-':
      driver = get_network_driver('eos')
    elif conf[:3] == 'vmx':
      driver = get_network_driver('junos')
    else:
      print "Ignoring file %s - invalid type" % conf
  
    device = driver(hostname, 'ntc', 'ntc123')
    device.open()

    device.load_replace_candidate(filename='%s/%s' % (conf_path, conf))

    print "--- DIFF ---"
    print device.compare_config()
    device.commit_config()

    device.close()
  except napalm_base.exceptions.ConnectionException as e:
    print "Failed to connect to host %s: %s" % (conf, e)
  
