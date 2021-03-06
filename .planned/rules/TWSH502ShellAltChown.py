from ansiblelint import AnsibleLintRule

class ShellAltChown(AnsibleLintRule):
    id = 'TWSH502'
    shortdesc = 'Use chown module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if 'chown' in task['action']['__ansible_arguments__']:
            return True
        return False
