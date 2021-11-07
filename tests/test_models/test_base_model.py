#!/usr/bin/python3
"""
Unittest for base_model([..])
"""
import unittest
from models.base_model import BaseModel
base_model = __import__('base_model').__init__


class Test__init__(unittest.TestCase):
    """
    Test for BaseModel class
    """
