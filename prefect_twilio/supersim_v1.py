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
async def get_v1_e_sim_profiles(
    twilio_credentials: "TwilioCredentials",
    eid: str = None,
    sim_sid: str = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of eSIM Profiles.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        eid:
            List the eSIM Profiles that have been associated with an EId.
        sim_sid:
            Find the eSIM Profile resource related to a
            [Sim](https://www.twilio.com/docs/wireless/api/sim-resource)
            resource by providing the SIM SID. Will always return an
            array with either 1 or 0 records.
        status:
            List the eSIM Profiles that are in a given status.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/ESimProfiles?&eid=%s&sim_sid=%s&status=%s&page_size=%s](
    https://supersim.twilio.com/v1/ESimProfiles?&eid=%s&sim_sid=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/ESimProfiles"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "eid": eid,
        "sim_sid": sim_sid,
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
async def post_v1_e_sim_profiles(
    twilio_credentials: "TwilioCredentials",
    callback_method: str = None,
    callback_url: str = None,
    eid: str = None,
) -> Dict[str, Any]:
    """
    Order an eSIM Profile.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_method:
            The HTTP method we should use to call `callback_url`. Can be: `GET` or
            `POST` and the default is POST.
        callback_url:
            The URL we should call using the `callback_method` when the status of
            the eSIM Profile changes. At this stage of the eSIM Profile
            pilot, the a request to the URL will only be called when the
            ESimProfile resource changes from `reserving` to
            `available`.
        eid:
            Identifier of the eUICC that will claim the eSIM Profile.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/ESimProfiles?](
    https://supersim.twilio.com/v1/ESimProfiles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/ESimProfiles"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "callback_method": callback_method,
        "callback_url": callback_url,
        "eid": eid,
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
async def get_v1_e_sim_profiles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an eSIM Profile.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/ESimProfiles/{sid}?](
    https://supersim.twilio.com/v1/ESimProfiles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/ESimProfiles/{sid}"  # noqa
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


@task
async def get_v1_network_access_profiles(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Network Access Profiles from your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles?&page_size=%s](
    https://supersim.twilio.com/v1/NetworkAccessProfiles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/NetworkAccessProfiles"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
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
async def post_v1_network_access_profiles(
    twilio_credentials: "TwilioCredentials",
    networks: list = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Network Access Profile.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        networks:
            List of Network SIDs that this Network Access Profile will allow
            connections to.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used in place of the resource's `sid` in the URL to
            address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/NetworkAccessProfiles"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "networks": networks,
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
async def get_v1_network_access_profiles_network_access_profile_sid_networks(  # noqa
    network_access_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Network Access Profile resource's Network resource.

    Args:
        network_access_profile_sid:
            Network access profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks?&page_size=%s](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
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
async def post_v1_network_access_profiles_network_access_profile_sid_networks(  # noqa
    network_access_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    network: str = None,
) -> Dict[str, Any]:
    """
    Add a Network resource to the Network Access Profile resource.

    Args:
        network_access_profile_sid:
            Network access profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        network:
            The SID of the Network resource to be added to the Network Access
            Profile resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "network": network,
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
async def delete_v1_network_access_profiles_network_access_profile_sid_networks_sid(  # noqa
    network_access_profile_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove a Network resource from the Network Access Profile resource's.

    Args:
        network_access_profile_sid:
            Network access profile sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}"  # noqa
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
async def get_v1_network_access_profiles_network_access_profile_sid_networks_sid(  # noqa
    network_access_profile_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Network Access Profile resource's Network resource.

    Args:
        network_access_profile_sid:
            Network access profile sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}"  # noqa
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
async def get_v1_network_access_profiles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Network Access Profile instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}"  # noqa
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
async def post_v1_network_access_profiles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Updates the given properties of a Network Access Profile in your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        unique_name:
            The new unique name of the Network Access Profile.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
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
async def get_v1_networks(
    twilio_credentials: "TwilioCredentials",
    iso_country: str = None,
    mcc: str = None,
    mnc: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Network resources.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        iso_country:
            The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            of the Network resources to read.
        mcc:
            The 'mobile country code' of a country. Network resources with this
            `mcc` in their `identifiers` will be read.
        mnc:
            The 'mobile network code' of a mobile operator network. Network
            resources with this `mnc` in their `identifiers` will be
            read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Networks?&iso_country=%s&mcc=%s&mnc=%s&page_size=%s](
    https://supersim.twilio.com/v1/Networks?&iso_country=%s&mcc=%s&mnc=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/Networks"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "iso_country": iso_country,
        "mcc": mcc,
        "mnc": mnc,
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
async def get_v1_networks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Network resource.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Networks/{sid}?](
    https://supersim.twilio.com/v1/Networks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Networks/{sid}"  # noqa
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
async def get_v1_sims(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    fleet: str = None,
    iccid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Super SIMs from your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The status of the Sim resources to read. Can be `new`, `ready`,
            `active`, `inactive`, or `scheduled`.
        fleet:
            The SID or unique name of the Fleet to which a list of Sims are
            assigned.
        iccid:
            The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module
            ICCID) associated with a Super SIM to filter the list by.
            Passing this parameter will always return a list containing
            zero or one SIMs.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims?&status=%s&fleet=%s&iccid=%s&page_size=%s](
    https://supersim.twilio.com/v1/Sims?&status=%s&fleet=%s&iccid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/Sims"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "fleet": fleet,
        "iccid": iccid,
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
async def post_v1_sims(
    twilio_credentials: "TwilioCredentials",
    iccid: str = None,
    registration_code: str = None,
) -> Dict[str, Any]:
    """
    Register a Super SIM to your Account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        iccid:
            The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module
            ICCID) of the Super SIM to be added to your Account.
        registration_code:
            The 10-digit code required to claim the Super SIM for your Account.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims?](
    https://supersim.twilio.com/v1/Sims?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/Sims"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "iccid": iccid,
        "registration_code": registration_code,
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
async def get_v1_sims_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Super SIM instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims/{sid}?](
    https://supersim.twilio.com/v1/Sims/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Sims/{sid}"  # noqa
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
async def post_v1_sims_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    account_sid: str = None,
    callback_method: str = None,
    callback_url: str = None,
    fleet: str = None,
    status: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Updates the given properties of a Super SIM instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        account_sid:
            The SID of the Account to which the Sim resource should belong. The
            Account SID can only be that of the requesting Account or
            that of a Subaccount of the requesting Account. Only valid
            when the Sim resource's status is new.
        callback_method:
            The HTTP method we should use to call `callback_url`. Can be: `GET` or
            `POST` and the default is POST.
        callback_url:
            The URL we should call using the `callback_method` after an asynchronous
            update has finished.
        fleet:
            The SID or unique name of the Fleet to which the SIM resource should be
            assigned.
        status:
            The new status of the resource. Can be: `ready`, `active`, or
            `inactive`. See the [Super SIM Status
            Values](https://www.twilio.com/docs/iot/supersim/api/sim-
            resource
            status-values) for more info.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used in place of the resource's `sid` in the URL to
            address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims/{sid}?](
    https://supersim.twilio.com/v1/Sims/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 202 | Accepted. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Sims/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
        202: "Accepted.",  # noqa
    }

    data = {
        "account_sid": account_sid,
        "callback_method": callback_method,
        "callback_url": callback_url,
        "fleet": fleet,
        "status": status,
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
async def get_v1_sims_sim_sid_billing_periods(
    sim_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Billing Periods for a Super SIM.

    Args:
        sim_sid:
            Sim sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims/{sim_sid}/BillingPeriods?&page_size=%s](
    https://supersim.twilio.com/v1/Sims/{sim_sid}/BillingPeriods?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Sims/{sim_sid}/BillingPeriods"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
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
async def get_v1_sms_commands(
    twilio_credentials: "TwilioCredentials",
    sim: str = None,
    status: str = None,
    direction: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of SMS Commands from your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        sim:
            The SID or unique name of the Sim resource that SMS Command was sent to
            or from.
        status:
            The status of the SMS Command. Can be: `queued`, `sent`, `delivered`,
            `received` or `failed`. See the [SMS Command Status
            Values](https://www.twilio.com/docs/wireless/api/smscommand-
            resource
            status-values) for a description of each.
        direction:
            The direction of the SMS Command. Can be `to_sim` or `from_sim`. The
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
    [https://supersim.twilio.com/v1/SmsCommands?&sim=%s&status=%s&direction=%s&page_size=%s](
    https://supersim.twilio.com/v1/SmsCommands?&sim=%s&status=%s&direction=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/SmsCommands"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "sim": sim,
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
async def post_v1_sms_commands(
    twilio_credentials: "TwilioCredentials",
    callback_method: str = None,
    callback_url: str = None,
    payload: str = None,
    sim: str = None,
) -> Dict[str, Any]:
    """
    Send SMS Command to a Sim.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_method:
            The HTTP method we should use to call `callback_url`. Can be: `GET` or
            `POST` and the default is POST.
        callback_url:
            The URL we should call using the `callback_method` after we have sent
            the command.
        payload:
            The message body of the SMS Command.
        sim:
            The `sid` or `unique_name` of the
            [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-
            resource) to send the SMS Command to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/SmsCommands?](
    https://supersim.twilio.com/v1/SmsCommands?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/SmsCommands"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "callback_method": callback_method,
        "callback_url": callback_url,
        "payload": payload,
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
async def get_v1_sms_commands_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch SMS Command instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/SmsCommands/{sid}?](
    https://supersim.twilio.com/v1/SmsCommands/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/SmsCommands/{sid}"  # noqa
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
async def get_v1_usage_records(
    twilio_credentials: "TwilioCredentials",
    sim: str = None,
    fleet: str = None,
    network: str = None,
    iso_country: str = None,
    group: str = None,
    granularity: str = None,
    start_time: str = None,
    end_time: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List UsageRecords.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        sim:
            SID or unique name of a Sim resource. Only show UsageRecords
            representing usage incurred by this Super SIM.
        fleet:
            SID or unique name of a Fleet resource. Only show UsageRecords
            representing usage for Super SIMs belonging to this Fleet
            resource at the time the usage occurred.
        network:
            SID of a Network resource. Only show UsageRecords representing usage on
            this network.
        iso_country:
            Alpha-2 ISO Country Code. Only show UsageRecords representing usage in
            this country.
        group:
            Dimension over which to aggregate usage records. Can be: `sim`, `fleet`,
            `network`, `isoCountry`. Default is to not aggregate across
            any of these dimensions, UsageRecords will be aggregated
            into the time buckets described by the `Granularity`
            parameter.
        granularity:
            Time-based grouping that UsageRecords should be aggregated by. Can be:
            `hour`, `day`, or `all`. Default is `all`. `all` returns one
            UsageRecord that describes the usage for the entire period.
        start_time:
            Only include usage that occurred at or after this time, specified in
            [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
            Default is one month before the `end_time`.
        end_time:
            Only include usage that occurred before this time (exclusive), specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format. Default is the current time.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/UsageRecords?&sim=%s&fleet=%s&network=%s&iso_country=%s&group=%s&granularity=%s&start_time=%s&end_time=%s&page_size=%s](
    https://supersim.twilio.com/v1/UsageRecords?&sim=%s&fleet=%s&network=%s&iso_country=%s&group=%s&granularity=%s&start_time=%s&end_time=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/UsageRecords"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "sim": sim,
        "fleet": fleet,
        "network": network,
        "iso_country": iso_country,
        "group": group,
        "granularity": granularity,
        "start_time": start_time,
        "end_time": end_time,
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
