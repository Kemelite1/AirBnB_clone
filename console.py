#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
        '''
        Contains the entry point of the command interpreter.
        '''
        prompt = "(hbnb) "
        
        def do_create(self, command):
                """the create command is to create a new class instance"""
                if not command:
                        print("** class name missing **")
                elif command == "BaseModel":
                        model = BaseModel()
                        print(model.id)
                        model.save()
                elif command != "BaseModel":
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
                elif arg[0] != "BaseModel":
                        print("** class doesn't exist **")
                        return
                
                storage.reload()
                stored = storage.all()
                try:
                        val = stored[f"BaseModel.{arg[1]}"]
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
                elif arg[0] != "BaseModel":
                        print("** class doesn't exist **")
                        return
                
                stored = storage.all()
                try:
                        stored[f"BaseModel.{arg[1]}"]
                except KeyError:
                        print("** no instance found **")
                        return
                
                del stored[f"BaseModel.{arg[1]}"]
                storage.save()
                
        def do_all(self, cl):
                """command prints out all existing model instaces"""
                if cl != "BaseModel":
                        print("** class doesn't exist **")
                        return
                stored = storage.all()
                for val in stored.values():
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
                elif arg[0] != 'BaseModel':
                        print("** class doesn't exist **")
                        return        
                stored = storage.all()
                try:
                        stored[f"BaseModel.{arg[1]}"]
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
                        val = stored[f"BaseModel.{arg[1]}"]
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