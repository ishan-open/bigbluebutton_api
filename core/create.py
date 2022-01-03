class Create:
    def __init__(self, parsed_xml):
        self.meeting_id = parsed_xml["meetingID"]
        self.internal_meeting_id = parsed_xml["internalMeetingID"]
        self.parent_meeting_id = parsed_xml["parentMeetingID"]
        self.attendee_pw = parsed_xml["attendeePW"]
        self.moderator_pw = parsed_xml["moderatorPW"]
        self.has_been_forcibly_ended = parsed_xml["hasBeenForciblyEnded"]
        self.duration = parsed_xml["duration"]
        self.has_user_joined = parsed_xml["hasUserJoined"]
        self.create_date = parsed_xml["createDate"]
        self.dial_number = parsed_xml["dialNumber"]
        self.voice_bridge = parsed_xml["voiceBridge"]
        self.create_time = parsed_xml["createTime"]

    def __repr__(self):
        return f"MeetingID:'{self.meeting_id}'"
