from uuid import uuid4

from .utils.url import UrlGenerator
from .core.api_methods import ApiMethods
from .core.api_parameters import ApiParameters
from .responses import (
    CreateResponse, DeleteRecordingsResponse,
    EndResponse, GetMeetingsResponse,
    GetMeetingInfo, GetRecordingsResponse,
    IsMeetingRunningResponse, PublishRecordingsResponse,
    SetConfigXMLResponse, UpdateRecordingsResponse,
)


class BigBlueButton:
    """
    BigBlueButton
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

    Parameters
    ----------
        base_url : str

        shared_secret : str

    Examples
    --------
    >>> from BigBlueButton import BigBlueButton
    >>> b = BigBlueButton(base_url="https://bbbservcer.com/bigbluebutton/api, shared_secret="your shared secret")
    """
    def __init__(self, base_url, shared_secret):
        if base_url[-1] != "/":
            base_url = base_url + "/"
        self.base_url = base_url
        self.shared_secret = shared_secret
        self.url_builder = UrlGenerator(self.base_url, shared_secret)

    def create_meeting(
            self,
            name: str,
            meeting_id: str = None,
            attendee_pw: str = None,
            moderator_pw: str = None,
            welcome: str = None,
            dial_number: str = None,
            voice_bridge: str = None,
            max_participants: int = None,
            logout_url: str = None,
            record: bool = None,
            duration: int= None,
            is_breakout: bool = None,
            parent_meeting_id: str = None,
            sequence: int = None,
            free_join: bool = None,
            breakout_rooms_enabled: bool = None,
            breakout_rooms_private_chat_enabled: bool = None,
            breakout_rooms_record: bool = None,
            meta: dict = {},
            moderator_only_message: bool = None,
            auto_start_recording: bool = None,
            allow_start_stop_recording: bool = None,
            webcams_only_for_moderator: bool = None,
            logo: str = None,
            banner_text: str = None,
            banner_color: str = None,
            copy_right: str = None,
            mute_on_start: bool = None,
            allow_mods_to_unmute_users: bool = None,
            lock_settings_disable_cam: bool = None,
            lock_settings_disable_mic: bool = None,
            lock_settings_disable_private_chat: bool = None,
            lock_settings_disable_public_chat: bool = None,
            lock_settings_disable_note: bool = None,
            lock_settings_locked_layout: bool = None,
            lock_settings_lock_on_join: bool = None,
            lock_settings_lock_on_join_configurable: bool = None,
            quest_policy: str = None,
            meeting_keep_events: bool = None,
            end_when_no_moderator: bool = None,
            end_when_no_moderator_delay_in_minutes: int = None,
            meeting_layout: str = None,
            learning_dashboard_enabled: bool = None,
            learning_dashboard_cleanup_delay_in_minutes: int = None,
            allow_mods_to_eject_cameras: bool = None
        ) -> CreateResponse:
        """
        Creates a BigBlueButton meeting.
        The create call is idempotent : you can call it multiple times with the same parameters without side effects.
        This simplifies the logic for joining a user into a session as your application can
        always call create before returning the join URL to the user.
        This way, regardless of the order in which users join,
        the meeting will always exist when the user tries to join
        (the first create call actually creates the meeting; subsequent calls to create simply return SUCCESS,
        you can access that with return_code).

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
        name: str
            A name for the meeting.

        meeting_id : str
            A meeting ID that can be used to identify this meeting by the 3rd-party application.
            * It is created automatically, but you can assign a custom ID according to your wishes.
            This must be unique to the server that you are calling:
            different active meetings can not have the same meeting ID.
            If you supply a non-unique meeting ID
            (a meeting is already in progress with the same meeting ID),
            then if the other parameters in the create call are identical,
            the create call will succeed (but will receive a warning message in the response).
            The create call is idempotent: calling multiple times does not have any side effect.
            This enables a 3rd-party applications to avoid checking if the meeting is running and always
            call create before joining each user.
            Meeting IDs should only contain upper/lower ASCII letters, numbers, dashes, or underscores.
            A good choice for the meeting ID is to generate a GUID value as this all but guarantees that
            different meetings will not have the same meetingID.

        attendee_pw : str
            The password that the join URL can later provide as its password parameter to indicate the user
            will join as a viewer.
            If no attendeePW is provided, the create call will
            return a randomly generated attendeePW password for the meeting.

        moderator_pw : str
            The password that will join URL can later provide as its password parameter to indicate the user will
            as a moderator. if no moderatorPW is provided, create will return a randomly
            generated moderatorPW password for the meeting.

        welcome : str
            A welcome message that gets displayed on the chat window when the participant joins.

        dial_number : str
            The dial access number that participants can call in using regular phone.

        voice_bridge : str
            Voice conference number for the FreeSWITCH voice conference associated with this meeting.
            This must be a 5-digit number in the range 10000 to 99999.
            a phone number to your BigBlueButton server, This parameter sets the personal
            identification number (PIN) that FreeSWITCH will prompt for a phone-only user to enter.

        max_participants : str
            Set the maximum number of users allowed to joined the conference at the same time.

        logout_url : str
            The URL that the BigBlueButton client will go to after users click the
            OK button on the ‘You have been logged out message’.

        record : str
            Setting ‘record=true’ instructs the BigBlueButton server to record the
            media and events in the session for later playback. The default is false.
            In order for a playback file to be generated, a moderator must click the Start/Stop Recording button at
            least once during the sesssion; otherwise, in the absence of any recording marks,
            the record and playback scripts will not generate a playback file.

        duration : str
            The maximum length (in minutes) for the meeting.
            Normally is 120 minutes.

        is_breakout : str
            Must be set to true to create a breakout room.

        parent_meeting_id : str
            Must be provided when creating a breakout room, the parent room must be running.

        sequence : str
            The sequence number of the breakout room.

        free_join : str
            If set to true, the client will give the user the choice to choose the breakout rooms he wants to join.

        breakout_rooms_enabled : bool
             	If set to false, breakout rooms will be disabled.
                Default: true

        breakout_rooms_private_chat_enabled : bool
            If set to false, the private chat will be disabled in breakout rooms.
            Default: true

        breakout_rooms_record : bool
            If set to false, breakout rooms will not be recorded.
            Default: true

        meta : dict
            This is a special parameter type (there is no parameter named just meta).

        moderator_only_message : str
            Display a message to all moderators in the public chat.
            The value is interpreted in the same way as the welcome parameter.

        auto_start_recording : str
            Whether to automatically start recording when first user joins (default false).
            When this parameter is true, the recording UI in BigBlueButton will be initially active.
            Moderators in the session can still pause and restart recording using the UI control.
            Don’t pass autoStartRecording=false and allowStartStopRecording=false -
            the moderator won’t be able to start recording!

        allow_start_stop_recording : str
            Allow the user to start/stop recording. (default true)
            If you set both allow_start_stop_recording=false and allow_start_stop_recording=true,
            then the entire length of the session will be recorded,
            and the moderators in the session will not be able to pause/resume the recording.

        webcams_only_for_moderator : str
            Setting webcams_only_for_moderator=true will cause all webcams shared by
            viewers during this meeting to only appear for moderators.

        logo : str
            Setting logo=http://www.example.com/my-custom-logo.png
            will replace the default logo in the Flash client.

        banner_text : str
            Will set the banner text in the client.

        banner_color : str
            Will set the banner background color in the client. The required format is color hex #FFFFFF.

        copy_right : str
            Setting copy_right=My custom copyright will replace the
            default copyright on the footer of the Flash client.

        mute_on_start : str
            Setting mute_on_start=true will mute all users when the meeting starts.

        allow_mods_to_unmute_users : str
            Default allow_mods_to_unmute_users=false.
            Setting to allow_mods_to_unmute_users=true will allow moderators to unmute other users in the meeting.

        lock_settings_disable_cam : str
            Default lock_settings_disable_cam=false.
            Setting lock_settings_disable_cam=true will prevent users from sharing their camera in the meeting.

        lock_settings_disable_mic : str
            Default lock_settings_disable_mic=false.
            Setting to lock_settings_disable_mic=true will only allow user to join listen only.

        lock_settings_disable_private_chat : str
            Default lock_settings_disable_private_chat=false.
            Setting to lock_settings_disable_private_chat=true will disable private chats in the meeting.

        lock_settings_disable_public_chat : str
            Default lock_settings_disable_public_chat=false.
            Setting to lock_settings_disable_public_chat=true will disable public chat in the meeting.

        lock_settings_disable_note : str
            Default lock_settings_disable_note=false.
            Setting to lock_settings_disable_note=true will disable notes in the meeting.

        lock_settings_locked_layout : str
            Default lock_settings_locked_layout=false.
            Setting to lock_settings_locked_layout=true will lock the layout in the meeting.

        lock_settings_lock_on_join : str
            Default lock_settings_lock_on_join=true.
            Setting to lock_settings_lock_on_join=false will not apply lock setting to users when they join.

        lock_settings_lock_on_join_configurable : str
            Default lock_settings_lock_on_join_configurable=false.
            Setting to lock_settings_lock_on_join_configurable=true will allow applying of lockSettingsLockOnJoin param.

        quest_policy : str
            Default quest_policy=ALWAYS_ACCEPT.
            Will set the guest policy for the meeting.
            The guest policy determines whether or not users who send a join request with guest=true
            will be allowed to join the meeting. Possible values are ALWAYS_ACCEPT, ALWAYS_DENY, and ASK_MODERATOR.

        meeting_keep_events: str
            Defaults to the value of defaultKeepEvents.
            If meetingKeepEvents is true BigBlueButton saves meeting events even if the meeting is not recorded.

        end_when_no_moderator: str
            Default endWhenNoModerator=false.
            If endWhenNoModerator is true the meeting will end automatically after a delay.
            see endWhenNoModeratorDelayInMinutes

        end_when_no_moderator_delay_in_minutes: str
            Defaults to the value of endWhenNoModeratorDelayInMinutes=1.
            If endWhenNoModerator is true, the meeting will be automatically ended after this many minutes.

        meeting_layout : str
            Will set the default layout for the meeting.
            Possible values are: CUSTOM_LAYOUT, SMART_LAYOUT, PRESENTATION_FOCUS, VIDEO_FOCUS. (added 2.4)
            Default: SMART_LAYOUT

        learning_dashboard_enabled : bool
            Default learningDashboardEnabled=true.
            When this option is enabled BigBlueButton generates a Dashboard where moderators can view a summary of the activities of the meeting. (added 2.4)
            Default: true

        learning_dashboard_cleanup_delay_in_minutes : int
             	Default learningDashboardCleanupDelayInMinutes=2.
                This option set the delay (in minutes) before the Learning Dashboard become unavailable after the end of the meeting.
                If this value is zero, the Learning Dashboard will keep available permanently. (added 2.4)
                Default: 2

        allow_mods_to_eject_cameras : bool
            Setting to true will allow moderators to close other users cameras in the meeting. (added 2.4)
            Default: false

        Note
        ----
        Returns this Object :

        Returns
        -------
            CreateResponse

        Note
        ----
        Example :
        Examples
        --------
        >>> from BigBlueButton import BigBlueButton
        >>> b = BigBlueButton(base_url="https://bbbservcer.com/bigbluebutton/api/", shared_secret="your shared secret")
        >>> meeting = b.create_meeting(name="room1").meeting
        >>> meeting.meeting_id
        >>> meeting.attendee_pw

        """
        # if dont pass any meetingID will get automacilly a unique ID form uuid4
        if meeting_id is None:
            meeting_id = uuid4()

        query_dict = {
            "name": name,
            ApiParameters.attendee_pw: attendee_pw,
            ApiParameters.moderator_pw: moderator_pw,
            ApiParameters.welcome_message: welcome,
            ApiParameters.dial_number: dial_number,
            ApiParameters.voice_bridge: voice_bridge,
            ApiParameters.max_participants: max_participants,
            ApiParameters.logout_url: logout_url,
            ApiParameters.record: record,
            ApiParameters.duration: duration,
            ApiParameters.is_breakout: is_breakout,
            ApiParameters.parent_meeting_id: parent_meeting_id,
            ApiParameters.sequence: sequence,
            ApiParameters.free_join: free_join,
            ApiParameters.breakout_rooms_enabled: breakout_rooms_enabled,
            ApiParameters.breakout_rooms_private_chat_enabled: breakout_rooms_private_chat_enabled,
            ApiParameters.breakout_rooms_record: breakout_rooms_record,
            ApiParameters.meta: meta,
            ApiParameters.moderator_only_message: moderator_only_message,
            ApiParameters.auto_start_recording: auto_start_recording,
            ApiParameters.allow_start_stop_recording: allow_start_stop_recording,
            ApiParameters.webcams_only_for_moderator: webcams_only_for_moderator,
            ApiParameters.logo: logo,
            ApiParameters.banner_text: banner_text,
            ApiParameters.banner_color: banner_color,
            ApiParameters.copy_right: copy_right,
            ApiParameters.mute_on_start: mute_on_start,
            ApiParameters.allow_mods_to_unmute_users: allow_mods_to_unmute_users,
            ApiParameters.lock_settings_disable_cam: lock_settings_disable_cam,
            ApiParameters.lock_settings_disable_mic: lock_settings_disable_mic,
            ApiParameters.lock_settings_disable_private_chat: lock_settings_disable_private_chat,
            ApiParameters.lock_settings_disable_public_chat: lock_settings_disable_public_chat,
            ApiParameters.lock_settings_disable_note: lock_settings_disable_note,
            ApiParameters.lock_settings_locked_layout: lock_settings_locked_layout,
            ApiParameters.lock_settings_lock_on_join: lock_settings_lock_on_join,
            ApiParameters.lock_settings_lock_on_join_configurable: lock_settings_lock_on_join_configurable,
            ApiParameters.quest_policy: quest_policy,
            ApiParameters.meeting_keep_events: meeting_keep_events,
            ApiParameters.end_when_no_moderator: end_when_no_moderator,
            ApiParameters.end_when_no_moderator_delay_in_minutes: end_when_no_moderator_delay_in_minutes,
            ApiParameters.meeting_id: meeting_id,
            ApiParameters.meeting_layout: meeting_layout,
            ApiParameters.learning_dashboard_enabled: learning_dashboard_enabled,
            ApiParameters.learning_dashboard_cleanup_delay_in_minutes: learning_dashboard_cleanup_delay_in_minutes,
            ApiParameters.allow_mods_to_eject_cameras: allow_mods_to_eject_cameras,
        }

        return CreateResponse(self.url_builder.get_url(
            ApiMethods.create, query_dict
        ))

    def join_meeting(
            self,
            full_name: str,
            meeting_id: str,
            password: str,
            create_time: str = None,
            user_id: str = None,
            web_voice_conf: str = None,
            config_token: str = None,
            default_layout: str = None,
            avatar_url: str = None,
            redirect: str = None,
            client_url: str = None,
            quest: str=None,
            role: str = None,
            exclude_from_dashboard: str = None,
        ) -> str:
        """
        Joins a user to the meeting specified in the meetingID parameter.

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
        full_name: str
            The full name that is to be used to identify this user to other conference attendees.

        meeting_id: str
            The meeting ID that identifies the meeting you are attempting to join.

        password: str
            The password that this attendee is using.
            If the moderator password is supplied,
            he will be given moderator status (and the same for attendee password, etc)

        create_time: str
            Third-party apps using the API can now pass create_time parameter
            (which was created in the create call),
            BigBlueButton will ensure it matches the ‘create_time’ for the session.
            If they differ, BigBlueButton will not proceed with the join request.
            This prevents a user from reusing their join URL for a subsequent session with the same meetingID.

        user_id: str
            An identifier for this user that will help your application to identify which person this is.
            This user ID will be returned for this user in the getMeetingInfo API call so that you can check

        web_voice_conf: str
            If you want to pass in a custom voice-extension when a user joins the voice conference using voip.
            This is useful if you want to collect more info in you Call Detail Records about the user joining
            the conference. You need to modify your /etc/asterisk/bbb-extensions.conf to handle this new extensions.

        config_token: str
            The token returned by a setConfigXML API call. This causes the BigBlueButton client to load the config.
            xml associated with the token (not the default config.xml)

        default_layout: str
            The layout name to be loaded first when the application is loaded.

        avatar_url: str
            The link for the user’s avatar to be displayed when displayAvatar in config.xml is set to true
            (not yet implemented in the HTML5 client.)

        redirect: str
            The default behaviour of the JOIN API is to redirect the browser to the Flash client when the JOIN call
            succeeds. There have been requests if it’s possible to embed the Flash client in a “container” page and
            that the client starts as a hidden DIV tag which becomes visible on the successful JOIN.
            Setting this variable to FALSE will not redirect the browser but returns an XML instead whether the
            JOIN call has succeeded or not. The third party app is responsible for displaying the
            client to the user.

        client_url: str
            Some third party apps what to display their own custom client.
            These apps can pass the URL containing the custom client and when redirect is not set to false,
            the browser will get redirected to the value of client_url.

        quest: str
            Set to “true” to indicate that the user is a guest, otherwise do NOT send this parameter.

        role: str
            Define user role for the meeting.
            Accept the values(case insensitive) MODERATOR or VIEWER.
            If the role parameter is present and it's a valid option, it will take over of any password parameter provided.
            Added in BBB 2.4 

        exclude_from_dashboard: str
            If the parameter is passed on JOIN with value `true`, 
            the user will be omitted from being displayed in the Learning Dashboard.
            The use case is for support agents who drop by to support the meeting / resolve tech difficulties. Added in BBB 2.4 

        Note
        ----
        Returns this Object :

        Returns
        -------
            url : str
        """
        query_dict = {
            ApiParameters.full_name: full_name,
            ApiParameters.meeting_id: meeting_id,
            ApiParameters.password: password,
            ApiParameters.create_time: create_time,
            ApiParameters.user_id: user_id,
            ApiParameters.web_voice_conf: web_voice_conf,
            ApiParameters.config_token: config_token,
            ApiParameters.default_layout: default_layout,
            ApiParameters.avatar_url: avatar_url,
            ApiParameters.redirect: redirect,
            ApiParameters.client_url: client_url,
            ApiParameters.quest: quest,
            ApiParameters.role: role,
            ApiParameters.exclude_from_dashboard: exclude_from_dashboard
        }

        return self.url_builder.url_generator(ApiMethods.join, query_dict)

    def end_meeting(self, meeting_id: str, password: str) -> EndResponse:
        """
        Use this to forcibly end a meeting and kick all participants out of the meeting.

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
        meeting_id: str
            The meeting ID that identifies the meeting you are attempting to end.

        password: str
            The moderator password for this meeting. You can not end a meeting using the attendee password.

        Note
        ----
        Returns this Object :

        Returns
        -------
            EndResponse
        """
        query_dict = {
            ApiParameters.meeting_id: meeting_id,
            ApiParameters.password: password
        }
        res = self.url_builder.get_url(ApiMethods.end, query_dict)
        return EndResponse(res)

    def is_meeting_running(self, meeting_id: str) -> IsMeetingRunningResponse:
        """
        This call enables you to simply check on whether or not a meeting is running by looking it up
        with your meeting ID.

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
        meeting_id: str
            The meeting ID that identifies the meeting you are attempting to check on.

        Note
        ----
        Returns this Object :

        Returns
        -------
            IsMeetingRunningResponse
        """
        query_dict = {
            ApiParameters.meeting_id: meeting_id
        }
        res = self.url_builder.get_url(ApiMethods.is_meeting_running, query_dict)
        return IsMeetingRunningResponse(res)

    def get_meetings(self) -> GetMeetingsResponse:
        """
        This call will return a list of all the meetings found on this server.

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
            Takes no parameters

        Note
        ----
        Returns this Object :

        Returns
        -------
             GetMeetingsResponse
        """
        res = self.url_builder.get_url(ApiMethods.get_meetings, {})
        return GetMeetingsResponse(res)

    def get_meeting_info(self, meeting_id: str) -> GetMeetingInfo:
        """
        This call will return all of a meeting’s information,
        including the list of attendees as well as start and end times.

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
        meeting_id: str
            The meeting ID that identifies the meeting you are attempting to check on.

        Note
        ----
        Returns this Object :

        Returns
        -------
             GetMeetingInfo
        """
        query_dict = {
            ApiParameters.meeting_id: meeting_id
        }
        res = self.url_builder.get_url(ApiMethods.get_meeting_info, query_dict)
        return GetMeetingInfo(res)

    def get_recordings(
            self,
            meetings_id=None,
            record_id=None,
            state=None,
            meta={}
        ) -> GetRecordingsResponse:
        """
        Retrieves the recordings that are available for playback for a given meetingID (or set of meeting IDs).

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
        meetings_id: str
            A meeting ID for get the recordings.
            It can be a set of meetingIDs separate by commas.
            If the meeting ID is not specified, it will get ALL the recordings.
            If a recordID is specified, the meetingID is ignored.

        record_id: str
            A record ID for get the recordings.
            It can be a set of recordIDs separate by commas.
            If the record ID is not specified, it will use meeting ID as the main criteria.
            If neither the meeting ID is specified, it will get ALL the recordings.
            The recordID can also be used as a wildcard by including only the first characters in the string.

        state: str
            Since version 1.0 the recording has an attribute that shows a state that Indicates if the recording is
            [processing|processed|published|unpublished|deleted].
            The parameter state can be used to filter results. It can be a set of states separate by commas.
            If it is not specified only the states [published|unpublished] are considered
            (same as in previous versions). If it is specified as “any”, recordings in all states are included.

        meta: str
            You can pass one or more metadata values to filter the recordings returned.
            The format of these parameters is the same as the metadata passed to the create call.
            For more information see the docs for the create_meeting call.

        Note
        ----
        Returns this Object :

        Returns
        -------
            GetRecordingsResponse
        """
        query_dict = {
            ApiParameters.meeting_id: meetings_id,
            ApiParameters.record_id: record_id,
            ApiParameters.state: state,
            ApiParameters.meta: meta
        }
        res = self.url_builder.get_url(ApiMethods.get_recordings, query_dict)
        return GetRecordingsResponse(res)

    def publish_recordings(self, record_id: str, publish: bool) -> PublishRecordingsResponse:
        """
        Publish and unpublish recordings for a given recordID (or set of record IDs).

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
        record_id: str
            A record ID for specify the recordings to apply the publish action.
            It can be a set of record IDs separated by commas.

        publish: bool
            The value for publish or unpublish the recording(s). Available values: true or false.

        Note
        ----
        Returns this Object :

        Returns
        -------
             PublishRecordingsResponse
        """
        query_dict = {
            ApiParameters.record_id: record_id,
            ApiParameters.publish: publish
        }
        res = self.url_builder.get_url(ApiMethods.publish_recordings, query_dict)
        return PublishRecordingsResponse(res)

    def delete_recordings(self, record_id: str) -> DeleteRecordingsResponse:
        """
        Delete one or more recordings for a given recordID (or set of record IDs).

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
            record_id:
                A record ID for specify the recordings to delete. It can be a set of record IDs separated by commas.

        Note
        ----
        Returns this Object :

        Returns
        -------
            DeleteRecordingsResponse
        """
        query_dict = {
            ApiParameters.record_id: record_id
        }
        res = self.url_builder.get_url(ApiMethods.delete_recordings, query_dict)
        return DeleteRecordingsResponse(res)

    def update_recordings(
            self,
            record_id: str,
            meta: dict = {}
        ) -> UpdateRecordingsResponse:
        """
        Update metadata for a given recordID (or set of record IDs).

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
            record_id: str
                A record ID for specify the recordings to apply the publish action.
                It can be a set of record IDs separated by commas.

            meta: str
                You can pass one or more metadata values to be updated.
                The format of these parameters is the same as the metadata passed to the create call.
                For more information see the docs for the create call.
                When meta_parameter=NOT EMPTY and meta_parameter exists its value is updated,
                if it doesn’t exist, the parameter is added. When meta_parameter=,
                and meta_parameter exists the key is removed, when it doesn’t exist the action is ignored.

        Note
        ----
        Returns this Object :

        Returns
        -------
             UpdateRecordingsResponse
        """
        query_dict = {
            ApiParameters.record_id: record_id,
            ApiParameters.meta: meta
        }
        res = self.url_builder.get_url(ApiMethods.update_recordings, query_dict)
        return UpdateRecordingsResponse(res)

    def get_default_config_xml(self) -> dict:
        """
        Retrieve the default config.xml.
        This call enables a 3rd party application to get the current config.xml, modify it’s parameters,
        and use setConfigXML to store it on the BigBlueButton server (getting a reference token to the new config.xml),
        then using the token in as a parameter in the join URL to override the default config.xml.

        
        Note
        ----
        Takes this parameters :

        Parameters
        ----------
            None

        Note
        ----
        Returns this Object :

        Returns
        -------
            dict
        """
        return self.url_builder.get_url(ApiMethods.get_default_config_xml, {})

    def set_config_xml(self, meeting_id: str, config_xml: str) -> SetConfigXMLResponse:
        """
        Associate a custom config.xml file with the current session.
        This call returns a token that can later be passed as a parameter to a join URL.
        When passed as a parameter, the BigBlueButton client will use the associated config.xml for the user instead of using the default config.xml.
        This enables 3rd party applications to provide user-specific config.xml files.

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
            meetingID : str
             	A meetingID to an active meeting
            configXML : str
             	A valid config.xml file

        Note
        ----
        Returns this Object :

        Returns
        -------
            SetConfigXMLResponse
        """
        query_dict = {
            ApiParameters.meeting_id: meeting_id,
            ApiParameters.config_xml: config_xml
        }

        return SetConfigXMLResponse(self.url_builder.get_url(
            ApiMethods.set_config_xml, query_dict
        ))

    def get_recording_text_tracks(self, record_id: str):
        """
        Get a list of the caption/subtitle files currently available for a recording.
        It will include information about the captions (language, etc.), as well as a download link.
        This may be useful to retrieve live or automatically transcribed subtitles from a recording for manual editing.

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
            record_id : str
                A single recording ID to retrieve the available captions for.
                (Unlike other recording APIs, you cannot provide a comma-separated list of recordings.) 

        Note
        ----
        Returns this Object :

        Returns
        -------
            dict
        """
        query_dict = {
            ApiParameters.record_id: record_id
        }
        return self.url_builder.url_get_recordings_text_track(ApiMethods.get_recording_text_tracks, query_dict)

    def put_recordings_text_track(
            self,
            record_id: str,
            kind: str,
            lang: str,
            label: str
        ):
        """
        Upload a caption or subtitle file to add it to the recording.
        If there is any existing track with the same values for kind and lang, it will be replaced.

        Note that this api requires using a POST request.
        The parameters listed as GET parameters must be included in the request URI, and the actual uploaded file must be included in the body of the request in the multipart/form-data format.

        Note that the standard BigBlueButton checksum algorithm must be performed on the GET parameters,
        but that the body of the request (the subtitle file) is not checksummed.

        This design is such that a web application could generate a form with a signed url, and display it in the browser with a file upload selection box.
        When the user submits the form, it will upload the track directly to the recording api.
        The API may be used programmatically as well, of course.

        This API is asynchronous.
        It can take several minutes for the uploaded file to be incorporated into the published recording, and if an uploaded file contains unrecoverable errors, it may never appear.

        Note
        ----
        Takes this parameters :

        Parameters
        ----------
            record_id : str
                A single recording ID to retrieve the available captions for.
                (Unlike other recording APIs, you cannot provide a comma-separated list of recordings.) 

            kind : str
                Indicates the intended use of the text track.
                See the getRecordingTextTracks description for details.
                Using a value other than one listed in this document will cause an error to be returned. 

            lang : str
                Indicates the intended use of the text track.
                See the getRecordingTextTracks description for details.
                Using a value other than one listed in this document will cause an error to be returned. 

            label : str
                A human-readable label for the text track.
                If not specified, the system will automatically generate a label containing the name of the language identified by the lang parameter.

        Note
        ----
        Returns this Object :

        Returns
        -------
            dict
        """
        query_dict = {
            ApiParameters.record_id: record_id,
            ApiParameters.kind: kind,
            ApiParameters.lang: lang,
            ApiParameters.label: label
        }
        return self.url_builder.url_put_recording_text_track(ApiMethods.put_recording_text_track, query_dict)
