import json


class Record:
    def __init__(self, parsed_xml):
        self.record_id = parsed_xml["recordID"]
        self.meeting_id = parsed_xml["meetingID"]
        self.name = parsed_xml["name"]
        self.is_published = parsed_xml["published"]
        self.state = parsed_xml["state"]
        self.start_time = parsed_xml["startTime"]
        self.end_time = parsed_xml["endTime"]
        self.playback_type = parsed_xml["playback"]["format"]["type"]
        self.playback_url = parsed_xml["playback"]["format"]["url"]
        self.playback_length = parsed_xml["playback"]["format"]["length"]
        try:
            self.meta = json.loads(json.dumps(parsed_xml["metadata"]))
        except KeyError:
            self.meta = []

    def __repr__(self):
        return f"RecordID:'{self.record_id}'"
