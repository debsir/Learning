#!/usr/bin/python

import os

class diskwalk(object):
    """API for getting directory walking collections"""
    def __init__(self, path):
        self.path = path

    def enumeratepaths(self):
        """Returns the path to all the files in a directory recursively"""
        path_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                fullpath = os.path.join(dirpath, file)
                path_collection.append(fullpath)
        return path_collection
    
    def enumeratefiles(self):
        """Returns the files in a directory as a list"""
        file_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                file_collection.append(file)
        return file_collection
    
    def enumeratedir(self):
        """Returns all the directories in a dirctory as a list"""
        dir_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for dir in dirnames:
                dir_collection.append(dir)
        return dir_collection
    
    if __name__ == "__main__":
        print "\nRecursive listing of all paths in a dir:"
        for path in enumeratepaths():
            print path
        print "\nRecursive listing of all files in dir:"
        for file in enumeratefiles():
            print file
        print "\nRecursive listing of all dirs in dir:"
        for dir in enumeratedir():
            print dir






















