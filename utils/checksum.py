import hashlib


def checksum_generator(call_name, query_string, shared_secret):
    string = f"{call_name}{query_string}{shared_secret}"
    x = hashlib.sha1(string.encode()).hexdigest()
    return x
