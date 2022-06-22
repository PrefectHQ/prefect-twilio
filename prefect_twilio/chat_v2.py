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
    [https://chat.twilio.com/v2/Credentials?&page_size=%s](
    https://chat.twilio.com/v2/Credentials?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://chat.twilio.com/v2/Credentials"  # noqa

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
            [GCM only] The API key for the project that was obtained from the Google
            Developer console for your GCM Service application
            credential.
        certificate:
            [APN only] The URL encoded representation of the certificate. For
            example,  `-----BEGIN CERTIFICATE-----
            MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A==
            -----END CERTIFICATE-----`.
        friendly_name:
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        private_key:
            [APN only] The URL encoded representation of the private key. For
            example, `-----BEGIN RSA PRIVATE KEY-----
            MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE
            KEY-----`.
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
    [https://chat.twilio.com/v2/Credentials?](
    https://chat.twilio.com/v2/Credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://chat.twilio.com/v2/Credentials"  # noqa

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
    [https://chat.twilio.com/v2/Credentials/{sid}?](
    https://chat.twilio.com/v2/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Credentials/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Credentials/{sid}?](
    https://chat.twilio.com/v2/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Credentials/{sid}"  # noqa
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
            [GCM only] The API key for the project that was obtained from the Google
            Developer console for your GCM Service application
            credential.
        certificate:
            [APN only] The URL encoded representation of the certificate. For
            example,  `-----BEGIN CERTIFICATE-----
            MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A==
            -----END CERTIFICATE-----`.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        private_key:
            [APN only] The URL encoded representation of the private key. For
            example, `-----BEGIN RSA PRIVATE KEY-----
            MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE
            KEY-----`.
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
    [https://chat.twilio.com/v2/Credentials/{sid}?](
    https://chat.twilio.com/v2/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Credentials/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services?&page_size=%s](
    https://chat.twilio.com/v2/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://chat.twilio.com/v2/Services"  # noqa

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
            A descriptive string that you create to describe the new resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services?](
    https://chat.twilio.com/v2/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://chat.twilio.com/v2/Services"  # noqa

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
            The push technology used by the Binding resources to read.  Can be:
            `apn`, `gcm`, or `fcm`.  See [push notification
            configuration](https://www.twilio.com/docs/chat/push-
            notification-configuration) for more info.
        identity:
            The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s
            `identity` value of the resources to read. See [access
            tokens](https://www.twilio.com/docs/chat/create-tokens) for
            more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Bindings"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}"  # noqa
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
            The visibility of the Channels to read. Can be: `public` or `private`
            and defaults to `public`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels?&type=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels?&type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels"  # noqa
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
            A valid JSON string that contains application-specific data.
        created_by:
            The `identity` of the User that created the channel. Default is:
            `system`.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            Note that this should only be used in cases where a Channel
            is being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated. The
            default value is `null`. Note that this parameter should
            only be used in cases where a Channel is being recreated
            from a backup/separate source  and where a Message was
            previously updated.
        friendly_name:
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        type:
            The visibility of the channel. Can be: `public` or `private` and
            defaults to `public`.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the Channel
            resource's `sid` in the URL. This value must be 64
            characters or less in length and be unique within the
            Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels"  # noqa
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
            The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s
            `identity` value of the resources to read. See [access
            tokens](https://www.twilio.com/docs/chat/create-tokens) for
            more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
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
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource). See [access
            tokens](https://www.twilio.com/docs/chat/create-tokens) for
            more info.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) assigned to the new member.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
            The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s
            `identity` value of the Member resources to read. See
            [access tokens](https://www.twilio.com/docs/chat/create-
            tokens) for more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
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
            A valid JSON string that contains application-specific data.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            Note that this parameter should only be used when a Member
            is being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated. The
            default value is `null`. Note that this parameter should
            only be used when a Member is being recreated from a
            backup/separate source and where a Member was previously
            updated.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource). See [access
            tokens](https://www.twilio.com/docs/chat/create-tokens) for
            more info.
        last_consumed_message_index:
            The index of the last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) in the
            [Channel](https://www.twilio.com/docs/chat/channels) that
            the Member has read. This parameter should only be used when
            recreating a Member from a backup/separate source.
        last_consumption_timestamp:
            The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the
            last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) read event for the Member within the
            [Channel](https://www.twilio.com/docs/chat/channels).
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) to assign to the member. The default roles are
            those specified on the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
            A valid JSON string that contains application-specific data.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            Note that this parameter should only be used when a Member
            is being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated.
        last_consumed_message_index:
            The index of the last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) that the Member has read within the
            [Channel](https://www.twilio.com/docs/chat/channels).
        last_consumption_timestamp:
            The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the
            last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) read event for the Member within the
            [Channel](https://www.twilio.com/docs/chat/channels).
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) to assign to the member. The default roles are
            those specified on the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
            The sort order of the returned messages. Can be: `asc` (ascending) or
            `desc` (descending) with `asc` as the default.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
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
            A valid JSON string that contains application-specific data.
        body:
            The message to send to the channel. Can be an empty string or `null`,
            which sets the value as an empty string. You can send
            structured data in the body by serializing it as a string.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            This parameter should only be used when a Chat's history is
            being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated.
        from_:
            The [Identity](https://www.twilio.com/docs/chat/identity) of the new
            message's author. The default value is `system`.
        last_updated_by:
            The [Identity](https://www.twilio.com/docs/chat/identity) of the User
            who last updated the Message, if applicable.
        media_sid:
            The SID of the [Media](https://www.twilio.com/docs/chat/rest/media) to
            attach to the new Message.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
            A valid JSON string that contains application-specific data.
        body:
            The message to send to the channel. Can be an empty string or `null`,
            which sets the value as an empty string. You can send
            structured data in the body by serializing it as a string.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            This parameter should only be used when a Chat's history is
            being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated.
        from_:
            The [Identity](https://www.twilio.com/docs/chat/identity) of the
            message's author.
        last_updated_by:
            The [Identity](https://www.twilio.com/docs/chat/identity) of the User
            who last updated the Message, if applicable.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks"  # noqa
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
            The events that cause us to call the Channel Webhook. Used when `type`
            is `webhook`. This parameter takes only one event. To
            specify more than one event, repeat this parameter for each
            event. For the list of possible events, see [Webhook Event
            Triggers](https://www.twilio.com/docs/chat/webhook-events
            webhook-event-trigger).
        configuration_flow_sid:
            The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-
            api/flow) to call when an event in `configuration.filters`
            occurs. Used only when `type` is `studio`.
        configuration_method:
            The HTTP method used to call `configuration.url`. Can be: `GET` or
            `POST` and the default is `POST`.
        configuration_retry_count:
            The number of times to retry the webhook if the first attempt fails. Can
            be an integer between 0 and 3, inclusive, and the default is
            0.
        configuration_triggers:
            A string that will cause us to call the webhook when it is present in a
            message body. This parameter takes only one trigger string.
            To specify more than one, repeat this parameter for each
            trigger string up to a total of 5 trigger strings. Used only
            when `type` = `trigger`.
        configuration_url:
            The URL of the webhook to call using the `configuration.method`.
        type:
            The type of webhook. Can be: `webhook`, `studio`, or `trigger`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
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
            The events that cause us to call the Channel Webhook. Used when `type`
            is `webhook`. This parameter takes only one event. To
            specify more than one event, repeat this parameter for each
            event. For the list of possible events, see [Webhook Event
            Triggers](https://www.twilio.com/docs/chat/webhook-events
            webhook-event-trigger).
        configuration_flow_sid:
            The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-
            api/flow) to call when an event in `configuration.filters`
            occurs. Used only when `type` = `studio`.
        configuration_method:
            The HTTP method used to call `configuration.url`. Can be: `GET` or
            `POST` and the default is `POST`.
        configuration_retry_count:
            The number of times to retry the webhook if the first attempt fails. Can
            be an integer between 0 and 3, inclusive, and the default is
            0.
        configuration_triggers:
            A string that will cause us to call the webhook when it is present in a
            message body. This parameter takes only one trigger string.
            To specify more than one, repeat this parameter for each
            trigger string up to a total of 5 trigger strings. Used only
            when `type` = `trigger`.
        configuration_url:
            The URL of the webhook to call using the `configuration.method`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
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
            A valid JSON string that contains application-specific data.
        created_by:
            The `identity` of the User that created the channel. Default is:
            `system`.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            Note that this should only be used in cases where a Channel
            is being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 256 characters long.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL. This value must be 256
            characters or less in length and unique within the Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles?&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles"  # noqa
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
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        permission:
            A permission that you grant to the new role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. The values
            for this parameter depend on the role's `type`.
        type:
            The type of role. Can be: `channel` for
            [Channel](https://www.twilio.com/docs/chat/channels) roles
            or `deployment` for
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource) roles.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles?](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
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
            A permission that you grant to the role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. Note that
            the update action replaces all previously assigned
            permissions with those defined in the update action. To
            remove a permission, do not include it in the subsequent
            update action. The values for this parameter depend on the
            role's `type`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users?&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users"  # noqa
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
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the new resource. This
            value is often used for display purposes.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource). This value is often a username or email address.
            See the Identity documentation for more info.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) to assign to the new User.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
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
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the resource. It is
            often used for display purposes.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) to assign to the User.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
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
            The push technology used by the User Binding resources to read. Can be:
            `apn`, `gcm`, or `fcm`.  See [push notification
            configuration](https://www.twilio.com/docs/chat/push-
            notification-configuration) for more info.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings?&binding_type=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings?&binding_type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels"  # noqa
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
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Removes User from selected Channel.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
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
            The index of the last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) in the
            [Channel](https://www.twilio.com/docs/chat/channels) that
            the Member has read.
        last_consumption_timestamp:
            The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the
            last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) read event for the Member within the
            [Channel](https://www.twilio.com/docs/chat/channels).
        notification_level:
            The push notification level to assign to the User Channel. Can be:
            `default` or `muted`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{sid}?](
    https://chat.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{sid}"  # noqa
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
    [https://chat.twilio.com/v2/Services/{sid}?](
    https://chat.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{sid}"  # noqa
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
            DEPRECATED. The interval in seconds between consumption reports
            submission batches from client endpoints.
        default_channel_creator_role_sid:
            The channel role assigned to a channel creator when they join a new
            channel. See the [Role
            resource](https://www.twilio.com/docs/chat/rest/role-
            resource) for more info about roles.
        default_channel_role_sid:
            The channel role assigned to users when they are added to a channel. See
            the [Role
            resource](https://www.twilio.com/docs/chat/rest/role-
            resource) for more info about roles.
        default_service_role_sid:
            The service role assigned to users when they are added to the service.
            See the [Role
            resource](https://www.twilio.com/docs/chat/rest/role-
            resource) for more info about roles.
        friendly_name:
            A descriptive string that you create to describe the resource.
        limits_channel_members:
            The maximum number of Members that can be added to Channels within this
            Service. Can be up to 1,000.
        limits_user_channels:
            The maximum number of Channels Users can be a Member of within this
            Service. Can be up to 1,000.
        media_compatibility_message:
            The message to send when a media message has no text. Can be used as
            placeholder message.
        notifications_added_to_channel_enabled:
            Whether to send a notification when a member is added to a channel. The
            default is `false`.
        notifications_added_to_channel_sound:
            The name of the sound to play when a member is added to a channel and
            `notifications.added_to_channel.enabled` is `true`.
        notifications_added_to_channel_template:
            The template to use to create the notification text displayed when a
            member is added to a channel and
            `notifications.added_to_channel.enabled` is `true`.
        notifications_invited_to_channel_enabled:
            Whether to send a notification when a user is invited to a channel. The
            default is `false`.
        notifications_invited_to_channel_sound:
            The name of the sound to play when a user is invited to a channel and
            `notifications.invited_to_channel.enabled` is `true`.
        notifications_invited_to_channel_template:
            The template to use to create the notification text displayed when a
            user is invited to a channel and
            `notifications.invited_to_channel.enabled` is `true`.
        notifications_log_enabled:
            Whether to log notifications. The default is `false`.
        notifications_new_message_badge_count_enabled:
            Whether the new message badge is enabled. The default is `false`.
        notifications_new_message_enabled:
            Whether to send a notification when a new message is added to a channel.
            The default is `false`.
        notifications_new_message_sound:
            The name of the sound to play when a new message is added to a channel
            and `notifications.new_message.enabled` is `true`.
        notifications_new_message_template:
            The template to use to create the notification text displayed when a new
            message is added to a channel and
            `notifications.new_message.enabled` is `true`.
        notifications_removed_from_channel_enabled:
            Whether to send a notification to a user when they are removed from a
            channel. The default is `false`.
        notifications_removed_from_channel_sound:
            The name of the sound to play to a user when they are removed from a
            channel and `notifications.removed_from_channel.enabled` is
            `true`.
        notifications_removed_from_channel_template:
            The template to use to create the notification text displayed to a user
            when they are removed from a channel and
            `notifications.removed_from_channel.enabled` is `true`.
        post_webhook_retry_count:
            The number of times to retry a call to the `post_webhook_url` if the
            request times out (after 5 seconds) or it receives a 429,
            503, or 504 HTTP response. The default is 0, which means the
            call won't be retried.
        post_webhook_url:
            The URL for post-event webhooks, which are called by using the
            `webhook_method`. See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.
        pre_webhook_retry_count:
            The number of times to retry a call to the `pre_webhook_url` if the
            request times out (after 5 seconds) or it receives a 429,
            503, or 504 HTTP response. Default retry count is 0 times,
            which means the call won't be retried.
        pre_webhook_url:
            The URL for pre-event webhooks, which are called by using the
            `webhook_method`. See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
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
            The list of webhook events that are enabled for this Service instance.
            See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.
        webhook_method:
            The HTTP method to use for calls to the `pre_webhook_url` and
            `post_webhook_url` webhooks.  Can be: `POST` or `GET` and
            the default is `POST`. See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{sid}?](
    https://chat.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{sid}"  # noqa
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
