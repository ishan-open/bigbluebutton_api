class Attendee:

    def __init__(self, parsed_xml):
        self.user_id = parsed_xml["userID"]
        self.full_name = parsed_xml["fullName"]
        self.role = parsed_xml["role"]
        self.is_presenter = parsed_xml["isPresenter"]
        self.is_listening_only = parsed_xml["isListeningOnly"]
        self.has_joined_voice = parsed_xml["hasJoinedVoice"]
        self.has_video = parsed_xml["hasVideo"]

    def __repr__(self):
        return f"user_id:'{self.user_id}'"
