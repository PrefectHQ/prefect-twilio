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
    [https://chat.twilio.com/v1/Credentials?&page_size=%s](
    https://chat.twilio.com/v1/Credentials?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://chat.twilio.com/v1/Credentials"  # noqa

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
            [GCM only] The API key for the project that was obtained from the Google
            Developer console for your GCM Service application
            credential.
        certificate:
            [APN only] The URL encoded representation of the certificate. For
            example,  `-----BEGIN CERTIFICATE-----
            MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==
            -----END CERTIFICATE-----`.
        friendly_name:
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        private_key:
            [APN only] The URL encoded representation of the private key. For
            example, `-----BEGIN RSA PRIVATE KEY-----
            MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR.
            -----END RSA PRIVATE KEY-----`.
        sandbox:
            [APN only] Whether to send the credential to sandbox APNs. Can be `true`
            to send to sandbox APNs or `false` to send to production.
        secret:
            [FCM only] The **Server key** of your project from the Firebase console,
            found under Settings / Cloud messaging.
        type:
            The type of push-notification service the credential is for. Can be:
            `gcm`, `fcm`, or `apn`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Credentials?](
    https://chat.twilio.com/v1/Credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://chat.twilio.com/v1/Credentials"  # noqa

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
    [https://chat.twilio.com/v1/Credentials/{sid}?](
    https://chat.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Credentials/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Credentials/{sid}?](
    https://chat.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Credentials/{sid}"  # noqa
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
            [GCM only] The API key for the project that was obtained from the Google
            Developer console for your GCM Service application
            credential.
        certificate:
            [APN only] The URL encoded representation of the certificate. For
            example,  `-----BEGIN CERTIFICATE-----
            MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==
            -----END CERTIFICATE-----`.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        private_key:
            [APN only] The URL encoded representation of the private key. For
            example, `-----BEGIN RSA PRIVATE KEY-----
            MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR.
            -----END RSA PRIVATE KEY-----`.
        sandbox:
            [APN only] Whether to send the credential to sandbox APNs. Can be `true`
            to send to sandbox APNs or `false` to send to production.
        secret:
            [FCM only] The **Server key** of your project from the Firebase console,
            found under Settings / Cloud messaging.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Credentials/{sid}?](
    https://chat.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Credentials/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services?&page_size=%s](
    https://chat.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://chat.twilio.com/v1/Services"  # noqa

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
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services?](
    https://chat.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://chat.twilio.com/v1/Services"  # noqa

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
            The visibility of the Channels to read. Can be: `public` or `private`
            and defaults to `public`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels?&type=%s&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels?&type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels"  # noqa
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
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        type:
            The visibility of the channel. Can be: `public` or `private` and
            defaults to `public`.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL. This value must be 64
            characters or less in length and be unique within the
            Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels"  # noqa
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
            The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)'s
            `identity` value of the resources to read. See [access
            tokens](https://www.twilio.com/docs/api/chat/guides/create-
            tokens) for more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
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
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/api/chat/rest/v1/user)
            within the
            [Service](https://www.twilio.com/docs/api/chat/rest/v1/service).
            See [access
            tokens](https://www.twilio.com/docs/api/chat/guides/create-
            tokens) for more info.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            assigned to the new member.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
            The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)'s
            `identity` value of the resources to read. See [access
            tokens](https://www.twilio.com/docs/api/chat/guides/create-
            tokens) for more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
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
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/api/chat/rest/v1/user)
            within the
            [Service](https://www.twilio.com/docs/api/chat/rest/services).
            See [access
            tokens](https://www.twilio.com/docs/api/chat/guides/create-
            tokens) for more details.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            to assign to the member. The default roles are those
            specified on the
            [Service](https://www.twilio.com/docs/chat/api/services).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
            The index of the last
            [Message](https://www.twilio.com/docs/api/chat/rest/messages)
            that the Member has read within the
            [Channel](https://www.twilio.com/docs/api/chat/rest/channels).
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            to assign to the member. The default roles are those
            specified on the
            [Service](https://www.twilio.com/docs/chat/api/services).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
            The sort order of the returned messages. Can be: `asc` (ascending) or
            `desc` (descending) with `asc` as the default.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
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
            A valid JSON string that contains application-specific data.
        body:
            The message to send to the channel. Can also be an empty string or
            `null`, which sets the value as an empty string. You can
            send structured data in the body by serializing it as a
            string.
        from_:
            The [identity](https://www.twilio.com/docs/api/chat/guides/identity) of
            the new message's author. The default value is `system`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
            A valid JSON string that contains application-specific data.
        body:
            The message to send to the channel. Can also be an empty string or
            `null`, which sets the value as an empty string. You can
            send structured data in the body by serializing it as a
            string.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
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
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL. This value must be 64
            characters or less in length and be unique within the
            Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles?&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles"  # noqa
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
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        permission:
            A permission that you grant to the new role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. The values
            for this parameter depend on the role's `type` and are
            described in the documentation.
        type:
            The type of role. Can be: `channel` for
            [Channel](https://www.twilio.com/docs/chat/api/channels)
            roles or `deployment` for
            [Service](https://www.twilio.com/docs/chat/api/services)
            roles.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles?](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
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
            A permission that you grant to the role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. The values
            for this parameter depend on the role's `type` and are
            described in the documentation.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Users?&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users"  # noqa
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
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the new resource. This
            value is often used for display purposes.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/api/chat/rest/v1/user)
            within the
            [Service](https://www.twilio.com/docs/api/chat/rest/v1/service).
            This value is often a username or email address. See the
            Identity documentation for more details.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            assigned to the new User.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Users?](
    https://chat.twilio.com/v1/Services/{service_sid}/Users?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
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
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the resource. It is
            often used for display purposes.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            assigned to this user.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
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
    List all Channels for a given User.

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
    [https://chat.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels"  # noqa
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
    [https://chat.twilio.com/v1/Services/{sid}?](
    https://chat.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{sid}?](
    https://chat.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{sid}"  # noqa
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
            DEPRECATED. The interval in seconds between consumption reports
            submission batches from client endpoints.
        default_channel_creator_role_sid:
            The channel role assigned to a channel creator when they join a new
            channel. See the [Roles
            endpoint](https://www.twilio.com/docs/chat/api/roles) for
            more details.
        default_channel_role_sid:
            The channel role assigned to users when they are added to a channel. See
            the [Roles
            endpoint](https://www.twilio.com/docs/chat/api/roles) for
            more details.
        default_service_role_sid:
            The service role assigned to users when they are added to the service.
            See the [Roles
            endpoint](https://www.twilio.com/docs/chat/api/roles) for
            more details.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        limits_channel_members:
            The maximum number of Members that can be added to Channels within this
            Service. Can be up to 1,000.
        limits_user_channels:
            The maximum number of Channels Users can be a Member of within this
            Service. Can be up to 1,000.
        notifications_added_to_channel_enabled:
            Whether to send a notification when a member is added to a channel. Can
            be: `true` or `false` and the default is `false`.
        notifications_added_to_channel_template:
            The template to use to create the notification text displayed when a
            member is added to a channel and
            `notifications.added_to_channel.enabled` is `true`.
        notifications_invited_to_channel_enabled:
            Whether to send a notification when a user is invited to a channel. Can
            be: `true` or `false` and the default is `false`.
        notifications_invited_to_channel_template:
            The template to use to create the notification text displayed when a
            user is invited to a channel and
            `notifications.invited_to_channel.enabled` is `true`.
        notifications_new_message_enabled:
            Whether to send a notification when a new message is added to a channel.
            Can be: `true` or `false` and the default is `false`.
        notifications_new_message_template:
            The template to use to create the notification text displayed when a new
            message is added to a channel and
            `notifications.new_message.enabled` is `true`.
        notifications_removed_from_channel_enabled:
            Whether to send a notification to a user when they are removed from a
            channel. Can be: `true` or `false` and the default is
            `false`.
        notifications_removed_from_channel_template:
            The template to use to create the notification text displayed to a user
            when they are removed from a channel and
            `notifications.removed_from_channel.enabled` is `true`.
        post_webhook_url:
            The URL for post-event webhooks, which are called by using the
            `webhook_method`. See [Webhook
            Events](https://www.twilio.com/docs/api/chat/webhooks) for
            more details.
        pre_webhook_url:
            The URL for pre-event webhooks, which are called by using the
            `webhook_method`. See [Webhook
            Events](https://www.twilio.com/docs/api/chat/webhooks) for
            more details.
        reachability_enabled:
            Whether to enable the [Reachability
            Indicator](https://www.twilio.com/docs/chat/reachability-
            indicator) for this Service instance. The default is
            `false`.
        read_status_enabled:
            Whether to enable the [Message Consumption
            Horizon](https://www.twilio.com/docs/chat/consumption-
            horizon) feature. The default is `true`.
        typing_indicator_timeout:
            How long in seconds after a `started typing` event until clients should
            assume that user is no longer typing, even if no `ended
            typing` message was received.  The default is 5 seconds.
        webhook_filters:
            The list of WebHook events that are enabled for this Service instance.
            See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.
        webhook_method:
            The HTTP method to use for calls to the `pre_webhook_url` and
            `post_webhook_url` webhooks.  Can be: `POST` or `GET` and
            the default is `POST`. See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.
        webhooks_on_channel_add_method:
            The HTTP method to use when calling the `webhooks.on_channel_add.url`.
        webhooks_on_channel_add_url:
            The URL of the webhook to call in response to the `on_channel_add` event
            using the `webhooks.on_channel_add.method` HTTP method.
        webhooks_on_channel_added_method:
            The URL of the webhook to call in response to the `on_channel_added`
            event`.
        webhooks_on_channel_added_url:
            The URL of the webhook to call in response to the `on_channel_added`
            event using the `webhooks.on_channel_added.method` HTTP
            method.
        webhooks_on_channel_destroy_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_destroy.url`.
        webhooks_on_channel_destroy_url:
            The URL of the webhook to call in response to the `on_channel_destroy`
            event using the `webhooks.on_channel_destroy.method` HTTP
            method.
        webhooks_on_channel_destroyed_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_destroyed.url`.
        webhooks_on_channel_destroyed_url:
            The URL of the webhook to call in response to the `on_channel_added`
            event using the `webhooks.on_channel_destroyed.method` HTTP
            method.
        webhooks_on_channel_update_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_update.url`.
        webhooks_on_channel_update_url:
            The URL of the webhook to call in response to the `on_channel_update`
            event using the `webhooks.on_channel_update.method` HTTP
            method.
        webhooks_on_channel_updated_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_updated.url`.
        webhooks_on_channel_updated_url:
            The URL of the webhook to call in response to the `on_channel_updated`
            event using the `webhooks.on_channel_updated.method` HTTP
            method.
        webhooks_on_member_add_method:
            The HTTP method to use when calling the `webhooks.on_member_add.url`.
        webhooks_on_member_add_url:
            The URL of the webhook to call in response to the `on_member_add` event
            using the `webhooks.on_member_add.method` HTTP method.
        webhooks_on_member_added_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_updated.url`.
        webhooks_on_member_added_url:
            The URL of the webhook to call in response to the `on_channel_updated`
            event using the `webhooks.on_channel_updated.method` HTTP
            method.
        webhooks_on_member_remove_method:
            The HTTP method to use when calling the `webhooks.on_member_remove.url`.
        webhooks_on_member_remove_url:
            The URL of the webhook to call in response to the `on_member_remove`
            event using the `webhooks.on_member_remove.method` HTTP
            method.
        webhooks_on_member_removed_method:
            The HTTP method to use when calling the
            `webhooks.on_member_removed.url`.
        webhooks_on_member_removed_url:
            The URL of the webhook to call in response to the `on_member_removed`
            event using the `webhooks.on_member_removed.method` HTTP
            method.
        webhooks_on_message_remove_method:
            The HTTP method to use when calling the
            `webhooks.on_message_remove.url`.
        webhooks_on_message_remove_url:
            The URL of the webhook to call in response to the `on_message_remove`
            event using the `webhooks.on_message_remove.method` HTTP
            method.
        webhooks_on_message_removed_method:
            The HTTP method to use when calling the
            `webhooks.on_message_removed.url`.
        webhooks_on_message_removed_url:
            The URL of the webhook to call in response to the `on_message_removed`
            event using the `webhooks.on_message_removed.method` HTTP
            method.
        webhooks_on_message_send_method:
            The HTTP method to use when calling the `webhooks.on_message_send.url`.
        webhooks_on_message_send_url:
            The URL of the webhook to call in response to the `on_message_send`
            event using the `webhooks.on_message_send.method` HTTP
            method.
        webhooks_on_message_sent_method:
            The URL of the webhook to call in response to the `on_message_sent`
            event`.
        webhooks_on_message_sent_url:
            The URL of the webhook to call in response to the `on_message_sent`
            event using the `webhooks.on_message_sent.method` HTTP
            method.
        webhooks_on_message_update_method:
            The HTTP method to use when calling the
            `webhooks.on_message_update.url`.
        webhooks_on_message_update_url:
            The URL of the webhook to call in response to the `on_message_update`
            event using the `webhooks.on_message_update.method` HTTP
            method.
        webhooks_on_message_updated_method:
            The HTTP method to use when calling the
            `webhooks.on_message_updated.url`.
        webhooks_on_message_updated_url:
            The URL of the webhook to call in response to the `on_message_updated`
            event using the `webhooks.on_message_updated.method` HTTP
            method.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{sid}?](
    https://chat.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{sid}"  # noqa
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
