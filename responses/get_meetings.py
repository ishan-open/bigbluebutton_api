from .base_response import BaseResponse
from ..core.meeting import Meeting
import json


class GetMeetingsResponse(BaseResponse):
    @property
    def meetings(self):
        final_meetings = []
        meetings = json.loads(json.dumps(self.get_field("meetings")))
        if meetings is not None:
            if isinstance(meetings["meeting"], dict):
                return [Meeting(meetings["meeting"])]
            elif isinstance(meetings["meeting"], list):
                for meet in self.get_field("meetings")["meeting"]:
                    final_meetings.append(Meeting(meet))
        return final_meetings
