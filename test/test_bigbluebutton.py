from ..bigbluebutton import BigBlueButton
from uuid import uuid4

b = BigBlueButton("http://test-install.blindsidenetworks.com/bigbluebutton/api", "8cd8ef52e8e101574e400365b55e11a6")
_id = uuid4()


def test_create1():
    assert b.create_meeting("this is my name", meeting_id=_id, moderator_pw="12345678").return_code == "SUCCESS"


def test_create2():
    assert b.create_meeting("this is my name", meeting_id=_id).message_key == "duplicateWarning"


def test_is_meeting_running():
    running = b.is_meeting_running(meeting_id=_id).running
    assert running == "true" or running == "false"


def test_get_meetings():
    assert b.get_meetings().return_code == "SUCCESS"


def test_get_meeting_info():
    info = b.get_meeting_info(meeting_id=_id)
    assert info.return_code == "SUCCESS" or info.message_key == "notFound"


def test_end_meeting():
    info = b.end_meeting(meeting_id=_id, password="12345678")
    assert info.return_code == "SUCCESS" or info.message_key == "notFound" or info.message_key == "invalidPassword"


def test_publish_recordings():
    info = b.publish_recording(record_id="1234", publish="true")
    assert info.message_key == "notFound" or info.return_code == "SUCCESS"


def test_delete_recordings():
    info = b.delete_recording(record_id="1234")
    assert info.message_key == "notFound" or info.return_code == "SUCCESS"


def test_update_recordings():
    info = b.update_recording(record_id="1234", meta={"name": "test"})
    assert info.message_key == "notFound" or info.return_code == "SUCCESS"


def test_get_recordings():
    assert b.get_recordings(record_id="1234").return_code == "SUCCESS"
