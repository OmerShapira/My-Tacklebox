
import os
import sys

"""
This module shall contain put/pop actions
"""

def put(cl_args):
    '''
    If destination path is alrady specified:
        * if never been used, verify it's correct
        * otherwise, proceed to execute
    Else:
        * EXIT, ask for directory
    '''
    pass

def pop(cl_args):
    pass


def collect(cl_args):
    pass 

class file_replacement_op:
    def __init__(self, source_dir, backup_dir):
        pass
    
    def exec(self):
        """
        check if folder can accept files
        check if folder needs backup
        check write permissions
        acquire locks
        backup
        place new files
        """
        pass

    def move_to_backup(self):
        pass
    
     
