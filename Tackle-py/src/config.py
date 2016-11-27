"""Tacklebox v0.01
Written by Omer Shapira"""

import os
import ConfigParser

class config_file:

	def __init__(self):
		home_dir = os.path.expanduser("~")
		self.config_file_path = os.path.join(home_dir, '.tacklebox')
		self.config_parser = ConfigParser.ConfigParser()

	def __enter__(self):
		self.config_parser.read(self.config_file_path)
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type is not None:
			print exc_type, exc_value, traceback

		try:
			if not os.path.exists(self.config_file_path):
				print ("Creating configuration file at " + str(self.config_file_path))
			else:
				print ("Writing configuration file at " + str(self.config_file_path))
			with open(self.config_file_path, 'w') as file_handle:
				self.config_parser.write(file_handle)
		except E:
			# TODO (OS): Catch this
			pass
		return self

	def set(self, section, option, arg):
		if not self.config_parser.has_section(section):
			self.config_parser.add_section(section)
		self.config_parser.set(section, option, arg)

	def get(self,section,option):
		return self.config_parser.get(section, option)


def config(args):
	'''Handle the 'config' command'''
	if not os.path.exists(args.path):
		exit("Path does not exist: " + args.path )		

	path = os.path.realpath(args.path)

	if not os.path.exists(os.path.join(path, ".git")):
		exit("No git repository at " + path)

	with config_file() as f:
		f.set("Repository", "Path", path)
	return

