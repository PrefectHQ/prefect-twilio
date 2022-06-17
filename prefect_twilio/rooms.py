"""
This is a module for interacting with Twilio REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from typing import TYPE_CHECKING, Any, Dict

from prefect import task

from prefect_twilio.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_twilio import TwilioCredentials


@task
async def get_v1_rooms(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    unique_name: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Read only the rooms with this status. Can be: `in-progress` (default) or
            `completed`.
        unique_name:
            Read only rooms with the this `unique_name`.
        date_created_after:
            Read only rooms that started on or after this date, given as `YYYY-MM-
            DD`.
        date_created_before:
            Read only rooms that started before this date, given as `YYYY-MM-DD`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms?&status=%s&unique_name=%s&date_created_after=%s&date_created_before=%s&page_size=%s](
    https://video.twilio.com/v1/Rooms?&status=%s&unique_name=%s&date_created_after=%s&date_created_before=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://video.twilio.com/v1/Rooms"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "unique_name": unique_name,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "page_size": page_size,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result


@task
async def post_v1_rooms(
    twilio_credentials: "TwilioCredentials",
    audio_only: bool = None,
    empty_room_timeout: int = None,
    enable_turn: bool = None,
    large_room: bool = None,
    max_participant_duration: int = None,
    max_participants: int = None,
    media_region: str = None,
    record_participants_on_connect: bool = None,
    recording_rules: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    type: str = None,
    unique_name: str = None,
    unused_room_timeout: int = None,
    video_codecs: list = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        audio_only:
            When set to true, indicates that the participants in the room will only
            publish audio. No video tracks will be allowed. Group rooms
            only.
        empty_room_timeout:
            Configures how long (in minutes) a room will remain active after last
            participant leaves. Valid values range from 1 to 60 minutes
            (no fractions).
        enable_turn:
            Deprecated, now always considered to be true.
        large_room:
            When set to true, indicated that this is the large room.
        max_participant_duration:
            The maximum number of seconds a Participant can be connected to the
            room. The maximum possible value is 86400 seconds (24
            hours). The default is 14400 seconds (4 hours).
        max_participants:
            The maximum number of concurrent Participants allowed in the room. Peer-
            to-peer rooms can have up to 10 Participants. Small Group
            rooms can have up to 4 Participants. Group rooms can have up
            to 50 Participants.
        media_region:
            The region for the media server in Group Rooms.  Can be: one of the
            [available Media
            Regions](https://www.twilio.com/docs/video/ip-address-
            whitelisting
            group-rooms-media-servers). ***This feature is not available
            in `peer-to-peer` rooms.***.
        record_participants_on_connect:
            Whether to start recording when Participants connect. ***This feature is
            not available in `peer-to-peer` rooms.***.
        recording_rules:
            A collection of Recording Rules that describe how to include or exclude
            matching tracks for recording.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application on every room event. See
            [Status
            Callbacks](https://www.twilio.com/docs/video/api/status-
            callbacks) for more info.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be `POST`
            or `GET`.
        type:
            The type of room. Can be: `go`, `peer-to-peer`, `group-small`, or
            `group`. The default value is `group`.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used as a `room_sid` in place of the resource's `sid`
            in the URL to address the resource, assuming it does not
            contain any [reserved
            characters](https://tools.ietf.org/html/rfc3986
            section-2.2) that would need to be URL encoded. This value
            is unique for `in-progress` rooms. SDK clients can use this
            name to connect to the room. REST API clients can use this
            name in place of the Room SID to interact with the room as
            long as the room is `in-progress`.
        unused_room_timeout:
            Configures how long (in minutes) a room will remain active if no one
            joins. Valid values range from 1 to 60 minutes (no
            fractions).
        video_codecs:
            An array of the video codecs that are supported when publishing a track
            in the room.  Can be: `VP8` and `H264`.  ***This feature is
            not available in `peer-to-peer` rooms***.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms?](
    https://video.twilio.com/v1/Rooms?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://video.twilio.com/v1/Rooms"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "audio_only": audio_only,
        "empty_room_timeout": empty_room_timeout,
        "enable_turn": enable_turn,
        "large_room": large_room,
        "max_participant_duration": max_participant_duration,
        "max_participants": max_participants,
        "media_region": media_region,
        "record_participants_on_connect": record_participants_on_connect,
        "recording_rules": recording_rules,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "type": type,
        "unique_name": unique_name,
        "unused_room_timeout": unused_room_timeout,
        "video_codecs": video_codecs,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_rooms_room_sid_participants(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    identity: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Read only the participants with this status. Can be: `connected` or
            `disconnected`. For `in-progress` Rooms the default Status
            is `connected`, for `completed` Rooms only `disconnected`
            Participants are returned.
        identity:
            Read only the Participants with this
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            `identity` value.
        date_created_after:
            Read only Participants that started after this date in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601
            UTC) format.
        date_created_before:
            Read only Participants that started before this date in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601
            UTC) format.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants?&status=%s&identity=%s&date_created_after=%s&date_created_before=%s&page_size=%s](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants?&status=%s&identity=%s&date_created_after=%s&date_created_before=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "identity": identity,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "page_size": page_size,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v1_rooms_room_sid_participants_participant_sid_published_tracks(
    room_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Returns a list of tracks associated with a given Participant. Only `currently`
    Published Tracks are in the list resource.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks?&page_size=%s](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "page_size": page_size,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v1_rooms_room_sid_participants_participant_sid_published_tracks_sid(
    room_sid: str,
    participant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single Track resource represented by TrackName or SID.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_v1_rooms_room_sid_participants_participant_sid_subscribe_rules(
    room_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a list of Subscribe Rules for the Participant.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_v1_rooms_room_sid_participants_participant_sid_subscribe_rules(
    room_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
    rules: str = None,
) -> Dict[str, Any]:
    """
    Update the Subscribe Rules for the Participant.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        rules:
            A JSON-encoded array of subscribe rules. See the [Specifying Subscribe
            Rules](https://www.twilio.com/docs/video/api/track-
            subscriptions
            specifying-sr) section for further information.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 202 | Accepted. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules"  # noqa
    responses = {
        202: "Accepted.",  # noqa
    }

    data = {
        "rules": rules,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_rooms_room_sid_participants_participant_sid_subscribed_tracks(
    room_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Returns a list of tracks that are subscribed for the participant.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks?&page_size=%s](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "page_size": page_size,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v1_rooms_room_sid_participants_participant_sid_subscribed_tracks_sid(
    room_sid: str,
    participant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single Track resource represented by `track_sid`.  Note: This is one
    resource with the Video API that requires a SID, be Track Name on the
    subscriber side is not guaranteed to be unique.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_v1_rooms_room_sid_participants_sid(
    room_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_v1_rooms_room_sid_participants_sid(
    room_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The new status of the resource. Can be: `connected` or `disconnected`.
            For `in-progress` Rooms the default Status is `connected`,
            for `completed` Rooms only `disconnected` Participants are
            returned.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "status": status,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_rooms_room_sid_recording_rules(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a list of Recording Rules for the Room.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules?](
    https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_v1_rooms_room_sid_recording_rules(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
    rules: str = None,
) -> Dict[str, Any]:
    """
    Update the Recording Rules for the Room.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        rules:
            A JSON-encoded array of recording rules.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules?](
    https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 202 | Accepted. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules"  # noqa
    responses = {
        202: "Accepted.",  # noqa
    }

    data = {
        "rules": rules,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_rooms_room_sid_recordings(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    source_sid: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Read only the recordings with this status. Can be: `processing`,
            `completed`, or `deleted`.
        source_sid:
            Read only the recordings that have this `source_sid`.
        date_created_after:
            Read only recordings that started on or after this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with
            time zone.
        date_created_before:
            Read only Recordings that started before this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with
            time zone.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Recordings?&status=%s&source_sid=%s&date_created_after=%s&date_created_before=%s&page_size=%s](
    https://video.twilio.com/v1/Rooms/{room_sid}/Recordings?&status=%s&source_sid=%s&date_created_after=%s&date_created_before=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Recordings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "source_sid": source_sid,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "page_size": page_size,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result


@task
async def delete_v1_rooms_room_sid_recordings_sid(
    room_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_v1_rooms_room_sid_recordings_sid(
    room_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_v1_rooms_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{sid}?](
    https://video.twilio.com/v1/Rooms/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_v1_rooms_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The new status of the resource. Set to `completed` to end the room.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{sid}?](
    https://video.twilio.com/v1/Rooms/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "status": status,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
