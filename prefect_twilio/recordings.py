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
async def get_v1_recordings(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    source_sid: str = None,
    grouping_sid: list = None,
    date_created_after: str = None,
    date_created_before: str = None,
    media_type: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List of all Track recordings.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Read only the recordings that have this status. Can be: `processing`,
            `completed`, or `deleted`.
        source_sid:
            Read only the recordings that have this `source_sid`.
        grouping_sid:
            Read only recordings with this `grouping_sid`, which may include a
            `participant_sid` and/or a `room_sid`.
        date_created_after:
            Read only recordings that started on or after this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with
            time zone.
        date_created_before:
            Read only recordings that started before this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with
            time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-
            MM-DDThh:mm:ssZ`.
        media_type:
            Read only recordings that have this media type. Can be either `audio` or
            `video`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Recordings?&status=%s&source_sid=%s&grouping_sid=%s&date_created_after=%s&date_created_before=%s&media_type=%s&page_size=%s](
    https://video.twilio.com/v1/Recordings?&status=%s&source_sid=%s&grouping_sid=%s&date_created_after=%s&date_created_before=%s&media_type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://video.twilio.com/v1/Recordings"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "source_sid": source_sid,
        "grouping_sid": grouping_sid,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "media_type": media_type,
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
async def delete_v1_recordings_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Recording resource identified by a Recording SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Recordings/{sid}?](
    https://video.twilio.com/v1/Recordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Recordings/{sid}"  # noqa
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
async def get_v1_recordings_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single Recording resource identified by a Recording SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Recordings/{sid}?](
    https://video.twilio.com/v1/Recordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Recordings/{sid}"  # noqa
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
