# Checklist for automation testing API of Google Maps simulator.

This checklist provides a step-by-step guide for testing the Google Maps Simulator API.

## 1. Creating a new place on the Google Map (the POST method):

	- Ensure that the status code is 200.
	- Verify that all required fields in the response are present.
	- Validate the correctness of the required field 'status'.

## 2. Checking a new place on the Google Map (the GET method):

	- Ensure that the status code is 200.
	- Verify that all required fields in the response are present.
	- Validate the correctness of the required field 'address'.
	
## 3. Updating a new place on the Google Map (the PUT method):

	- Ensure that the status code is 200.
	- Verify that all required fields in the response are present.
	- Validate the correctness of the required field 'msg'.

## 4. Checking an updated place on the Google Map (the GET method):

	- Ensure that the status code is 200.
	- Verify that all required fields in the response are present.
	- Validate the correctness of the required field 'address'.
	
## 5. Deleting an updated place on the Google Map (the DELETE method):

	- Ensure that the status code is 200.
	- Verify that all required fields in the response are present.
	- Validate the correctness of the required field 'status'.
	
## 6. Checking a place on the Google Map with the deleted place_id (the GET method) - negative testing:

	- Ensure that the status code is 404.
	- Verify that all required fields in the response are present.
	- Check if the word "failed" is present in the required field 'msg'.
