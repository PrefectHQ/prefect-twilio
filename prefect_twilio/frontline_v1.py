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
async def get_v1_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a frontline user.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://frontline-api.twilio.com/v1/Users/{sid}?](
    https://frontline-api.twilio.com/v1/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://frontline-api.twilio.com/v1/Users/{sid}"  # noqa
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
async def post_v1_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    avatar: str = None,
    friendly_name: str = None,
    is_available: bool = None,
    state: str = None,
) -> Dict[str, Any]:
    """
    Update an existing frontline user.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        avatar:
            The avatar URL which will be shown in Frontline application.
        friendly_name:
            The string that you assigned to describe the User.
        is_available:
            Whether the User is available for new conversations. Set to `false` to
            prevent User from receiving new inbound conversations if you
            are using [Pool
            Routing](https://www.twilio.com/docs/frontline/handle-
            incoming-conversations
            3-pool-routing).
        state:
            Current state of this user. Can be either `active` or `deactivated`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://frontline-api.twilio.com/v1/Users/{sid}?](
    https://frontline-api.twilio.com/v1/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://frontline-api.twilio.com/v1/Users/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "avatar": avatar,
        "friendly_name": friendly_name,
        "is_available": is_available,
        "state": state,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
