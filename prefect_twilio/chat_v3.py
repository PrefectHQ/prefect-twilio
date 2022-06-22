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
async def post_v3_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    messaging_service_sid: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Channel.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        messaging_service_sid:
            The unique ID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) this
            channel belongs to.
        type:
            TThe Type for this Channel to migrate to. Can only be `private`.
            Migration to 'public' is not allowed.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v3/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v3/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v3/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "messaging_service_sid": messaging_service_sid,
        "type": type,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
        data=data,
    )
    return result
