#!/bin/sh

apt-get install python3-pip -y	#to install pip3
apt-get install python3-bs4 -y	#to install bs4
#to install transmission-cli
add-apt-repository ppa:transmissionbt/ppa	
apt-get update
apt-get install transmission-cli -y
chmod +x TorrentDownloader.py	#to make script executable as ./TorrentDownloader.py
chmod +x killTransmisssion.sh	#to make the script executable
