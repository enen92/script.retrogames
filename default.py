#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Author: enen92 

 License: I don't care version 3.0
 
"""

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,xbmcvfs
import os,sys,json
from resources.common_variables import *
from resources.directory import *
from resources.webutils import *
from resources.utilities import *
from resources.downloadtools import *


def main_menu():
	addDir(translate(30001),'https://archive.org/details/softwarelibrary_msdos_games?&sort=-downloads&page=1',1, os.path.join(artfolder,'dosboxicon.png'),1,os.path.join(artfolder,'dosbox.jpg'))
	addDir(translate(30014),'https://archive.org/details/sega_genesis_library?&sort=-downloads&page=1',1,'http://thegamesdb.net/banners/platform/consoleart/18.png',1,'http://thegamesdb.net/banners/platform/fanart/18-3.jpg')
	addDir(translate(30015),'https://archive.org/details/gamegear_library?&sort=-downloads&page=1',1,'http://thegamesdb.net/banners/platform/consoleart/20.png',1,'http://thegamesdb.net/banners/platform/fanart/20-2.jpg')
	addDir(translate(30016),'https://archive.org/details/atari_2600_library?&sort=-downloads&page=1',1,'http://psx-scene.com/forums/attachments/f190/35672d1339560883-%5Bps3%5D-emulator-downloads-w-complete-info-atari-2600.png',1,'http://thegamesdb.net/banners/platform/fanart/22-3.jpg')
	

def dos_box(url):
	try:
		page_source = get_page_source(url)
	except: page_source = None
	if page_source:
		matchgames = re.findall('<div class="item-ia"(.*?)<div class="C5"></div>',page_source,re.DOTALL)
		totalmatch = len(matchgames)
		if matchgames:
			
			#add costumized search url
			if '_msdos_games' in url: 
				console_fanart = os.path.join(artfolder,'dosbox.jpg')
				addDir(translate(30002),'https://archive.org/details/softwarelibrary_msdos_games?and[]=',2,'',1,os.path.join(artfolder,'dosbox.jpg'))
			elif 'sega_genesis' in url:
				console_fanart = 'http://thegamesdb.net/banners/platform/fanart/18-3.jpg'
				addDir(translate(30002),'https://archive.org/details/sega_genesis_library?and[]=',2,'',1,console_fanart)
			elif 'atari_2600' in url:
				console_fanart = 'http://thegamesdb.net/banners/platform/fanart/22-3.jpg'
				addDir(translate(30002),'https://archive.org/details/atari_2600_library?and[]=',2,'',1,console_fanart)
			elif 'gamegear' in url:
				console_fanart = 'http://thegamesdb.net/banners/platform/fanart/20-2.jpg'
				addDir(translate(30002),'https://archive.org/details/gamegear_library?and[]=',2,'',1,console_fanart)
			
			year = 0
			for gameinfo in matchgames:
				title = re.compile('title=".+?">(.+?)</a>').findall(gameinfo)
				if selfAddon.getSetting('img-resolution') == '0':
					try: 
						game_file = re.compile('<img class="item-img" source="(.+?)"').findall(gameinfo)[0].split('/')[-1]
						iconimage = 'http://archive.org/serve/' + game_file + '/' + game_file.replace('msdos_','').replace('sg_','').replace('gg_','') + '_screenshot.gif'
						if 'atari_2600' in iconimage: iconimage = iconimage.replace('.gif','.png')
					except: iconimage = ''
				else:
					try: 
						game_file = re.compile('<img class="item-img" source="(.+?)"').findall(gameinfo)[0]
						iconimage = 'http://archive.org' + game_file
					except: iconimage = ''
					
				try:	gameurl = 'http://archive.org' + re.findall('<a href="(.+?)" title="',gameinfo)[0]
				except: gameurl = ''
				try: 
					gameplot = re.compile('<span>(.+?)</span>').findall(gameinfo)[0]
					#year
					try: 
						year_str = re.compile('Released(.+?)(?:Also|Platform)').findall(gameplot)
						if year_str:
							year_dig = re.findall('(\d+)',year_str[0])
							if year_dig:
								if len(year_dig) > 1: year = year_dig[-1]
								else: year = year_dig[0]
					except:
						try:
							year_str = re.compile('_(\d+)_').findall(gameplot)[-1]
							if len(year_str) == 4 and year_str != 2600: year = int(year_str)
						except: year = 0
					
					#Genre
					try: genre = re.compile('Genre (.+?) .+?Description').findall(gameplot)[0].replace(',','')
					except: genre = ''
					
					#developed by
					try: author = re.findall('Developed by (.+?) Released',gameplot)[0]
					except: author = ''
					
					#description	
					gameplot = gameplot.split('Description ')	
					if len(gameplot) > 1: gameplot = gameplot[-1]
					else: gameplot = gameplot[0]
					
				except: 
					gameplot = ''
					year = 0
					genre = ''
					author = ''
					
				#Put year to zero match year in plot
				if year == 2600: year= 0
				year_opt = re.compile('19(\d+)').findall(gameplot)
				if year_opt:
					year = int('19'+str(year_opt[0]))
				
					
				if title:
					infolab = { "Title": title[0],"Plot": gameplot, "Year":year, "Genre":genre, "Studio":author,"Director":author, "Writer":author}
					addGame('[B]'+title[0]+'[/B]',gameurl,3,iconimage,totalmatch,iconimage,infolab)#os.path.join(artfolder,'dosbox.jpg'))
					
			#next page stuff
			if totalmatch > 70:
				try:
					cur_page = re.findall('&page=(\d+)',url)[0]
					next_page = int(cur_page) + 1
					url_next = url.replace('page='+str(cur_page),'page='+str(next_page))
					addDir(translate(30003),url_next,1,'',1,console_fanart)
				except: pass
			xbmcplugin.setContent(int(sys.argv[1]), 'movies')
			xbmc.sleep(200)
			if "confluence" in xbmc.getSkinDir() and selfAddon.getSetting("confluence-res") == 'true':
				xbmc.sleep(200)
				xbmc.executebuiltin("Container.SetViewMode(504)")
			elif selfAddon.getSetting("view-id") != '':
				xbmc.executebuiltin("Container.SetViewMode("+str(selfAddon.getSetting("view-id"))+")")
	else: msgok(translate(30000),translate(30004))
	
	
def archive_resolver(url):
	url = url.replace('/details/','/metadata/')
	source = json.load(urllib2.urlopen(url))
	d1 = source["d1"]
	dire = source["dir"]
	files = source["files"]
	rom = ''
	for _file_ in files:
		if _file_["name"].endswith('.zip') or _file_["name"].endswith('.bin'):
			rom = _file_["name"]
			break
		else: pass
	if rom:
		download_url = "http://"+d1+dire+'/'+rom
		if selfAddon.getSetting('download-folder') == '':
			downloadPath = xbmcgui.Dialog().browse(int(3), 'Select Download Folder','myprograms')
			selfAddon.setSetting('download-folder',downloadPath)
		else: downloadPath = selfAddon.getSetting('download-folder')
		
		if 'sg_' in download_url: destination_folder = os.path.join(downloadPath,'genesis')
		elif 'gg_' in download_url: destination_folder = os.path.join(downloadPath,'gamegear')
		elif 'msdos_' in download_url: destination_folder = os.path.join(downloadPath,'DOS')
		elif 'atari_2600_' in download_url: destination_folder = os.path.join(downloadPath,'atari2600')
		
		if not os.path.exists(destination_folder): xbmcvfs.mkdir(destination_folder)
		
		destination_file = os.path.join(destination_folder,rom)
		download_tools().Downloader(download_url,destination_file,translate(30007) + rom,translate(30000))
		msgok(translate(30000),translate(30005) + destination_folder,translate(30006))
		
def read_details(name,url):
	url = url.replace('/details/','/metadata/')
	source = json.load(urllib2.urlopen(url))
	
	plot = source["metadata"]["description"]

	xbmc.executebuiltin("ActivateWindow(10147)")
	window = xbmcgui.Window(10147)
	xbmc.sleep(100)
	window.getControl(1).setLabel(name)
	window.getControl(5).setText(strip_tags(plot))
		
	

	
	
def archive_search(url):

	keyb = xbmc.Keyboard('', translate(30008))
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		encode=urllib.quote(search)
		urltmp = url+encode+'&page=1'
		dos_box(urltmp)



"""

Addon navigation is below
 
"""	
			
            
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
                               
	return param


params=get_params()
url=None
name=None
mode=None
iconimage=None
plot=None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except:
	try: 
		mode=params["mode"]
	except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: plot=urllib.unquote_plus(params["plot"])
except: pass

print ("Mode: "+str(mode))
print ("URL: "+str(url))
print ("Name: "+str(name))
print ("iconimage: "+str(iconimage))


if mode==None: main_menu()
elif mode==1: dos_box(url)
elif mode==2: archive_search(url)
elif mode==3: archive_resolver(url)
elif mode==4: read_details(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
