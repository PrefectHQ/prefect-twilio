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
async def get_v1_conferences_conference_sid_participants_participant_sid(
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
