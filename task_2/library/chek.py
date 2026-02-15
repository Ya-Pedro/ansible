#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

def main():
    module_args = dict(
        port=dict(type='int', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    port = module.params['port']
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    if 1 <= port <= 65535:
        result['message'] = f"Port {port} is valid and ready to be used."
        module.exit_json(**result)
    else:
        module.fail_json(msg=f"Port {port} is invalid. Must be between 1 and 65535.", **result)

if __name__ == '__main__':
    main()
