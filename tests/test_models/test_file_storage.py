#!/usr/bin/python3
"""
Unittest for file_storage([..])
"""
import unittest
from models.base_model import BaseModel
base_model = __import__('base_model').__init__


class TestFileStorage(unittest.TestCase):
    """
    Test for FileStorage class
    """
