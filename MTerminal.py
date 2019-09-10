#!/usr/bin/python3

import vlc
import time
import os
import argparse
import sys

def get_parser():
	parser = argparse.ArgumentParser(description='MTerminal')
	parser.add_argument('-l','--location', help='Play music from aa certain location')
	parser.add_argument('-f', '--find', help="find files")
	return parser

def get_path():
	path = input("Input folder to search(default '/home'):")
	if path:
		return path 
	else:
		path = '/home'
		return path
		
def get_mp3():
	
	action = input("Type (a|A) add to music list (n|N) to create new (q|Q) to exit :")
	if action.lower() == "a":
		path = get_path()
		try:
			with open("musiclist.list", 'r+') as mp3:
				musics = os.system(f"find -L {path} -type f -ipath '*.mp3'")
				lines = mp3.readlines().strip()
				music = []
				
				for x in music:
					if x not in lines:
						music.append(x)
					else:
						continue
				for i in music:
					mp3.write(i + n)
		except FileNotFoundError as e:
			os.system('echo "\\e[1;34mFirst time or deleted music list please create new\\e[0m"')
			get_mp3()
			
	elif action.lower() == "n":
		path = get_path()
		os.system(f"find -L {path} -type f -ipath '*.mp3' >musiclist.list")
		
	elif action.lower() == "q":
		sys.exit(1)
			
	

def  play_controll():
	pass


def main():
	os.system("clear")
	os.system('echo  "\\e[1;31m\"')
	os.system("figlet -f shadow     WinterFreak   ")
	os.system('echo "\\e[1;32m\"')
	os.system('echo "\\e[1;34m Created By W1nterFr3ak\\e[0m"')
	os.system('echo "\\e[4;32m This Player Was Created By W1nterFr3ak \\e[0m"')
	os.system('echo "\\e[1;32m   Mail: WinterFreak@protonmaail.comm \\e[0m"')
	
	
if __name__ == "__main__":
	main()
