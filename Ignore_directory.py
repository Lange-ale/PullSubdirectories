# a class that ignores the directory in the ignore_list.json
class Ignore_directory:

    def __init__(self):
        try:
            import json
            with open('ignore_list.json') as f:
                file = json.load(f)
            self.ignore_list = file['ignore_list']
        except:
            print('Error reading ignore_list.json')

    def is_ignored(self, directory):
        return directory in self.ignore_list

