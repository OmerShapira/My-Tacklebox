"""Tacklebox v 0.01
Written by Omer Shapira

"""
import os
import sys
import ctypes 			#for windows admin checking

import argparse

import config


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
	parser_config.set_defaults(func=config.config)

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
