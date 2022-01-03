from .base_response import BaseResponse
from ..exceptions.api_exception import MessageKeys, NotFound


class PublishRecordingsResponse(BaseResponse):
    @property
    def published(self):
        if self.message_key == MessageKeys.not_found:
            raise NotFound(self.message_key, self.message)
        return self.get_field("published")
