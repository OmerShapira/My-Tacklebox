import errno
import os
import toml
import consts

class FileWrapper:
    def __init__(self, path, mode, warn_if_created=False):
        self.path = os.path.realpath(path)
        self.dirname, self.filename = os.path.split(path)
        self.warn_if_created = warn_if_created
        self.mode = mode

    def ensure_path_exists(self):
        if os.path.exists(self.path):
            return
        try:
            os.makedirs(self.dirname)
        except IOError as E: #TODO (OS): not only possible error
            raise

    def touch(self):
        #TOOD (OS): Needed?
        if os.path.exists(self.path):
            return
        try:
            self.ensure_path_exists()
            handle = open(self.path)
            close(handle)
        except IOError as E:
            raise

    def __enter__(self):
        self.ensure_path_exists()
        if self.warn_if_created:
            print "Creating " + self.path
        self.handle = open(self.path, mode)
        return self.handle

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.handle.close()


class ConfigFile:
    def __init__(self, basepath, kind="bait"):
        self.path = basepath
        #Check if parent exists:
        # parent_path = os.path.realpath("../")

