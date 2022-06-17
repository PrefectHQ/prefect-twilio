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
