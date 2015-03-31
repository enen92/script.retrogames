#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Author: enen92 

 License: I don't care version 3.0
 
"""
import xbmc,xbmcplugin,xbmcaddon,xbmcgui,sys,os,urllib,xbmcvfs
from common_variables import *



#Function to add a regular directory
def addDir(name,url,mode,iconimage,number_of_items,fan_art,pasta=True):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fan_art)
	liz.setInfo( type="Video", infoLabels={ "Title": name })
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=number_of_items)
	return ok
	
def addGame(name,url,mode,iconimage,number_of_items,fan_art,infolab):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	contextmen = []
	if 'archive.org' in url:
		contextmen.append((translate(30009), 'XBMC.RunPlugin(%s?mode=4&url=%s&name=%s&iconimage=%s)' % (sys.argv[0], urllib.quote_plus(url),name,iconimage)))
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fan_art)
	liz.setInfo( type="Video", infoLabels=infolab)
	liz.addContextMenuItems(contextmen,replaceItems=False)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False,totalItems=number_of_items)
	return ok
