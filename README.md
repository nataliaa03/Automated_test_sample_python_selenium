# python_selenium_netguru_task2
Task nr2 - two of test scenarios automated. As an example I used timeanddate random application with simple login and registration form.
I decided to automate TC1 - login with valid login and pasword and TC2a - login with invalid password
I used page object pattern in the framework. As a logging and report form I used allure which generates reports after running tests in html file (see below).
The test can be run on popular browsers - Chrome and Firefox.


## Project Structure
Here you can find a short description of main directories and it's content
- [locators](locators) - there are locators of web elements in locators.py grouped in classes
- [pages](pages) - there are sets of method for each test step (notice: some repeated methods were moved to [functions.py](utils/functions.py))
- [tests](tests) - there are sets of tests for main functionalities of website
- [reports](reports) - if you run tests with Allure, tests reports will be saved in this directory
- [utils](utils) - this directory contains files responsible for configuration, e.g. driver_factory.py for webdriver management or [read_xlsx.py](utils/read_xlsx.py) for reading input data from xlsx files included in project



## Getting Started

- download the project or clone repository. 
- install packages using pip according to requirements.txt file.

Using LInux:
```
$ python3 -m pip install -r requirements.txt
```

Using Windows:
```
$ pip install -r requirements.txt
```


## Run Automated Tests

```
$ pip install -r requirements.txt
```

## Html report by allure
1. You need to have java JDK installed on your system (and Set JAVA_HOME in PATH variables).
2. install allure on your system (to use allure as a command you need also add it to PATH) - see below.

## Running test
1. you need to have /tests as a working directory
```
$ python3 -m pytest test_login.py
```


### If you use Pycharm:

To run selected test without Allure report you need to set pytest as default test runner in Pycharm first
```
File > Settings > Tools > Python Integrated Tools > Testing
```
After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow. 


## Generate Test Report

To generate all tests report using Allure you need to run tests by command first:
```
$ pytest --alluredir=<reports directory path>
```
After that you need to use command:
```
$ allure serve <reports directory path>
```

Report is generated in Chrome browser.
