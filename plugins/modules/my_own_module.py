#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function
import os

__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates file

version_added: "1.0.0"

description: Module creates new file and adds content to it

options:
    name:
        description: This is the file name
        required: true
        type: str
    path:
        description: Path to the file
        required: true
        type: str
    content:
        description: File content
        required: false
        type: str

author:
    - Michael Yamshchikov
'''

EXAMPLES = r'''
- name: file creation
  my_namespace.my_collection.my_own_module:
    name: text.txt
    path: /tmp/
    content: Hello World!!
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'File successfully created'
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():

    module_args = dict(
        name=dict(type='str', required=True),
        path=dict(type='str', required=True),
        content=dict(type='str', required=False)
    )
    result = dict(
        changed=False,
        message='File already exists'
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    os.makedirs(module.params['path'], mode=0o755, exist_ok=True)
    if not os.path.exists(module.params['path'] + module.params['name']):
        with open(module.params['path'] + module.params['name'], 'w') as f:
            f.write(module.params['content'])
        result['changed'] = True
        result['message'] = 'File successfully created'
 
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
