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
async def get_v1_video_rooms(
    twilio_credentials: "TwilioCredentials",
    room_type: list = None,
    codec: list = None,
    room_name: str = None,
    created_after: str = None,
    created_before: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Get a list of Programmable Video Rooms.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        room_type:
            Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        codec:
            Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        room_name:
            Room friendly name.
        created_after:
            Only read rooms that started on or after this ISO 8601 timestamp.
        created_before:
            Only read rooms that started before this ISO 8601 timestamp.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Video/Rooms?&room_type=%s&codec=%s&room_name=%s&created_after=%s&created_before=%s&page_size=%s](
    https://insights.twilio.com/v1/Video/Rooms?&room_type=%s&codec=%s&room_name=%s&created_after=%s&created_before=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://insights.twilio.com/v1/Video/Rooms"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "room_type": room_type,
        "codec": codec,
        "room_name": room_name,
        "created_after": created_after,
        "created_before": created_before,
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
async def get_v1_video_rooms_room_sid(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Get Video Log Analyzer data for a Room.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Video/Rooms/{room_sid}?](
    https://insights.twilio.com/v1/Video/Rooms/{room_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Video/Rooms/{room_sid}"  # noqa
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
async def get_v1_video_rooms_room_sid_participants(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Get a list of room participants.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Video/Rooms/{room_sid}/Participants?&page_size=%s](
    https://insights.twilio.com/v1/Video/Rooms/{room_sid}/Participants?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Video/Rooms/{room_sid}/Participants"  # noqa
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
async def get_v1_video_rooms_room_sid_participants_participant_sid(
    room_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Get Video Log Analyzer data for a Room Participant.

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
    [https://insights.twilio.com/v1/Video/Rooms/{room_sid}/Participants/{participant_sid}?](
    https://insights.twilio.com/v1/Video/Rooms/{room_sid}/Participants/{participant_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Video/Rooms/{room_sid}/Participants/{participant_sid}"  # noqa
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
