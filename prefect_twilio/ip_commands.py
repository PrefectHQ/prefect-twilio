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
async def get_v1_ip_commands(
    twilio_credentials: "TwilioCredentials",
    sim: str = None,
    sim_iccid: str = None,
    status: str = None,
    direction: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of IP Commands from your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        sim:
            The SID or unique name of the Sim resource that IP Command was sent to
            or from.
        sim_iccid:
            The ICCID of the Sim resource that IP Command was sent to or from.
        status:
            The status of the IP Command. Can be: `queued`, `sent`, `received` or
            `failed`. See the [IP Command Status
            Values](https://www.twilio.com/docs/wireless/api/ipcommand-
            resource
            status-values) for a description of each.
        direction:
            The direction of the IP Command. Can be `to_sim` or `from_sim`. The
            value of `to_sim` is synonymous with the term `mobile
            terminated`, and `from_sim` is synonymous with the term
            `mobile originated`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/IpCommands?&sim=%s&sim_iccid=%s&status=%s&direction=%s&page_size=%s](
    https://supersim.twilio.com/v1/IpCommands?&sim=%s&sim_iccid=%s&status=%s&direction=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/IpCommands"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "sim": sim,
        "sim_iccid": sim_iccid,
        "status": status,
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
async def post_v1_ip_commands(
    twilio_credentials: "TwilioCredentials",
    callback_method: str = None,
    callback_url: str = None,
    device_port: int = None,
    payload: str = None,
    payload_type: str = None,
    sim: str = None,
) -> Dict[str, Any]:
    """
    Send an IP Command to a Super SIM.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_method:
            The HTTP method we should use to call `callback_url`. Can be `GET` or
            `POST`, and the default is `POST`.
        callback_url:
            The URL we should call using the `callback_method` after we have sent
            the IP Command.
        device_port:
            The device port to which the IP Command will be sent.
        payload:
            The payload to be delivered to the device.
        payload_type:
            Indicates how the payload is encoded. Either `text` or `binary`.
            Defaults to `text`.
        sim:
            The `sid` or `unique_name` of the [Super
            SIM](https://www.twilio.com/docs/iot/supersim/api/sim-
            resource) to send the IP Command to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/IpCommands?](
    https://supersim.twilio.com/v1/IpCommands?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/IpCommands"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "callback_method": callback_method,
        "callback_url": callback_url,
        "device_port": device_port,
        "payload": payload,
        "payload_type": payload_type,
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
async def get_v1_ip_commands_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch IP Command instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/IpCommands/{sid}?](
    https://supersim.twilio.com/v1/IpCommands/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/IpCommands/{sid}"  # noqa
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
