print("Raspberry-Pi-FM-DJ.py")
print("Raspberry-Pi-FM-DJ code made by catdogmat/beano09 at:")
print("https://github.com/catdogmat/Raspberry-Pi-FM-DJ")
print("PiFM code made by Oliver Mattos and Oskar Weigl at:")
print("https://github.com/rm-hull/pifm")
# Imports
print("Imports:")
print("Importing OS, random, wave, contextlib and time.")
import os, random
import wave
import contextlib
import time
print("Imported OS, random, wave, contextlib and time.")
# Config
print("Config:")
name = "nameofradio" # You don't have to touch this
fmsettings = "100.0"
introdir = "enterpathhere"
songdir = "enterpathhere"
outrodir = "enterpathhere"
funnydir = "enterpathhere"
print("fmsettings is set to " + fmsettings)
print("introdir is set to " + introdir)
print("songdir is set to " + songdir)
print("outrodir is set to " + outrodir)
print("funnydir is set to " + funnydir)
# Unused Settings. Will be used in a later update.
timeplaylists = "off" # This can be on or off.
playlist1 = "off" # This can be on or off.
playlist2 = "off" # This can be on or off.
playlist3 = "off" # This can be on or off.
playlist4 = "off" # This can be on or off.
playlist5 = "off" # This can be on or off.
playlist1introdir = "enterpathhere"
playlist2introdir = "enterpathhere"
playlist3introdir = "enterpathhere"
playlist4introdir = "enterpathhere"
playlist5introdir = "enterpathhere"
playlist1songdir = "enterpathhere"
playlist2songdir = "enterpathhere"
playlist3songdir = "enterpathhere"
playlist4songdir = "enterpathhere"
playlist5songdir = "enterpathhere"
playlist1outrodir = "enterpathhere"
playlist2outrodir = "enterpathhere"
playlist3outrodir = "enterpathhere"
playlist4outrodir = "enterpathhere"
playlist5outrodir = "enterpathhere"
playlist1funnydir = "enterpathhere"
playlist2funnydir = "enterpathhere"
playlist3funnydir = "enterpathhere"
playlist4funnydir = "enterpathhere"
playlist5funnydir = "enterpathhere"
playlist1starttime = "entertimehere"
playlist2starttime = "entertimehere"
playlist3starttime = "entertimehere"
playlist4starttime = "entertimehere"
playlist5starttime = "entertimehere"
playlist1endtime = "entertimehere"
playlist2endtime = "entertimehere"
playlist3endtime = "entertimehere"
playlist4endtime = "entertimehere"
playlist5endtime = "entertimehere"
# CONFIG SETTINGS (DO NOT CHANGE)
config = "0.1"
name = "Raspberry-Pi-FM-DJ" # You don't have to touch this
# Code starts here
print("Code:")
# This picks a song
print("Picking filename")
file = random.choice(os.listdir(introdir))
print("Filename picked was " + file)
# This finds how long the .wav is
print("Finding duration of intro")
fname = introdir + file
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    introdur = duration + 1
print("Intro is " + introdur + " seconds long")
# This plays the intro
print("TO ADD")
os.system('sudo ./pifm'  + introdir + file + " " + fmsettings)
print("TO ADD")
# Sleeps intil done
print("TO ADD")
time.sleep(introdur)
print("TO ADD")
#This finds how long the song is
print("TO ADD")
fname = songdir + file
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    songdur = duration + 1
print("TO ADD")
# Playing the song
print("TO ADD")
os.system('sudo ./pifm'  + songdir + file + " " + fmsettings)
print("TO ADD")
# Waits
print("TO ADD")
time.sleep(songdur)
print("TO ADD")
# Finds how long the outro is
print("TO ADD")
fname = outrodir + file
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    outrodur = duration + 1
print("TO ADD")
# Plays outro
print("TO ADD")
os.system('sudo ./pifm'  + outrodir + file + " " + fmsettings)
print("TO ADD")
# Sleeps
print("TO ADD")
time.sleep(outrodur)
print("TO ADD")
# Finds funny part
print("TO ADD")
funnyfile = random.choice(os.listdir(funnydir))
print("TO ADD")
# Finds length
print("TO ADD")
fname = funnydir + funnyfile
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    funnydur = duration + 1
print("TO ADD")
# Plays
print("TO ADD")
os.system('sudo ./pifm'  + funnydir + funnyfile + " " + fmsettings)
print("TO ADD")
# Sleeps
print("TO ADD")
time.sleep(funnydur)
print("TO ADD")
