#!/usr/bin/python3
"""unittest for the console.py"""
import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """unittest for the HBNB command line interpreter"""
    console = HBNBCommand()

    def test_quit(self):
        """Testing the quit command"""
        with patch('builtins.input', return_value="quit"):
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Testing the EndOfFile command"""
        with patch('builtins.input', return_value="EOF"):
            self.assertTrue(self.console.onecmd("EOF"))

if __name__ == '__main__':
    unittest.main()
