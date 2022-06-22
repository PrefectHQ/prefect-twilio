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
async def get_v1_conferences(
    twilio_credentials: "TwilioCredentials",
    conference_sid: str = None,
    friendly_name: str = None,
    status: str = None,
    created_after: str = None,
    created_before: str = None,
    mixer_region: str = None,
    tags: str = None,
    subaccount: str = None,
    detected_issues: str = None,
    end_reason: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Conferences.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        conference_sid:
            The SID of the conference.
        friendly_name:
            Custom label for the conference resource, up to 64 characters.
        status:
            Conference status.
        created_after:
            Conferences created after the provided timestamp specified in ISO 8601
            format.
        created_before:
            Conferences created before the provided timestamp specified in ISO 8601
            format.
        mixer_region:
            Twilio region where the conference media was mixed.
        tags:
            Tags applied by Twilio for common potential configuration, quality, or
            performance issues.
        subaccount:
            Account SID for the subaccount whose resources you wish to retrieve.
        detected_issues:
            Potential configuration, behavior, or performance issues detected during
            the conference.
        end_reason:
            Conference end reason; e.g. last participant left, modified by API, etc.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Conferences?&conference_sid=%s&friendly_name=%s&status=%s&created_after=%s&created_before=%s&mixer_region=%s&tags=%s&subaccount=%s&detected_issues=%s&end_reason=%s&page_size=%s](
    https://insights.twilio.com/v1/Conferences?&conference_sid=%s&friendly_name=%s&status=%s&created_after=%s&created_before=%s&mixer_region=%s&tags=%s&subaccount=%s&detected_issues=%s&end_reason=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://insights.twilio.com/v1/Conferences"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "conference_sid": conference_sid,
        "friendly_name": friendly_name,
        "status": status,
        "created_after": created_after,
        "created_before": created_before,
        "mixer_region": mixer_region,
        "tags": tags,
        "subaccount": subaccount,
        "detected_issues": detected_issues,
        "end_reason": end_reason,
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
async def get_v1_conferences_conference_sid(
    conference_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Conference.

    Args:
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Conferences/{conference_sid}?](
    https://insights.twilio.com/v1/Conferences/{conference_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Conferences/{conference_sid}"  # noqa
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
async def get_v1_conferences_conference_sid_participants(
    conference_sid: str,
    twilio_credentials: "TwilioCredentials",
    participant_sid: str = None,
    label: str = None,
    events: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List Conference Participants.

    Args:
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        participant_sid:
            The unique SID identifier of the Participant.
        label:
            User-specified label for a participant.
        events:
            Conference events generated by application or participant activity; e.g.
            `hold`, `mute`, etc.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Conferences/{conference_sid}/Participants?&participant_sid=%s&label=%s&events=%s&page_size=%s](
    https://insights.twilio.com/v1/Conferences/{conference_sid}/Participants?&participant_sid=%s&label=%s&events=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Conferences/{conference_sid}/Participants"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "participant_sid": participant_sid,
        "label": label,
        "events": events,
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
async def get_v1_conferences_conference_sid_participants_participant_sid(  # noqa
    conference_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
    events: str = None,
    metrics: str = None,
) -> Dict[str, Any]:
    """
    Fetch a specific Conference Participant Summary.

    Args:
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        events:
            Conference events generated by application or participant activity; e.g.
            `hold`, `mute`, etc.
        metrics:
            Object. Contains participant call quality metrics.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Conferences/{conference_sid}/Participants/{participant_sid}?&events=%s&metrics=%s](
    https://insights.twilio.com/v1/Conferences/{conference_sid}/Participants/{participant_sid}?&events=%s&metrics=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Conferences/{conference_sid}/Participants/{participant_sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "events": events,
        "metrics": metrics,
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
async def get_v1_video_rooms_room_sid_participants_participant_sid(  # noqa
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


@task
async def get_v1_voice_settings(
    twilio_credentials: "TwilioCredentials",
    subaccount_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        subaccount_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/Settings?&subaccount_sid=%s](
    https://insights.twilio.com/v1/Voice/Settings?&subaccount_sid=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://insights.twilio.com/v1/Voice/Settings"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "subaccount_sid": subaccount_sid,
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
async def post_v1_voice_settings(
    twilio_credentials: "TwilioCredentials",
    advanced_features: bool = None,
    subaccount_sid: str = None,
    voice_trace: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        advanced_features:

        subaccount_sid:

        voice_trace:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/Settings?](
    https://insights.twilio.com/v1/Voice/Settings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://insights.twilio.com/v1/Voice/Settings"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "advanced_features": advanced_features,
        "subaccount_sid": subaccount_sid,
        "voice_trace": voice_trace,
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
async def get_v1_voice_summaries(
    twilio_credentials: "TwilioCredentials",
    from_: str = None,
    to: str = None,
    from_carrier: str = None,
    to_carrier: str = None,
    from_country_code: str = None,
    to_country_code: str = None,
    branded: bool = None,
    verified_caller: bool = None,
    has_tag: bool = None,
    start_time: str = None,
    end_time: str = None,
    call_type: str = None,
    call_state: str = None,
    direction: str = None,
    processing_state: str = None,
    sort_by: str = None,
    subaccount: str = None,
    abnormal_session: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        from_:

        to:

        from_carrier:

        to_carrier:

        from_country_code:

        to_country_code:

        branded:

        verified_caller:

        has_tag:

        start_time:

        end_time:

        call_type:

        call_state:

        direction:

        processing_state:

        sort_by:

        subaccount:

        abnormal_session:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/Summaries?&from_=%s&to=%s&from_carrier=%s&to_carrier=%s&from_country_code=%s&to_country_code=%s&branded=%s&verified_caller=%s&has_tag=%s&start_time=%s&end_time=%s&call_type=%s&call_state=%s&direction=%s&processing_state=%s&sort_by=%s&subaccount=%s&abnormal_session=%s&page_size=%s](
    https://insights.twilio.com/v1/Voice/Summaries?&from_=%s&to=%s&from_carrier=%s&to_carrier=%s&from_country_code=%s&to_country_code=%s&branded=%s&verified_caller=%s&has_tag=%s&start_time=%s&end_time=%s&call_type=%s&call_state=%s&direction=%s&processing_state=%s&sort_by=%s&subaccount=%s&abnormal_session=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://insights.twilio.com/v1/Voice/Summaries"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "from_": from_,
        "to": to,
        "from_carrier": from_carrier,
        "to_carrier": to_carrier,
        "from_country_code": from_country_code,
        "to_country_code": to_country_code,
        "branded": branded,
        "verified_caller": verified_caller,
        "has_tag": has_tag,
        "start_time": start_time,
        "end_time": end_time,
        "call_type": call_type,
        "call_state": call_state,
        "direction": direction,
        "processing_state": processing_state,
        "sort_by": sort_by,
        "subaccount": subaccount,
        "abnormal_session": abnormal_session,
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
async def get_v1_voice_call_sid_annotation(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Annotation?](
    https://insights.twilio.com/v1/Voice/{call_sid}/Annotation?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Annotation"  # noqa
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
async def post_v1_voice_call_sid_annotation(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    answered_by: str = None,
    call_score: int = None,
    comment: str = None,
    connectivity_issue: str = None,
    incident: str = None,
    quality_issues: str = None,
    spam: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        answered_by:

        call_score:

        comment:

        connectivity_issue:

        incident:

        quality_issues:

        spam:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Annotation?](
    https://insights.twilio.com/v1/Voice/{call_sid}/Annotation?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Annotation"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "answered_by": answered_by,
        "call_score": call_score,
        "comment": comment,
        "connectivity_issue": connectivity_issue,
        "incident": incident,
        "quality_issues": quality_issues,
        "spam": spam,
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
async def get_v1_voice_call_sid_events(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    edge: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        edge:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Events?&edge=%s&page_size=%s](
    https://insights.twilio.com/v1/Voice/{call_sid}/Events?&edge=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Events"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "edge": edge,
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
async def get_v1_voice_call_sid_metrics(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    edge: str = None,
    direction: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        edge:

        direction:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Metrics?&edge=%s&direction=%s&page_size=%s](
    https://insights.twilio.com/v1/Voice/{call_sid}/Metrics?&edge=%s&direction=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Metrics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "edge": edge,
        "direction": direction,
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
async def get_v1_voice_call_sid_summary(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    processing_state: str = None,
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        processing_state:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Summary?&processing_state=%s](
    https://insights.twilio.com/v1/Voice/{call_sid}/Summary?&processing_state=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Summary"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "processing_state": processing_state,
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
async def get_v1_voice_sid(
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
    [https://insights.twilio.com/v1/Voice/{sid}?](
    https://insights.twilio.com/v1/Voice/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{sid}"  # noqa
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
