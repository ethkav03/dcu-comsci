class Student(object):
    def set_attributes(self, sid, name, modlist):
        self.name = name
        self.sid = sid
        self.modlist = modlist

    def print_attributes(self):
        print(f'ID: {self.sid}')
        print(f'Name: {self.name}')
        print(f"Modules: {(', '.join(self.modlist)).strip(',')}")

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)
