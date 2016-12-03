import errno
import os
import toml
import consts

import shutil #used for rmtree

class FileWrapper(object):
    def __init__(self, path, mode, warn_if_created=False):
        self.warn_if_created = warn_if_created
        self.mode = mode
        self.set_path(path)

    def set_path(self, path):
        self.path = os.path.realpath(path)
        self.dirname, self.filename = os.path.split(path)

    def ensure_path_exists(self):
        if os.path.exists(self.dirname):
            return
        try:
            os.makedirs(self.dirname)
        except IOError as E: #TODO (OS): not only possible error
            raise

    def exists(self):
        return os.path.exists(self.path)

    def touch(self):
        #TODO (OS): Needed?
        if os.path.exists(self.path):
            return
        try:
            self.ensure_path_exists()
            handle = open(self.path)
            close(handle)
        except IOError as E:
            raise

    def delete(self):
        return os.remove(self.path)

    def rename(self, new_name):
        new_path = os.path.realpath (os.path.join( self.path, new_name ))
        if os.path.exists(new_path):
            raise Exception("Can't rename to existing file")
        if self.exists():
            os.rename(self.path, new_path)
        self.set_path(new_path)

    def __enter__(self):
        self.ensure_path_exists()
        if self.warn_if_created:
            print "Creating " + self.path
        self.handle = open(self.path, mode)
        return self.handle

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.handle.close()


class Folder(object):
    def __init__(self, path):
        if os.path.isfile(path):
            raise TypeError("% is a file")
        self.path = os.path.realpath(path)

    def exists(self):
        return os.path.exists(self.path) && os.path.isdir(self.path)

    def ensure_exists(self):
        if self.exists():
            return
        try:
            os.makedirs(self.path)
        except IOError as E:
            raise

    def rename(self, new_name):
        parent = os.path.join(self.path, os.pardir)
        new_path = os.path.realpath(os.path.join(parent, new_name))
        #check that nothing in the new name exists
        if new_path == self.path:
            return
        if os.path.exists(new_path):
            #TODO (OS): Not sure which exception to raise
            raise Exception("Path Exists")
        try:
            os.rename(self.path, new_path)
            self.path = new_path
        except IOError as E:
            raise

    def delete(self):
        return shutil.rmtree(self.path) 

    def child(self, name):
        return Folder(os.path.join(self.path, name))

    def parent(self):
        return Folder(os.path.realpath(os.path.join(self.path, os.pardir)))

    def child_names(self, dirs=True, files=True):
        raw =  os.listdir(self.path)
        if files && dirs:
            return raw
        l_files = [] if not files else [f for f in raw if os.path.isfile(f)]
        l_dirs  = [] if not dirs  else [d for f in raw if os.path.isdir(d)]
        return l_files + l_dirs


class UserConfigFolder(object):
    def __init__(self, path=None):
        path = os.path.expanduser(consts.USER_CONFIG_HOME)
        self.folder = Folder(path)
        self.backup_folder_name = consts.BACKUP_DIR_NAME + CONFIG_EXTENSION_CURRENT
        self.config_file_name = consts.USER_CONFIG_FILE_NAME

    def create(self):
        self.folder.ensure_exists()
        self.push_backup()
        self.folder.child(self.backup_folder_name).ensure_exists()
        #TODO (OS): Create config file

    def destroy(self):
        self.pop_backup()
        #TODO (OS): check if folder needs to be removed

    def push_backup(self):
        """
        If a backup folder exists, moves the configuration file into it,
        and upadtes the name to be the latest archived backup.
        Does not create new backup folder.
        """
        master = self.folder.child(self.backup_folder_name)
        if not master.exists():
            return
        #find latest
        next_archived_backup = self.find_latest_backup_number() + 1
        # move config file into backup folder
        # TODO (OS): move config file into backup
        archived_backup_folder_name = consts.BACKUP_DIR_NAME + "." + next_archived_backup
        master.rename(archived_backup_folder_name)

    def pop_backup(self):
        """
        If an archived folder exists, deletes the current backup folder and configuration file,
        and replaces them with the most recent archived backup and
        configuration file inside the archived backup.
        """
        archive_num = self.find_latest_backup_number()
        if archive_num == 0:
            return
        archived_backup_folder_name = consts.BACKUP_DIR_NAME + "." + archive_num
        archived_backup_folder = self.folder.child(archived_backup_folder_name)
        if not archived_backup_folder.exists():
            return
        # remove current setup
        self.folder.child(self.backup_folder_name).delete()
        # make the latest one "current"
        archived_backup_folder.rename(self.backup_folder_name)
        # will return false if can't complete

    def find_latest_backup_number(self):
        """
        Scans the backup folders to see if previous backups exist.
        Unable to detect different versions of file and folder.
        """
        names = [n for n in self.folder.child_names(files=False)
                    if (n.startswith(consts.BACKUP_DIR_NAME)
                    && not n.endswith(consts.CONFIG_EXTENSION_CURRENT))]
        highest_num = 0
        for name in names:
            #take last string beyond point
            numstr = name.split(".")[-1]
            try:
                highest_num = max(highest_num, int(numstr))
            except:
                pass
        return highest_num


class ConfigFile(object):
    def __init__(self, path):
        self.path = path

class BaitConfigFile(ConfigFile):
    def __init__(self, path):
        # Find if is local root
        super(BaitConfigFile, self).__init__(path)

class UserConfigFile(ConfigFile):
    '''refers to user config file only by name.
    performs atomic actions and keeps file closed.'''
    def __init__(self, config_folder)
        path = os.path.expanduser(consts.USER_CONFIG_HOME)
        super(UserConfigFile, self).init(self, path)
