class BaseResponse:
    def __init__(self, parsed_xml_data):
        self.response = parsed_xml_data

    def get_field(self, label):
        if not self.response == {}:
            try:
                return self.response[label]
            except KeyError:
                raise KeyError

    @property
    def return_code(self):
        return self.get_field("returncode")

    @property
    def message_key(self):
        try:
            return self.get_field("messageKey")
        except KeyError:
            return None

    @property
    def message(self):
        try:
            return self.get_field("message")
        except KeyError:
            return None
