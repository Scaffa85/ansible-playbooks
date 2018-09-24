#!/usr/local/bin/python
import os

# This script sets up ansible playbooks folder structures, as per;
# http://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html

dir_list = ["group_vars", "host_vars", "library", "module_utils", "filter_plugins",]

dir_nest = ["roles/common/tasks","roles/common/handlers","roles/common/templates","roles/common/files","roles/common/vars","roles/common/defaults","roles/common/meta","roles/common/library","roles/common/module_utils","roles/common/lookup_plugins"]


# Create parent folders
for d in dir_list:
  if not os.path.exists(d):
      os.makedirs(d)

# Create nested folders
for n in dir_nest:
    if not os.path.exists(n):
        os.makedirs(n)
