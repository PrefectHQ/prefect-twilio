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
async def get_v1_player_streamers(
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Returns a list of PlayerStreamers.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            The sort order of the list by `date_created`. Can be: `asc` (ascending)
            or `desc` (descending) with `desc` as the default.
        status:
            Status to filter by, with possible values `created`, `started`, `ended`,
            or `failed`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/PlayerStreamers?&order=%s&status=%s&page_size=%s](
    https://media.twilio.com/v1/PlayerStreamers?&order=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://media.twilio.com/v1/PlayerStreamers"  # noqa

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
async def post_v1_player_streamers(
    twilio_credentials: "TwilioCredentials",
    max_duration: int = None,
    status_callback: str = None,
    status_callback_method: str = None,
    video: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        max_duration:
            The maximum time, in seconds, that the PlayerStreamer can run before
            automatically ends. The default value is 300 seconds, and
            the maximum value is 90000 seconds. Once this maximum
            duration is reached, Twilio will end the PlayerStreamer,
            regardless of whether media is still streaming.
        status_callback:
            The URL to which Twilio will send asynchronous webhook requests for
            every PlayerStreamer event. See [Status
            Callbacks](/docs/live/status-callbacks) for more details.
        status_callback_method:
            The HTTP method Twilio should use to call the `status_callback` URL. Can
            be `POST` or `GET` and the default is `POST`.
        video:
            Specifies whether the PlayerStreamer is configured to stream video.
            Defaults to `true`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/PlayerStreamers?](
    https://media.twilio.com/v1/PlayerStreamers?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://media.twilio.com/v1/PlayerStreamers"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "max_duration": max_duration,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "video": video,
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
async def get_v1_player_streamers_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single PlayerStreamer resource identified by a SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/PlayerStreamers/{sid}?](
    https://media.twilio.com/v1/PlayerStreamers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://media.twilio.com/v1/PlayerStreamers/{sid}"  # noqa
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
async def post_v1_player_streamers_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Updates a PlayerStreamer resource identified by a SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The status the PlayerStreamer should be transitioned to. Can be:
            `ended`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/PlayerStreamers/{sid}?](
    https://media.twilio.com/v1/PlayerStreamers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://media.twilio.com/v1/PlayerStreamers/{sid}"  # noqa
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
async def get_v1_player_streamers_sid_playback_grant(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    **This method is not enabled.** Returns a single PlaybackGrant resource
    identified by a SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/PlayerStreamers/{sid}/PlaybackGrant?](
    https://media.twilio.com/v1/PlayerStreamers/{sid}/PlaybackGrant?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://media.twilio.com/v1/PlayerStreamers/{sid}/PlaybackGrant"  # noqa
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
async def post_v1_player_streamers_sid_playback_grant(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    access_control_allow_origin: str = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        access_control_allow_origin:
            The full origin URL where the livestream can be streamed. If this is not
            provided, it can be streamed from any domain.
        ttl:
            The time to live of the PlaybackGrant. Default value is 15 seconds.
            Maximum value is 60 seconds.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://media.twilio.com/v1/PlayerStreamers/{sid}/PlaybackGrant?](
    https://media.twilio.com/v1/PlayerStreamers/{sid}/PlaybackGrant?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://media.twilio.com/v1/PlayerStreamers/{sid}/PlaybackGrant"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "access_control_allow_origin": access_control_allow_origin,
        "ttl": ttl,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
