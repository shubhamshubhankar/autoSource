# AutoSource

AutoSource is an automated source code review framework integrated with SonarQube which is capable of performing static code analysis/reviews. It can be used for effectively finding the vulnerabilities at very early stage of the SDLC(Software Development Life Cycle). The user can scan the code by just giving GIT repository link into the framework. 

AutoSource framework is capable of performing source code review on all platforms(MAC, Linux and Windows).  

## Steps for Setup:

1. Download the AutoSource repository into your system.
2. Read the prerequisites.txt file and install the dependencies (mentioned for each platform)
3. Execute python3 downloadSonar.py, this will download and setup the SonarQube framework which can be access from 'http://127.0.0.1:9000'
4. After that run python3 executeScanner.py, this will ask for your GIT repository that you want to scan.
5. Access the results on SonarQube Portal('http://127.0.0.1:9000')

## Collaborators
* Malkit Singh
* Shubham Shubhankar Sharma
