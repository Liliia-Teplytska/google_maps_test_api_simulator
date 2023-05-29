# **Requirements for Google Maps simulator API**
	
## 1. The POST method

	Base URL: https://rahulshettyacademy.com
	Resource: /maps/api/place/add/json
	The parameter for all requests: key=qaclick123

### REQUEST:
	
	Body:
	{ 
		"location": { 
			"lat": -38.383494, 
			"lng": 33.427362 
		}, 
		"accuracy": 50, 
		"name": "Frontline house", 
		"phone_number": "(+91) 983 893 3937", 
		"address": "29, side layout, cohen 09", 
		"types": [
		"shoe park", 
		"shop"
		],
		"website": "http://google.com", 
		"language": "French-IN"
	}
	
### RESPONSE:
	
	Status code: 200. The request was successfull.
	
	Body:
	{
		"status": "OK",
		"place_id": "dea036e58d6773b3f8bfb256249a1593",
		"scope": "APP",
		"reference": "1f71a23b1374071eecbb70eed1054cf91f71a23b1374071eecbb70eed1054cf9",
		"id": "1f71a23b1374071eecbb70eed1054cf9"
	}

## 2. The GET method

Base URL: https://rahulshettyacademy.com
Resource: /maps/api/place/get/json
The parameters for all requests: key=qaclick123, place_id

### RESPONSE:
	
	1) Status code: 200. The request was successfull.
	
	Body:
	{
		"location": {
			"latitude": "-38.383494",
			"longitude": "33.427362"
		},
		"accuracy": "50",
		"name": "Frontline house",
		"phone_number": "(+91) 983 893 3937",
		"address": "29, side layout, cohen 09",
		"types": "shoe park,shop",
		"website": "http://google.com",
		"language": "French-IN"
	}

	2) Statuc code: 404. Error, there is no location with this place_id.
	
	Body:
	{
		"msg": "Get operation failed, looks like place_id  doesn't exists"
	}

## 3. The PUT method

Base URL: https://rahulshettyacademy.com
Resource: /maps/api/place/update/json
The parameter for all requests: key=qaclick123

### REQUEST:
	
	Body:
	{ 
		"place_id":"c104d917f4b60e2c9a5feda6c9cbf279",
		"address":"100, Svetlaya street, RU", 
		"key":"qaclick123" 
	}

### RESPONSE:
	
	1) Statuc code: 200. The request was successfull.
	
	Body:
	{
		"msg": "Address successfully updated"
	}

	2) Statuc code: 404. Error, there is no location with this place_id.
	
	Body:
	{
		"msg": "Update address operation failed, looks like the data doesn't exists"
	}

## 4. The DELETE method

Base URL: https://rahulshettyacademy.com
Resource: /maps/api/place/delete/json
The parameter for all requests: key=qaclick123

### REQUEST:
	
	Body:
	{ 
		"place_id":"928b51f64aed18713b0d164d9be8d67f" 
	}

### RESPONSE:
	
	1) Statuc code: 200. The request was successfull.
	
	Body:
	{
		"status": "OK"
	}

	2) Statuc code: 404. Error, there is no location with this place_id.
	
	Body:
	{
		"msg": "Delete operation failed, looks like the data doesn't exists"
	}



