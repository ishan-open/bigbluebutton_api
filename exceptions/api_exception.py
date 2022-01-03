class MessageKeys:
    no_meetings = "noMeetings"
    no_recordings = "noRecordings"
    invalid_password = "invalidPassword"
    not_found = "notFound"
    already_ended = "alreadyEnded"
    id_not_unique = "idNotUnique"
    duplicate_warning = "duplicateWarning"


class Error(Exception):
    pass


class ConnectionLost(Error):
    def __init__(self):
        self.message = "NO RESPONSE! MAYBE YOUR SERVER IS DOWN OR INVALID BASE URL"


class NoMeetings(Error):
    def __init__(self, *args, **kwargs):
        pass


class NoRecordings(Error):
    def __init__(self, *args, **kwargs):
        pass


class InvalidPassword(Error):
    def __init__(self, message_key, message):
        self.message_key = message_key
        self.message = message

    def __str__(self):
        return f"{self.message_key}, {self.message}"


class NotFound(Error):
    def __init__(self, message_key, message):
        self.message_key = message_key
        self.message = message

    def __str__(self):
        return f"{self.message_key}, {self.message}"


class AlreadyEnded(Error):
    def __init__(self, message_key, message):
        self.message_key = message_key
        self.message = message

    def __str__(self):
        return f"{self.message_key}, {self.message}"


class IdNotUnique(Error):
    def __init__(self, message_key, message):
        self.message_key = message_key
        self.message = message

    def __str__(self):
        return f"{self.message_key}, {self.message}"


class DuplicateWarning(Error):
    def __init__(self, message_key, message):
        self.message_key = message_key
        self.message = message

    def __str__(self):
        return f"--> {self.message_key}, {self.message}"


class DictMeta(Error):
    def __init__(self):
        pass

    def __str__(self):
        return "invalid meta type, meta must be a dict!"
