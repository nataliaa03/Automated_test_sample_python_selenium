# Test sample - Python Selenium for a random web application

This is an exmple of an autmated test using Selenium Framework. It includes two test cases:


TC1 - login with valid login and pasword <br>
TC2a - login with invalid password. <br>
<br>
I used page object pattern in the framework. As a logging and report form I used allure which generates reports after running tests in html file (it is OPTIONAL - see below). <br>
The test can be run on Chrome and Firefox.


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

<br>
<br>

## Run Tests
# Requirements: 
docker installed on your machine

# To start the container use command:
`docker-compose up -d` -> then you are able to go to http://localhost:4444/ and see sessions with tests run.

# To start tests use command:
```
$ python -m pytest --tb=short tests/test_login.py
```
You need to have /tests as a working directory


<br>
<br>
<br>

### [OPTIONAL] Allure (Test Reportng) - installation

1. You need to have java JDK installed on your system (and Set JAVA_HOME in PATH variables).
2. Install allure on your system (to use allure as a command you need also add it to PATH) - https://github.com/allure-framework/allure2/releases


### Generate Test Report

To generate all tests report using Allure you need to run tests by command first:
```
$ python3 -m pytest --alluredir=<reports directory path>
```
After that you need to use command:
```
$ allure serve <reports directory path>
```
Remember that if you did not add allure to system PATH instead of "allure" you need to type all the path of the directory where allure/bin is in your system,
for exmple (Linux) run this command in your project directory:
```
$ ~/*/allure-2.13.8/bin/allure serve report

```
where "report" is the directory with report in the project file.
Report is generated in Chrome browser.
