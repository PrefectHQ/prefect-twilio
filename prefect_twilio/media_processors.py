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
async def get_v1_media_processors(
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Returns a list of MediaProcessors.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            The sort order of the list by `date_created`. Can be: `asc` (ascending)
            or `desc` (descending) with `desc` as the default.
        status:
            Status to filter by, with possible values `started`, `ended` or
            `failed`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/MediaProcessors?&order=%s&status=%s&page_size=%s](
    https://media.twilio.com/v1/MediaProcessors?&order=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://media.twilio.com/v1/MediaProcessors"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
        "status": status,
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
async def post_v1_media_processors(
    twilio_credentials: "TwilioCredentials",
    extension: str = None,
    extension_context: str = None,
    extension_environment: str = None,
    max_duration: int = None,
    status_callback: str = None,
    status_callback_method: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        extension:
            The [Media Extension](/docs/live/api/media-extensions-overview) name or
            URL. Ex: `video-composer-v2`.
        extension_context:
            The context of the Media Extension, represented as a JSON dictionary.
            See the documentation for the specific [Media
            Extension](/docs/live/api/media-extensions-overview) you are
            using for more information about the context to send.
        extension_environment:
            User-defined environment variables for the Media Extension, represented
            as a JSON dictionary of key/value strings. See the
            documentation for the specific [Media
            Extension](/docs/live/api/media-extensions-overview) you are
            using for more information about whether you need to provide
            this.
        max_duration:
            The maximum time, in seconds, that the MediaProcessor can run before
            automatically ends. The default value is 300 seconds, and
            the maximum value is 90000 seconds. Once this maximum
            duration is reached, Twilio will end the MediaProcessor,
            regardless of whether media is still streaming.
        status_callback:
            The URL to which Twilio will send asynchronous webhook requests for
            every MediaProcessor event. See [Status
            Callbacks](/docs/live/status-callbacks) for details.
        status_callback_method:
            The HTTP method Twilio should use to call the `status_callback` URL. Can
            be `POST` or `GET` and the default is `POST`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/MediaProcessors?](
    https://media.twilio.com/v1/MediaProcessors?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://media.twilio.com/v1/MediaProcessors"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "extension": extension,
        "extension_context": extension_context,
        "extension_environment": extension_environment,
        "max_duration": max_duration,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
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
async def get_v1_media_processors_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single MediaProcessor resource identified by a SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/MediaProcessors/{sid}?](
    https://media.twilio.com/v1/MediaProcessors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://media.twilio.com/v1/MediaProcessors/{sid}"  # noqa
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
async def post_v1_media_processors_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Updates a MediaProcessor resource identified by a SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The status of the MediaProcessor. Can be `ended`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/MediaProcessors/{sid}?](
    https://media.twilio.com/v1/MediaProcessors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://media.twilio.com/v1/MediaProcessors/{sid}"  # noqa
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
