#!/usr/bin/python3
"""
console module
"""
import cmd
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
        '''
        Contains the entry point of the command interpreter.
        '''
        prompt = "(hbnb) "

        cl = {'BaseModel': BaseModel, 
              'User': User,
              'State': State,
              'Place': Place,
              'Review': Review,
              'City': City,
              'Amenity': Amenity}

        def ccr(self, cll):
                """returns a class"""
                if cll in self.cl:
                        return self.cl[cll]
                
        def do_create(self, command):
                """the create command is to create a new class instance"""
                if not command:
                        print("** class name missing **")
                        return
                if command in self.cl:
                        model = self.ccr(command)()
                        print(model.id)
                        model.save()
                else:
                        print("** class doesn't exist **")
                
        def do_show(self, *args):
                """command displays a model based on the given id"""
                arg = args[0].split(' ')
                arg = [arg for arg in arg if arg != '']
                lent = len(arg)
                if lent == 0:
                        print("** class name missing **")
                        return
                elif lent == 1:
                        print("** instance id missing **")
                        return
                elif arg[0] not in self.cl:
                        print("** class doesn't exist **")
                        return
                
                storage.reload()
                stored = storage.all()
                try:
                        val = stored["{}.{}".format(arg[0],arg[1])]
                except KeyError:
                        print("** no instance found **")
                        return
                
                print(val)
                
                
                # elif arg[0] == "BaseModel":
                #         stored = storage.all()
                #         for val in stored.values():
                #                 try:
                                        
                                #     if val.id == arg[1]:
                                #         print(val)
                                #         return

                                    
        def do_destroy(self, *args):
                """comand destroys the given model instance"""
                arg = args[0].split(' ')
                arg = [arg for arg in arg if arg != '']
                lent = len(arg)
                if lent == 0:
                        print("** class name missing **")
                        return
                elif lent == 1:
                        print("** instance id missing **")
                        return
                elif arg[0] not in self.cl:
                        print("** class doesn't exist **")
                        return
                
                stored = storage.all()
                try:
                        stored["{}.{}".format(arg[0],arg[1])]
                except KeyError:
                        print("** no instance found **")
                        return
                
                del stored["{}.{}".format(arg[0],arg[1])]
                storage.save()
                
        def cmd_str_format(self, strng):
            dot_ind = strng.index('.')
            brkt_ind = strng.index('(')
            cl_name = strng[:dot_ind]
            cmd_name = strng[dot_ind:brkt_ind]
            brkt = strng[brkt_ind:]
            return [cmd_name[1:], cl_name, brkt]
        
        def precmd(self, arg):
            if len(arg.split('.')) > 1:
                cmds = self.cmd_str_format(arg)
                return '{} {}'.format(cmds[0],cmds[1])
            else:
                return arg
            
        def do_all(self, cl):
                """command prints out all existing model instaces"""
                if cl not in self.cl:
                        print("** class doesn't exist **")
                        return
                stored = storage.all()
                for val in stored.values():
                        if type(val).__name__ == cl:
                                print(val)  
        
        def do_update(self, *args):
                """command helps you add updates to an existing model instance"""
                arg = args[0].split(' ')
                arg = [arg for arg in arg if arg != '']
                lent = len(arg)

                if lent == 0:
                        print("** class name missing **")
                        return
                elif lent == 1:
                        print("** instance id missing **")
                        return
                elif arg[0] not in self.cl:
                        print("** class doesn't exist **")
                        return        
                stored = storage.all()
                try:
                        stored["{}.{}".format(arg[0],arg[1])]
                except KeyError:
                        print("** no instance found **")
                        return
                if lent == 2:
                        print("** attribute name missing **")
                        return
                elif lent == 3:
                        print("** value missing **")
                        return
                try:                       
                        val = stored["{}.{}".format(arg[0],arg[1])]
                except KeyError:
                        print("** no instance found **")
                        return
                key = arg[2]
                v = arg[3]
                setattr(val, key, v)
                val.save()                
                                            
        def do_EOF(self, line):
                """EOF exits the program"""
                return True
        
        def do_quit(self, line):
                """quit command to exit the program"""
                return True
        
        
        
        
        
if __name__ == '__main__':
    """this is the main program loop it iterates on every command"""
    HBNBCommand().cmdloop()
