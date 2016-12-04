"""Tacklebox v0.01
Written by Omer Shapira"""


# TODO (OS): Change to toml

import os
import errno
import ConfigParser
from src.FileWrapper import UserConfigFolder

class config_file:

	def __init__(self):
		user_dir = os.path.expanduser("~")
		self.home_folder_path = os.path.join(user_dir, '.tacklebox')
        self.config_file_path = os.path.join(self.home_folder_path, 'config.tacklebox')
        self.config_parser = ConfigParser.ConfigParser()

	def __enter__(self):
		self.config_parser.read(self.config_file_path)
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type is not None:
            #TODO (OS): handle the error
			print exc_type, exc_value, traceback
		try:
			if not os.path.exists(self.config_file_path):
				print ("Creating configuration file at " + str(self.config_file_path))
                # os.makedirs(self.home_folder_path)
			else:
				print ("Writing configuration file at " + str(self.config_file_path))
			with open(self.config_file_path, 'w') as file_handle:
				self.config_parser.write(file_handle)
		except E:
            if E.errno != errno.EEXIST: #we're ok with the path existing
                raise

		return self

	def set(self, section, option, arg):
 		if not self.config_parser.has_section(section):
			self.config_parser.add_section(section)
		self.config_parser.set(section, option, arg)

	def get(self,section,option):
		return self.config_parser.get(section, option)


def config(args):
	'''Handle the 'config' command'''
    # Check if path exists
	if not os.path.exists(args.path):
		exit("Path does not exist: " + args.path )

	path = os.path.realpath(args.path)

	if not os.path.exists(os.path.join(path, ".git")):
		exit("No git repository at " + path)

    config_folder = UserConfigFolder()
# Check user folder access
# using os.access(file)
# Check if backups exist there
# If yes, archive (add a .n number at end) by default


# Then create new file
	with config_file() as f:
		f.set("Repository", "Path", path)
	return

