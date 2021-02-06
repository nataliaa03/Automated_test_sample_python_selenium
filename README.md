# python_selenium_netguru_task2
Task nr2 - two of test scenarios automated. As an example I used timeanddate random application with simple login and registration form. 

I decided to automate TC1 - login with valid login and pasword and TC2a - login with invalid password. 
I used page object pattern in the framework. As a logging and report form I used allure which generates reports after running tests in html file (see below). 
The test can be run on popular browsers - Chrome and Firefox.


## Project Structure

- [locators](locators) - there are locators of web elements in locators.py grouped in classes
- [pages](pages) - there are sets of method for each test step (webdriver methos are stored in [helpers](helpers) directory)
- [tests](tests) - there are sets of tests for main functionalities of website
- [helpers](helpers) - selelnium webdriver methods stored ready to import and use
- [reports](reports) - if you run tests with Allure, tests reports will be saved in this directory
- [utils](utils) - with drivers.py for webdriver management (Chrome, Firefox)
- config.py - storing paramters for running the tests

## Getting Started

- download the project or clone repository. 
- install packages using pip according to requirements.txt file.

Using Linux:
```
$ python3 -m pip install -r requirements.txt
```

Using Windows:
```
$ pip install -r requirements.txt
```


## Run Tests
In config.py file by entering paramaters you can choose which browser you choose (Chrome and Firefox are available).

You need to have /tests as a working directory
```
$ python3 -m pytest test_login.py
```



### If you use Pycharm:

To run selected test without Allure report you need to set pytest as default test runner in Pycharm first
```
File > Settings > Tools > Python Integrated Tools > Testing
```
After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow. 




### [OPTIONAL] Allure (Test Reportng) - installation 

1. You need to have java JDK installed on your system (and Set JAVA_HOME in PATH variables).
2. Install allure on your system (to use allure as a command you need also add it to PATH) - https://github.com/allure-framework/allure2/releases


### Generate Test Report

To generate all tests report using Allure you need to run tests by command first:
```
$ pytest --alluredir=<reports directory path>
```
After that you need to use command:
```
$ allure serve <reports directory path>
```
Remember that if you did not add allure to system PATH instead of "allure" you need to type all the path of the directory where allure is in your system. 
for exmple:
```
$ cd */allure-2.13.8/bin
$ allure serve <reports directory path>
```

Report is generated in Chrome browser.
