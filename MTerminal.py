#!/usr/bin/python3

import vlc
import time
import os
import argparse
import sys

def get_parser():
	parser = argparse.ArgumentParser(description='MTerminal')
	parser.add_argument("-p","--play", help="Play music", \
			action="store_true")
	parser.add_argument('-f', '--find', help="find files", \
			action="store_true")
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
				os.system(f'echo "\\e[1;33mNew songs added : {len(music)}\\e[0m"')
		except FileNotFoundError as e:
			os.system('echo "\\e[1;34mFirst time or deleted music list please create new\\e[0m"')
			get_mp3()
			
	elif action.lower() == "n":
		path = get_path()
		os.system(f"find -L {path} -type f -ipath '*.mp3' >musiclist.list")
		os.system(f'echo "\\e[1;33mNew music list created \\e[0m"')
	elif action.lower() == "q":
		sys.exit(1)
			


def  play_control(sound):
	instance = vlc.Instance()
	player = instance.media_player_new()
	media = instance.media_new(sound)
	player.set_media(media)
	player.play()
	while True:
		state = player.get_state()
		action = input("MTplayer :")
		if action.lower() == "pause":
			player.pause()
			action = input(f"MTplayer {state}:")
		elif action.lower() == "stop":
			player.stop()
			action = input(f"MTplayer {state}:")
		elif action.lower() == "play":
			player.play()
			action = input(f"MTplayer {state}:")
	
	
	
	
	
def play_music():
	f = os.getcwd()+'/'+"musiclist.list"
	if os.path.isfile(f):
		with open('musiclist.list', 'r') as f:
			muc = f.readlines()
			for sound in muc:
				play_control(sound.strip('\n'))
	else:
		os.system('echo "\\e[1;34mFirst time or deleted music list please create new\\e[0m"')
		get_mp3()
			
	


def main():
	os.system("clear")
	os.system('echo  "\\e[1;31m\"')
	os.system("figlet -f shadow     WinterFreak   ")
	os.system('echo "\\e[1;32m\"')
	os.system('echo "\\e[1;34m Created By W1nterFr3ak\\e[0m"')
	os.system('echo "\\e[4;32m This Player Was Created By W1nterFr3ak \\e[0m"')
	os.system('echo "\\e[1;32m   Mail: WinterFreak@protonmaail.comm \\e[0m"')
	parser  = get_parser()
	args  = vars(parser.parse_args())
	play = args['play']
	find = args['find']
	if play:
		play_music()
	elif find:
		get_mp3()
	else:
		parser.print_help()
		
	
if __name__ == "__main__":
	main()
