#!/usr/bin/env python
#
from __future__ import unicode_literals
import youtube_dl
import os
import sys

os.system("clear && clear && clear")
logo = '''
 /$$$$$$$                  /$$  /$$$$$$                   /$$$$$$$$        /$$                
| $$__  $$                | $$ /$$__  $$                 |__  $$__/       | $$                
| $$  \ $$  /$$$$$$   /$$$$$$$| $$  \__/  /$$$$$$   /$$$$$$$| $$ /$$   /$$| $$$$$$$   /$$$$$$ 
| $$  | $$ /$$__  $$ /$$__  $$|  $$$$$$  /$$__  $$ /$$_____/| $$| $$  | $$| $$__  $$ /$$__  $$
| $$  | $$| $$$$$$$$| $$  | $$ \____  $$| $$$$$$$$| $$      | $$| $$  | $$| $$  \ $$| $$$$$$$$
| $$  | $$| $$_____/| $$  | $$ /$$  \ $$| $$_____/| $$      | $$| $$  | $$| $$  | $$| $$_____/
| $$$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/| $$$$$$$/|  $$$$$$$
|_______/  \_______/ \_______/ \______/  \_______/ \_______/|__/ \______/ |_______/  \_______/

   \033[0m  \033[91m   \033[1m     }--{+} Coded By Manisso the original pytube creator. 		    
   \033[0m  \033[91m    \033[1m    }--{+} Lets download some stuff. 		         	     
   \033[0m  \033[91m   \033[1m     }--{+} supported platforms: dailymotion,vimeo,vivo and many more.
'''
menu = '''\033[0m
    {1}--Video Download
    {2}--Audio Download
    {3}--Audio PlayList Download

    {4}-Exit
 '''
print logo
print menu


def quit():
    con = raw_input('Continue [Y/n] -> ')
    if con[0].upper() == 'N':
        exit()
    else:
        os.system("clear")
        print logo
        print menu
        select()


def select():
    try:
        choice = input("SnapTub~# ")
        if choice == 1:
            os.system("clear")
            print """
 __     __  __        __
/  |   /  |/  |      /  |
$$ |   $$ |$$/   ____$$ |  ______    ______
$$ |   $$ |/  | /    $$ | /      \  /      \
$$  \ /$$/ $$ |/$$$$$$$ |/$$$$$$  |/$$$$$$  |
 $$  /$$/  $$ |$$ |  $$ |$$    $$ |$$ |  $$ |
  $$ $$/   $$ |$$ \__$$ |$$$$$$$$/ $$ \__$$ |
   $$$/    $$ |$$    $$ |$$       |$$    $$/
    $/     $$/  $$$$$$$/  $$$$$$$/  $$$$$$/

PUT URL HERE:
"""
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([raw_input('URL: ')])
            print("")
            quit()
        elif choice == 2:
            os.system("clear")
            print """
  /$$$$$$                  /$$ /$$
 /$$__  $$                | $$|__/
| $$  \ $$ /$$   /$$  /$$$$$$$ /$$  /$$$$$$
| $$$$$$$$| $$  | $$ /$$__  $$| $$ /$$__  $$
| $$__  $$| $$  | $$| $$  | $$| $$| $$  \ $$
| $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$
| $$  | $$|  $$$$$$/|  $$$$$$$| $$|  $$$$$$/
|__/  |__/ \______/  \_______/|__/ \______/

PUT URL HERE:
"""
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([raw_input('URL: ')])
            quit()
        elif choice == 3:
            os.system("clear")
            print("""
 /$$$$$$$  /$$                     /$$ /$$             /$$
| $$__  $$| $$                    | $$|__/            | $$
| $$  \ $$| $$  /$$$$$$  /$$   /$$| $$ /$$  /$$$$$$$ /$$$$$$
| $$$$$$$/| $$ |____  $$| $$  | $$| $$| $$ /$$_____/|_  $$_/
| $$____/ | $$  /$$$$$$$| $$  | $$| $$| $$|  $$$$$$   | $$
| $$      | $$ /$$__  $$| $$  | $$| $$| $$ \____  $$  | $$ /$$
| $$      | $$|  $$$$$$$|  $$$$$$$| $$| $$ /$$$$$$$/  |  $$$$/
|__/      |__/ \_______/ \____  $$|__/|__/|_______/    \___/
                         /$$  | $$
                        |  $$$$$$/
                         \______/

PUT URL HERE:
""")
            d3 = raw_input('playlist URL: ')
            os.system("clear")
            os.system("youtube-dl -cit --extract-audio --audio-format mp3 " + d3)
            print("")
            quit()
    except(KeyboardInterrupt):
        print ""


select()
