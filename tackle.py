"""Tacklebox v 0.01
Written by Omer Shapira

"""
import os
import sys
import ctypes 			#for windows admin checking

import argparse
import ConfigParser


'''
Usage

tackle
(usage)

tackle put all
tackle put vimrc
tackle pop vimrc

tackle fetch
(pull changes)
tackle rerfresh [bait/file]
(deploy changes)
tackle collect [bait/file]
(collects changes to baits and pushes them)

tackle inventory
(shows baits)

tackle snip glsl
(returns a list of all glsl snippets)
tackle snip glsl/noise
(prints glsl/noise.glsl into the console)
tackle snip -c glsl/nosie
tackle clip glsl/noise


State:
~/.tacklebox/
  - backup/
  - 
  - state.tackle


'''

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

def check_git_repo(path):
	#TODO (OS): Make
	pass

def halt_if_admin():
	try:
 		is_admin = os.getuid() == 0
	except AttributeError:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

	if is_admin:
		exit("Tacklebox won't run under admin privilieges. You might hurt yourself.")


def main():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(help="Options:") 

	parser_config = subparsers.add_parser('config', help="configure the project")	
	parser_config.add_argument('path', type=str)
	parser_config.set_defaults(func=config)

	parser_put = subparsers.add_parser('put', help="put an asset in place, backing up the old one, if it exists")
	parser_put.add_argument('config_name', type=str, action='store')
	parser_put.add_argument('--path', type=str, action='store')

	parser_pop = subparsers.add_parser('pop', help="remove an asset, restore the previous one from backup if possible")
	parser_pop.add_argument('config_name')	

	parser_fetch = subparsers.add_parser('fetch', help="pull the latest from remote repository, point repository to head of the current branch.")

	parser_refresh = subparsers.add_parser('refresh', help="put most recent assets for all currently deployed assets, backing up current ones.")

	parser_collect = subparsers.add_parser('collect', help="adds a deployed asset into the repository and pushes to the remote repository, if exists.")

	parser_snip = subparsers.add_parser('snip', help="pastes a snippet")	
	parser_clip = subparsers.add_parser('clip', help="pastes a snippet into the clipboard")	

	# Read
	args = parser.parse_args()

	# Safety check
	halt_if_admin()

	# Execute!
	args.func(args)


if __name__ == "__main__":
	main()
