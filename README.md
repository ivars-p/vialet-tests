Test automation project for web-application: 'https://vialet.pl/'
=======================================

The following tests are automated:
----------------------------------


- 1.Scenario: Registration form - User Interface - L1

Requirements
-------------
- Python 
- Browser on which to execute tests 'chrome' preferably

Quick start
-------------

1. Install all required dependencies located in requirements.txt file running comand.

```python
pip3 install -r requirements.txt 
```
2. Run the test automation suit generating report in ./report folder.
```python
python3 -m pytest --html-report=./report/report.html 
```

Troubleshooting
---------------

There can be as scenario where chromedriver is not recognized automatically by the system in that case please copy 
and paste the location path to the following method under //tests/conftest.py
```python
webdriver.Chrome() -> webdriver.Chrome('full path to chromedriver')
```
Possible improvements
---------------
- Create more classes for page objects for example: 'amount_calculator_tool' etc. 
- Add logger for understandable console logs on each test step
- Add assertion error messages
- Save screenshots in report on failed test steps
- Add more configuration options like 'resolution' / 'parallel tests' etc.