class Student(object):
    def __init__(self, sid, name, modlist=None):
        self.name = name
        self.sid = sid
        self.modlist = [] if modlist is None else modlist

    def add_module(self, mod):
        if mod not in self.modlist:
            self.modlist.append(mod)

    def del_module(self, mod):
        if mod in self.modlist:
            self.modlist.remove(mod)

    def __str__(self):
        a = []
        a.append('ID: {}'.format(self.sid))
        a.append('Name: {}'.format(self.name))
        a.append('Modules: {}'.format(', '.join(self.modlist)))
        return '\n'.join(a)
