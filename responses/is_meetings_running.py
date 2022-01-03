from .base_response import BaseResponse


class IsMeetingRunningResponse(BaseResponse):
    @property
    def running(self):
        return self.get_field("running")
