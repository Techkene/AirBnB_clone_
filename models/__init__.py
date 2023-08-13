#!/usr/bin/python3
""" Importing Filestorage """
from models.engine.file_storage import FileStorage
from models.base_model import BaseMode
storage = FileStorage()
storage.reload()
