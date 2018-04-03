#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from subprocess import *
import time
import sys

def main():
	url = sys.argv[1]
	episodeName = sys.argv[2]
	downloadDirectory = sys.argv[3]
	magnetLink = returnDownloadLink(url, episodeName)
	#downloadDirectory = "/home/aravindh/Videos/TVSeries/SiliconValley/Season5"	#downloadDirectory 
	downloadTorrent(magnetLink, downloadDirectory)	
	
	
def returnDownloadLink(url, episodeName):
	#url= "http://thetvtorrents.com/show/silicon-valley"	#url from which we download torrent/magnet link
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = Request(url, headers=hdr)
	page = urlopen(req)
	soup = BeautifulSoup(page, "html.parser")	#creating soup of the page
	for link in soup.find_all('a'):
		magnetLink = link.get('href')
		if magnetLink.startswith("magnet") and episodeName in magnetLink and "720p" in magnetLink:
			return magnetLink		        #return magnet link of required episode
			
    	
def downloadTorrent(magnetLink, downloadDirectory):
	command = ["transmission-cli", "-w", downloadDirectory, magnetLink]
	try:
		check_call(command) #calling the command line to download torrent
	except CalledProcessError:
		time.sleep(300)	#wait for 5 minutes before calling the function again
		downloadTorrent(magnetLink, downloadDirectory)	#call the function again
	else:
		call(["notify-send", "Silicon valley new episode downloaded!"])	#notify the user
				
	
main()	#calling main function
