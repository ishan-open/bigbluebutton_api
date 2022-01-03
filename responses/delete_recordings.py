from .base_response import BaseResponse
from ..exceptions.api_exception import MessageKeys
from ..exceptions.api_exception import NotFound


class DeleteRecordingsResponse(BaseResponse):
    @property
    def deleted(self):
        if self.message_key == MessageKeys.not_found:
            raise NotFound(self.message_key, self.message)
        return self.get_field("deleted")
