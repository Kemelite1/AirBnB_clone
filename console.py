# #!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
        '''
        Contains the entry point of the command interpreter.
        '''
        prompt = "(hbnb) "
        
        def do_EOF(self, line):
                """EOF exits the program"""
                return True
        
        def do_quit(self, line):
                """quit command to exit the program"""
                return True
        
        
        
        
        
if __name__ == '__main__':
    """this is the main program loop it iterates on every command"""
    HBNBCommand().cmdloop()