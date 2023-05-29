from utils.http_methods import HttpMethod

"""The methods for testing Google Maps API (simulator)"""

base_url = "https://rahulshettyacademy.com"         # Base URL
key = "?key=qaclick123"                             # The parameter for all requests

class GoogleMapsApi():

    """Creating a new place on the Google Map (the POST method)"""

    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
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

        post_resource = "/maps/api/place/add/json"      # The POST method resource
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethod.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post


    """Checking a new place on the Google Map (the GET method)"""

    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json"       # The GET method resource
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethod.get(get_url)
        print(result_get.text)
        return result_get

    """Updating a new place on the Google Map (the PUT method)"""

    @staticmethod
    def put_new_place(place_id):

        put_resource = "/maps/api/place/update/json"       # The PUT method resource
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100, Svetlaya street, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethod.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put


    """Deleting an updated place on the Google Map (the DELETE method)"""

    @staticmethod
    def delete_new_place(place_id):

        delete_resource = "/maps/api/place/delete/json"       # The DELETE method resource
        put_url = base_url + delete_resource + key
        print(put_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = HttpMethod.delete(put_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete