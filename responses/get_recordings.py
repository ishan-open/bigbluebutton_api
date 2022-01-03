from .base_response import BaseResponse
from ..core.record import Record
import json


class GetRecordingsResponse(BaseResponse):
    @property
    def recordings(self):
        final_recordings = []
        recordings = json.loads(json.dumps(self.get_field("recordings")))
        if recordings is not None:
            if isinstance(recordings["recording"], dict):
                return [Record(recordings["recording"])]
            elif isinstance(recordings["recording"], list):
                for record in self.get_field("recordings")["recording"]:
                    final_recordings.append(Record(record))
        return final_recordings
