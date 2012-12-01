import os
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

ICON = 'icon-default.png'

####################################################################################################
def Start():
	Plugin.AddPrefixHandler("/video/microshutdown", MainMenu, "Turn off Server", ICON)
	Plugin.AddViewGroup('List', viewMode='List', mediaType='items')

	MediaContainer.thumb = R(ICON)
	DirectoryItem.thumb = R(ICON)
	
	
####################################################################################################
def MainMenu():
	dir = MediaContainer(viewGroup="List")
	dir.Append(Function(DirectoryItem(ShutDown, "Shutdown", subtitle="Shutdown the Server Now", thumb=R(ICON))))
	dir.Append(PrefsItem(title="Settings"))
	return dir

####################################################################################################
	
def ShutDown(sender):

	os.system("sudo shutdown -h now")
	#os.system("shutdown /s /t 0")
	return MessageContainer("MicroShutDown", "Shutdown command executed, Goodbye.")
