import os
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

ICON = 'icon-default.png'

####################################################################################################
def Start():
	Plugin.AddPrefixHandler("/applications/microshutdown", MainMenu, "Turn off Server", ICON)
	Plugin.AddViewGroup('List', viewMode='List', mediaType='items')

	MediaContainer.thumb = R(ICON)
	DirectoryItem.thumb = R(ICON)
	
	
####################################################################################################
#@handler("/applications/microshutdown", "Turn off Media Server")
def MainMenu():
	dir = MediaContainer(viewGroup="List")
	dir.Append(Function(DirectoryItem(ShutDown, "Shutdown", subtitle="mime", thumb=R(ICON))))
	dir.Append(PrefsItem(title="Settings"))
	return dir

####################################################################################################
	
def ShutDown(sender):

	#command = "shutdown.sh"
	#Helper.Run(command)
	os.system("sudo shutdown -h now")
	return "Done"
