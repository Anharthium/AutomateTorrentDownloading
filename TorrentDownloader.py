#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from subprocess import *
import time
import sys

def main():

	season = "05"	#season number 
	f = open("episode.txt", "r+")	#opening the file that contains previous episode downloaded
	prevEpisodeDownloaded = eval(f.readLine().strip())
	currentEpisode = prevEpisodeDownloaded + 1
	if currentEpisode < 10:
		episodeName = "S" + season + "E0" + str(currentEpisode)
	else:
		episodeName = "S" + season + "E" + str(currentEpisode)
	url = "http://thetvtorrents.com/show/silicon-valley"	#url to scrape from
	downloadDirectory = "/home/aravindh/Videos/TVSeries/SiliconValley/Season5"	#downloadDirectory
	magnetLink = returnDownloadLink(url, episodeName) 
	if downloadTorrent(magnetLink, downloadDirectory):
		prevEpisodeDownloaded = currentEpisode	#prev episode set to current episode
		f.truncate()	#delete contents of the file
		f.write(str(prevEpisodeDownloaded)) #writing back prev downloaded episode
	f.close()	#close the file	
	
	
def returnDownloadLink(url, episodeName):
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = Request(url, headers=hdr)
	page = urlopen(req)
	soup = BeautifulSoup(page, "html.parser")	#creating soup of the page
	for link in soup.find_all('a'):
		magnetLink = link.get('href')
		if magnetLink.startswith("magnet") and episodeName in magnetLink and "720p" in magnetLink:
			return magnetLink		        #return magnet link of required episode
			
    	
def downloadTorrent(magnetLink, downloadDirectory):
	command = ["transmission-cli -f killTransmission.sh -w", downloadDirectory, magnetLink]
	try:
		check_call(command) #calling the command line to download torrent
	except CalledProcessError:
		time.sleep(300)	#wait for 5 minutes before calling the function again
		downloadTorrent(magnetLink, downloadDirectory)	#call the function again
	else:
		call(["notify-send", "Silicon valley new episode downloaded!"])	#notify the user
	return 1	#return value of 1 in case of success	
				
	
main()	#calling main function
