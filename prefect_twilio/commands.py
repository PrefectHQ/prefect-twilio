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
async def get_v1_commands(
    twilio_credentials: "TwilioCredentials",
    sim: str = None,
    status: str = None,
    direction: str = None,
    transport: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Commands from your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        sim:
            The `sid` or `unique_name` of the [Sim
            resources](https://www.twilio.com/docs/wireless/api/sim-
            resource) to read.
        status:
            The status of the resources to read. Can be: `queued`, `sent`,
            `delivered`, `received`, or `failed`.
        direction:
            Only return Commands with this direction value.
        transport:
            Only return Commands with this transport value. Can be: `sms` or `ip`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Commands?&sim=%s&status=%s&direction=%s&transport=%s&page_size=%s](
    https://wireless.twilio.com/v1/Commands?&sim=%s&status=%s&direction=%s&transport=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://wireless.twilio.com/v1/Commands"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "sim": sim,
        "status": status,
        "direction": direction,
        "transport": transport,
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
async def post_v1_commands(
    twilio_credentials: "TwilioCredentials",
    callback_method: str = None,
    callback_url: str = None,
    command: str = None,
    command_mode: str = None,
    delivery_receipt_requested: bool = None,
    include_sid: str = None,
    sim: str = None,
) -> Dict[str, Any]:
    """
    Send a Command to a Sim.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_method:
            The HTTP method we use to call `callback_url`. Can be: `POST` or `GET`,
            and the default is `POST`.
        callback_url:
            The URL we call using the `callback_url` when the Command has finished
            sending, whether the command was delivered or it failed.
        command:
            The message body of the Command. Can be plain text in text mode or a
            Base64 encoded byte string in binary mode.
        command_mode:
            The mode to use when sending the SMS message. Can be: `text` or
            `binary`. The default SMS mode is `text`.
        delivery_receipt_requested:
            Whether to request delivery receipt from the recipient. For Commands
            that request delivery receipt, the Command state transitions
            to 'delivered' once the server has received a delivery
            receipt from the device. The default value is `true`.
        include_sid:
            Whether to include the SID of the command in the message body. Can be:
            `none`, `start`, or `end`, and the default behavior is
            `none`. When sending a Command to a SIM in text mode, we can
            automatically include the SID of the Command in the message
            body, which could be used to ensure that the device does not
            process the same Command more than once.  A value of `start`
            will prepend the message with the Command SID, and `end`
            will append it to the end, separating the Command SID from
            the message body with a space. The length of the Command SID
            is included in the 160 character limit so the SMS body must
            be 128 characters or less before the Command SID is
            included.
        sim:
            The `sid` or `unique_name` of the
            [SIM](https://www.twilio.com/docs/wireless/api/sim-resource)
            to send the Command to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Commands?](
    https://wireless.twilio.com/v1/Commands?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://wireless.twilio.com/v1/Commands"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "callback_method": callback_method,
        "callback_url": callback_url,
        "command": command,
        "command_mode": command_mode,
        "delivery_receipt_requested": delivery_receipt_requested,
        "include_sid": include_sid,
        "sim": sim,
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
async def delete_v1_commands_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Command instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Commands/{sid}?](
    https://wireless.twilio.com/v1/Commands/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/Commands/{sid}"  # noqa
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
async def get_v1_commands_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Command instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Commands/{sid}?](
    https://wireless.twilio.com/v1/Commands/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/Commands/{sid}"  # noqa
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
