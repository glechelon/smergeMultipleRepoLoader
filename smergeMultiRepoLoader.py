##!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess
import argparse
from pathlib import Path
from os import path, system



def verify_smerge_present():
	try:
		subprocess.run(["smerge", "-v"])
	except Exception as e:
		raise SystemExit("ERROR: 'smerge' command seems to be missing.")


def open_repositories(root_directory):
	for path in Path(root_directory).rglob('.git'):
		print(path)
		subprocess.run(["smerge", "-b", path])
		system('taskkill /f /im sublime_merge.exe')
	print("Repositories opened")



def main():
	verify_smerge_present()
	parser = argparse.ArgumentParser()
	parser.add_argument('directory')
	args = parser.parse_args()
	print("Running Sublime Merge multi repo loader on directory: ", args.directory)
	if not path.exists(args.directory):
		raise SystemExit("ERROR: Directory not found")
	open_repositories(args.directory)
	subprocess.run(["smerge"])
	SystemExit("Repositories loaded with success!!")



if __name__ == "__main__":
	main()