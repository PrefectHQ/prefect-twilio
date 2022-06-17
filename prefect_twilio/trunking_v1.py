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
async def get_v1_trunks(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


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
    [https://trunking.twilio.com/v1/Trunks?&page_size=%s](
    https://trunking.twilio.com/v1/Trunks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://trunking.twilio.com/v1/Trunks"  # noqa

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
async def post_v1_trunks(
    twilio_credentials: "TwilioCredentials",
    cnam_lookup_enabled: bool = None,
    disaster_recovery_method: str = None,
    disaster_recovery_url: str = None,
    domain_name: str = None,
    friendly_name: str = None,
    secure: bool = None,
    transfer_caller_id: str = None,
    transfer_mode: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        cnam_lookup_enabled:
            Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If
            enabled, all inbound calls to the SIP Trunk from the United
            States and Canada automatically perform a CNAM Lookup and
            display Caller ID data on your phone. See [CNAM
            Lookups](https://www.twilio.com/docs/sip-trunking
            CNAM) for more information.
        disaster_recovery_method:
            The HTTP method we should use to call the `disaster_recovery_url`. Can
            be: `GET` or `POST`.
        disaster_recovery_url:
            The URL we should call using the `disaster_recovery_method` if an error
            occurs while sending SIP traffic towards the configured
            Origination URL. We retrieve TwiML from the URL and execute
            the instructions like any other normal TwiML call. See
            [Disaster Recovery](https://www.twilio.com/docs/sip-trunking
            disaster-recovery) for more information.
        domain_name:
            The unique address you reserve on Twilio to which you route your SIP
            traffic. Domain names can contain letters, digits, and `-`
            and must end with `pstn.twilio.com`. See [Termination
            Settings](https://www.twilio.com/docs/sip-trunking
            termination) for more information.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        secure:
            Whether Secure Trunking is enabled for the trunk. If enabled, all calls
            going through the trunk will be secure using SRTP for media
            and TLS for signaling. If disabled, then RTP will be used
            for media. See [Secure
            Trunking](https://www.twilio.com/docs/sip-trunking
            securetrunking) for more information.
        transfer_caller_id:
            Caller Id for transfer target. Can be: `from-transferee` (default) or
            `from-transferor`.
        transfer_mode:
            The call transfer settings for the trunk. Can be: `enable-all`, `sip-
            only` and `disable-all`. See
            [Transfer](https://www.twilio.com/docs/sip-trunking/call-
            transfer) for more information.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks?](
    https://trunking.twilio.com/v1/Trunks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://trunking.twilio.com/v1/Trunks"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "cnam_lookup_enabled": cnam_lookup_enabled,
        "disaster_recovery_method": disaster_recovery_method,
        "disaster_recovery_url": disaster_recovery_url,
        "domain_name": domain_name,
        "friendly_name": friendly_name,
        "secure": secure,
        "transfer_caller_id": transfer_caller_id,
        "transfer_mode": transfer_mode,
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
async def delete_v1_trunks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{sid}"  # noqa
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
async def get_v1_trunks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{sid}"  # noqa
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
async def post_v1_trunks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    cnam_lookup_enabled: bool = None,
    disaster_recovery_method: str = None,
    disaster_recovery_url: str = None,
    domain_name: str = None,
    friendly_name: str = None,
    secure: bool = None,
    transfer_caller_id: str = None,
    transfer_mode: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        cnam_lookup_enabled:
            Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If
            enabled, all inbound calls to the SIP Trunk from the United
            States and Canada automatically perform a CNAM Lookup and
            display Caller ID data on your phone. See [CNAM
            Lookups](https://www.twilio.com/docs/sip-trunking
            CNAM) for more information.
        disaster_recovery_method:
            The HTTP method we should use to call the `disaster_recovery_url`. Can
            be: `GET` or `POST`.
        disaster_recovery_url:
            The URL we should call using the `disaster_recovery_method` if an error
            occurs while sending SIP traffic towards the configured
            Origination URL. We retrieve TwiML from the URL and execute
            the instructions like any other normal TwiML call. See
            [Disaster Recovery](https://www.twilio.com/docs/sip-trunking
            disaster-recovery) for more information.
        domain_name:
            The unique address you reserve on Twilio to which you route your SIP
            traffic. Domain names can contain letters, digits, and `-`
            and must end with `pstn.twilio.com`. See [Termination
            Settings](https://www.twilio.com/docs/sip-trunking
            termination) for more information.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        secure:
            Whether Secure Trunking is enabled for the trunk. If enabled, all calls
            going through the trunk will be secure using SRTP for media
            and TLS for signaling. If disabled, then RTP will be used
            for media. See [Secure
            Trunking](https://www.twilio.com/docs/sip-trunking
            securetrunking) for more information.
        transfer_caller_id:
            Caller Id for transfer target. Can be: `from-transferee` (default) or
            `from-transferor`.
        transfer_mode:
            The call transfer settings for the trunk. Can be: `enable-all`, `sip-
            only` and `disable-all`. See
            [Transfer](https://www.twilio.com/docs/sip-trunking/call-
            transfer) for more information.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "cnam_lookup_enabled": cnam_lookup_enabled,
        "disaster_recovery_method": disaster_recovery_method,
        "disaster_recovery_url": disaster_recovery_url,
        "domain_name": domain_name,
        "friendly_name": friendly_name,
        "secure": secure,
        "transfer_caller_id": transfer_caller_id,
        "transfer_mode": transfer_mode,
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
async def get_v1_trunks_trunk_sid_credential_lists(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists?&page_size=%s](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists"  # noqa
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
async def post_v1_trunks_trunk_sid_credential_lists(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
    credential_list_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        credential_list_sid:
            The SID of the [Credential
            List](https://www.twilio.com/docs/voice/sip/api/sip-
            credentiallist-resource) that you want to associate with the
            trunk. Once associated, we will authenticate access to the
            trunk against this list.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "credential_list_sid": credential_list_sid,
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
async def delete_v1_trunks_trunk_sid_credential_lists_sid(
    trunk_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists/{sid}"  # noqa
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
async def get_v1_trunks_trunk_sid_credential_lists_sid(
    trunk_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists/{sid}"  # noqa
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
async def get_v1_trunks_trunk_sid_ip_access_control_lists(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all IP Access Control Lists for a Trunk.

    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists?&page_size=%s](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists"  # noqa
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
async def post_v1_trunks_trunk_sid_ip_access_control_lists(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
    ip_access_control_list_sid: str = None,
) -> Dict[str, Any]:
    """
    Associate an IP Access Control List with a Trunk.

    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ip_access_control_list_sid:
            The SID of the [IP Access Control
            List](https://www.twilio.com/docs/voice/sip/api/sip-
            ipaccesscontrollist-resource) that you want to associate
            with the trunk.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "ip_access_control_list_sid": ip_access_control_list_sid,
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
async def delete_v1_trunks_trunk_sid_ip_access_control_lists_sid(
    trunk_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an associated IP Access Control List from a Trunk.

    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists/{sid}"  # noqa
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
async def get_v1_trunks_trunk_sid_ip_access_control_lists_sid(
    trunk_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/IpAccessControlLists/{sid}"  # noqa
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
async def get_v1_trunks_trunk_sid_origination_urls(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls?&page_size=%s](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls"  # noqa
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
async def post_v1_trunks_trunk_sid_origination_urls(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
    enabled: bool = None,
    friendly_name: str = None,
    priority: int = None,
    sip_url: str = None,
    weight: int = None,
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        enabled:
            Whether the URL is enabled. The default is `true`.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        priority:
            The relative importance of the URI. Can be an integer from 0 to 65535,
            inclusive, and the default is 10. The lowest number
            represents the most important URI.
        sip_url:
            The SIP address you want Twilio to route your Origination calls to. This
            must be a `sip:` schema.
        weight:
            The value that determines the relative share of the load the URI should
            receive compared to other URIs with the same priority. Can
            be an integer from 1 to 65535, inclusive, and the default is
            10. URLs with higher values receive more load than those
            with lower ones with the same priority.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "enabled": enabled,
        "friendly_name": friendly_name,
        "priority": priority,
        "sip_url": sip_url,
        "weight": weight,
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
async def delete_v1_trunks_trunk_sid_origination_urls_sid(
    trunk_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}"  # noqa
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
async def get_v1_trunks_trunk_sid_origination_urls_sid(
    trunk_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}"  # noqa
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
async def post_v1_trunks_trunk_sid_origination_urls_sid(
    trunk_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    enabled: bool = None,
    friendly_name: str = None,
    priority: int = None,
    sip_url: str = None,
    weight: int = None,
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        enabled:
            Whether the URL is enabled. The default is `true`.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        priority:
            The relative importance of the URI. Can be an integer from 0 to 65535,
            inclusive, and the default is 10. The lowest number
            represents the most important URI.
        sip_url:
            The SIP address you want Twilio to route your Origination calls to. This
            must be a `sip:` schema. `sips` is NOT supported.
        weight:
            The value that determines the relative share of the load the URI should
            receive compared to other URIs with the same priority. Can
            be an integer from 1 to 65535, inclusive, and the default is
            10. URLs with higher values receive more load than those
            with lower ones with the same priority.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "enabled": enabled,
        "friendly_name": friendly_name,
        "priority": priority,
        "sip_url": sip_url,
        "weight": weight,
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
async def get_v1_trunks_trunk_sid_phone_numbers(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers?&page_size=%s](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers"  # noqa
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
async def post_v1_trunks_trunk_sid_phone_numbers(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
    phone_number_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        phone_number_sid:
            The SID of the [Incoming Phone
            Number](https://www.twilio.com/docs/phone-
            numbers/api/incomingphonenumber-resource) that you want to
            associate with the trunk.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "phone_number_sid": phone_number_sid,
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
async def delete_v1_trunks_trunk_sid_phone_numbers_sid(
    trunk_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers/{sid}"  # noqa
    )
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
async def get_v1_trunks_trunk_sid_phone_numbers_sid(
    trunk_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers/{sid}?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/PhoneNumbers/{sid}"  # noqa
    )
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
async def get_v1_trunks_trunk_sid_recording(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/Recording?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/Recording?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/Recording"  # noqa
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
async def post_v1_trunks_trunk_sid_recording(
    trunk_sid: str,
    twilio_credentials: "TwilioCredentials",
    mode: str = None,
    trim: str = None,
) -> Dict[str, Any]:
    """


    Args:
        trunk_sid:
            Trunk sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        mode:
            The recording mode for the trunk. Can be do-not-record (default),
            record-from-ringing, record-from-answer, record-from-
            ringing-dual, or record-from-answer-dual.
        trim:
            The recording trim setting for the trunk. Can be do-not-trim (default)
            or trim-silence.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trunking.twilio.com/v1/Trunks/{trunk_sid}/Recording?](
    https://trunking.twilio.com/v1/Trunks/{trunk_sid}/Recording?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 202 | Accepted. |
    """  # noqa
    url = f"https://trunking.twilio.com/v1/Trunks/{trunk_sid}/Recording"  # noqa
    responses = {
        202: "Accepted.",  # noqa
    }

    data = {
        "mode": mode,
        "trim": trim,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
