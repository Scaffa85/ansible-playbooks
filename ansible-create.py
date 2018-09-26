#!/usr/local/bin/python
import os
import argparse

# This script sets up ansible playbooks folder structures, as per;
# http://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html

# Set's up '-h' flag and populates with information.
parser=argparse.ArgumentParser(
        description='''This script sets up an ansible playbook folder structure as per the best practices prescribed by RedHat.''')
parser.add_argument("--role", action="store", default="common", dest="role", help="Enter the name of a new role you would like to initialize" )
args=parser.parse_args()

args=str(args.role)

# Directory's which exist at the base level of the playbooks directory.
dir_list = ["group_vars", "host_vars", "library", "module_utils", "filter_plugins",]

# Directory's which are nested inside a role.
dir_nest = ["roles/"+ args +"/tasks","roles/"+ args +"/handlers","roles/"+ args +"/templates","roles/"+ args +"/files","roles/"+ args +"/vars","roles/"+ args +"/defaults","roles/"+ args +"/meta","roles/"+ args +"/library","roles/"+ args +"/module_utils","roles/"+ args +"/lookup_plugins"]


# Create parent folders
for d in dir_list:
  if not os.path.exists(d):
      os.makedirs(d)

# Create nested folders
for n in dir_nest:
    if not os.path.exists(n):
        os.makedirs(n)
