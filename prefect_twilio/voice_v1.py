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
async def delete_v1_archives_date_calls_sid(
    date: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete an archived call record from Bulk Export. Note: this does not also delete
    the record from the Voice API.

    Args:
        date:
            Date used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/Archives/{date}/Calls/{sid}?](
    https://voice.twilio.com/v1/Archives/{date}/Calls/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/Archives/{date}/Calls/{sid}"  # noqa
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
async def get_v1_byoc_trunks(
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
    [https://voice.twilio.com/v1/ByocTrunks?&page_size=%s](
    https://voice.twilio.com/v1/ByocTrunks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://voice.twilio.com/v1/ByocTrunks"  # noqa

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
async def post_v1_byoc_trunks(
    twilio_credentials: "TwilioCredentials",
    cnam_lookup_enabled: bool = None,
    connection_policy_sid: str = None,
    friendly_name: str = None,
    from_domain_sid: str = None,
    status_callback_method: str = None,
    status_callback_url: str = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        cnam_lookup_enabled:
            Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If
            enabled, all inbound calls to the BYOC Trunk from the United
            States and Canada automatically perform a CNAM Lookup and
            display Caller ID data on your phone. See [CNAM
            Lookups](https://www.twilio.com/docs/sip-trunking
            CNAM) for more information.
        connection_policy_sid:
            The SID of the Connection Policy that Twilio will use when routing
            traffic to your communications infrastructure.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        from_domain_sid:
            The SID of the SIP Domain that should be used in the `From` header of
            originating calls sent to your SIP infrastructure. If your
            SIP infrastructure allows users to "call back" an incoming
            call, configure this with a [SIP
            Domain](https://www.twilio.com/docs/voice/api/sending-sip)
            to ensure proper routing. If not configured, the from domain
            will default to "sip.twilio.com".
        status_callback_method:
            The HTTP method we should use to call `status_callback_url`. Can be:
            `GET` or `POST`.
        status_callback_url:
            The URL that we should call to pass status parameters (such as call
            ended) to your application.
        voice_fallback_method:
            The HTTP method we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs while retrieving or
            executing the TwiML from `voice_url`.
        voice_method:
            The HTTP method we should use to call `voice_url`. Can be: `GET` or
            `POST`.
        voice_url:
            The URL we should call when the BYOC Trunk receives a call.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ByocTrunks?](
    https://voice.twilio.com/v1/ByocTrunks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://voice.twilio.com/v1/ByocTrunks"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "cnam_lookup_enabled": cnam_lookup_enabled,
        "connection_policy_sid": connection_policy_sid,
        "friendly_name": friendly_name,
        "from_domain_sid": from_domain_sid,
        "status_callback_method": status_callback_method,
        "status_callback_url": status_callback_url,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_url": voice_url,
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
async def delete_v1_byoc_trunks_sid(
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
    [https://voice.twilio.com/v1/ByocTrunks/{sid}?](
    https://voice.twilio.com/v1/ByocTrunks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ByocTrunks/{sid}"  # noqa
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
async def get_v1_byoc_trunks_sid(
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
    [https://voice.twilio.com/v1/ByocTrunks/{sid}?](
    https://voice.twilio.com/v1/ByocTrunks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ByocTrunks/{sid}"  # noqa
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
async def post_v1_byoc_trunks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    cnam_lookup_enabled: bool = None,
    connection_policy_sid: str = None,
    friendly_name: str = None,
    from_domain_sid: str = None,
    status_callback_method: str = None,
    status_callback_url: str = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        cnam_lookup_enabled:
            Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If
            enabled, all inbound calls to the BYOC Trunk from the United
            States and Canada automatically perform a CNAM Lookup and
            display Caller ID data on your phone. See [CNAM
            Lookups](https://www.twilio.com/docs/sip-trunking
            CNAM) for more information.
        connection_policy_sid:
            The SID of the Connection Policy that Twilio will use when routing
            traffic to your communications infrastructure.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        from_domain_sid:
            The SID of the SIP Domain that should be used in the `From` header of
            originating calls sent to your SIP infrastructure. If your
            SIP infrastructure allows users to "call back" an incoming
            call, configure this with a [SIP
            Domain](https://www.twilio.com/docs/voice/api/sending-sip)
            to ensure proper routing. If not configured, the from domain
            will default to "sip.twilio.com".
        status_callback_method:
            The HTTP method we should use to call `status_callback_url`. Can be:
            `GET` or `POST`.
        status_callback_url:
            The URL that we should call to pass status parameters (such as call
            ended) to your application.
        voice_fallback_method:
            The HTTP method we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs while retrieving or
            executing the TwiML requested by `voice_url`.
        voice_method:
            The HTTP method we should use to call `voice_url`.
        voice_url:
            The URL we should call when the BYOC Trunk receives a call.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ByocTrunks/{sid}?](
    https://voice.twilio.com/v1/ByocTrunks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ByocTrunks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "cnam_lookup_enabled": cnam_lookup_enabled,
        "connection_policy_sid": connection_policy_sid,
        "friendly_name": friendly_name,
        "from_domain_sid": from_domain_sid,
        "status_callback_method": status_callback_method,
        "status_callback_url": status_callback_url,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_url": voice_url,
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
async def get_v1_connection_policies(
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
    [https://voice.twilio.com/v1/ConnectionPolicies?&page_size=%s](
    https://voice.twilio.com/v1/ConnectionPolicies?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://voice.twilio.com/v1/ConnectionPolicies"  # noqa

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
async def post_v1_connection_policies(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies?](
    https://voice.twilio.com/v1/ConnectionPolicies?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://voice.twilio.com/v1/ConnectionPolicies"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v1_connection_policies_connection_policy_sid_targets(  # noqa
    connection_policy_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets?&page_size=%s](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets"  # noqa
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
async def post_v1_connection_policies_connection_policy_sid_targets(  # noqa
    connection_policy_sid: str,
    twilio_credentials: "TwilioCredentials",
    enabled: bool = None,
    friendly_name: str = None,
    priority: int = None,
    target: str = None,
    weight: int = None,
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        enabled:
            Whether the Target is enabled. The default is `true`.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        priority:
            The relative importance of the target. Can be an integer from 0 to
            65535, inclusive, and the default is 10. The lowest number
            represents the most important target.
        target:
            The SIP address you want Twilio to route your calls to. This must be a
            `sip:` schema. `sips` is NOT supported.
        weight:
            The value that determines the relative share of the load the Target
            should receive compared to other Targets with the same
            priority. Can be an integer from 1 to 65535, inclusive, and
            the default is 10. Targets with higher values receive more
            load than those with lower ones with the same priority.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets?](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "enabled": enabled,
        "friendly_name": friendly_name,
        "priority": priority,
        "target": target,
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
async def delete_v1_connection_policies_connection_policy_sid_targets_sid(  # noqa
    connection_policy_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}"  # noqa
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
async def get_v1_connection_policies_connection_policy_sid_targets_sid(  # noqa
    connection_policy_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}"  # noqa
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
async def post_v1_connection_policies_connection_policy_sid_targets_sid(  # noqa
    connection_policy_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    enabled: bool = None,
    friendly_name: str = None,
    priority: int = None,
    target: str = None,
    weight: int = None,
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        enabled:
            Whether the Target is enabled.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        priority:
            The relative importance of the target. Can be an integer from 0 to
            65535, inclusive. The lowest number represents the most
            important target.
        target:
            The SIP address you want Twilio to route your calls to. This must be a
            `sip:` schema. `sips` is NOT supported.
        weight:
            The value that determines the relative share of the load the Target
            should receive compared to other Targets with the same
            priority. Can be an integer from 1 to 65535, inclusive.
            Targets with higher values receive more load than those with
            lower ones with the same priority.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "enabled": enabled,
        "friendly_name": friendly_name,
        "priority": priority,
        "target": target,
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
async def delete_v1_connection_policies_sid(
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
    [https://voice.twilio.com/v1/ConnectionPolicies/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{sid}"  # noqa
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
async def get_v1_connection_policies_sid(
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
    [https://voice.twilio.com/v1/ConnectionPolicies/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{sid}"  # noqa
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
async def post_v1_connection_policies_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def post_v1_dialing_permissions_bulk_country_updates(
    twilio_credentials: "TwilioCredentials",
    update_request: str = None,
) -> Dict[str, Any]:
    """
    Create a bulk update request to change voice dialing country permissions of one
    or more countries identified by the corresponding [ISO country
    code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        update_request:
            URL encoded JSON array of update objects. example : `[ { "iso_code":
            "GB", "low_risk_numbers_enabled": "true",
            "high_risk_special_numbers_enabled":"true",
            "high_risk_tollfraud_numbers_enabled": "false" } ]`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/DialingPermissions/BulkCountryUpdates?](
    https://voice.twilio.com/v1/DialingPermissions/BulkCountryUpdates?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://voice.twilio.com/v1/DialingPermissions/BulkCountryUpdates"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "update_request": update_request,
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
async def get_v1_dialing_permissions_countries(
    twilio_credentials: "TwilioCredentials",
    iso_code: str = None,
    continent: str = None,
    country_code: str = None,
    low_risk_numbers_enabled: bool = None,
    high_risk_special_numbers_enabled: bool = None,
    high_risk_tollfraud_numbers_enabled: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve all voice dialing country permissions for this account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        iso_code:
            Filter to retrieve the country permissions by specifying the [ISO
            country
            code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        continent:
            Filter to retrieve the country permissions by specifying the continent.
        country_code:
            Filter the results by specified [country
            codes](https://www.itu.int/itudoc/itu-t/ob-
            lists/icc/e164_763.html).
        low_risk_numbers_enabled:
            Filter to retrieve the country permissions with dialing to low-risk
            numbers enabled. Can be: `true` or `false`.
        high_risk_special_numbers_enabled:
            Filter to retrieve the country permissions with dialing to high-risk
            special service numbers enabled. Can be: `true` or `false`.
        high_risk_tollfraud_numbers_enabled:
            Filter to retrieve the country permissions with dialing to high-risk
            [toll fraud](https://www.twilio.com/learn/voice-and-
            video/toll-fraud) numbers enabled. Can be: `true` or
            `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/DialingPermissions/Countries?&iso_code=%s&continent=%s&country_code=%s&low_risk_numbers_enabled=%s&high_risk_special_numbers_enabled=%s&high_risk_tollfraud_numbers_enabled=%s&page_size=%s](
    https://voice.twilio.com/v1/DialingPermissions/Countries?&iso_code=%s&continent=%s&country_code=%s&low_risk_numbers_enabled=%s&high_risk_special_numbers_enabled=%s&high_risk_tollfraud_numbers_enabled=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://voice.twilio.com/v1/DialingPermissions/Countries"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "iso_code": iso_code,
        "continent": continent,
        "country_code": country_code,
        "low_risk_numbers_enabled": low_risk_numbers_enabled,
        "high_risk_special_numbers_enabled": high_risk_special_numbers_enabled,
        "high_risk_tollfraud_numbers_enabled": high_risk_tollfraud_numbers_enabled,
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
async def get_v1_dialing_permissions_countries_iso_code(
    iso_code: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve voice dialing country permissions identified by the given ISO country
    code.

    Args:
        iso_code:
            Iso code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}?](
    https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}"  # noqa
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
async def get_v1_dialing_permissions_countries_iso_code_high_risk_special_prefixes(  # noqa
    iso_code: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Fetch the high-risk special services prefixes from the country resource
    corresponding to the [ISO country
    code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

    Args:
        iso_code:
            Iso code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}/HighRiskSpecialPrefixes?&page_size=%s](
    https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}/HighRiskSpecialPrefixes?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}/HighRiskSpecialPrefixes"  # noqa
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
async def get_v1_ip_records(
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
    [https://voice.twilio.com/v1/IpRecords?&page_size=%s](
    https://voice.twilio.com/v1/IpRecords?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://voice.twilio.com/v1/IpRecords"  # noqa

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
async def post_v1_ip_records(
    twilio_credentials: "TwilioCredentials",
    cidr_prefix_length: int = None,
    friendly_name: str = None,
    ip_address: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        cidr_prefix_length:
            An integer representing the length of the
            [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use
            with this IP address. By default the entire IP address is
            used, which for IPv4 is value 32.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        ip_address:
            An IP address in dotted decimal notation, IPv4 only.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/IpRecords?](
    https://voice.twilio.com/v1/IpRecords?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://voice.twilio.com/v1/IpRecords"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "cidr_prefix_length": cidr_prefix_length,
        "friendly_name": friendly_name,
        "ip_address": ip_address,
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
async def delete_v1_ip_records_sid(
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
    [https://voice.twilio.com/v1/IpRecords/{sid}?](
    https://voice.twilio.com/v1/IpRecords/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/IpRecords/{sid}"  # noqa
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
async def get_v1_ip_records_sid(
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
    [https://voice.twilio.com/v1/IpRecords/{sid}?](
    https://voice.twilio.com/v1/IpRecords/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/IpRecords/{sid}"  # noqa
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
async def post_v1_ip_records_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/IpRecords/{sid}?](
    https://voice.twilio.com/v1/IpRecords/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/IpRecords/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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


@task
async def get_v1_source_ip_mappings(
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
    [https://voice.twilio.com/v1/SourceIpMappings?&page_size=%s](
    https://voice.twilio.com/v1/SourceIpMappings?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://voice.twilio.com/v1/SourceIpMappings"  # noqa

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
async def post_v1_source_ip_mappings(
    twilio_credentials: "TwilioCredentials",
    ip_record_sid: str = None,
    sip_domain_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ip_record_sid:
            The Twilio-provided string that uniquely identifies the IP Record
            resource to map from.
        sip_domain_sid:
            The SID of the SIP Domain that the IP Record should be mapped to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/SourceIpMappings?](
    https://voice.twilio.com/v1/SourceIpMappings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://voice.twilio.com/v1/SourceIpMappings"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "ip_record_sid": ip_record_sid,
        "sip_domain_sid": sip_domain_sid,
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
async def delete_v1_source_ip_mappings_sid(
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
    [https://voice.twilio.com/v1/SourceIpMappings/{sid}?](
    https://voice.twilio.com/v1/SourceIpMappings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/SourceIpMappings/{sid}"  # noqa
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
async def get_v1_source_ip_mappings_sid(
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
    [https://voice.twilio.com/v1/SourceIpMappings/{sid}?](
    https://voice.twilio.com/v1/SourceIpMappings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/SourceIpMappings/{sid}"  # noqa
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
async def post_v1_source_ip_mappings_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    sip_domain_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        sip_domain_sid:
            The SID of the SIP Domain that the IP Record should be mapped to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/SourceIpMappings/{sid}?](
    https://voice.twilio.com/v1/SourceIpMappings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/SourceIpMappings/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "sip_domain_sid": sip_domain_sid,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
