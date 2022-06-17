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
async def get_v1_credentials(
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
    [https://ip-messaging.twilio.com/v1/Credentials?&page_size=%s](
    https://ip-messaging.twilio.com/v1/Credentials?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v1/Credentials"  # noqa

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
async def post_v1_credentials(
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
    [https://ip-messaging.twilio.com/v1/Credentials?](
    https://ip-messaging.twilio.com/v1/Credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v1/Credentials"  # noqa

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
async def delete_v1_credentials_sid(
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
    [https://ip-messaging.twilio.com/v1/Credentials/{sid}?](
    https://ip-messaging.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Credentials/{sid}"  # noqa
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
async def get_v1_credentials_sid(
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
    [https://ip-messaging.twilio.com/v1/Credentials/{sid}?](
    https://ip-messaging.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Credentials/{sid}"  # noqa
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
async def post_v1_credentials_sid(
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
    [https://ip-messaging.twilio.com/v1/Credentials/{sid}?](
    https://ip-messaging.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Credentials/{sid}"  # noqa
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
async def get_v1_services(
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
    [https://ip-messaging.twilio.com/v1/Services?&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v1/Services"  # noqa

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
async def post_v1_services(
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
    [https://ip-messaging.twilio.com/v1/Services?](
    https://ip-messaging.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v1/Services"  # noqa

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
async def get_v1_services_service_sid_channels(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels?&type=%s&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels?&type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels"  # noqa
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
async def post_v1_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
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
        attributes:

        friendly_name:

        type:

        unique_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "type": type,
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
async def get_v1_services_service_sid_channels_channel_sid_invites(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
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
async def post_v1_services_service_sid_channels_channel_sid_invites(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
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
async def delete_v1_services_service_sid_channels_channel_sid_invites_sid(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_invites_sid(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_members(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
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
async def post_v1_services_service_sid_channels_channel_sid_members(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
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
async def delete_v1_services_service_sid_channels_channel_sid_members_sid(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_members_sid(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
async def post_v1_services_service_sid_channels_channel_sid_members_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    last_consumed_message_index: int = None,
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
        last_consumed_message_index:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "last_consumed_message_index": last_consumed_message_index,
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
async def get_v1_services_service_sid_channels_channel_sid_messages(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
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
async def post_v1_services_service_sid_channels_channel_sid_messages(  # noqa
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    body: str = None,
    from_: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:

        body:

        from_:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "body": body,
        "from_": from_,
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
async def delete_v1_services_service_sid_channels_channel_sid_messages_sid(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_messages_sid(  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
async def post_v1_services_service_sid_channels_channel_sid_messages_sid(  # noqa
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    body: str = None,
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
        attributes:

        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
        "body": body,
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
async def delete_v1_services_service_sid_channels_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
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
async def post_v1_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
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
        attributes:

        friendly_name:

        unique_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
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
async def get_v1_services_service_sid_roles(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles?&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles"  # noqa
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
async def post_v1_services_service_sid_roles(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles"  # noqa
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
async def delete_v1_services_service_sid_roles_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
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
async def get_v1_services_service_sid_roles_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
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
async def post_v1_services_service_sid_roles_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
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
async def get_v1_services_service_sid_users(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users?&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users"  # noqa
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
async def post_v1_services_service_sid_users(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
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
        attributes:

        friendly_name:

        identity:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users"  # noqa
    responses = {
        201: "Created.",  # noqa
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
        responses=responses,
        data=data,
    )
    return result


@task
async def delete_v1_services_service_sid_users_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
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
async def get_v1_services_service_sid_users_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
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
async def post_v1_services_service_sid_users_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
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
        attributes:

        friendly_name:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
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
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_services_service_sid_users_user_sid_channels(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels"  # noqa
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
async def delete_v1_services_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{sid}"  # noqa
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
async def get_v1_services_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{sid}"  # noqa
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
async def post_v1_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    consumption_report_interval: int = None,
    default_channel_creator_role_sid: str = None,
    default_channel_role_sid: str = None,
    default_service_role_sid: str = None,
    friendly_name: str = None,
    limits_channel_members: int = None,
    limits_user_channels: int = None,
    notifications_added_to_channel_enabled: bool = None,
    notifications_added_to_channel_template: str = None,
    notifications_invited_to_channel_enabled: bool = None,
    notifications_invited_to_channel_template: str = None,
    notifications_new_message_enabled: bool = None,
    notifications_new_message_template: str = None,
    notifications_removed_from_channel_enabled: bool = None,
    notifications_removed_from_channel_template: str = None,
    post_webhook_url: str = None,
    pre_webhook_url: str = None,
    reachability_enabled: bool = None,
    read_status_enabled: bool = None,
    typing_indicator_timeout: int = None,
    webhook_filters: list = None,
    webhook_method: str = None,
    webhooks_on_channel_add_method: str = None,
    webhooks_on_channel_add_url: str = None,
    webhooks_on_channel_added_method: str = None,
    webhooks_on_channel_added_url: str = None,
    webhooks_on_channel_destroy_method: str = None,
    webhooks_on_channel_destroy_url: str = None,
    webhooks_on_channel_destroyed_method: str = None,
    webhooks_on_channel_destroyed_url: str = None,
    webhooks_on_channel_update_method: str = None,
    webhooks_on_channel_update_url: str = None,
    webhooks_on_channel_updated_method: str = None,
    webhooks_on_channel_updated_url: str = None,
    webhooks_on_member_add_method: str = None,
    webhooks_on_member_add_url: str = None,
    webhooks_on_member_added_method: str = None,
    webhooks_on_member_added_url: str = None,
    webhooks_on_member_remove_method: str = None,
    webhooks_on_member_remove_url: str = None,
    webhooks_on_member_removed_method: str = None,
    webhooks_on_member_removed_url: str = None,
    webhooks_on_message_remove_method: str = None,
    webhooks_on_message_remove_url: str = None,
    webhooks_on_message_removed_method: str = None,
    webhooks_on_message_removed_url: str = None,
    webhooks_on_message_send_method: str = None,
    webhooks_on_message_send_url: str = None,
    webhooks_on_message_sent_method: str = None,
    webhooks_on_message_sent_url: str = None,
    webhooks_on_message_update_method: str = None,
    webhooks_on_message_update_url: str = None,
    webhooks_on_message_updated_method: str = None,
    webhooks_on_message_updated_url: str = None,
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

        notifications_added_to_channel_enabled:

        notifications_added_to_channel_template:

        notifications_invited_to_channel_enabled:

        notifications_invited_to_channel_template:

        notifications_new_message_enabled:

        notifications_new_message_template:

        notifications_removed_from_channel_enabled:

        notifications_removed_from_channel_template:

        post_webhook_url:

        pre_webhook_url:

        reachability_enabled:

        read_status_enabled:

        typing_indicator_timeout:

        webhook_filters:

        webhook_method:

        webhooks_on_channel_add_method:

        webhooks_on_channel_add_url:

        webhooks_on_channel_added_method:

        webhooks_on_channel_added_url:

        webhooks_on_channel_destroy_method:

        webhooks_on_channel_destroy_url:

        webhooks_on_channel_destroyed_method:

        webhooks_on_channel_destroyed_url:

        webhooks_on_channel_update_method:

        webhooks_on_channel_update_url:

        webhooks_on_channel_updated_method:

        webhooks_on_channel_updated_url:

        webhooks_on_member_add_method:

        webhooks_on_member_add_url:

        webhooks_on_member_added_method:

        webhooks_on_member_added_url:

        webhooks_on_member_remove_method:

        webhooks_on_member_remove_url:

        webhooks_on_member_removed_method:

        webhooks_on_member_removed_url:

        webhooks_on_message_remove_method:

        webhooks_on_message_remove_url:

        webhooks_on_message_removed_method:

        webhooks_on_message_removed_url:

        webhooks_on_message_send_method:

        webhooks_on_message_send_url:

        webhooks_on_message_sent_method:

        webhooks_on_message_sent_url:

        webhooks_on_message_update_method:

        webhooks_on_message_update_url:

        webhooks_on_message_updated_method:

        webhooks_on_message_updated_url:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{sid}"  # noqa
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
        "notifications_added_to_channel_enabled": notifications_added_to_channel_enabled,  # noqa
        "notifications_added_to_channel_template": notifications_added_to_channel_template,  # noqa
        "notifications_invited_to_channel_enabled": notifications_invited_to_channel_enabled,  # noqa
        "notifications_invited_to_channel_template": notifications_invited_to_channel_template,  # noqa
        "notifications_new_message_enabled": notifications_new_message_enabled,
        "notifications_new_message_template": notifications_new_message_template,
        "notifications_removed_from_channel_enabled": notifications_removed_from_channel_enabled,  # noqa
        "notifications_removed_from_channel_template": notifications_removed_from_channel_template,  # noqa
        "post_webhook_url": post_webhook_url,
        "pre_webhook_url": pre_webhook_url,
        "reachability_enabled": reachability_enabled,
        "read_status_enabled": read_status_enabled,
        "typing_indicator_timeout": typing_indicator_timeout,
        "webhook_filters": webhook_filters,
        "webhook_method": webhook_method,
        "webhooks_on_channel_add_method": webhooks_on_channel_add_method,
        "webhooks_on_channel_add_url": webhooks_on_channel_add_url,
        "webhooks_on_channel_added_method": webhooks_on_channel_added_method,
        "webhooks_on_channel_added_url": webhooks_on_channel_added_url,
        "webhooks_on_channel_destroy_method": webhooks_on_channel_destroy_method,
        "webhooks_on_channel_destroy_url": webhooks_on_channel_destroy_url,
        "webhooks_on_channel_destroyed_method": webhooks_on_channel_destroyed_method,  # noqa
        "webhooks_on_channel_destroyed_url": webhooks_on_channel_destroyed_url,
        "webhooks_on_channel_update_method": webhooks_on_channel_update_method,
        "webhooks_on_channel_update_url": webhooks_on_channel_update_url,
        "webhooks_on_channel_updated_method": webhooks_on_channel_updated_method,
        "webhooks_on_channel_updated_url": webhooks_on_channel_updated_url,
        "webhooks_on_member_add_method": webhooks_on_member_add_method,
        "webhooks_on_member_add_url": webhooks_on_member_add_url,
        "webhooks_on_member_added_method": webhooks_on_member_added_method,
        "webhooks_on_member_added_url": webhooks_on_member_added_url,
        "webhooks_on_member_remove_method": webhooks_on_member_remove_method,
        "webhooks_on_member_remove_url": webhooks_on_member_remove_url,
        "webhooks_on_member_removed_method": webhooks_on_member_removed_method,
        "webhooks_on_member_removed_url": webhooks_on_member_removed_url,
        "webhooks_on_message_remove_method": webhooks_on_message_remove_method,
        "webhooks_on_message_remove_url": webhooks_on_message_remove_url,
        "webhooks_on_message_removed_method": webhooks_on_message_removed_method,
        "webhooks_on_message_removed_url": webhooks_on_message_removed_url,
        "webhooks_on_message_send_method": webhooks_on_message_send_method,
        "webhooks_on_message_send_url": webhooks_on_message_send_url,
        "webhooks_on_message_sent_method": webhooks_on_message_sent_method,
        "webhooks_on_message_sent_url": webhooks_on_message_sent_url,
        "webhooks_on_message_update_method": webhooks_on_message_update_method,
        "webhooks_on_message_update_url": webhooks_on_message_update_url,
        "webhooks_on_message_updated_method": webhooks_on_message_updated_method,
        "webhooks_on_message_updated_url": webhooks_on_message_updated_url,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
