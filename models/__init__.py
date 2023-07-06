#!/usr/bin/python3
"""Unique File Storage Instance for app 
    - Creates an instance of File Storage class
    - Load the object form the file
    """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
