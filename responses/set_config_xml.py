from .base_response import BaseResponse


class SetConfigXMLResponse(BaseResponse):
    @property
    def token(self):
        return self.get_field("token")
