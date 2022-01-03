import json
from .base_response import BaseResponse
from ..core.meeting import Meeting
from ..core.attendee import Attendee
from ..exceptions.api_exception import MessageKeys, NotFound


class GetMeetingInfo(BaseResponse):
    @property
    def info(self):
        if self.message_key == MessageKeys.not_found:
            raise NotFound(self.message_key, self.message)
        return Meeting(self.response)

    @property
    def attendees(self):
        final_attendees = []
        attendees = json.loads(json.dumps(self.get_field("attendees")))
        if attendees is not None:
            attendees = attendees["attendee"]
            if type(attendees) == dict:
                final_attendees.append(Attendee(attendees))
            elif type(attendees) == list:
                for attendee in attendees:
                    final_attendees.append(Attendee(attendee))
            elif attendees is None:
                pass
        return final_attendees

    @property
    def meta(self):
        meta_data = json.loads(json.dumps(self.get_field("metadata")))
        return meta_data
