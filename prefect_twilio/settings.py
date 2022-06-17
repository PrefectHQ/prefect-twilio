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
async def get_v1_settings(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve voice dialing permissions inheritance for the sub-account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/Settings?](
    https://voice.twilio.com/v1/Settings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://voice.twilio.com/v1/Settings"  # noqa

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
async def post_v1_settings(
    twilio_credentials: "TwilioCredentials",
    dialing_permissions_inheritance: bool = None,
) -> Dict[str, Any]:
    """
    Update voice dialing permissions inheritance for the sub-account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        dialing_permissions_inheritance:
            `true` for the sub-account to inherit voice dialing permissions from the
            Master Project; otherwise `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/Settings?](
    https://voice.twilio.com/v1/Settings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 202 | Accepted. |
    """  # noqa
    url = "https://voice.twilio.com/v1/Settings"  # noqa

    responses = {
        202: "Accepted.",  # noqa
    }

    data = {
        "dialing_permissions_inheritance": dialing_permissions_inheritance,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
