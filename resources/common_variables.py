#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Author: enen92 

 License: I don't care version 3.0
 
"""
import xbmc,xbmcgui,xbmcaddon,os

addon_id = 'script.retrogames'
selfAddon = xbmcaddon.Addon(id=addon_id)
datapath = xbmc.translatePath(selfAddon.getAddonInfo('profile')).decode('utf-8')
addonfolder = xbmc.translatePath(selfAddon.getAddonInfo('path')).decode('utf-8')
artfolder = os.path.join(addonfolder,'resources','img')
msgok = xbmcgui.Dialog().ok

def translate(text):
      return selfAddon.getLocalizedString(text).encode('utf-8')
