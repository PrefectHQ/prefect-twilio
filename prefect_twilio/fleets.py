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
async def get_v1_fleets(
    twilio_credentials: "TwilioCredentials",
    network_access_profile: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Fleets from your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        network_access_profile:
            The SID or unique name of the Network Access Profile that controls which
            cellular networks the Fleet's SIMs can connect to.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Fleets?&network_access_profile=%s&page_size=%s](
    https://supersim.twilio.com/v1/Fleets?&network_access_profile=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/Fleets"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "network_access_profile": network_access_profile,
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
async def post_v1_fleets(
    twilio_credentials: "TwilioCredentials",
    data_enabled: bool = None,
    data_limit: int = None,
    ip_commands_method: str = None,
    ip_commands_url: str = None,
    network_access_profile: str = None,
    sms_commands_enabled: bool = None,
    sms_commands_method: str = None,
    sms_commands_url: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a Fleet.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        data_enabled:
            Defines whether SIMs in the Fleet are capable of using
            2G/3G/4G/LTE/CAT-M data connectivity. Defaults to `true`.
        data_limit:
            The total data usage (download and upload combined) in Megabytes that
            each Sim resource assigned to the Fleet resource can consume
            during a billing period (normally one month). Value must be
            between 1MB (1) and 2TB (2,000,000). Defaults to 1GB
            (1,000).
        ip_commands_method:
            A string representing the HTTP method to use when making a request to
            `ip_commands_url`. Can be one of `POST` or `GET`. Defaults
            to `POST`.
        ip_commands_url:
            The URL that will receive a webhook when a Super SIM in the Fleet is
            used to send an IP Command from your device to a special IP
            address. Your server should respond with an HTTP status code
            in the 200 range; any response body will be ignored.
        network_access_profile:
            The SID or unique name of the Network Access Profile that will control
            which cellular networks the Fleet's SIMs can connect to.
        sms_commands_enabled:
            Defines whether SIMs in the Fleet are capable of sending and receiving
            machine-to-machine SMS via Commands. Defaults to `true`.
        sms_commands_method:
            A string representing the HTTP method to use when making a request to
            `sms_commands_url`. Can be one of `POST` or `GET`. Defaults
            to `POST`.
        sms_commands_url:
            The URL that will receive a webhook when a Super SIM in the Fleet is
            used to send an SMS from your device to the SMS Commands
            number. Your server should respond with an HTTP status code
            in the 200 range; any response body will be ignored.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used in place of the resource's `sid` in the URL to
            address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Fleets?](
    https://supersim.twilio.com/v1/Fleets?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/Fleets"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "data_enabled": data_enabled,
        "data_limit": data_limit,
        "ip_commands_method": ip_commands_method,
        "ip_commands_url": ip_commands_url,
        "network_access_profile": network_access_profile,
        "sms_commands_enabled": sms_commands_enabled,
        "sms_commands_method": sms_commands_method,
        "sms_commands_url": sms_commands_url,
        "unique_name": unique_name,
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
async def get_v1_fleets_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Fleet instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Fleets/{sid}?](
    https://supersim.twilio.com/v1/Fleets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Fleets/{sid}"  # noqa
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
async def post_v1_fleets_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    ip_commands_method: str = None,
    ip_commands_url: str = None,
    network_access_profile: str = None,
    sms_commands_method: str = None,
    sms_commands_url: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Updates the given properties of a Super SIM Fleet instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ip_commands_method:
            A string representing the HTTP method to use when making a request to
            `ip_commands_url`. Can be one of `POST` or `GET`. Defaults
            to `POST`.
        ip_commands_url:
            The URL that will receive a webhook when a Super SIM in the Fleet is
            used to send an IP Command from your device to a special IP
            address. Your server should respond with an HTTP status code
            in the 200 range; any response body will be ignored.
        network_access_profile:
            The SID or unique name of the Network Access Profile that will control
            which cellular networks the Fleet's SIMs can connect to.
        sms_commands_method:
            A string representing the HTTP method to use when making a request to
            `sms_commands_url`. Can be one of `POST` or `GET`. Defaults
            to `POST`.
        sms_commands_url:
            The URL that will receive a webhook when a Super SIM in the Fleet is
            used to send an SMS from your device to the SMS Commands
            number. Your server should respond with an HTTP status code
            in the 200 range; any response body will be ignored.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used in place of the resource's `sid` in the URL to
            address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Fleets/{sid}?](
    https://supersim.twilio.com/v1/Fleets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Fleets/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "ip_commands_method": ip_commands_method,
        "ip_commands_url": ip_commands_url,
        "network_access_profile": network_access_profile,
        "sms_commands_method": sms_commands_method,
        "sms_commands_url": sms_commands_url,
        "unique_name": unique_name,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
