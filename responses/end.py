from .base_response import BaseResponse
from ..exceptions.api_exception import MessageKeys, InvalidPassword, AlreadyEnded, NotFound


class EndResponse(BaseResponse):
    @property
    def end(self):
        if self.message_key == MessageKeys.not_found:
            raise NotFound(self.message_key, self.message)
        elif self.message_key == MessageKeys.invalid_password:
            raise InvalidPassword(self.message_key, self.message)
        elif self.message_key == MessageKeys.already_ended:
            raise AlreadyEnded(self.message_key, self.message)
        return f"{self.message_key}, {self.message}"
