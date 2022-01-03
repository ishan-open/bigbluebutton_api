import json
from requests import get, post, put
from requests.exceptions import ConnectionError
from .checksum import checksum_generator
from .query import query_generator
from .parser import parser


class UrlGenerator:
    def __init__(self, base_url, shared_secret):
        self.base_url = base_url
        self.shared_secret = shared_secret

    def url_generator(self, call_name, query_dict):
        query_string = query_generator(query_dict)
        checksum = checksum_generator(call_name, query_string, self.shared_secret)
        url = f"{self.base_url}{call_name}?{query_string}&checksum={checksum}"
        return url

    def get_url(self, call_name, query_dict):
        url = self.url_generator(call_name, query_dict)

        try:
            result = get(url)
            return parser(result.text)
        except ConnectionError:
            raise ConnectionError("No Response!", "Maybe your Server is down or base url is invalid")

    def post_url(self, call_name, query_dict):
        url = self.url_generator(call_name, query_dict)
        try:
            result = post(url)
            return parser(result.text)
        except ConnectionError:
            raise ConnectionError("No Response!", "Maybe your Server is down or base url is invalid")

    # This is Only for GET recording text tracks
    def url_get_recordings_text_track(self, call_name, query_dict):
        try:
            query_string = query_generator(query_dict)
            checksum = checksum_generator(call_name, query_string, self.shared_secret)
            url = f"{self.base_url}{call_name}?{query_string}&checksum={checksum}"
            result = get(url)
            return json.loads(result.text)
        except ConnectionError:
            raise ConnectionError("No Response!", "Maybe your Server is down or base url is invalid")

    # This is Only for PUT recordings text tracks
    def url_put_recording_text_track(self, call_name, query_dict):
        try:
            query_string = query_generator(query_dict)
            checksum = checksum_generator(call_name, query_string, self.shared_secret)
            url = f"{self.base_url}{call_name}?{query_string}&checksum={checksum}"
            result = put(url)
            return json.loads(result.text)
        except ConnectionError:
            raise ConnectionError("No Response!", "Maybe your Server is down or base url is invalid")