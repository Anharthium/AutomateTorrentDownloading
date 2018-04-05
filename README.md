# AutomateTorrentDownloading
1) This is a small script to automate downloading of your favorite TV shoes through torrent. Supported for Python3 only. Tested on Ubuntu 16.04 only.

2) Dependencies
	a) bs4 should be installed for python3.
	b) transmission-cli should be installed.
	c) run install.sh to get these things installed on your system. First make install.sh executable and run the script. You may need root privileges.
	
3) To make it work for you, some changes have to be made:
	a) In TorrentDownloader.py:
		i) Change the downloadDirectory variable in themain function to the download directory of your choice.
		ii) Change the url to the page that updates magnet links of your favorite TV shoes. I recommend using the same site as I did since they update all the episodes in one page. It is easy to scrape.
		iii) Change the video quality to the video quality that you like, and is available in that web page that you have updated.
	b) Make all .sh files executable with chmod +x <ScriptName>.sh
	c) Run crontab to schedule the python script to run at specified time(s)
	
4) LastEpisodeDownloaded.txt contains the last episode downloaded. DO NOT delete that file. Edit it with single number denoting the latest episode number that you already have.

5) If your torrent is not downloading, open transmission. Under Edit -> Preferences -> Network -> select pick random port every time it is started.

6) This is a small script which you could break easily. So feel free to modify it according to your use or use the idea to design your own. 

7) I will try to make it as useful as possible by adding a number of functionalities. So feel free to contribute.
	
