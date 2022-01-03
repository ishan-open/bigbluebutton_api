#BigBlueButton
    BigBlueButton is an open source web conferencing system for online learning. This means :
    Open source - you have full access to BigBlueButton’s source code under an open source license.
    With the source code, installation steps, and community support, you can easily deploy your own BigBlueButton server
    (or 10 servers if you want).

    For each server you can customize it, modify it and integrate it into your products and services. Cool.
    Web conferencing system - you get the core features you would expect from a commercial web conferencing system
    (but under an open source license). These features include real-time sharing of audio, video, presentation,
    and screen – along with collaboration tools such as whiteboard, shared notes, polling, and breakout rooms.
    BigBlueButton can record your sessions for later playback.

    Online learning - BigBlueButton extends these core features to enable a teacher to engage students for learning.
    For example, a tutor can use BigBlueButton’s multi-user whiteboard to help a student with solving a difficult math
    problem. BigBlueButton has built-in integrations with all the major learning management systems (LMS),
    including Canvas, Jenzabar, Moodle, Sakai, and Schoology.

    It also supports Learning Tools Interoperability (LTI) 1.0 for integration
    with other LMS systems (such as Blackboard and D2L).


## Usage:
### Reference Document: <a href="https://docs.bigbluebutton.org/dev/api.html"> BigBlueButton reference Doc </a>

## instantiate:
```python
>>> from bigbluebutton_api import BigBlueButton
>>> B = BigBlueButton("https://example.com/bigbluebutton/api/", "secret key")
```

### Note:
#### here are "return_code", "message_key", "message" and "response" arguments in all responses received from the server.
#### You can access these arguments as follows:
```python
>>> B.craete_room().return_code
>>> B.end_meeting(meeting_id,password).messageKey
>>> B.is_meeting_running(meeting_id).message
>>> B.create_room().response
```

## Available Methods:
### Create (create_meeting):
    Creates a BigBlueButton meeting.
    The create call is idempotent: you can call it multiple times with the same parameters without side effects.
    simplifies the logic for joining a user into a session as your application can always call create before returning the join URL to the user.
    This way, regardless of the order in which users join, the meeting will always exist when the user tries to join (the first create call actually creates the meeting; subsequent calls to create simply return SUCCESS).
    The BigBlueButton server will automatically remove empty meetings that were created but have never had any users after a number of minutes specified by meetingExpireIfNoUserJoinedInMinutes defined in bigbluebutton.properties.

