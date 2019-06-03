# AutoSource

AutoSource is an automated source code review framework integrated with SonarQube which is capable of performing static code analysis/reviews. It can be used for effectively finding the vulnerabilities at very early stage of the SDLC(Software Development Life Cycle). The user can scan the code by just giving GIT repository link into the framework. 

AutoSource framework is capable of performing source code review on all platforms(MAC, Linux and Windows).  

## INSTALL

1. Download the AutoSource repository into your system.
2. Read the prerequisites.txt file and install the dependencies (mentioned for each platform)
3. Execute downloadSonar.py (python3 downloadSonar.py), this will download and setup the SonarQube framework which can be access from 'http://127.0.0.1:9000'
4. After that run executeScanner.py (python3 executeScanner.py), this will ask for your GIT repository that you want to scan.
5. Access the results on SonarQube Portal('http://127.0.0.1:9000')


## Screenshots

### Downloading SonarQube and SonarScanner
![Downloading SonarQube and SonarScanner](/images/downloadSonar.png)

### SonarQube is up and running
![SonarQube is Up and Running](/images/sonarIsUp.png)

### Executing Scanner
![Executing SonarScanner](/images/executeScanner.png)

### Scanning Started
![SonarScanning Started](/images/executingScript.png)

### Scanner Execution Successful
![Scanner Execution Successful](/images/scannerExecutionSuccess.png)

### Results showing in SonarQube Dashboard
![Results showing in SonarQube Dashboard](/images/resultInSonar.png)

## Collaborators
* [Malkit Singh](https://www.linkedin.com/in/malkit-singh-oscp-crest-cpsa-crt-4005b916/)
* [Shubham Shubhankar Sharma](https://www.linkedin.com/in/shubham-subhankar-sharma-4b410695/)
