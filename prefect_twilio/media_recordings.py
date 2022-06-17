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
async def get_v1_media_recordings(
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    status: str = None,
    processor_sid: str = None,
    source_sid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Returns a list of MediaRecordings.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            The sort order of the list by `date_created`. Can be: `asc` (ascending)
            or `desc` (descending) with `desc` as the default.
        status:
            Status to filter by, with possible values `processing`, `completed`,
            `deleted`, or `failed`.
        processor_sid:
            SID of a MediaProcessor to filter by.
        source_sid:
            SID of a MediaRecording source to filter by.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/MediaRecordings?&order=%s&status=%s&processor_sid=%s&source_sid=%s&page_size=%s](
    https://media.twilio.com/v1/MediaRecordings?&order=%s&status=%s&processor_sid=%s&source_sid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://media.twilio.com/v1/MediaRecordings"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
        "status": status,
        "processor_sid": processor_sid,
        "source_sid": source_sid,
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
async def delete_v1_media_recordings_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Deletes a MediaRecording resource identified by a SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/MediaRecordings/{sid}?](
    https://media.twilio.com/v1/MediaRecordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://media.twilio.com/v1/MediaRecordings/{sid}"  # noqa
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
async def get_v1_media_recordings_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single MediaRecording resource identified by a SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/MediaRecordings/{sid}?](
    https://media.twilio.com/v1/MediaRecordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://media.twilio.com/v1/MediaRecordings/{sid}"  # noqa
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
