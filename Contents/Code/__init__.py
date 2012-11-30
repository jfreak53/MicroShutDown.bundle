from PMS import *



####################################################################################################
def Start():
	MediaContainer.thumb = R("icon-default.png")
	DirectoryItem.thumb = R("icon-default.png")
	
	
####################################################################################################
@handler("/applications/microshutdown", "Turn off Media Server")
def MainMenu():
	dir = MediaContainer(title1="Turn Off Media Server")
	dir.Append(Function(DirectoryItem(ShutDown, title="Shutdown")))
	dir.Append(PrefsItem(title="Settings"))
	return dir

####################################################################################################
	
def ShutDown(sender):

	command = "shutdown.sh"
	Helper.Run(command)
	return
			
