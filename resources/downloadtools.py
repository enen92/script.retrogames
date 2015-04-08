# -*- coding: utf-8 -*-

"""
 Author: enen92 

 License: I don't care version 3.0
 
"""
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,urllib,urllib2,tarfile,os,sys,re
from common_variables import *

user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36'

class download_tools():	
	def Downloader(self,url,dest,description,heading):
		dp = xbmcgui.DialogProgress()
		dp.create(heading,description,'')
		dp.update(0)
		urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: self._pbhook(nb,bs,fs,dp))
		
	def _pbhook(self,numblocks, blocksize, filesize,dp=None):
		try:
			percent = int((int(numblocks)*int(blocksize)*100)/int(filesize))
			dp.update(percent)
		except:
			percent = 100
			dp.update(percent)
		if dp.iscanceled(): 
			dp.close()
			

def extract(_in,_out,dp=None,type='all'):
    import zipfile
    if type=='all':
        if dp:
            return allWithProgress(_in, _out, dp)

        return allNoProgress(_in, _out)
            
    elif type=='allNoProgress':
        try:
            zin = zipfile.ZipFile(_in, 'r')
            zin.extractall(_out)
        except Exception, e:
            print str(e)
            return False
        return True

    elif type=='allWithProgress':
        dp = xbmcgui.DialogProgress()
        dp.create(translate(30000),translate(30030),'')
        zin = zipfile.ZipFile(_in,  'r')
        nFiles = float(len(zin.infolist()))
        count  = 0
        try:
            for item in zin.infolist():
                count += 1
                update = count / nFiles * 100
                dp.update(int(update))
                zin.extract(item, _out)
        except Exception, e:
            print str(e)
            return False
        return True
