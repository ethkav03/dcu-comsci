from cmd import Cmd
import os
import time
from pwd import getpwuid

class MyPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
    
        print ("Hello, %s" % name)

    def do_ls(self, args):
        """Lists all files/directories inside the specified path, or all files/directories in current directory if no path specified."""
        if len(args) == 0:
            path = '.'
            files = os.listdir(path)
            print(" ".join(files))
        else:
            if args == '-l':
                path = '.'
                files = os.listdir(path)

                for name in files:
                    full_path = os.path.join(path, name)
                    inode = os.stat(full_path)
                    ctime = os.path.getctime(full_path)
                    creator = getpwuid(os.stat(name).st_uid).pw_name
                    mode = str(oct(inode.st_mode))[2:]
                    print(f"{mode} {creator} {inode.st_size:>4} {time.ctime(ctime)} {name}")
            else:
                files = os.listdir(path)
                print(" ".join(files))
        
                

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


prompt = MyPrompt()
prompt.prompt = '$ '
prompt.cmdloop('Starting prompt...')