#!/bin/python3

print("Raspberry-Pi-FM-DJ.py")
print("Raspberry-Pi-FM-DJ code made by catdogmat/beano09 at:")
print("https://github.com/catdogmat/Raspberry-Pi-FM-DJ")
print("PiFM code made by Oliver Mattos and Oskar Weigl at:")
print("https://github.com/rm-hull/pifm")
# Imports
print("Imports:")
print("Importing OS, random, wave, contextlib, subprocess, datetime and time.")
import os, random
import wave
import contextlib
import subprocess
from datetime import *
import time
print("Imported OS, random, wave, contextlib, subprocess, datetime and time.")
# Config
print("Config:")
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
# Timeplaylist settings.
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
# Time Playlist Stuff
print("Setting up time playlists.")
onintrodir = introdir
onsongdir = songdir
onoutrodir = outrodir
onfunnydir = funnydir
timeofplaylists = datetime.strptime("03/02/21 16:30", "%d/%m/%y %H:%M")
timetogo = "{:d}:{:02d}".format(time.hour, time.minute)
if timetogo > playlist1starttime:
    if timetogo < playlist1endtime:
        if timeplaylists == "yes":
            if playlist1 == "yes":
               onintrodir = playlist1introdir
               onsongdir = playlist1songdir
               onoutrodir = playlist1outrodir
if timetogo > playlist2starttime:
    if timetogo < playlist2endtime:
        if timeplaylists == "yes":
            if playlist2 == "yes":
               onintrodir = playlist2introdir
               onsongdir = playlist2songdir
               onoutrodir = playlist2outrodir
if timetogo > playlist3starttime:
    if timetogo < playlist3endtime:
        if timeplaylists == "yes":
            if playlist3 == "yes":
               onintrodir = playlist3introdir
               onsongdir = playlist3songdir
               onoutrodir = playlist3outrodir
if timetogo > playlist4starttime:
    if timetogo < playlist4endtime:
        if timeplaylists == "yes":
            if playlist4 == "yes":
               onintrodir = playlist4introdir
               onsongdir = playlist4songdir
               onoutrodir = playlist4outrodir
if timetogo > playlist5starttime:
    if timetogo < playlist5endtime:
        if timeplaylists == "yes":
            if playlist5 == "yes":
               onintrodir = playlist5introdir
               onsongdir = playlist5songdir
               onoutrodir = playlist5outrodir
print("Setup time playlists.")
# This picks a song
print("Picking filename")
file = random.choice(os.listdir(onintrodir))
print("Filename picked was " + file)
# This finds how long the .wav is
print("Finding duration of intro")
fname = onintrodir + file
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    onintrodur = duration + 1
print("Intro is " + onintrodur + " seconds long")
# This plays the intro
print("Playing intro")
subprocess.run('sudo ./pifm'  + onintrodir + file + " " + fmsettings)
#This finds how long the song is
print("Finding how long the song is")
fname = onsongdir + file
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    onsongdur = duration + 1
# Playing the song
print("Playing song")
subprocess.run('sudo ./pifm'  + onsongdir + file + " " + fmsettings)
# Finds how long the outro is
print("Finding how long the outro is")
fname = onoutrodir + file
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    onoutrodur = duration + 1
# Plays outro
print("Playing outro")
subprocess.run('sudo ./pifm'  + onoutrodir + file + " " + fmsettings)
# Finds funny part
print("Finding funny part")
funnyfile = random.choice(os.listdir(onfunnydir))
# Finds length
print("Finding how long the funny part is")
fname = onfunnydir + funnyfile
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    onfunnydur = duration + 1
# Plays
print("Playing funny part")
subprocess.run('sudo ./pifm'  + onfunnydir + funnyfile + " " + fmsettings)
print("Done!")
