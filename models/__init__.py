#!/usr/bin/python3
""" init module entry point """


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
