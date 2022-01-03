from .base_response import BaseResponse


class UpdateRecordingsResponse(BaseResponse):
    @property
    def updated(self):
        return self.get_field("updated")
