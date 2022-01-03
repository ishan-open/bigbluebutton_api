from .base_response import BaseResponse
from ..core.create import Create
from ..exceptions.api_exception import MessageKeys, DuplicateWarning, IdNotUnique


class CreateResponse(BaseResponse):
    @property
    def meeting(self):
        if self.return_code == "SUCCESS" and self.message is None:
            return Create(self.response)
        elif self.message_key == MessageKeys.duplicate_warning:
            raise DuplicateWarning(self.message_key, self.message)
        elif self.message_key == MessageKeys.id_not_unique:
            raise IdNotUnique(self.message_key, self.message)
