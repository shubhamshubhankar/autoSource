
#Program to run SonarQube, SonarScanner and ElasticSearch which will scan a repo and provide results. 

from sys import platform
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
import git
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


# Function to download the repository taken as an arguement
# ******************************************************************************************************************

def downloadRepositoryWindows(url):
	# Fetching the arguement from the command line, which contains the real name for the repo

	# Snippet to find the filename from the URL
	[url_first_part,mname]=url.rsplit('/', 1)
	mname = mname.replace('.git','')
	
	# To create new directory used in place of mkdir for keeping the projects
	projectPathWindows = dir_path+'\sonarScanner\\bin\project'
	
	# Create the project here if it doesn't exist
	if not os.path.exists(projectPathWindows):
		os.makedirs(projectPathWindows)

	# Cloning the repo into the path1 variable
	git.Git(projectPathWindows+"\\").clone(url)

	print("\nThe repo has been cloned in our system ............... \n ")

	# Path of the properties file
	propertiesFilePath = dir_path + '\sonarScanner\conf\sonar-scanner.properties'

	# For comparing purposes
	data1 = open(propertiesFilePath,'r')

	# Reading the properties file
	with open(propertiesFilePath, 'r') as file:
		data = file.readlines()

	# Reading the properties File and deleting all the contents in them

	print("\nDeleting Old properties ................ \n")

	f = open(propertiesFilePath, 'r+')
	f.truncate(0)
	data = f.readlines()
	
	#  Appending the properties in the file one by one
	data.append("sonar.sourceEncoding=UTF-8")
	data.append("\n")
	data.append("\n")
	data.append("export SONAR_SCANNER_OPTS=-Xms512m\ -Xmx2048m")
	data.append("\n")
	data.append("\n")
	data.append("sonar.projectKey="+mname)
	data.append("\n")
	data.append("\n")
	data.append("sonar.projectName="+mname)
	data.append("\n")
	data.append("\n")
	data.append("sonar.projectVersion=1.0")
	data.append("\n")
	data.append("\n")
	data.append("sonar.scm.disabled=true")
	data.append("\n")
	data.append("\n")

	#data.append("sonar.nodejs.executable=/usr/local/n/versions/node/11.6.0")
	
	#converting to double slash to write to file
	doubleSlashPathWindows = dir_path.replace('\\', '\\\\')

	data.append("sonar.sources="+doubleSlashPathWindows+"\\\\sonarScanner\\\\bin\\\\project\\\\"+mname)
	data.append("\n")
	data.append("\n")
	data.append("sonar.java.binaries="+doubleSlashPathWindows+"\\\\sonarScanner\\\\bin\\\\project\\\\"+mname)
	data.append("\n")

	# and write everything back
	with open(propertiesFilePath, 'w') as file:
		file.writelines(data)

	# Running the command for scanning the files
	print("\n Running sonar-scanner.bat file. \n Scanning of " +mname+ " repo started ................. \n")
	
	p = Popen(dir_path+"\sonarScanner\\bin\sonar-scanner.bat")
	stdout, stderr = p.communicate()

	# Remaning the project name with current Date and Time
	tempTime = datetime.datetime.now()
	tempTime = tempTime.strftime("%Y-%m-%d--%H-%M")
	os.rename(projectPathWindows+"\\"+mname,projectPathWindows+"\\"+mname+tempTime)


# Function to download the repository taken as an arguement
# ******************************************************************************************************************

def downloadRepositoryUnix(url):
	
	# Snippet to find the filename from the URL
	[url_first_part,mname]=url.rsplit('/', 1)
	mname = mname.replace('.git','')

	subprocess.call("mkdir -p sonarScanner/bin/project",shell=True)
	# Path where you want to download the project
	path2 = dir_path+'/sonarScanner/bin/project/'
	
	
	print("\nDownloading Started ............ \n")  
	# Cloning the repo into the path1 variable
	git.Git(path2).clone(url)

	print("\nThe repo has been cloned in our system .................... \n")

	# Path of the properties file
	propertiesFilePath = dir_path + '/sonarScanner/conf/sonar-scanner.properties'

	# Reading the properties File and deleting all the contents in them

	print("\nDeleting Old properties ................ \n")

	f = open(propertiesFilePath, 'r+')
	f.truncate(0)
	data = f.readlines()

	#  Appending the properties in the file one by one
	data.append("sonar.sourceEncoding=UTF-8")
	data.append("\n")
	data.append("\n")
	data.append("export SONAR_SCANNER_OPTS=-Xms512m\ -Xmx2048m")
	data.append("\n")
	data.append("\n")
	data.append("sonar.projectKey="+mname)
	data.append("\n")
	data.append("\n")
	data.append("sonar.projectName="+mname)
	data.append("\n")
	data.append("\n")
	data.append("sonar.projectVersion=1.0")
	data.append("\n")
	data.append("\n")
	data.append("sonar.scm.disabled=true")
	data.append("\n")
	data.append("\n")

	#data.append("sonar.nodejs.executable=/usr/local/n/versions/node/11.6.0")
	
	data.append("sonar.sources="+dir_path+"/sonarScanner/bin/project/"+mname)
	data.append("\n")
	data.append("\n")
	data.append("sonar.java.binaries="+dir_path+"/sonarScanner/bin/project/"+mname)

	# and write everything back
	with open(propertiesFilePath, 'w') as file:
		file.writelines(data)

	# Running the command for scanning the files

	# Changing the mod for sonarScanner in Unix 

	print("\nChanging the mode of sonarScanner directory ............. \n")
	subprocess.call("chmod -R 777 sonarScanner",shell=True)
	bashCommand = './sonarScanner/bin/sonar-scanner'

	print("\nRunning sonarScanner.sh file.\nScanning of " + mname + " repo started ................. \n")
	# Running the sonarScanner in Unix
	process = subprocess.call(bashCommand, shell=True)
	
	tempTime = str(datetime.datetime.now())
	os.rename(path2+mname,path2+mname+tempTime)




# Function to start the Elastic Search, SonarQube and Download repositories and run sonarScanner in different threads
#***********************************************************************************************************************

if __name__ == '__main__':
	
	# Fetching the arguement from the command line, which contains the real name for the repo
	if len(sys.argv) == 2:
		url = sys.argv[1]	
	elif len(sys.argv) == 1:
		url = input("Enter the valid git URL of the repo you want to download (Should end with .git) ................ \n")
		url = url.strip()
		# If url doesn't ends with .git file
		while not url.endswith(".git"):
			print("\nURL provided is not compatible ..............")
			url = input("Please enter a repo URL ending with .git  ..................\n")
			url = url.strip()


	# Checking the OS of the user's system
	if platform=="darwin":
		print("Mac OS recognised ... \n")	
		Thread(target=runElasticSearchUnix).start()
		time.sleep(8)
		Thread(target=runSonarQubeUnix).start()
		time.sleep(8)
		Thread(target=downloadRepositoryUnix, args=(url,)).start()

	elif platform=="win32" or platform=="win64"  or "win" in platform:
		print("Windows recognised ... \n")
		Thread(target=runElasticSearchAndSonarWindows).start()
		time.sleep(8)
		Thread(target=downloadRepositoryWindows,  args=(url,)).start()


	elif platform=="linux1" or platform=="linux2":
		print("Linux recognised ... \n")	
		Thread(target=runElasticSearchUnix).start()
		time.sleep(8)
		Thread(target=runSonarQubeUnix).start()
		time.sleep(8)
		Thread(target=downloadRepositoryUnix, args=(url,)).start()
	