#!/usr/local/bin/python3
import os
import argparse

# This script sets up ansible playbooks folder structures, as per;
# http://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html

# Set's up '-h' flag and populates with information.
parser=argparse.ArgumentParser(
        description='''This script sets up an ansible playbook folder structure as per the best practices prescribed by RedHat.''')
parser.add_argument('--role', default='common', help='Enter the name of a new role you would like to initialize' )
args=parser.parse_args()

# Directory's which exist at the base level of the playbooks directory.
dir_list = ["group_vars", "host_vars", "library", "module_utils", "filter_plugins",]

# Directory's which are nested inside a role.
dir_nest = ["roles/common/tasks","roles/common/handlers","roles/common/templates","roles/common/files","roles/common/vars","roles/common/defaults","roles/common/meta","roles/common/library","roles/common/module_utils","roles/common/lookup_plugins"]


# Create parent folders
for d in dir_list:
  if not os.path.exists(d):
      os.makedirs(d)

# Create nested folders
for n in dir_nest:
    if not os.path.exists(n):
        os.makedirs(n)
