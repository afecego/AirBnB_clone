#!/usr/bin/python3
"""Creat class review"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """class review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
