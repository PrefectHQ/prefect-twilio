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
async def get_v2_credentials(
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
    [https://ip-messaging.twilio.com/v2/Credentials?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Credentials?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v2/Credentials"  # noqa

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
async def post_v2_credentials(
    twilio_credentials: "TwilioCredentials",
    api_key: str = None,
    certificate: str = None,
    friendly_name: str = None,
    private_key: str = None,
    sandbox: bool = None,
    secret: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        api_key:

        certificate:

        friendly_name:

        private_key:

        sandbox:

        secret:

        type:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Credentials?](
    https://ip-messaging.twilio.com/v2/Credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v2/Credentials"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "api_key": api_key,
        "certificate": certificate,
        "friendly_name": friendly_name,
        "private_key": private_key,
        "sandbox": sandbox,
        "secret": secret,
        "type": type,
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
async def delete_v2_credentials_sid(
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
    [https://ip-messaging.twilio.com/v2/Credentials/{sid}?](
    https://ip-messaging.twilio.com/v2/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Credentials/{sid}"  # noqa
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
async def get_v2_credentials_sid(
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
    [https://ip-messaging.twilio.com/v2/Credentials/{sid}?](
    https://ip-messaging.twilio.com/v2/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Credentials/{sid}"  # noqa
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
async def post_v2_credentials_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    api_key: str = None,
    certificate: str = None,
    friendly_name: str = None,
    private_key: str = None,
    sandbox: bool = None,
    secret: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        api_key:

        certificate:

        friendly_name:

        private_key:

        sandbox:

        secret:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Credentials/{sid}?](
    https://ip-messaging.twilio.com/v2/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Credentials/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "api_key": api_key,
        "certificate": certificate,
        "friendly_name": friendly_name,
        "private_key": private_key,
        "sandbox": sandbox,
        "secret": secret,
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
async def get_v2_services(
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
    [https://ip-messaging.twilio.com/v2/Services?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v2/Services"  # noqa

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
async def post_v2_services(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services?](
    https://ip-messaging.twilio.com/v2/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v2/Services"  # noqa

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
async def get_v2_services_service_sid_bindings(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    binding_type: list = None,
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_type:

        identity:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "binding_type": binding_type,
        "identity": identity,
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
async def delete_v2_services_service_sid_bindings_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_bindings_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    type: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        type:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels?&type=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels?&type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "type": type,
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
async def post_v2_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    created_by: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    type: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        created_by:

        date_created:

        date_updated:

        friendly_name:

        type:

        unique_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "created_by": created_by,
        "date_created": date_created,
        "date_updated": date_updated,
        "friendly_name": friendly_name,
        "type": type,
        "unique_name": unique_name,
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


@task
async def get_v2_services_service_sid_channels_channel_sid_invites(  # noqa
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v2_services_service_sid_channels_channel_sid_invites(  # noqa
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v2_services_service_sid_channels_channel_sid_invites_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels_channel_sid_invites_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels_channel_sid_members(  # noqa
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v2_services_service_sid_channels_channel_sid_members(  # noqa
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    identity: str = None,
    last_consumed_message_index: int = None,
    last_consumption_timestamp: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        date_created:

        date_updated:

        identity:

        last_consumed_message_index:

        last_consumption_timestamp:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "identity": identity,
        "last_consumed_message_index": last_consumed_message_index,
        "last_consumption_timestamp": last_consumption_timestamp,
        "role_sid": role_sid,
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


@task
async def delete_v2_services_service_sid_channels_channel_sid_members_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v2_services_service_sid_channels_channel_sid_members_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_members_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    last_consumed_message_index: int = None,
    last_consumption_timestamp: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        date_created:

        date_updated:

        last_consumed_message_index:

        last_consumption_timestamp:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "last_consumed_message_index": last_consumed_message_index,
        "last_consumption_timestamp": last_consumption_timestamp,
        "role_sid": role_sid,
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


@task
async def get_v2_services_service_sid_channels_channel_sid_messages(  # noqa
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
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
async def post_v2_services_service_sid_channels_channel_sid_messages(  # noqa
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
    from_: str = None,
    last_updated_by: str = None,
    media_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        body:

        date_created:

        date_updated:

        from_:

        last_updated_by:

        media_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
        "from_": from_,
        "last_updated_by": last_updated_by,
        "media_sid": media_sid,
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


@task
async def delete_v2_services_service_sid_channels_channel_sid_messages_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v2_services_service_sid_channels_channel_sid_messages_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_messages_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
    from_: str = None,
    last_updated_by: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        body:

        date_created:

        date_updated:

        from_:

        last_updated_by:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
        "from_": from_,
        "last_updated_by": last_updated_by,
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


@task
async def get_v2_services_service_sid_channels_channel_sid_webhooks(  # noqa
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks(  # noqa
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_retry_count: int = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:

        configuration_flow_sid:

        configuration_method:

        configuration_retry_count:

        configuration_triggers:

        configuration_url:

        type:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_retry_count": configuration_retry_count,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
        "type": type,
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
async def delete_v2_services_service_sid_channels_channel_sid_webhooks_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels_channel_sid_webhooks_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_retry_count: int = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:

        configuration_flow_sid:

        configuration_method:

        configuration_retry_count:

        configuration_triggers:

        configuration_url:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_retry_count": configuration_retry_count,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
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
async def delete_v2_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v2_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    created_by: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        created_by:

        date_created:

        date_updated:

        friendly_name:

        unique_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "created_by": created_by,
        "date_created": date_created,
        "date_updated": date_updated,
        "friendly_name": friendly_name,
        "unique_name": unique_name,
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


@task
async def get_v2_services_service_sid_roles(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles"  # noqa
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
async def post_v2_services_service_sid_roles(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    permission: list = None,
    type: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:

        permission:

        type:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "permission": permission,
        "type": type,
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
async def delete_v2_services_service_sid_roles_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
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
async def get_v2_services_service_sid_roles_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
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
async def post_v2_services_service_sid_roles_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    permission: list = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        permission:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "permission": permission,
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
async def get_v2_services_service_sid_users(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users"  # noqa
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
async def post_v2_services_service_sid_users(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        friendly_name:

        identity:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "identity": identity,
        "role_sid": role_sid,
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


@task
async def delete_v2_services_service_sid_users_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
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
async def get_v2_services_service_sid_users_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
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
async def post_v2_services_service_sid_users_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        friendly_name:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "role_sid": role_sid,
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


@task
async def get_v2_services_service_sid_users_user_sid_bindings(
    service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    binding_type: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_type:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings?&binding_type=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings?&binding_type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "binding_type": binding_type,
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
async def delete_v2_services_service_sid_users_user_sid_bindings_sid(  # noqa
    service_sid: str,
    user_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_users_user_sid_bindings_sid(  # noqa
    service_sid: str,
    user_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_users_user_sid_channels(
    service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels"  # noqa
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
async def delete_v2_services_service_sid_users_user_sid_channels_channel_sid(  # noqa
    service_sid: str,
    user_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
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
async def get_v2_services_service_sid_users_user_sid_channels_channel_sid(  # noqa
    service_sid: str,
    user_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
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
async def post_v2_services_service_sid_users_user_sid_channels_channel_sid(  # noqa
    service_sid: str,
    user_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    last_consumed_message_index: int = None,
    last_consumption_timestamp: str = None,
    notification_level: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        last_consumed_message_index:

        last_consumption_timestamp:

        notification_level:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "last_consumed_message_index": last_consumed_message_index,
        "last_consumption_timestamp": last_consumption_timestamp,
        "notification_level": notification_level,
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
async def delete_v2_services_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{sid}"  # noqa
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
async def get_v2_services_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{sid}"  # noqa
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
async def post_v2_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    consumption_report_interval: int = None,
    default_channel_creator_role_sid: str = None,
    default_channel_role_sid: str = None,
    default_service_role_sid: str = None,
    friendly_name: str = None,
    limits_channel_members: int = None,
    limits_user_channels: int = None,
    media_compatibility_message: str = None,
    notifications_added_to_channel_enabled: bool = None,
    notifications_added_to_channel_sound: str = None,
    notifications_added_to_channel_template: str = None,
    notifications_invited_to_channel_enabled: bool = None,
    notifications_invited_to_channel_sound: str = None,
    notifications_invited_to_channel_template: str = None,
    notifications_log_enabled: bool = None,
    notifications_new_message_badge_count_enabled: bool = None,
    notifications_new_message_enabled: bool = None,
    notifications_new_message_sound: str = None,
    notifications_new_message_template: str = None,
    notifications_removed_from_channel_enabled: bool = None,
    notifications_removed_from_channel_sound: str = None,
    notifications_removed_from_channel_template: str = None,
    post_webhook_retry_count: int = None,
    post_webhook_url: str = None,
    pre_webhook_retry_count: int = None,
    pre_webhook_url: str = None,
    reachability_enabled: bool = None,
    read_status_enabled: bool = None,
    typing_indicator_timeout: int = None,
    webhook_filters: list = None,
    webhook_method: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        consumption_report_interval:

        default_channel_creator_role_sid:

        default_channel_role_sid:

        default_service_role_sid:

        friendly_name:

        limits_channel_members:

        limits_user_channels:

        media_compatibility_message:

        notifications_added_to_channel_enabled:

        notifications_added_to_channel_sound:

        notifications_added_to_channel_template:

        notifications_invited_to_channel_enabled:

        notifications_invited_to_channel_sound:

        notifications_invited_to_channel_template:

        notifications_log_enabled:

        notifications_new_message_badge_count_enabled:

        notifications_new_message_enabled:

        notifications_new_message_sound:

        notifications_new_message_template:

        notifications_removed_from_channel_enabled:

        notifications_removed_from_channel_sound:

        notifications_removed_from_channel_template:

        post_webhook_retry_count:

        post_webhook_url:

        pre_webhook_retry_count:

        pre_webhook_url:

        reachability_enabled:

        read_status_enabled:

        typing_indicator_timeout:

        webhook_filters:

        webhook_method:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "consumption_report_interval": consumption_report_interval,
        "default_channel_creator_role_sid": default_channel_creator_role_sid,
        "default_channel_role_sid": default_channel_role_sid,
        "default_service_role_sid": default_service_role_sid,
        "friendly_name": friendly_name,
        "limits_channel_members": limits_channel_members,
        "limits_user_channels": limits_user_channels,
        "media_compatibility_message": media_compatibility_message,
        "notifications_added_to_channel_enabled": notifications_added_to_channel_enabled,  # noqa
        "notifications_added_to_channel_sound": notifications_added_to_channel_sound,  # noqa
        "notifications_added_to_channel_template": notifications_added_to_channel_template,  # noqa
        "notifications_invited_to_channel_enabled": notifications_invited_to_channel_enabled,  # noqa
        "notifications_invited_to_channel_sound": notifications_invited_to_channel_sound,  # noqa
        "notifications_invited_to_channel_template": notifications_invited_to_channel_template,  # noqa
        "notifications_log_enabled": notifications_log_enabled,
        "notifications_new_message_badge_count_enabled": notifications_new_message_badge_count_enabled,  # noqa
        "notifications_new_message_enabled": notifications_new_message_enabled,
        "notifications_new_message_sound": notifications_new_message_sound,
        "notifications_new_message_template": notifications_new_message_template,
        "notifications_removed_from_channel_enabled": notifications_removed_from_channel_enabled,  # noqa
        "notifications_removed_from_channel_sound": notifications_removed_from_channel_sound,  # noqa
        "notifications_removed_from_channel_template": notifications_removed_from_channel_template,  # noqa
        "post_webhook_retry_count": post_webhook_retry_count,
        "post_webhook_url": post_webhook_url,
        "pre_webhook_retry_count": pre_webhook_retry_count,
        "pre_webhook_url": pre_webhook_url,
        "reachability_enabled": reachability_enabled,
        "read_status_enabled": read_status_enabled,
        "typing_indicator_timeout": typing_indicator_timeout,
        "webhook_filters": webhook_filters,
        "webhook_method": webhook_method,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