#### <b> parameters </b>:
<p><b> name </b>: A name for the meeting. This is now required as of BigBlueButton 2.4.</p>
<p><b> meeting_id </b>: A meeting ID that can be used to identify this meeting by the 3rd-party application.</p>
<p><b> attendee_pw </b>: The password that the join URL can later provide as its password parameter to indicate the user will join as a viewer.</p>
<p><b> moderator_pw </b>: The password that will join URL can later provide as its password parameter to indicate the user will as a moderator.</p>
<p><b> welcome </b>: A welcome message that gets displayed on the chat window when the participant joins.</p>
<p><b> dial_number </b>: The dial access number that participants can call in using regular phone.</p>
<p><b> voice_bridge </b>: Voice conference number for the FreeSWITCH voice conference associated with this meeting.</p>
<p><b>max_participants</b>: Set the maximum number of users allowed to joined the conference at the same time. </p>
<p><b>logout_url</b>: The URL that the BigBlueButton client will go to after users click the OK button on the ‘You have been logged out message’.</p>
<p><b>record</b>: Setting ‘record=true’ instructs the BigBlueButton server to record the media and events in the session for later playback. The default is false.</p>
<p><b>duration</b>: The maximum length (in minutes) for the meeting.</p>
<p><b>is_breakout</b>: Must be set to true to create a breakout room. </p>
<p><b>parent_meeting_id</b>: Must be provided when creating a breakout room, the parent room must be running. </p>
<p><b>sequence</b>: The sequence number of the breakout room. </p>
<p><b>free_join</b>: If set to true, the client will give the user the choice to choose the breakout rooms he wants to join. </p>
<p><b>breakout_rooms_enabled</b>: If set to false, breakout rooms will be disabled. Default: true</p>
<p><b>breakout_rooms_private_chat_enabled</b>: If set to false, the private chat will be disabled in breakout rooms. Default: true</p>
<p><b>breakout_rooms_record</b>: If set to false, breakout rooms will not be recorded. Default: true</p>
<p><b>meta</b>: This is a special parameter type (there is no parameter named just meta).</p>
<p><b>moderator_only_message</b>: Display a message to all moderators in the public chat.</p>
<p><b>auto_start_recording</b>: Whether to automatically start recording when first user joins (default false).</p>
<p><b>allow_start_stop_recording</b>: Allow the user to start/stop recording. (default true)</p>
<p><b>webcams_only_for_moderator</b>: Setting webcamsOnlyForModerator=true will cause all webcams shared by viewers during this meeting to only appear for moderators (added 1.1) </p>
<p><b>logo</b>: Setting logo=http://www.example.com/my-custom-logo.png will replace the default logo in the Flash client. (added 2.0) </p>
<p><b>banner_text</b>: Will set the banner text in the client. (added 2.0) </p>
<p><b>banner_color</b>: Will set the banner background color in the client. The required format is color hex #FFFFFF. (added 2.0) </p>
<p><b>copyright</b>: Setting copyright=My custom copyright will replace the default copyright on the footer of the Flash client. (added 2.0) </p>
<p><b>mute_on_start</b>: Setting true will mute all users when the meeting starts. (added 2.0) </p>
<p><b>allow_mods_to_unmute_users</b>: Setting to true will allow moderators to unmute other users in the meeting. (added 2.2) Default: false</p>
<p><b>lock_settings_disable_cam</b>: Setting to true will allow moderators to unmute other users in the meeting. (added 2.2) Default: false</p>
<p><b>lock_settings_disable_mic</b>: Setting to true will only allow user to join listen only. (added 2.2) Default: false</p>
<p><b>lock_settings_disable_private_chat</b>: Setting to true will disable private chats in the meeting. (added 2.2) Default: false</p>
<p><b>lock_settings_disable_public_chat</b>: Setting to true will disable public chat in the meeting. (added 2.2) Default: false</p>
<p><b> lock_settings_disable_note </b>: Setting to true will disable notes in the meeting. (added 2.2) Default: false</p>
<p><b>lock_settings_locked_layout</b>: Setting to true will lock the layout in the meeting. (added 2.2) Default: false</p>
<p><b> lock_settings_lock_on_join </b>: Setting to false will not apply lock setting to users when they join. (added 2.2) Default: true</p>
<p><b> lock_settings_lock_on_join_configurable </b>: Setting to lockSettingsLockOnJoinConfigurable=true` will allow applying of `lockSettingsLockOnJoin. Default: false</p>
<p><b>guest_policy</b>: Will set the guest policy for the meeting. The guest policy determines whether or not users who send a join request with guest=true will be allowed to join the meeting. Possible values are ALWAYS_ACCEPT, ALWAYS_DENY, and ASK_MODERATOR. Default: ALWAYS_ACCEPT</p>
<p><b>meeting_keep_events</b>: Defaults to the value of defaultKeepEvents. If meetingKeepEvents is true BigBlueButton saves meeting events even if the meeting is not recorded (added in 2.3) Default: false</p>
<p><b>end_when_no_moderator</b>: Default endWhenNoModerator=false. If endWhenNoModerator is true the meeting will end automatically after a delay - see endWhenNoModeratorDelayInMinutes (added in 2.3) Default: false</p>
<p><b>end_when_no_moderator_delay_in_minutes</b>: Defaults to the value of endWhenNoModeratorDelayInMinutes=1. If endWhenNoModerator is true, the meeting will be automatically ended after this many minutes (added in 2.2) Default: 1</p>
<p><b>meeting_layout</b>: Will set the default layout for the meeting. Possible values are: CUSTOM_LAYOUT, SMART_LAYOUT, PRESENTATION_FOCUS, VIDEO_FOCUS. (added 2.4) Default: SMART_LAYOUT</p>
<p><b>learning_dashboard_enabled</b>: Default learningDashboardEnabled=true. When this option is enabled BigBlueButton generates a Dashboard where moderators can view a summary of the activities of the meeting. (added 2.4) Default: true</p>
<p><b>learning_dashboard_cleanup_delay_in_minutes</b>: Default learningDashboardCleanupDelayInMinutes=2. This option set the delay (in minutes) before the Learning Dashboard become unavailable after the end of the meeting. If this value is zero, the Learning Dashboard will keep available permanently. (added 2.4) Default: 2</p>
<p><b>allow_mods_to_eject_cameras</b>: Setting to true will allow moderators to close other users cameras in the meeting. (added 2.4) Default: false</p>

