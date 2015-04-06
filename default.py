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
	addDir('[B]Vtech Criativision[/B] (Archive.org)','https://archive.org/details/vtech_creativision_library?&sort=-downloads&page=1',1,'http://www.atomicfe.com/ladite/Images/creativision.png',1,'http://www.videogameconsolelibrary.com/images/1980s/81_VTech_CreatiVision/vtech_creativision_15.jpg')
	addDir('[B]Vtech Socrates[/B] (Archive.org)','https://archive.org/details/socrates_library?&sort=-downloads&page=1',1,'http://www.museo8bits.es/wiki/images/thumb/0/08/VTech_Socrates_Saitout_01.jpg/300px-VTech_Socrates_Saitout_01.jpg',1,'http://media.engadget.com/img/product/19/f4r/socrates-1h3m-800.jpg')
	addDir("[B]Super A'can[/B] (Archive.org)",'https://archive.org/details/superacan_library?&sort=-downloads&page=1',1,'http://static.giantbomb.com/uploads/scale_small/0/26/2392023-superacan.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/2/2c/Super-ACan-Console-set-h.jpg')
	addDir("[B]Sega Master System[/B] (Archive.org)",'https://archive.org/details/sega_sms_library?&sort=-downloads&page=1',1,'http://clipart-fr.com/en/data/icons/set_01/icones_00206.png',1,'http://cloud-4.steamusercontent.com/ugc/46493803785332279/AA4F9D55545B2C15A21C94FA21193EA034F4BC6E/')
	addDir("[B]Neo Geo Pocket[/B] (Archive.org)",'https://archive.org/details/ngp_library?&sort=-downloads&page=1',1,'http://thegamesdb.net/banners/platform/consoleart/4922.png',1,'http://i.imgur.com/4dPue.jpg')
	addDir("[B]Atari 7800[/B] (Archive.org)",'https://archive.org/details/atari_7800_library?&sort=-downloads&page=1',1,'http://jscustom.theoldcomputer.com/images/manufacturers_systems/Atari/7800/306965atari-7800.system.png',1,'http://thegamesdb.net/banners/platform/fanart/27-1.jpg')
	addDir("[B]Atari 5200[/B] (Archive.org)",'https://archive.org/details/atari_5200_library?&sort=-downloads&page=1',1,'http://thegamesdb.net/banners/_platformviewcache/platform/boxart/26-1.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/e/e6/Atari_5200_-_trojandan_14871272.jpg')
	addDir("[B]Amstrad Gx-4000[/B] (Archive.org)",'https://archive.org/details/gx4000_library?&sort=-downloads&page=1',1,'http://www.pugo.org/media/collection/console/amstrad_gx4000.png',1,'http://fc07.deviantart.net/fs71/i/2012/058/4/9/amstrad_gx4000_by_mellergaard-d4r5bil.jpg')
	addDir("[B]Sega SG-1000[/B] (Archive.org)",'https://archive.org/details/sg_1000_library?&sort=-downloads&page=1',1,'http://img.gamefaqs.net/box/7/1/6/307716_front.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/b/b8/Sega_SG-1000_Bock.jpg')
	addDir("[B]Megaduck[/B] (Archive.org)",'https://archive.org/details/megaduck_library?&sort=-downloads&page=1',1,'https://archive.org/services/img/megaduck_library',1,'http://i.ytimg.com/vi/qHT4n1kgqyU/maxresdefault.jpg')
	addDir("[B]Mattel Intellivision[/B] (Archive.org)",'https://archive.org/details/intellivision?&sort=-downloads&page=1',1,'http://thegamesdb.net/banners/_platformviewcache/platform/boxart/32-1.jpg',1,'http://thegamesdb.net/banners/platform/fanart/32-1.jpg')
	addDir("[B]Mattel Aquarius[/B] (Archive.org)",'https://archive.org/details/mattelaquarius?&sort=-downloads&page=1',1,'http://oldcomputers.net/pics/aquarius-expander.jpg',1,'http://www.zock.com/8-Bit/Ad_Aquarius.JPG')
	addDir("[B]The Fairchild Channel F[/B] (Archive.org)",'https://archive.org/details/channelf_library?&sort=-downloads&page=1',1,'http://www.videogames.org/html/images/ChannelF.gif',1,'http://upload.wikimedia.org/wikipedia/commons/5/56/Fairchild-Channel-F-System-II-Console.jpg')
	addDir("[B]APF-MP1000[/B] (Archive.org)",'https://archive.org/details/apfm1000_library?&sort=-downloads&page=1',1,'http://hcvgm.org/Images/MP1000S.jpg',1,'http://atariage.com/forums/uploads/monthly_11_2010/post-10944-128979518522.jpg')
	addDir("[B]Emerson Arcadia[/B] (Archive.org)",'https://archive.org/details/emerson_arcadia_library?&sort=-downloads&page=1',1,'http://www.emuunlim.com/doteaters/Arcadia.gif',1,'http://i.ytimg.com/vi/j4o31uRZs3w/maxresdefault.jpg')
	addDir("[B]Entex Adventure Vision[/B] (Archive.org)",'https://archive.org/details/adventurevision_library?&sort=-downloads&page=1',1,'https://c2.staticflickr.com/4/3273/5832604040_46164b3b04.jpg',1,'http://www.miniarcade.com/ebay/adventurevision3.jpg')
	addDir("[B]Epoch Game Pocket Computer[/B] (Archive.org)",'https://archive.org/details/gamepocket_library?&sort=-downloads&page=1',1,'https://rfmp.files.wordpress.com/2011/06/250px-epoch_game_pocket_computer.jpg',1,'http://www.chrismcovell.com/GamePokekon/Epoch_System.jpg')
	
	#Single packs
	addDir("[B]Sinclair ZX Spectrum[/B] (Archive.org)",'https://archive.org/details/Sinclair_ZX_Spectrum_TOSEC_2012_04_23',5,'http://www.c64vsspectrum.com/spectrum48k_jpg.jpg',1,'http://thegamesdb.net/banners/platform/fanart/4913-1.jpg')
	addDir("[B]Atari 8-bit[/B] (Archive.org)",'https://archive.org/details/Atari_8_bit_TOSEC_2012_04_23',5,'http://gury.atari8.info/images/Atari_800xe_System_s1.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/9/9f/Atari_800XL_Plain_White.jpg')
	addDir("[B]Atari ST[/B] (Archive.org)",'https://archive.org/details/Atari_ST_TOSEC_2012_04_23',5,'http://jscustom.theoldcomputer.com/images/manufacturers_systems/Atari/ST/624674atarifalcon.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/3/39/Atari_1040STf.jpg')
	addDir("[B]Bandai Wonderswan[/B] (Archive.org)",'https://archive.org/details/Bandai_Wonderswan_TOSEC_2012_04_23',5,'http://jscustom.theoldcomputer.com/images/manufacturers_systems/Bandai/Wonderswan/590187wonderswan.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/0/0f/Wonderswan_color-JD.jpg')
	addDir("[B]Magnavox Odyssey 2 & Philips Videopac G7000[/B] (Archive.org)",'https://archive.org/details/Magnavox_Odyssey_2_TOSEC_2012_04_23',5,'http://www.videopac.org/G7000/g7kbut.gif',1,'http://upload.wikimedia.org/wikipedia/commons/2/2d/Magnavox-Odyssey-2-Console-Set.jpg')
	addDir("[B]NEC PC-Engine & TurboGrafx 16[/B] (Archive.org)",'https://archive.org/details/NEC_PC-Engine_TurboGrafx-16_TOSEC_2012-04-23',5,'http://media.fnintendo.net/jabun//nec_turbografx_turbopad.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/d/d0/TurboGrafx16-Console-Set.jpg')
	addDir("[B]NEC SuperGrafx[/B] (Archive.org)",'https://archive.org/details/NEC_SuperGrafx_TOSEC_2012_04_23',5,'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Supergraphx.jpg/280px-Supergraphx.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/b/bf/SuperGrafx-Console-Set.jpg')
	addDir("[B]Nintendo Super Famicom[/B] (Archive.org)",'https://archive.org/details/Super_Famicom_and_Super_Entertainment_System_TOSEC_2012_04_14',5,'https://girlsofwar.files.wordpress.com/2010/12/superfamicom.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/e/e1/Super-Famicom-Console-Set.jpg')
	addDir("[B]Sega Mark III & Sega Master System[/B] (Archive.org)",'https://archive.org/details/Sega_Mark_III_and_Master_System_TOSEC_2012_04_13',5,'http://upload.wikimedia.org/wikipedia/commons/9/98/Sega_MarkIII_Joypad.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/d/dc/Sega_Mark_III.jpg')
	addDir("[B]Sega MegaDrive[/B] (Archive.org)",'https://archive.org/details/Sega_Megadrive_and_Genesis_TOSEC_2012_04_13',5,'http://blog.techcore.co.mz/wp-content/uploads/megadrive-official-original-sega-controller-25-p.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/6/6a/Sega-Genesis-Mk2-6button.jpg')
	addDir("[B]Sega 32x[/B] (Archive.org)",'https://archive.org/details/Sega_32x_TOSEC_2012_04_13',5,'http://www.powersonic.com.br/outros/especiais/media/32x_2.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/a/a0/Sega-Genesis-Model2-32X.jpg')
	addDir("[B]Sony MSX MSX2+[/B] (Archive.org)",'https://archive.org/details/MSX_MSX_Plus_TOSEC_2012_04_23',5,'http://s2.subirimagenes.com/otros/previo/thump_5587710img0923.jpg',1,'http://www.msxarchive.nl/pub/msx/photos/hardware/Sony_HB-F1XV_12.JPG')
	addDir("[B]Acorn Archimedes[/B] (Archive.org)",'https://archive.org/details/Acorn_Archimedes_TOSEC_2012_04_23',5,'http://chrisacorns.computinghistory.org.uk/Pics/A3101B.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/b/b5/Acorn_Archimedes_A3000_Computer_Main_Unit.jpg')
	addDir("[B]Amiga CDTV[/B] (Archive.org)",'https://archive.org/details/Amiga_CDTV_TOSEC_2009_04_18',5,'http://www.amigahistory.plus.com/cdtv.jpg',1,'http://oldcomputers.net/pics/cdtv-right.jpg')
	addDir("[B]Amstrad CPC[/B] (Archive.org)",'https://archive.org/details/Amstrad_CPC_TOSEC_2012_04_23',5,'http://www.old-computers.com/museum/photos/cpc464.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/9/91/Amstrad_CPC464.jpg')
	addDir("[B]Apple II[/B] (Archive.org)",'https://archive.org/details/Apple_2_TOSEC_2012_04_23',5,'http://oldcomputers.net/pics/appleii-system.jpg',1,'http://www.cs.columbia.edu/~sedwards/apple2fpga/Apple-II.jpg')
	addDir("[B]Apple IIgs[/B] (Archive.org)",'https://archive.org/details/Apple_II_GS_TOSEC_2012_04_23',5,'http://www.old-computers.com/museum/photos/apple_IIgs.jpg',1,'http://computers.popcorn.cx/apple/apple-ii/iigs/iigs-01.jpg')
	addDir("[B]Bally Professional Arcade & Astrocade [/B] (Archive.org)",'https://archive.org/details/Bally_Professional_Arcade_and_Astrocade_TOSEC_2012_04_23',5,'http://www.old-computers.com/museum/photos/bally_astrocade_1.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/5/5d/Bally-Arcade-Console.jpg')
	addDir("[B]Camputers Linx [/B] (Archive.org)",'https://archive.org/details/Camputers_Lynx_TOSEC_2012_04_23',5,'http://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Camputers_Lynx_48k_(white_background).jpg/350px-Camputers_Lynx_48k_(white_background).jpg',1,'http://www.heydon.org/kevan/collection/pictures/camputers-lynx-large.jpg')
	addDir("[B]Coleco ColecoVision [/B] (Archive.org)",'https://archive.org/details/Coleco_ColecoVision_TOSEC_2012_04_23',5,'http://www.old-computers.com/museum/photos/coleco_colecovision_1.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/3/37/ColecoVision.jpg')
	addDir("[B]Commodore C64[/B] (Archive.org)",'https://archive.org/details/Commodore_C64_TOSEC_2012_04_23',5,'http://www.geekvintage.com/images/commodore-64-system.jpg',1,'http://classiccmp.org/dunfield/c64/h/complete.jpg')
	addDir("[B]Commodore C-128[/B] (Archive.org)",'https://archive.org/details/Commodore_C128_TOSEC_2012_04_23',5,'http://www.qsl.net/hb9xch/computer/commodore/C128.jpg',1,'http://en.academic.ru/pictures/enwiki/67/Commodore_128_002.jpg')
	addDir("[B]Commodore VIC-20[/B] (Archive.org)",'https://archive.org/details/Commodore_VIC20_TOSEC_2012_04_23',5,'http://www.commodore.ca/gallery/brochures/vic-20/VIC-20_friendly_brochure_p1.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/3/39/CBMVIC20P8.jpg')
	addDir("[B]Commodore C16, C116 & Plus-4 [/B] (Archive.org)",'https://archive.org/details/Commodore_C16_C116_Plus_4_TOSEC_2012_04_23',5,'http://www.richardlagendijk.nl/foto/cnp/Commodore_C116.jpg',1,'http://jscustom.theoldcomputer.com/images/manufacturers_systems/Commodore/Plus4-C16-C116/361875commodore-plus4.system.jpg')
	addDir("[B]Commodore Amiga[/B] (Archive.org)",'https://archive.org/details/Commodore_Amiga_TOSEC_2012_04_10',5,'http://www.old-computers.com/museum/photos/commodore_amiga-500.jpg',1,'http://p1.pichost.me/i/5/1278747.png')
	addDir("[B]Epoch Super Cassette Vision[/B] (Archive.org)",'https://archive.org/details/Epoch_Super_Cassette_Vision_TOSEC_2012_04_23',5,'http://static.giantbomb.com/uploads/original/11/117006/1757954-super_cassette_vision.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/2/21/Super-Cassette-Vision-Console-L.jpg')
	addDir("[B]Sinclair ZX81[/B] (Archive.org)",'https://archive.org/details/Sinclair_ZX81_TOSEC_2012_04_23',5,'http://upload.wikimedia.org/wikipedia/commons/8/8a/Sinclair-ZX81.png',1,'http://upload.wikimedia.org/wikipedia/commons/e/e0/Sinclair-ZX81-Rama.jpg')
	addDir("[B]Sinclair QL[/B] (Archive.org)",'https://archive.org/details/Sinclair_QL_TOSEC_2012_04_23',5,'http://oldcomputers.net/pics/ql-2.jpg',1,'http://www.classic-computers.org.nz/blog/images/08-10-04-sinclair-ql-web.jpg')
	addDir("[B]Sega Visual Memory System[/B] (Archive.org)",'https://archive.org/details/Sega_Visual_Memory_System_TOSEC_2012_04_23',5,'http://jscustom.theoldcomputer.com/images/manufacturers_systems/Sega/Visual-Memory-Unit/654287VMU.jpg',1,'http://upload.wikimedia.org/wikipedia/commons/e/e2/Sega-Dreamcast-Cont-n-VMU.jpg')
	addDir("[B]Tandy TRS-80 Color Computer [/B] (Archive.org)",'https://archive.org/details/Tandy_TRS80_Color_Computer_TOSEC_2012_04_23',5,'http://www.radioshackcatalogs.com/images/computer/trs-80_color_computer.gif',1,'http://upload.wikimedia.org/wikipedia/commons/4/47/TRS-80_Color_Computer_3.jpg')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
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
			elif 'sega_sms_' in url:
				console_fanart = 'http://cloud-4.steamusercontent.com/ugc/46493803785332279/AA4F9D55545B2C15A21C94FA21193EA034F4BC6E/'
				addDir(translate(30002),'https://archive.org/details/sega_sms_library?and[]=',2,'',1,console_fanart)
			elif 'sega_genesis' in url:
				console_fanart = 'http://thegamesdb.net/banners/platform/fanart/18-3.jpg'
				addDir(translate(30002),'https://archive.org/details/sega_genesis_library?and[]=',2,'',1,console_fanart)
			elif 'atari_2600' in url:
				console_fanart = 'http://thegamesdb.net/banners/platform/fanart/22-3.jpg'
				addDir(translate(30002),'https://archive.org/details/atari_2600_library?and[]=',2,'',1,console_fanart)
			elif 'gamegear' in url:
				console_fanart = 'http://thegamesdb.net/banners/platform/fanart/20-2.jpg'
				addDir(translate(30002),'https://archive.org/details/gamegear_library?and[]=',2,'',1,console_fanart)
			elif 'vtech_creativision' in url:
				console_fanart = 'http://www.videogameconsolelibrary.com/images/1980s/81_VTech_CreatiVision/vtech_creativision_15.jpg'
				addDir(translate(30002),'https://archive.org/details/vtech_creativision_library?and[]=',2,'',1,console_fanart)
			elif 'socrates_' in url:
				console_fanart = 'http://media.engadget.com/img/product/19/f4r/socrates-1h3m-800.jpg'
				addDir(translate(30002),'https://archive.org/details/socrates_library?and[]=',2,'',1,console_fanart)
			elif 'ngp_' in url:
				console_fanart = 'http://i.imgur.com/4dPue.jpg'
				addDir(translate(30002),'https://archive.org/details/ngp_library?and[]=',2,'',1,console_fanart)
			elif 'atari_7800_' in url:
				console_fanart = 'http://thegamesdb.net/banners/platform/fanart/27-1.jpg'
				addDir(translate(30002),'https://archive.org/details/atari_7800_library?and[]=',2,'',1,console_fanart)
			elif 'atari_5200_' in url:
				console_fanart = 'http://upload.wikimedia.org/wikipedia/commons/e/e6/Atari_5200_-_trojandan_14871272.jpg'
				addDir(translate(30002),'https://archive.org/details/atari_5200_library?and[]=',2,'',1,console_fanart)
			elif 'gx4000_' in url:
				console_fanart = 'http://fc07.deviantart.net/fs71/i/2012/058/4/9/amstrad_gx4000_by_mellergaard-d4r5bil.jpg'
				addDir(translate(30002),'https://archive.org/details/gx4000_library?and[]=',2,'',1,console_fanart)
			elif 'gx4000_' in url:
				console_fanart = 'http://upload.wikimedia.org/wikipedia/commons/b/b8/Sega_SG-1000_Bock.jpg'
				addDir(translate(30002),'https://archive.org/details/sg_1000_library?and[]=',2,'',1,console_fanart)
			elif 'megaduck_' in url:
				console_fanart = 'http://i.ytimg.com/vi/qHT4n1kgqyU/maxresdefault.jpg'
				addDir(translate(30002),'https://archive.org/details/megaduck_library?and[]=',2,'',1,console_fanart)
			elif 'intellivision' in url:
				console_fanart = 'http://thegamesdb.net/banners/platform/fanart/32-1.jpg'
				addDir(translate(30002),'https://archive.org/details/intellivision?and[]=',2,'',1,console_fanart)
			elif 'mattelaquarius' in url:
				console_fanart = 'http://www.zock.com/8-Bit/Ad_Aquarius.JPG'
				addDir(translate(30002),'https://archive.org/details/mattelaquarius?and[]=',2,'',1,console_fanart)
			elif 'channelf_' in url:
				console_fanart = 'http://upload.wikimedia.org/wikipedia/commons/5/56/Fairchild-Channel-F-System-II-Console.jpg'
				addDir(translate(30002),'https://archive.org/details/channelf_library?and[]=',2,'',1,console_fanart)
			elif 'apfm1000_' in url:
				console_fanart = 'http://atariage.com/forums/uploads/monthly_11_2010/post-10944-128979518522.jpg'
				addDir(translate(30002),'https://archive.org/details/apfm1000_library?and[]=',2,'',1,console_fanart)
			elif 'emerson_arcadia' in url:
				console_fanart = 'http://i.ytimg.com/vi/j4o31uRZs3w/maxresdefault.jpg'
				addDir(translate(30002),'https://archive.org/details/emerson_arcadia_library?and[]=',2,'',1,console_fanart)
			elif 'adventurevision_' in url:
				console_fanart = 'http://www.miniarcade.com/ebay/adventurevision3.jpg'
				addDir(translate(30002),'https://archive.org/details/adventurevision_library?and[]=',2,'',1,console_fanart)
			elif 'gamepocket_' in url:
				console_fanart = 'http://www.chrismcovell.com/GamePokekon/Epoch_System.jpg'
				addDir(translate(30002),'https://archive.org/details/gamepocket_library?and[]=',2,'',1,console_fanart)
				
				
				
				
				
				
				
				
				
			
			year = 0
			for gameinfo in matchgames:
				title = re.compile('title=".+?">(.+?)</a>').findall(gameinfo)
				
				ignore_list = ['sega_sms_','socrates_','superacan_','ngp_','atari_7800_','atari_5200','gx4000_','sg_1000','megaduck_','intellivision','mattelaquarius','channelf_','apfm1000_','emerson_arcadia_','adventurevision_','gamepocket_']
				ignore = False
				for platform in ignore_list:
					if platform in url: ignore = True
				
				if selfAddon.getSetting('img-resolution') == '0' and not ignore:
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
	print url
	source = json.load(urllib2.urlopen(url))
	d1 = source["d1"]
	dire = source["dir"]
	files = source["files"]
	rom = ''
	for _file_ in files:
		if _file_["name"].endswith('.zip') or _file_["name"].endswith('.bin') or _file_["name"].endswith('.cpr'):
			rom = _file_["name"]
			break
		else: pass
	if not rom:
		for _file_ in files:
			if _file_["name"].endswith('.torrent'):
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
		elif '_VTL' in download_url: destination_folder = os.path.join(downloadPath,'vtechcreativision')
		elif 'socrates_' in download_url: destination_folder = os.path.join(downloadPath,'socrates')
		elif 'sa_' in download_url: destination_folder = os.path.join(downloadPath,'superacan')
		elif 'segasms_' in download_url: destination_folder = os.path.join(downloadPath,'segams')
		elif 'ngp_' in download_url: destination_folder = os.path.join(downloadPath,'neogeopocket')
		elif '_NTSC' in download_url: destination_folder = os.path.join(downloadPath,'atari7800')
		elif '_Atari' in download_url: destination_folder= os.path.join(downloadPath,'atari5200')
		elif 'gx4000_' in download_url: destination_folder =  os.path.join(downloadPath,'amstradgx4000')
		elif '_Sega_' in download_url: destination_folder =  os.path.join(downloadPath,'segasg1000')
		elif '_Sachen' in download_url or '_Commin' in download_url or '_Timlex' in download_url: destination_folder = os.path.join(downloadPath,'megaduck')
		elif 'intv_' in download_url: destination_folder = os.path.join(downloadPath,'intellivision')
		elif 'Mattel' in download_url or '_Microsoft' in download_url or '_proto' in download_url: destination_folder = os.path.join(downloadPath,'mattelaquarius')
		elif '_Fairchild' in download_url or '_E5frog' in download_url or '_Riddle' in download_url or '_Zircon' in download_url: destination_folder = os.path.join(downloadPath,'channelF')
		elif 'apfm1000' in download_url: destination_folder=os.path.join(downloadPath,'apfm1000')
		elif 'arcadia_' in download_url: destination_folder=os.path.join(downloadPath,'arcadia')
		elif 'advision_' in download_url: destination_folder=os.path.join(downloadPath,'adventurevision')
		elif 'gamepocket' in download_url: destination_folder=os.path.join(downloadPath,'gamepocket')
		
		
		
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
		
	
def get_zip_info(url,iconimage):
	try:
		page_source = get_page_source(url)
	except: page_source = None
	if page_source:
		match = re.compile('<div class="down-size">(.+?)</div>\n.+?<a href="(.+?)">ZIP</a>').findall(page_source)
		for size,urltmp in match:
			if 'http://' not in urltmp or 'https://' not in urltmp: urltmp = 'http://archive.org'+urltmp
			addDir(translate(30017)+size+')',urltmp,6,iconimage,1,'',False)
			
def download_zip_package(name,url,iconimage):
	if selfAddon.getSetting('download-folder') == '':
		downloadPath = xbmcgui.Dialog().browse(int(3), 'Select Download Folder','myprograms')
		selfAddon.setSetting('download-folder',downloadPath)
	else: downloadPath = selfAddon.getSetting('download-folder')
	download_subfolder = url.split('/')[4]
	destination_folder = os.path.join(downloadPath,download_subfolder)
	if not os.path.exists(destination_folder): xbmcvfs.mkdir(destination_folder)
	rom = url.split('/')[-1]
	destination_file = os.path.join(destination_folder,rom)
	download_tools().Downloader(url,destination_file,translate(30007) + rom,translate(30000))
	msgok(translate(30000),translate(30005) + destination_folder,translate(30006))
	
	
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
elif mode==5: get_zip_info(url,iconimage)
elif mode==6: download_zip_package(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
