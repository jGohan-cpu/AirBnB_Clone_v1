#!/usr/bin/python3
"""Unique File Storage Instance for app 
    - Creates an instance of File Storage class
    - Load the object form the file
    """
FileStorage = models.engine.file_storage.FileStorage

storage = FileStorage()
storage.reload()