### example
```python
>>> meeting = B.create_meeting("first meeting").meeting
>>> print(meeting.meeting_id)
>>> print(meeting.meeting_name)
>>> print(meeting.moderator_pw)
````


## Join (join_meeting)
    Joins a user to the meeting specified in the meetingID parameter.

### parameters
<p><b>full_name</b>: The full name that is to be used to identify this user to other conference attendees. </p>
<p><b>meeting_id</b>: The meeting ID that identifies the meeting you are attempting to join. </p>
<p><b>password</b>: The password that this attendee is using. If the moderator password is supplied, he will be given moderator status (and the same for attendee password, etc) </p>
<p><b>create_time</b>: Third-party apps using the API can now pass createTime parameter (which was created in the create call), BigBlueButton will ensure it matches the ‘createTime’ for the session. If they differ, BigBlueButton will not proceed with the join request. This prevents a user from reusing their join URL for a subsequent session with the same meetingID. </p>
<p><b>user_id</b>: An identifier for this user that will help your application to identify which person this is. This user ID will be returned for this user in the getMeetingInfo API call so that you can check </p>
<p><b>web_voice_conf</b>: If you want to pass in a custom voice-extension when a user joins the voice conference using voip. This is useful if you want to collect more info in you Call Detail Records about the user joining the conference.</p>
<p><b>config_token</b>: If you want to pass in a custom voice-extension when a user joins the voice conference using voip. This is useful if you want to collect more info in you Call Detail Records about the user joining the conference.</p>
<p><b>default_layout</b>: The layout name to be loaded first when the application is loaded. </p>
<p><b>avatar_url</b>: The link for the user’s avatar to be displayed (default can be enabled/disabled and set with “useDefaultAvatar“ and “defaultAvatarURL“ in bbb-web.properties). </p>
<p><b>redirect</b>: The default behaviour of the JOIN API is to redirect the browser to the Flash client when the JOIN call succeeds.</p>
<p><b>client_url</b>: Some third party apps what to display their own custom client. These apps can pass the URL containing the custom client and when redirect is not set to false, the browser will get redirected to the value of clientURL. </p>
<p><b>guest</b>: Set to “true” to indicate that the user is a guest, otherwise do NOT send this parameter. </p>
<p><b>role</b>: Define user role for the meeting. Accept the values(case insensitive) MODERATOR or VIEWER. If the role parameter is present and it's a valid option, it will take over of any password parameter provided. Added in BBB 2.4 </p>
<p><b>exclude_from_dashboard</b>: If the parameter is passed on JOIN with value `true`, the user will be omitted from being displayed in the Learning Dashboard. The use case is for support agents who drop by to support the meeting / resolve tech difficulties. Added in BBB 2.4 </p>

### example
```python
>>> print(B.join_meeting("fname lname", "meeting_id", "moderator password"))
>>> print(B.join_meeting("fname lname", "meeting_id", "attendee password"))
```


## isMeetingRunning (is_meeting_running)
    This call enables you to simply check on whether or not a meeting is running by looking it up with your meeting ID.

### parameters
<p><b>meeting_id</b>: The meeting ID that identifies the meeting you are attempting to check on. </p>

### example
```python
>>> print(B.is_meeting_running("meeting_id").running)
```


## End (end_meeting)
    Use this to forcibly end a meeting and kick all participants out of the meeting.

### parameters
<p><b>meeting_id</b>: The meeting ID that identifies the meeting you are attempting to end. </p>
<p><b>password</b>: The moderator password for this meeting. You can not end a meeting using the attendee password. </p>

### example
```python
>>> print(B.end_meeting("meeting_id", "moderator pw").message_key)
```


## getMeetingInfo (get_meeting_info)
    This call will return all of a meeting’s information, including the list of attendees as well as start and end times.

### parameters
<p><b>meeting_id</b>: The meeting ID that identifies the meeting you are attempting to check on. </p>

### example
```python
>>> meeting = B.get_meeting_info("meeting_id").info
>>> print(meeting.meeting_name)
>>> print(meeting.moderator_pw)
>>> print(meeting.has_user_joined)
```


## getMeetings (get_meetings)
    This call will return a list of all the meetings found on this server.

### example
```python
>>> meetings = B.get_meetings().meetings
>>> for meeting in meetings:
>>>     print(meeting.meeting_name)
>>>     print(meeting.meeting_id)
```


## getRecordings (get_recordings)
    Retrieves the recordings that are available for playback for a given meetingID (or set of meeting IDs).

### example
```python
>>> recordings = B.get_recordings().recordings
>>> for rec in recordings:
>>>    print(rec.record_id)
>>>    print(rec.meeting_id)
```


## publishRecordings (publish_recordings)
    Publish and unpublish recordings for a given recordID (or set of record IDs).

### parameters
<p><b>record_id</b>: A record ID for specify the recordings to apply the publish action. It can be a set of record IDs separated by commas. </p>
<p><b>publish</b>: The value for publish or unpublish the recording(s). Available values: true or false. </p>

### example
```python
>>> print(B.publish_recordings("record_id1,record_id2").published)
```


## deleteRecordings (delete_recordings)
    Delete one or more recordings for a given recordID (or set of record IDs).

### parameters
<p><b>record_id</b>: A record ID for specify the recordings to delete. It can be a set of record IDs separated by commas. </p>

### example
```python
print(B.delete_recordings("record_id1,record_id2").deleted)
```


## updateRecordings (update_recordings)
    Update metadata for a given recordID (or set of record IDs)

### parameters
<p><b>record_id</b>: A record ID for specify the recordings to apply the publish action. It can be a set of record IDs separated by commas. </p>
<p><b>meta</b>: You can pass one or more metadata values to be updated. The format of these parameters is the same as the metadata passed to the create call. For more information see the docs for the create call. When meta_parameter=NOT EMPTY and meta_parameter exists its value is updated, if it doesn’t exist, the parameter is added. When meta_parameter=, and meta_parameter exists the key is removed, when it doesn’t exist the action is ignored. </p>

### example
```python
print(B.update_recordings("record_id1,record_id2", {"new": "value"}).updated)
```


## getDefaultConfigXML (get_default_config_xml)
    Retrieve the default config.xml. This call enables a 3rd party application to get the current config.xml, modify it’s parameters, and use setConfigXML to store it on the BigBlueButton server (getting a reference token to the new config.xml), then using the token in as a parameter in the join URL to override the default config.xml.

### example
```python
print(B.get_default_config_xml()) # will returns configs as a dict
```


## setConfigXML (set_config_xml)
    Associate a custom config.xml file with the current session. This call returns a token that can later be passed as a parameter to a join URL. When passed as a parameter, the BigBlueButton client will use the associated config.xml for the user instead of using the default config.xml. This enables 3rd party applications to provide user-specific config.xml files.

### parameters
<p><b>meeting_id</b>: A meetingID to an active meeting</p>
<p><b>confix_xml</b>: A valid config.xml file as string</p>

### example
```python
print(B.set_config_xml("meeting_id", "some xml config").token)
```
