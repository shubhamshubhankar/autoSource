
#Program to download and scan SonarQube, SonarScanner and ElasticSearch.

import platform
from threading import Thread
import os 
import zipfile
import subprocess
import time
import urllib.request
import sys
import requests
import urllib
import datetime
import random
import requests
from subprocess import Popen


# Get the current directory where the script is running
dir_path = os.path.dirname(os.path.realpath(__file__))

# Function to run Elastic Search Mac OX
def runElasticSearchUnix():
	subprocess.call("chmod -R 777 sonarQube",shell=True)
	subprocess.call("./sonarQube/elasticsearch/bin/elasticsearch", shell=True)
	time.sleep(8)

# Function to run SonarQube Mac OX 
def runSonarQubeUnix():
	subprocess.call("chmod -R 777 sonarQube", shell=True)
	subprocess.call("./sonarQube/bin/macosx-universal-64/sonar.sh console", shell=True)
	time.sleep(8)

# Function to run Elastic Search and SonarQube for Windows
def runElasticSearchAndSonarWindows():
    bit = str(platform.architecture()[0])
    if(bit=="64bit"):
    	# This is path for StartSonar.bat file and will be run from here
    	sonarQubePath = dir_path+ r"\sonarQube\\bin\windows-x86-64\StartSonar.bat"
    elif(bit=="32bit"):
    	# This is path for StartSonar.bat file and will be run from here
    	sonarQubePath = dir_path+ r"\sonarQube\\bin\windows-x86-32\StartSonar.bat"
    
    p = Popen(sonarQubePath)
    p.communicate()
    time.sleep(8)


# Function Report Hook is to show the progress report of the downloading process in the terminal
def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

# Function to download the SonarQube and install it
#***********************************************************************************************************************
def downloadSonarQube():
	if os.path.isdir("sonarQube"):
		print("SonarQube already present in the current directory \n")
	
	else:

		print("Downloading SonarQube from source .......... \n " )
		# URL from where the zip file will be downloaded https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-7.6.zip
		url="https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-7.6.zip"

		filename = "sonarqube-7.6"

		# Name and path of the sonarQube zip file
		path = dir_path + "/" +filename + ".zip"

		# Downloading the zip file from the URL and showing the progress
		urllib.request.urlretrieve(url,path,reporthook)
		print(filename + ".zip has been downloaded in the current directory ...........")

		# Reading the sonarQube zipfile
		zip_ref = zipfile.ZipFile(path, 'r')
		print("Reading "+ filename + ".zip file .........")

		# Extracting the sonarQube zipfile
		zip_ref.extractall(dir_path+"/")
		print("Extracting "+ filename + ".zip file .........")

		# Closing the sonarQube reference
		zip_ref.close()

		# Renaming the name of the folder
		os.rename(filename,"sonarQube")
		print("Renaming "+ filename + ".zip file as sonarQube ..........")


# Function to download the SonarScanner and install it
#***********************************************************************************************************************
def downloadSonarScanner():
	if os.path.isdir("sonarScanner"):
		print("SonarScanner already present in the current directory")
	else:
		print("Downloading SonarScanner from source ..........")

		# Installing the sonarScanner from the source https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492.zip
		url1="https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492.zip"

		filename1 = "sonar-scanner-3.3.0.1492"

		# Name and path of the sonarScanner zip file
		path1 = dir_path + "/" +filename1 + ".zip"

		# Downloading the zip file from the URL and showing the progress
		urllib.request.urlretrieve(url1,path1,reporthook)
		print(filename1 + ".zip has been downloaded in the current directory ...........")

		# Reading the sonarScanner zipfile
		zip_ref1 = zipfile.ZipFile(path1, 'r')
		print("Reading "+ filename1 + ".zip file .........")

		# Extracting the sonarScanner zipfile
		zip_ref1.extractall(dir_path+"/")
		print("Extracting "+ filename1 + ".zip file .........")

		# Closing the sonarScanner reference
		zip_ref1.close()

		# Renaming the name of the 
		os.rename(filename1,"sonarScanner")
		print("Renaming "+ filename1 + ".zip file as sonarScanner ..........")




# Function to start the Elastic Search, SonarQube and Download repositories and run sonarScanner in different threads
#***********************************************************************************************************************

if __name__ == '__main__':
	
	
	# Function to download SonarQube
	downloadSonarQube()
	#Function to download SonarScanner
	downloadSonarScanner()

	# Checking the OS of the user's system
	if sys.platform=="darwin":
		print("Mac OS recognised ... \n")	
		Thread(target=runElasticSearchUnix).start()
		time.sleep(8)
		Thread(target=runSonarQubeUnix).start()
		time.sleep(8)

	elif sys.platform=="win32" or sys.platform=="win64"  or "win" in sys.platform:
		print("Windows recognised ... \n")
		Thread(target=runElasticSearchAndSonarWindows).start()
		time.sleep(8)


	elif sys.platform=="linux1" or sys.platform=="linux2":
		print("Linux recognised ... \n")	
		Thread(target=runElasticSearchUnix).start()
		time.sleep(8)
		Thread(target=runSonarQubeUnix).start()
		time.sleep(8)
	
	
