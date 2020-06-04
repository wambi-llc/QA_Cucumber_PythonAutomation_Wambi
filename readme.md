#Project Overview

For this automation framework, we are using a behave-Cucumber framework with Python. 
Framework structure is set using a Page Object Model.

Feature Files: 
 Feature files will include Scenarios in English Gherkin structure. 
 Test IDs will be added as tags for each Test Case
 @UI-Regression tag can be added to all UI Test Cases that will be part of regression. 
 UI and API feature files will be separated into separate folders API and UI Folders.
 In our application. For Team Member Login Each Tab will be organized as a feature file.
 
Step Definition Files: 
 These files will include step implementations for each step in the feature file. 
 
PageElements Folder: 
 Page Elements files will include all the xpaths for all the available elements under each tab. 
 Here we are simply setting the xpaths equal to a variable that we can call in step files as needed. 
 
Utilities
 Config.py file will include testing urls, username, passwords and any other config information needed 
 driverUtil.py: driver and common methods are written in this file. We can create wrappers around basic
 selenium methods to customize them based on our requirements. 
 
 





#Installation

--Python Installation
1. Download and install Python on your computer from 
https://www.python.org/downloads/

--IDE Setup
2. Download Pycharm IDE Professional Version
3. Open the automation project in Pycharm.
4. If on Mac install Homebrew on your computer by running the following command
on your terminal. 
'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"'

--Installing ChromeDriver
5. Use the following brew command to install chromedriver on Mac 
'brew cask install chromedriver'
6. If on Windows (or on Mac but brew command doesnt work) download
the chromedriver from https://chromedriver.chromium.org/ 
7. Then add the downloaded chromedriver in the local bin folder
 /usr/local/bin. 
8. Make sure /usr/local/bin system path is set. To check on Mac: 
Open Terminal. 
Enter following command 'sudo nano /etc/paths'
Enter Password. 
Validate /usr/local/bin is present. 
If not, add '/usr/local/bin' at the bottom and Press Ctrl X when done and
press 'Y' to Save

--Installing all the requirements
9. Navigate back to Pycharm and open its 
terminal and run following command to install all the requirements in 
requirements.txt 'pip install -r requirements.txt'


#Setting Up Runner to Run files
1. On the top right of pycharm click on Add Configurations
2. Add Path to your feature file here. 
3. If running specific scenario add <@tag> for that scenario in Scenario field
4. Python Interpreter: Choose the python interpreter available
5. In working directory add path to you steps definition folder. 



#Report Generation
Will update this sections once Allure report generation has been implemented.  