# Vidrip

from PMS import *



####################################################################################################
def Start():
	MediaContainer.thumb = R("icon-default.png")
	DirectoryItem.thumb = R("icon-default.png")
	
	
####################################################################################################
def MainMenu():
	dir = MediaContainer(title1="Turn Off Media Server")
	dir.Append(Function(DirectoryItem(EjectDisc, title="Shutdown")))
	dir.Append(PrefsItem(title="Settings"))
	return dir

####################################################################################################
	
def ShutDown(sender):

	command = "shutdown.sh"
	Helper.Run(command)
	return
			