import xmltodict


def parser(xml):
    parsed_data = xmltodict.parse(xml)
    parsed_data = dict(parsed_data)
    try:
        my_dict = {}
        for i in parsed_data["response"]:
            my_dict.update({i: parsed_data["response"][i]})
        return my_dict
    except KeyError:
        return parsed_data
