import json


class Meeting:
    def __init__(self, parsed_xml):
        self.meeting_id = parsed_xml["meetingID"]
        self.meeting_name = parsed_xml["meetingName"]
        self.creation_time = parsed_xml["createTime"]
        self.creation_date = parsed_xml["createDate"]
        self.voice_bridge = parsed_xml["voiceBridge"]
        self.dial_number = parsed_xml["dialNumber"]
        self.attendee_pw = parsed_xml["attendeePW"]
        self.moderator_pw = parsed_xml["moderatorPW"]
        self.has_been_forcibly_ended = parsed_xml["hasBeenForciblyEnded"]
        self.is_running = parsed_xml["running"]
        self.participant_count = parsed_xml["participantCount"]
        self.listener_count = parsed_xml["listenerCount"]
        self.voice_participant_count = parsed_xml["voiceParticipantCount"]
        self.video_count = parsed_xml["videoCount"]
        self.duration = parsed_xml["duration"]
        self.has_user_joined = parsed_xml["hasUserJoined"]
        self.moderator_count = parsed_xml["moderatorCount"]
        self.max_users = parsed_xml["maxUsers"]

        try:
            self.meta = json.loads(json.dumps(parsed_xml["metadata"]))
        except KeyError:
            self.meta = []

    def __repr__(self):
        return f"MeetingID:'{self.meeting_id}'"
