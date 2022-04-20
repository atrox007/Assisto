import os
import pyttsx3
#Smart App Launcher- Windows version
print("Welcome to Assisto, I will help you in your work.")
pyttsx3.speak("Welcome to Assisto, I will help you in your work.")
print()
while(True):
	pyttsx3.speak("What can I do for you ?")
	x=input("What can I do for you ?")
	pres = ( ("launch" in x) or ("start" in x) or ("run" in x) or ("execute" in x) or ("open" in x) )
	
	if( ("how" in x) and ("you" in x) ):
		pyttsx3.speak("I am fine. What about you ?")
		print("I am fine. What about you ?")
		continue

	if( ("i" in x) and ("fine" in x) ):
		pyttsx3.speak("great")
		print("Great")
		continue

	if(pres):
		if( ("notepad" in x) or ("editor" in x) or ("notes" in x) ):
			os.system("START /B notepad")
		elif ( ("firefox browser" in x) or ("firefox" in x) ):
			os.system("START /B firefox")
		elif ( ("edge browser" in x) or ("msedge" in x) ):
			os.system("START /B msedge")
		elif ( ("chrome" in x) or ("browser" in x) ): 
			os.system("START /B chrome")
		elif ( ("video converter" in x) ):
			os.system("START /B tvcshell")
		elif ( ("ide" in x) or ("sublime text" in x) ):
			os.system("START /B sublime_text")
		elif ( ("skype" in x) or ("video conferencing" in x) ):
			os.system("START /B skype")
		elif ( ("vmware" in x) or ("virtualisation" in x) ):
			os.system("START /B vmware")
		elif ( ("pdf" in x) or ("reader" in x) ):
			os.system("START /B AcroRd32")
		elif ( ("google earth" in x) ):
			os.system("START /B googleearth")
		elif ( ("shareit" in x) or ("file sharing" in x) ):
			os.system("START /B SHAREit")
		elif( ("download" in x) or ("fdm" in x) ):
			os.system("START /B fdm")
		elif ( ("windows update" in x) or ("wuapp" in x) ):
			os.system("START /B wuapp")
		elif ( ("calc" in x) or ("calculator" in x) ):
			os.system("START /B calc")
		elif ( ("wmplayer" in x) or ("windows media player" in x) ):
			os.system("START /B wmplayer")
	elif( ("close" in x) or ("terminate" in x) or ("dont" in x) or ("kill" in x) ):
		if("notepad" in x):
			os.system("taskkill /im notepad.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("firefox" in x):
			os.system("taskkill /im firefox.exe /F")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("chrome" in x):
			os.system("taskkill /im chrome.exe /F")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif(("edge" in x) or ("msedge" in x) ):
			os.system("taskkill /im msedge.exe /F")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("video converter" in x):
			os.system("taskkill /im tvcs.exe /F")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif( ("windows media" in x) or ("wmplayer" in x) ):
			os.system("taskkill /im wmplayer.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("vlc" in x):
			os.system("taskkill /im vlc.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("vmware" in x):
			os.system("taskkill /im vmware.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("sublime" in x):
			os.system("taskkill /im sublime_text.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("reader" in x):
			os.system("taskkill /im AcroRd32.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("skype" in x):
			os.system("taskkill /im skype.exe /f")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("google earth" in x):
			os.system("taskkill /im googleearth.exe /f")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("share it" in x):
			os.system("taskkill /im SHAREit.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("fdm" in x):
			os.system("taskkill /im fdm.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("windows update" in x):
			os.system("taskkill /im wuapp.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("mspaint" in x):
			os.system("taskkill /im mspaint.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("msword" in x):
			os.system("taskkill /im WINWORD.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("msexcel" in x):
			os.system("taskkill /im EXCEL.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif("power point" in x):
			os.system("taskkill /im POWERPNT.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
		elif(("calculator" in x) or ("calc" in x)):
			os.system("taskkill /im calc.exe")
			print("Program terminated")
			pyttsx3.speak("Program terminated")
	elif ( (pres or ("play" in x) ) and ( ("media player" in x) or ("music" in x) or ("songs" in x) or ("vlc" in x) ) ):
		os.system("START /B vlc")
	elif( ( pres or ("make" in x) or("want" in x) ) and ("draw" in x) or ("drawings" in x) or ("paint" in x) or ("mspaint" in x) or ("paintings" in x) ):
		os.system("START /B mspaint")
	elif ( (pres or ("create" in x) ) and ( ("document" in x) or ("word" in x) or ("msword" in x)) ):
		os.system("START /B WINWORD")
	elif ( (pres or ("create" in x) ) and ( ("spreadsheet" in x) or ("excel" in x) or ("data entry" in x)) ):
		os.system("START /B EXCEL")
	elif ( (pres or ("create" in x) ) and ( ("presentation" in x) or ("power point" in x) ) ):
		os.system("START /B POWERPNT")
	elif ( ("exit" in x) or ("quit" in x) or ("terminate" in x) or ("bye" in x) or ("good night" in x) or ("take rest" in x) ):
		print("Have a nice day.")
		pyttsx3.speak("have a nice day")
		break	
	elif( ("i" in x ) and ("tired" in x)):
		print("You should take rest")
		pyttsx3.speak("You should take rest")
		break
	else:
		print("Sorry, I couldn't understand what you want to do.")
		pyttsx3.speak("Sorry, I couldn't understand what you want to do.")

	
