# **Google Maps simulator API Testing Automation Project**

This project is dedicated to automated testing of the Google Maps simulator API. 
The testing API was created by Rahul Shetty and provides the following capabilities:

	- Create locations on the map with specified coordinates and address.
	- Update locations with changes in data about them.
	- Delete locations.

## Project Overview

This project is implemented in Python programming language and includes the following features:

	- Test HTTP methods by sending HTTP requests and checking HTTP responses.
	- Test execution using the Pytest framework.
	- Logging functionality to capture important information in a log file, including date, 
	request method, request URL, response code, response text, response headers
	and response cookies.
	- Generate a detailed report of test results using the Allure framework.

## Getting Started

To set up the project and run the tests, please follow these steps:

	- Clone the project repository to your local machine.
	- Install the required dependencies using pip (command 'pip install pytest').
	- Execute the tests using the provided Pytest command 
	'python -m pytest --alluredir=test_results/ tests/test_google_maps_api.py'.
	- View the generated Allure report to analyze the test results.

For detailed instructions on API requests and responses, refer to the [api.md](./api.md) file.

To see the screenshot with Allure reports, refer to the [allure_report.png](./screenshots/allure_report.png) file.

To see a detailed log of test execution, you can view the log files in /logs, 
which contains information about date, time, requests, responses, and other events during the test execution.

## Checklist

To ensure comprehensive testing coverage, refer to the [checklist.md](./checklist.md) file. 
It provides a list of API checkings that should be performed during the testing process.

## Contact

If you have any questions or inquiries regarding this project, 
please feel free to contact me at liliya_s@ukr.net.