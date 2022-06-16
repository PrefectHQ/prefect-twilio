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
async def get_v2_services_service_sid_channels_channel_sid_invites(
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
async def post_v2_services_service_sid_channels_channel_sid_invites(
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
async def delete_v2_services_service_sid_channels_channel_sid_invites_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_invites_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_members(
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
async def post_v2_services_service_sid_channels_channel_sid_members(
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
async def delete_v2_services_service_sid_channels_channel_sid_members_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_members_sid(
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
async def post_v2_services_service_sid_channels_channel_sid_members_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_messages(
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
async def post_v2_services_service_sid_channels_channel_sid_messages(
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
async def delete_v2_services_service_sid_channels_channel_sid_messages_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_messages_sid(
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
async def post_v2_services_service_sid_channels_channel_sid_messages_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_webhooks(
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks(
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
async def delete_v2_services_service_sid_channels_channel_sid_webhooks_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_webhooks_sid(
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks_sid(
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
async def delete_v2_services_service_sid_users_user_sid_bindings_sid(
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
async def get_v2_services_service_sid_users_user_sid_bindings_sid(
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
async def delete_v2_services_service_sid_users_user_sid_channels_channel_sid(
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
async def get_v2_services_service_sid_users_user_sid_channels_channel_sid(
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
async def post_v2_services_service_sid_users_user_sid_channels_channel_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_invites(
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
async def post_v2_services_service_sid_channels_channel_sid_invites(
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
async def delete_v2_services_service_sid_channels_channel_sid_invites_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_invites_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_members(
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
async def post_v2_services_service_sid_channels_channel_sid_members(
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
async def delete_v2_services_service_sid_channels_channel_sid_members_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_members_sid(
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
async def post_v2_services_service_sid_channels_channel_sid_members_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_messages(
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
async def post_v2_services_service_sid_channels_channel_sid_messages(
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
async def delete_v2_services_service_sid_channels_channel_sid_messages_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_messages_sid(
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
async def post_v2_services_service_sid_channels_channel_sid_messages_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_webhooks(
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks(
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
async def delete_v2_services_service_sid_channels_channel_sid_webhooks_sid(
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
async def get_v2_services_service_sid_channels_channel_sid_webhooks_sid(
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks_sid(
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
async def delete_v2_services_service_sid_users_user_sid_bindings_sid(
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
async def get_v2_services_service_sid_users_user_sid_bindings_sid(
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
async def delete_v2_services_service_sid_users_user_sid_channels_channel_sid(
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
async def get_v2_services_service_sid_users_user_sid_channels_channel_sid(
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
async def post_v2_services_service_sid_users_user_sid_channels_channel_sid(
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


@task
async def get_v2_phone_numbers_phone_number(
    phone_number: str,
    twilio_credentials: "TwilioCredentials",
    fields: str = None,
    country_code: str = None,
) -> Dict[str, Any]:
    """


    Args:
        phone_number:
            Phone number used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        fields:
            A comma-separated list of fields to return. Possible values are
            caller_name, sim_swap, call_forwarding, live_activity,
            enhanced_line_type or line_type_intelligence.
        country_code:
            The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            used if the phone number provided is in national format.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://lookups.twilio.com/v2/PhoneNumbers/{phone_number}?&fields=%s&country_code=%s](
    https://lookups.twilio.com/v2/PhoneNumbers/{phone_number}?&fields=%s&country_code=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://lookups.twilio.com/v2/PhoneNumbers/{phone_number}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "fields": fields,
        "country_code": country_code,
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
async def get_v2_regulatory_compliance_bundles(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    friendly_name: str = None,
    regulation_sid: str = None,
    iso_country: str = None,
    number_type: str = None,
    has_valid_until_date: bool = None,
    sort_by: str = None,
    sort_direction: str = None,
    valid_until_date: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Bundles for an account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The verification status of the Bundle resource. Please refer to [Bundle
            Statuses](https://www.twilio.com/docs/phone-
            numbers/regulatory/api/bundles
            bundle-statuses) for more details.
        friendly_name:
            The string that you assigned to describe the resource. The column can
            contain 255 variable characters.
        regulation_sid:
            The unique string of a [Regulation
            resource](https://www.twilio.com/docs/phone-
            numbers/regulatory/api/regulations) that is associated to
            the Bundle resource.
        iso_country:
            The 2-digit [ISO country
            code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of
            the Bundle's phone number country ownership request.
        number_type:
            The type of phone number of the Bundle's ownership request. Can be
            `local`, `mobile`, `national`, or `tollfree`.
        has_valid_until_date:
            Indicates that the Bundle is a valid Bundle until a specified expiration
            date.
        sort_by:
            Can be `valid-until` or `date-updated`. Defaults to `date-created`.
        sort_direction:
            Default is `DESC`. Can be `ASC` or `DESC`.
        valid_until_date:
            Date to filter Bundles having their `valid_until_date` before or after
            the specified date. Can be `ValidUntilDate>=` or
            `ValidUntilDate<=`. Both can be used in conjunction as well.
            [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the
            acceptable date format.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?&status=%s&friendly_name=%s&regulation_sid=%s&iso_country=%s&number_type=%s&has_valid_until_date=%s&sort_by=%s&sort_direction=%s&valid_until_date=%s&valid_until_date=%s&valid_until_date=%s&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?&status=%s&friendly_name=%s&regulation_sid=%s&iso_country=%s&number_type=%s&has_valid_until_date=%s&sort_by=%s&sort_direction=%s&valid_until_date=%s&valid_until_date=%s&valid_until_date=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "friendly_name": friendly_name,
        "regulation_sid": regulation_sid,
        "iso_country": iso_country,
        "number_type": number_type,
        "has_valid_until_date": has_valid_until_date,
        "sort_by": sort_by,
        "sort_direction": sort_direction,
        "valid_until_date": valid_until_date,
        "valid_until_date": valid_until_date,
        "valid_until_date": valid_until_date,
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
async def post_v2_regulatory_compliance_bundles(
    twilio_credentials: "TwilioCredentials",
    email: str = None,
    end_user_type: str = None,
    friendly_name: str = None,
    iso_country: str = None,
    number_type: str = None,
    regulation_sid: str = None,
    status_callback: str = None,
) -> Dict[str, Any]:
    """
    Create a new Bundle.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        email:
            The email address that will receive updates when the Bundle resource
            changes status.
        end_user_type:
            The [type of End User](https://www.twilio.com/docs/phone-
            numbers/regulatory/api/end-user-types) of the Bundle
            resource.
        friendly_name:
            The string that you assigned to describe the resource.
        iso_country:
            The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            of the Bundle's phone number country ownership request.
        number_type:
            The type of phone number of the Bundle's ownership request. Can be
            `local`, `mobile`, `national`, or `toll free`.
        regulation_sid:
            The unique string of a regulation that is associated to the Bundle
            resource.
        status_callback:
            The URL we call to inform your application of status changes.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "email": email,
        "end_user_type": end_user_type,
        "friendly_name": friendly_name,
        "iso_country": iso_country,
        "number_type": number_type,
        "regulation_sid": regulation_sid,
        "status_callback": status_callback,
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
async def get_v2_regulatory_compliance_bundles_bundle_sid_copies(
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Bundles Copies for a Bundle.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies"  # noqa
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
async def post_v2_regulatory_compliance_bundles_bundle_sid_copies(
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Creates a new copy of a Bundle. It will internally create copies of all the
    bundle items (identities and documents) of the original bundle.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The string that you assigned to describe the copied bundle.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies"  # noqa
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
async def get_v2_regulatory_compliance_bundles_bundle_sid_evaluations(
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Evaluations associated to the Bundle resource.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations"  # noqa
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
async def post_v2_regulatory_compliance_bundles_bundle_sid_evaluations(
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Creates an evaluation for a bundle.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_v2_regulatory_compliance_bundles_bundle_sid_evaluations_sid(
    bundle_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Evaluation Instance.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_bundles_bundle_sid_item_assignments(
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Assigned Items for an account.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments"  # noqa
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
async def post_v2_regulatory_compliance_bundles_bundle_sid_item_assignments(
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    object_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new Assigned Item.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        object_sid:
            The SID of an object bag that holds information of the different items.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "object_sid": object_sid,
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
async def delete_v2_regulatory_compliance_bundles_bundle_sid_item_assignments_sid(
    bundle_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an Assignment Item Instance.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_bundles_bundle_sid_item_assignments_sid(
    bundle_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Assigned Item Instance.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}"  # noqa
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
async def post_v2_regulatory_compliance_bundles_bundle_sid_replace_items(
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    from_bundle_sid: str = None,
) -> Dict[str, Any]:
    """
    Replaces all bundle items in the target bundle (specified in the path) with all
    the bundle items of the source bundle (specified by the from_bundle_sid body
    param).

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        from_bundle_sid:
            The source bundle sid to copy the item assignments from.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ReplaceItems?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ReplaceItems?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ReplaceItems"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "from_bundle_sid": from_bundle_sid,
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
async def delete_v2_regulatory_compliance_bundles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Bundle.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_bundles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Bundle instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}"  # noqa
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
async def post_v2_regulatory_compliance_bundles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    email: str = None,
    friendly_name: str = None,
    status: str = None,
    status_callback: str = None,
) -> Dict[str, Any]:
    """
    Updates a Bundle in an account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        email:
            The email address that will receive updates when the Bundle resource
            changes status.
        friendly_name:
            The string that you assigned to describe the resource.
        status:
            The verification status of the Bundle resource.
        status_callback:
            The URL we call to inform your application of status changes.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "email": email,
        "friendly_name": friendly_name,
        "status": status,
        "status_callback": status_callback,
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
async def get_v2_regulatory_compliance_end_user_types(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all End-User Types.

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
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes"  # noqa

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
async def get_v2_regulatory_compliance_end_user_types_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific End-User Type Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_end_users(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all End User for an account.

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
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers"  # noqa

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
async def post_v2_regulatory_compliance_end_users(
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Create a new End User.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            The set of parameters that are the attributes of the End User resource
            which are derived End User Types.
        friendly_name:
            The string that you assigned to describe the resource.
        type:
            The type of end user of the Bundle resource - can be `individual` or
            `business`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
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
async def delete_v2_regulatory_compliance_end_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific End User.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_end_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific End User Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}"  # noqa
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
async def post_v2_regulatory_compliance_end_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update an existing End User.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            The set of parameters that are the attributes of the End User resource
            which are derived End User Types.
        friendly_name:
            The string that you assigned to describe the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
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
async def get_v2_regulatory_compliance_regulations(
    twilio_credentials: "TwilioCredentials",
    end_user_type: str = None,
    iso_country: str = None,
    number_type: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Regulations.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_user_type:
            The type of End User the regulation requires - can be `individual` or
            `business`.
        iso_country:
            The ISO country code of the phone number's country.
        number_type:
            The type of phone number that the regulatory requiremnt is restricting.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations?&end_user_type=%s&iso_country=%s&number_type=%s&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations?&end_user_type=%s&iso_country=%s&number_type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end_user_type": end_user_type,
        "iso_country": iso_country,
        "number_type": number_type,
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
async def get_v2_regulatory_compliance_regulations_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Regulation Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_supporting_document_types(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Supporting Document Types.

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
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes"  # noqa

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
async def get_v2_regulatory_compliance_supporting_document_types_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Supporting Document Type Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_supporting_documents(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Supporting Document for an account.

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
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments"  # noqa
    )

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
async def post_v2_regulatory_compliance_supporting_documents(
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Create a new Supporting Document.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            The set of parameters that are the attributes of the Supporting
            Documents resource which are derived Supporting Document
            Types.
        friendly_name:
            The string that you assigned to describe the resource.
        type:
            The type of the Supporting Document.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments"  # noqa
    )

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
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
async def delete_v2_regulatory_compliance_supporting_documents_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Supporting Document.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_supporting_documents_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Supporting Document Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}"  # noqa
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
async def post_v2_regulatory_compliance_supporting_documents_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update an existing Supporting Document.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            The set of parameters that are the attributes of the Supporting Document
            resource which are derived Supporting Document Types.
        friendly_name:
            The string that you assigned to describe the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
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
async def get_v2_trunking_countries(
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
    [https://pricing.twilio.com/v2/Trunking/Countries?&page_size=%s](
    https://pricing.twilio.com/v2/Trunking/Countries?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://pricing.twilio.com/v2/Trunking/Countries"  # noqa

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
async def get_v2_trunking_countries_iso_country(
    iso_country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Country.

    Args:
        iso_country:
            Iso country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Trunking/Countries/{iso_country}?](
    https://pricing.twilio.com/v2/Trunking/Countries/{iso_country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Trunking/Countries/{iso_country}"  # noqa
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
async def get_v2_trunking_numbers_destination_number(
    destination_number: str,
    twilio_credentials: "TwilioCredentials",
    origination_number: str = None,
) -> Dict[str, Any]:
    """
    Fetch pricing information for a specific destination and, optionally,
    origination phone number.

    Args:
        destination_number:
            Destination number used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        origination_number:
            The origination phone number, in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format, for which to fetch the origin-based voice pricing
            information. E.164 format consists of a + followed by the
            country code and subscriber number.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Trunking/Numbers/{destination_number}?&origination_number=%s](
    https://pricing.twilio.com/v2/Trunking/Numbers/{destination_number}?&origination_number=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Trunking/Numbers/{destination_number}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "origination_number": origination_number,
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
async def get_v2_voice_countries(
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
    [https://pricing.twilio.com/v2/Voice/Countries?&page_size=%s](
    https://pricing.twilio.com/v2/Voice/Countries?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://pricing.twilio.com/v2/Voice/Countries"  # noqa

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
async def get_v2_voice_countries_iso_country(
    iso_country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Country.

    Args:
        iso_country:
            Iso country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Voice/Countries/{iso_country}?](
    https://pricing.twilio.com/v2/Voice/Countries/{iso_country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Voice/Countries/{iso_country}"  # noqa
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
async def get_v2_voice_numbers_destination_number(
    destination_number: str,
    twilio_credentials: "TwilioCredentials",
    origination_number: str = None,
) -> Dict[str, Any]:
    """
    Fetch pricing information for a specific destination and, optionally,
    origination phone number.

    Args:
        destination_number:
            Destination number used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        origination_number:
            The origination phone number, in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format, for which to fetch the origin-based voice pricing
            information. E.164 format consists of a + followed by the
            country code and subscriber number.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Voice/Numbers/{destination_number}?&origination_number=%s](
    https://pricing.twilio.com/v2/Voice/Numbers/{destination_number}?&origination_number=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Voice/Numbers/{destination_number}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "origination_number": origination_number,
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
async def get_v2_flows(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Flows.

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
    [https://studio.twilio.com/v2/Flows?&page_size=%s](
    https://studio.twilio.com/v2/Flows?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://studio.twilio.com/v2/Flows"  # noqa

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
async def post_v2_flows(
    twilio_credentials: "TwilioCredentials",
    commit_message: str = None,
    definition: str = None,
    friendly_name: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """
    Create a Flow.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        commit_message:
            Description of change made in the revision.
        definition:
            JSON representation of flow definition.
        friendly_name:
            The string that you assigned to describe the Flow.
        status:
            The status of the Flow. Can be: `draft` or `published`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows?](
    https://studio.twilio.com/v2/Flows?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://studio.twilio.com/v2/Flows"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "commit_message": commit_message,
        "definition": definition,
        "friendly_name": friendly_name,
        "status": status,
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
async def post_v2_flows_validate(
    twilio_credentials: "TwilioCredentials",
    commit_message: str = None,
    definition: str = None,
    friendly_name: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """
    Validate flow JSON definition.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        commit_message:
            Description of change made in the revision.
        definition:
            JSON representation of flow definition.
        friendly_name:
            The string that you assigned to describe the Flow.
        status:
            The status of the Flow. Can be: `draft` or `published`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/Validate?](
    https://studio.twilio.com/v2/Flows/Validate?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://studio.twilio.com/v2/Flows/Validate"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "commit_message": commit_message,
        "definition": definition,
        "friendly_name": friendly_name,
        "status": status,
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
async def get_v2_flows_flow_sid_executions(
    flow_sid: str,
    twilio_credentials: "TwilioCredentials",
    date_created_from: str = None,
    date_created_to: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Executions for the Flow.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created_from:
            Only show Execution resources starting on or after this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time,
            given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        date_created_to:
            Only show Execution resources starting before this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time,
            given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{flow_sid}/Executions?&date_created_from=%s&date_created_to=%s&page_size=%s](
    https://studio.twilio.com/v2/Flows/{flow_sid}/Executions?&date_created_from=%s&date_created_to=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{flow_sid}/Executions"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created_from": date_created_from,
        "date_created_to": date_created_to,
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
async def post_v2_flows_flow_sid_executions(
    flow_sid: str,
    twilio_credentials: "TwilioCredentials",
    from_: str = None,
    parameters: str = None,
    to: str = None,
) -> Dict[str, Any]:
    """
    Triggers a new Execution for the Flow.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        from_:
            The Twilio phone number to send messages or initiate calls from during
            the Flow's Execution. Available as variable
            `{{flow.channel.address}}`. For SMS, this can also be a
            Messaging Service SID.
        parameters:
            JSON data that will be added to the Flow's context and that can be
            accessed as variables inside your Flow. For example, if you
            pass in `Parameters={"name":"Zeke"}`, a widget in your Flow
            can reference the variable `{{flow.data.name}}`, which
            returns "Zeke". Note: the JSON value must explicitly be
            passed as a string, not as a hash object. Depending on your
            particular HTTP library, you may need to add quotes or URL
            encode the JSON string.
        to:
            The Contact phone number to start a Studio Flow Execution, available as
            variable `{{contact.channel.address}}`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{flow_sid}/Executions?](
    https://studio.twilio.com/v2/Flows/{flow_sid}/Executions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{flow_sid}/Executions"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "from_": from_,
        "parameters": parameters,
        "to": to,
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
async def get_v2_flows_flow_sid_executions_execution_sid_context(
    flow_sid: str,
    execution_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve the most recent context for an Execution.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        execution_sid:
            Execution sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Context?](
    https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Context?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Context"  # noqa
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
async def get_v2_flows_flow_sid_executions_execution_sid_steps(
    flow_sid: str,
    execution_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Steps for an Execution.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        execution_sid:
            Execution sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps?&page_size=%s](
    https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps"  # noqa
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
async def get_v2_flows_flow_sid_executions_execution_sid_steps_sid(
    flow_sid: str,
    execution_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a Step.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        execution_sid:
            Execution sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{sid}?](
    https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{sid}"  # noqa
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
async def get_v2_flows_flow_sid_executions_execution_sid_steps_step_sid_context(
    flow_sid: str,
    execution_sid: str,
    step_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve the context for an Execution Step.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        execution_sid:
            Execution sid used in formatting the endpoint URL.
        step_sid:
            Step sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{step_sid}/Context?](
    https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{step_sid}/Context?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{step_sid}/Context"  # noqa
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
async def delete_v2_flows_flow_sid_executions_sid(
    flow_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete the Execution and all Steps relating to it.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{sid}?](
    https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{sid}"  # noqa
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
async def get_v2_flows_flow_sid_executions_sid(
    flow_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve an Execution.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{sid}?](
    https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{sid}"  # noqa
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
async def post_v2_flows_flow_sid_executions_sid(
    flow_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Update the status of an Execution to `ended`.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The status of the Execution. Can only be `ended`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{sid}?](
    https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{flow_sid}/Executions/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "status": status,
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
async def delete_v2_flows_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Flow.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{sid}?](
    https://studio.twilio.com/v2/Flows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{sid}"  # noqa
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
async def get_v2_flows_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Flow.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{sid}?](
    https://studio.twilio.com/v2/Flows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{sid}"  # noqa
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
async def post_v2_flows_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    commit_message: str = None,
    definition: str = None,
    friendly_name: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """
    Update a Flow.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        commit_message:
            Description of change made in the revision.
        definition:
            JSON representation of flow definition.
        friendly_name:
            The string that you assigned to describe the Flow.
        status:
            The status of the Flow. Can be: `draft` or `published`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{sid}?](
    https://studio.twilio.com/v2/Flows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "commit_message": commit_message,
        "definition": definition,
        "friendly_name": friendly_name,
        "status": status,
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
async def get_v2_flows_sid_revisions(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Flows revisions.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{sid}/Revisions?&page_size=%s](
    https://studio.twilio.com/v2/Flows/{sid}/Revisions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{sid}/Revisions"  # noqa
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
async def get_v2_flows_sid_revisions_revision(
    sid: str,
    revision: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Flow revision.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        revision:
            Revision used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{sid}/Revisions/{revision}?](
    https://studio.twilio.com/v2/Flows/{sid}/Revisions/{revision}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{sid}/Revisions/{revision}"  # noqa
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
async def get_v2_flows_sid_test_users(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch flow test users.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{sid}/TestUsers?](
    https://studio.twilio.com/v2/Flows/{sid}/TestUsers?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{sid}/TestUsers"  # noqa
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
async def post_v2_flows_sid_test_users(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    test_users: list = None,
) -> Dict[str, Any]:
    """
    Update flow test users.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        test_users:
            List of test user identities that can test draft versions of the flow.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v2/Flows/{sid}/TestUsers?](
    https://studio.twilio.com/v2/Flows/{sid}/TestUsers?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v2/Flows/{sid}/TestUsers"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "test_users": test_users,
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
async def get_v2_attempts(
    twilio_credentials: "TwilioCredentials",
    date_created_after: str = None,
    date_created_before: str = None,
    channel_data_to: str = None,
    country: str = None,
    channel: str = None,
    verify_service_sid: str = None,
    verification_sid: str = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all the verification attempts for a given Account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created_after:
            Datetime filter used to query Verification Attempts created after this
            datetime. Given as GMT in RFC 2822 format.
        date_created_before:
            Datetime filter used to query Verification Attempts created before this
            datetime. Given as GMT in RFC 2822 format.
        channel_data_to:
            Destination of a verification. It is phone number in E.164 format.
        country:
            Filter used to query Verification Attempts sent to the specified
            destination country.
        channel:
            Filter used to query Verification Attempts by communication channel.
            Valid values are `SMS` and `CALL`.
        verify_service_sid:
            Filter used to query Verification Attempts by verify service. Only
            attempts of the provided SID will be returned.
        verification_sid:
            Filter used to return all the Verification Attempts of a single
            verification. Only attempts of the provided verification SID
            will be returned.
        status:
            Filter used to query Verification Attempts by conversion status. Valid
            values are `UNCONVERTED`, for attempts that were not
            converted, and `CONVERTED`, for attempts that were
            confirmed.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Attempts?&date_created_after=%s&date_created_before=%s&channel_data_to=%s&country=%s&channel=%s&verify_service_sid=%s&verification_sid=%s&status=%s&page_size=%s](
    https://verify.twilio.com/v2/Attempts?&date_created_after=%s&date_created_before=%s&channel_data_to=%s&country=%s&channel=%s&verify_service_sid=%s&verification_sid=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Attempts"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "channel_data_to": channel_data_to,
        "country": country,
        "channel": channel,
        "verify_service_sid": verify_service_sid,
        "verification_sid": verification_sid,
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
async def get_v2_attempts_summary(
    twilio_credentials: "TwilioCredentials",
    verify_service_sid: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    country: str = None,
    channel: str = None,
    destination_prefix: str = None,
) -> Dict[str, Any]:
    """
    Get a summary of how many attempts were made and how many were converted.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        verify_service_sid:
            Filter used to consider only Verification Attempts of the given verify
            service on the summary aggregation.
        date_created_after:
            Datetime filter used to consider only Verification Attempts created
            after this datetime on the summary aggregation. Given as GMT
            in RFC 2822 format.
        date_created_before:
            Datetime filter used to consider only Verification Attempts created
            before this datetime on the summary aggregation. Given as
            GMT in RFC 2822 format.
        country:
            Filter used to consider only Verification Attempts sent to the specified
            destination country on the summary aggregation.
        channel:
            Filter Verification Attempts considered on the summary aggregation by
            communication channel. Valid values are `SMS` and `CALL`.
        destination_prefix:
            Filter the Verification Attempts considered on the summary aggregation
            by Destination prefix. It is the prefix of a phone number in
            E.164 format.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Attempts/Summary?&verify_service_sid=%s&date_created_after=%s&date_created_before=%s&country=%s&channel=%s&destination_prefix=%s](
    https://verify.twilio.com/v2/Attempts/Summary?&verify_service_sid=%s&date_created_after=%s&date_created_before=%s&country=%s&channel=%s&destination_prefix=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Attempts/Summary"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "verify_service_sid": verify_service_sid,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "country": country,
        "channel": channel,
        "destination_prefix": destination_prefix,
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
async def get_v2_attempts_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific verification attempt.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Attempts/{sid}?](
    https://verify.twilio.com/v2/Attempts/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Attempts/{sid}"  # noqa
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
async def get_v2_forms_form_type(
    form_type: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the forms for a specific Form Type.

    Args:
        form_type:
            Form type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Forms/{form_type}?](
    https://verify.twilio.com/v2/Forms/{form_type}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Forms/{form_type}"  # noqa
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
async def get_v2_services(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Verification Services for an account.

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
    [https://verify.twilio.com/v2/Services?&page_size=%s](
    https://verify.twilio.com/v2/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Services"  # noqa

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
    code_length: int = None,
    custom_code_enabled: bool = None,
    default_template_sid: str = None,
    do_not_share_warning_enabled: bool = None,
    dtmf_input_required: bool = None,
    friendly_name: str = None,
    lookup_enabled: bool = None,
    psd2_enabled: bool = None,
    push_apn_credential_sid: str = None,
    push_fcm_credential_sid: str = None,
    push_include_date: bool = None,
    skip_sms_to_landlines: bool = None,
    totp_code_length: int = None,
    totp_issuer: str = None,
    totp_skew: int = None,
    totp_time_step: int = None,
    tts_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Verification Service.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        code_length:
            The length of the verification code to generate. Must be an integer
            value between 4 and 10, inclusive.
        custom_code_enabled:
            Whether to allow sending verifications with a custom code instead of a
            randomly generated one. Not available for all customers.
        default_template_sid:
            The default message
            [template](https://www.twilio.com/docs/verify/api/templates).
            Will be used for all SMS verifications unless explicitly
            overriden. SMS channel only.
        do_not_share_warning_enabled:
            Whether to add a security warning at the end of an SMS verification
            body. Disabled by default and applies only to SMS. Example
            SMS body: `Your AppName verification code is: 1234. Don’t
            share this code with anyone; our employees will never ask
            for the code`.
        dtmf_input_required:
            Whether to ask the user to press a number before delivering the verify
            code in a phone call.
        friendly_name:
            A descriptive string that you create to describe the verification
            service. It can be up to 30 characters long. **This value
            should not contain PII.**.
        lookup_enabled:
            Whether to perform a lookup with each verification started and return
            info about the phone number.
        psd2_enabled:
            Whether to pass PSD2 transaction parameters when starting a
            verification.
        push_apn_credential_sid:
            Optional configuration for the Push factors. Set the APN Credential for
            this service. This will allow to send push notifications to
            iOS devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_fcm_credential_sid:
            Optional configuration for the Push factors. Set the FCM Credential for
            this service. This will allow to send push notifications to
            Android devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_include_date:
            Optional configuration for the Push factors. If true, include the date
            in the Challenge's response. Otherwise, the date is omitted
            from the response. See
            [Challenge](https://www.twilio.com/docs/verify/api/challenge)
            resource’s details parameter for more info. Default: false.
            **Deprecated** do not use this parameter. This timestamp
            value is the same one as the one found in `date_created`,
            please use that one instead.
        skip_sms_to_landlines:
            Whether to skip sending SMS verifications to landlines. Requires
            `lookup_enabled`.
        totp_code_length:
            Optional configuration for the TOTP factors. Number of digits for
            generated TOTP codes. Must be between 3 and 8, inclusive.
            Defaults to 6.
        totp_issuer:
            Optional configuration for the TOTP factors. Set TOTP Issuer for this
            service. This will allow to configure the issuer of the TOTP
            URI. Defaults to the service friendly name if not provided.
        totp_skew:
            Optional configuration for the TOTP factors. The number of time-steps,
            past and future, that are valid for validation of TOTP
            codes. Must be between 0 and 2, inclusive. Defaults to 1.
        totp_time_step:
            Optional configuration for the TOTP factors. Defines how often, in
            seconds, are TOTP codes generated. i.e, a new TOTP code is
            generated every time_step seconds. Must be between 20 and 60
            seconds, inclusive. Defaults to 30 seconds.
        tts_name:
            The name of an alternative text-to-speech service to use in phone calls.
            Applies only to TTS languages.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services?](
    https://verify.twilio.com/v2/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "code_length": code_length,
        "custom_code_enabled": custom_code_enabled,
        "default_template_sid": default_template_sid,
        "do_not_share_warning_enabled": do_not_share_warning_enabled,
        "dtmf_input_required": dtmf_input_required,
        "friendly_name": friendly_name,
        "lookup_enabled": lookup_enabled,
        "psd2_enabled": psd2_enabled,
        "push_apn_credential_sid": push_apn_credential_sid,
        "push_fcm_credential_sid": push_fcm_credential_sid,
        "push_include_date": push_include_date,
        "skip_sms_to_landlines": skip_sms_to_landlines,
        "totp_code_length": totp_code_length,
        "totp_issuer": totp_issuer,
        "totp_skew": totp_skew,
        "totp_time_step": totp_time_step,
        "tts_name": tts_name,
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
async def post_v2_services_service_sid_access_tokens(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    factor_friendly_name: str = None,
    factor_type: str = None,
    identity: str = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """
    Create a new enrollment Access Token for the Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        factor_friendly_name:
            The friendly name of the factor that is going to be created with this
            access token.
        factor_type:
            The Type of this Factor. Eg. `push`.
        identity:
            The unique external identifier for the Entity of the Service. This
            identifier should be immutable, not PII, and generated by
            your external system, such as your user's UUID, GUID, or
            SID.
        ttl:
            How long, in seconds, the access token is valid. Can be an integer
            between 60 and 300. Default is 60.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens?](
    https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "factor_friendly_name": factor_friendly_name,
        "factor_type": factor_type,
        "identity": identity,
        "ttl": ttl,
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
async def get_v2_services_service_sid_access_tokens_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an Access Token for the Entity.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens/{sid}"  # noqa
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
async def get_v2_services_service_sid_entities(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Entities for a Service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities"  # noqa
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
async def post_v2_services_service_sid_entities(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
) -> Dict[str, Any]:
    """
    Create a new Entity for the Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The unique external identifier for the Entity of the Service. This
            identifier should be immutable, not PII, length between 8
            and 64 characters, and generated by your external system,
            such as your user's UUID, GUID, or SID. It can only contain
            dash (-) separated alphanumeric characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
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
async def delete_v2_services_service_sid_entities_identity(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}"  # noqa
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
async def get_v2_services_service_sid_entities_identity(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}"  # noqa
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
async def get_v2_services_service_sid_entities_identity_challenges(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    factor_sid: str = None,
    status: str = None,
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Challenges for a Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        factor_sid:
            The unique SID identifier of the Factor.
        status:
            The Status of the Challenges to fetch. One of `pending`, `expired`,
            `approved` or `denied`.
        order:
            The desired sort order of the Challenges list. One of `asc` or `desc`
            for ascending and descending respectively. Defaults to
            `asc`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?&factor_sid=%s&status=%s&order=%s&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?&factor_sid=%s&status=%s&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "factor_sid": factor_sid,
        "status": status,
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
async def post_v2_services_service_sid_entities_identity_challenges(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    auth_payload: str = None,
    details_fields: list = None,
    details_message: str = None,
    expiration_date: str = None,
    factor_sid: str = None,
    hidden_details: str = None,
) -> Dict[str, Any]:
    """
    Create a new Challenge for the Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auth_payload:
            Optional payload used to verify the Challenge upon creation. Only used
            with a Factor of type `totp` to carry the TOTP code that
            needs to be verified. For `TOTP` this value must be between
            3 and 8 characters long.
        details_fields:
            A list of objects that describe the Fields included in the Challenge.
            Each object contains the label and value of the field, the
            label can be up to 36 characters in length and the value can
            be up to 128 characters in length. Used when `factor_type`
            is `push`. There can be up to 20 details fields.
        details_message:
            Shown to the user when the push notification arrives. Required when
            `factor_type` is `push`. Can be up to 256 characters in
            length.
        expiration_date:
            The date-time when this Challenge expires, given in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format. The
            default value is five (5) minutes after Challenge creation.
            The max value is sixty (60) minutes after creation.
        factor_sid:
            The unique SID identifier of the Factor.
        hidden_details:
            Details provided to give context about the Challenge. Not shown to the
            end user. It must be a stringified JSON with only strings
            values eg. `{"ip": "172.168.1.234"}`. Can be up to 1024
            characters in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "auth_payload": auth_payload,
        "details_fields": details_fields,
        "details_message": details_message,
        "expiration_date": expiration_date,
        "factor_sid": factor_sid,
        "hidden_details": hidden_details,
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
async def post_v2_services_service_sid_entities_identity_challenges_challenge_sid_notifications(
    service_sid: str,
    identity: str,
    challenge_sid: str,
    twilio_credentials: "TwilioCredentials",
    ttl: int = None,
) -> Dict[str, Any]:
    """
    Create a new Notification for the corresponding Challenge.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        challenge_sid:
            Challenge sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ttl:
            How long, in seconds, the notification is valid. Can be an integer
            between 0 and 300. Default is 300. Delivery is attempted
            until the TTL elapses, even if the device is offline. 0
            means that the notification delivery is attempted
            immediately, only once, and is not stored for future
            delivery.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "ttl": ttl,
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
async def get_v2_services_service_sid_entities_identity_challenges_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Challenge.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}"  # noqa
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
async def post_v2_services_service_sid_entities_identity_challenges_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    auth_payload: str = None,
    metadata: str = None,
) -> Dict[str, Any]:
    """
    Verify a specific Challenge.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auth_payload:
            The optional payload needed to verify the Challenge. E.g., a TOTP would
            use the numeric code. For `TOTP` this value must be between
            3 and 8 characters long. For `Push` this value can be up to
            5456 characters in length.
        metadata:
            Custom metadata associated with the challenge. This is added by the
            Device/SDK directly to allow for the inclusion of device
            information. It must be a stringified JSON with only strings
            values eg. `{"os": "Android"}`. Can be up to 1024 characters
            in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "auth_payload": auth_payload,
        "metadata": metadata,
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
async def get_v2_services_service_sid_entities_identity_factors(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Factors for an Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors"  # noqa
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
async def post_v2_services_service_sid_entities_identity_factors(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    binding_alg: str = None,
    binding_public_key: str = None,
    binding_secret: str = None,
    config_alg: str = None,
    config_app_id: str = None,
    config_code_length: int = None,
    config_notification_platform: str = None,
    config_notification_token: str = None,
    config_sdk_version: str = None,
    config_skew: int = None,
    config_time_step: int = None,
    factor_type: str = None,
    friendly_name: str = None,
    metadata: str = None,
) -> Dict[str, Any]:
    """
    Create a new Factor for the Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_alg:
            The algorithm used when `factor_type` is `push`. Algorithm supported:
            `ES256`.
        binding_public_key:
            The Ecdsa public key in PKIX, ASN.1 DER format encoded in Base64.
            Required when `factor_type` is `push`.
        binding_secret:
            The shared secret for TOTP factors encoded in Base32. This can be
            provided when creating the Factor, otherwise it will be
            generated.  Used when `factor_type` is `totp`.
        config_alg:
            The algorithm used to derive the TOTP codes. Can be `sha1`, `sha256` or
            `sha512`. Defaults to `sha1`.  Used when `factor_type` is
            `totp`.
        config_app_id:
            The ID that uniquely identifies your app in the Google or Apple store,
            such as `com.example.myapp`. It can be up to 100 characters
            long.  Required when `factor_type` is `push`.
        config_code_length:
            Number of digits for generated TOTP codes. Must be between 3 and 8,
            inclusive. The default value is defined at the service level
            in the property `totp.code_length`. If not configured
            defaults to 6.  Used when `factor_type` is `totp`.
        config_notification_platform:
            The transport technology used to generate the Notification Token. Can be
            `apn`, `fcm` or `none`.  Required when `factor_type` is
            `push`.
        config_notification_token:
            For APN, the device token. For FCM, the registration token. It is used
            to send the push notifications. Must be between 32 and 255
            characters long.  Required when `factor_type` is `push`.
        config_sdk_version:
            The Verify Push SDK version used to configure the factor  Required when
            `factor_type` is `push`.
        config_skew:
            The number of time-steps, past and future, that are valid for validation
            of TOTP codes. Must be between 0 and 2, inclusive. The
            default value is defined at the service level in the
            property `totp.skew`. If not configured defaults to 1.  Used
            when `factor_type` is `totp`.
        config_time_step:
            Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP
            code is generated every time_step seconds. Must be between
            20 and 60 seconds, inclusive. The default value is defined
            at the service level in the property `totp.time_step`.
            Defaults to 30 seconds if not configured.  Used when
            `factor_type` is `totp`.
        factor_type:
            The Type of this Factor. Currently `push` and `totp` are supported.
        friendly_name:
            The friendly name of this Factor. This can be any string up to 64
            characters, meant for humans to distinguish between Factors.
            For `factor_type` `push`, this could be a device name. For
            `factor_type` `totp`, this value is used as the “account
            name” in constructing the `binding.uri` property. At the
            same time, we recommend avoiding providing PII.
        metadata:
            Custom metadata associated with the factor. This is added by the
            Device/SDK directly to allow for the inclusion of device
            information. It must be a stringified JSON with only strings
            values eg. `{"os": "Android"}`. Can be up to 1024 characters
            in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "binding_alg": binding_alg,
        "binding_public_key": binding_public_key,
        "binding_secret": binding_secret,
        "config_alg": config_alg,
        "config_app_id": config_app_id,
        "config_code_length": config_code_length,
        "config_notification_platform": config_notification_platform,
        "config_notification_token": config_notification_token,
        "config_sdk_version": config_sdk_version,
        "config_skew": config_skew,
        "config_time_step": config_time_step,
        "factor_type": factor_type,
        "friendly_name": friendly_name,
        "metadata": metadata,
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
async def delete_v2_services_service_sid_entities_identity_factors_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}"  # noqa
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
async def get_v2_services_service_sid_entities_identity_factors_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}"  # noqa
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
async def post_v2_services_service_sid_entities_identity_factors_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    auth_payload: str = None,
    config_alg: str = None,
    config_code_length: int = None,
    config_notification_platform: str = None,
    config_notification_token: str = None,
    config_sdk_version: str = None,
    config_skew: int = None,
    config_time_step: int = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Factor. This endpoint can be used to Verify a Factor if passed
    an `AuthPayload` param.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auth_payload:
            The optional payload needed to verify the Factor for the first time.
            E.g. for a TOTP, the numeric code.
        config_alg:
            The algorithm used to derive the TOTP codes. Can be `sha1`, `sha256` or
            `sha512`.
        config_code_length:
            Number of digits for generated TOTP codes. Must be between 3 and 8,
            inclusive.
        config_notification_platform:
            The transport technology used to generate the Notification Token. Can be
            `apn`, `fcm` or `none`.  Required when `factor_type` is
            `push`.
        config_notification_token:
            For APN, the device token. For FCM, the registration token. It is used
            to send the push notifications. Required when `factor_type`
            is `push`. If specified, this value must be between 32 and
            255 characters long.
        config_sdk_version:
            The Verify Push SDK version used to configure the factor.
        config_skew:
            The number of time-steps, past and future, that are valid for validation
            of TOTP codes. Must be between 0 and 2, inclusive.
        config_time_step:
            Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP
            code is generated every time_step seconds. Must be between
            20 and 60 seconds, inclusive.
        friendly_name:
            The new friendly name of this Factor. It can be up to 64 characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "auth_payload": auth_payload,
        "config_alg": config_alg,
        "config_code_length": config_code_length,
        "config_notification_platform": config_notification_platform,
        "config_notification_token": config_notification_token,
        "config_sdk_version": config_sdk_version,
        "config_skew": config_skew,
        "config_time_step": config_time_step,
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
async def get_v2_services_service_sid_messaging_configurations(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Messaging Configurations for a Service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations"  # noqa
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
async def post_v2_services_service_sid_messaging_configurations(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    country: str = None,
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new MessagingConfiguration for a service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        country:
            The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            country code of the country this configuration will be
            applied to. If this is a global configuration, Country will
            take the value `all`.
        messaging_service_sid:
            The SID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) to be
            used to send SMS to the country of this configuration.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "country": country,
        "messaging_service_sid": messaging_service_sid,
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
async def delete_v2_services_service_sid_messaging_configurations_country(
    service_sid: str,
    country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific MessagingConfiguration.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        country:
            Country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}"  # noqa
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
async def get_v2_services_service_sid_messaging_configurations_country(
    service_sid: str,
    country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific MessagingConfiguration.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        country:
            Country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}"  # noqa
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
async def post_v2_services_service_sid_messaging_configurations_country(
    service_sid: str,
    country: str,
    twilio_credentials: "TwilioCredentials",
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """
    Update a specific MessagingConfiguration.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        country:
            Country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        messaging_service_sid:
            The SID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) to be
            used to send SMS to the country of this configuration.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "messaging_service_sid": messaging_service_sid,
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
async def get_v2_services_service_sid_rate_limits(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Rate Limits for a service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits"  # noqa
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
async def post_v2_services_service_sid_rate_limits(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    description: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Rate Limit for a Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            Description of this Rate Limit.
        unique_name:
            Provides a unique and addressable name to be assigned to this Rate
            Limit, assigned by the developer, to be optionally used in
            addition to SID. **This value should not contain PII.**.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "description": description,
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
async def get_v2_services_service_sid_rate_limits_rate_limit_sid_buckets(
    service_sid: str,
    rate_limit_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Buckets for a Rate Limit.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets"  # noqa
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
async def post_v2_services_service_sid_rate_limits_rate_limit_sid_buckets(
    service_sid: str,
    rate_limit_sid: str,
    twilio_credentials: "TwilioCredentials",
    interval: int = None,
    max: int = None,
) -> Dict[str, Any]:
    """
    Create a new Bucket for a Rate Limit.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        interval:
            Number of seconds that the rate limit will be enforced over.
        max:
            Maximum number of requests permitted in during the interval.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "interval": interval,
        "max": max,
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
async def delete_v2_services_service_sid_rate_limits_rate_limit_sid_buckets_sid(
    service_sid: str,
    rate_limit_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Bucket.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}"  # noqa
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
async def get_v2_services_service_sid_rate_limits_rate_limit_sid_buckets_sid(
    service_sid: str,
    rate_limit_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Bucket.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}"  # noqa
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
async def post_v2_services_service_sid_rate_limits_rate_limit_sid_buckets_sid(
    service_sid: str,
    rate_limit_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    interval: int = None,
    max: int = None,
) -> Dict[str, Any]:
    """
    Update a specific Bucket.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        interval:
            Number of seconds that the rate limit will be enforced over.
        max:
            Maximum number of requests permitted in during the interval.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "interval": interval,
        "max": max,
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
async def delete_v2_services_service_sid_rate_limits_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Rate Limit.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}"  # noqa
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
async def get_v2_services_service_sid_rate_limits_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Rate Limit.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}"  # noqa
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
async def post_v2_services_service_sid_rate_limits_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    description: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Rate Limit.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            Description of this Rate Limit.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "description": description,
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
async def post_v2_services_service_sid_verification_check(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    amount: str = None,
    code: str = None,
    payee: str = None,
    to: str = None,
    verification_sid: str = None,
) -> Dict[str, Any]:
    """
    challenge a specific Verification Check.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        amount:
            The amount of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        code:
            The 4-10 character string being verified.
        payee:
            The payee of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        to:
            The phone number or [email](https://www.twilio.com/docs/verify/email) to
            verify. Either this parameter or the `verification_sid` must
            be specified. Phone numbers must be in [E.164
            format](https://www.twilio.com/docs/glossary/what-e164).
        verification_sid:
            A SID that uniquely identifies the Verification Check. Either this
            parameter or the `to` phone
            number/[email](https://www.twilio.com/docs/verify/email)
            must be specified.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/VerificationCheck?](
    https://verify.twilio.com/v2/Services/{service_sid}/VerificationCheck?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/VerificationCheck"  # noqa
    )
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "amount": amount,
        "code": code,
        "payee": payee,
        "to": to,
        "verification_sid": verification_sid,
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
async def post_v2_services_service_sid_verifications(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    amount: str = None,
    app_hash: str = None,
    channel: str = None,
    channel_configuration: str = None,
    custom_code: str = None,
    custom_friendly_name: str = None,
    custom_message: str = None,
    locale: str = None,
    payee: str = None,
    rate_limits: str = None,
    send_digits: str = None,
    template_custom_substitutions: str = None,
    template_sid: str = None,
    to: str = None,
) -> Dict[str, Any]:
    """
    Create a new Verification using a Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        amount:
            The amount of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        app_hash:
            Your [App Hash](https://developers.google.com/identity/sms-
            retriever/verify
            computing_your_apps_hash_string) to be appended at the end
            of your verification SMS body. Applies only to SMS. Example
            SMS body: `<
            > Your AppName verification code is: 1234 He42w354ol9`.
        channel:
            The verification method to use. Can be:
            [`email`](https://www.twilio.com/docs/verify/email), `sms`,
            `whatsapp` or `call`.
        channel_configuration:
            [`email`](https://www.twilio.com/docs/verify/email) channel
            configuration in json format. The fields 'from' and
            'from_name' are optional but if included the 'from' field
            must have a valid email address.
        custom_code:
            A pre-generated code to use for verification. The code can be between 4
            and 10 characters, inclusive.
        custom_friendly_name:
            A custom user defined friendly name that overwrites the existing one in
            the verification message.
        custom_message:
            The text of a custom message to use for the verification.
        locale:
            The locale to use for the verification SMS, WhatsApp or call. Can be:
            `af`, `ar`, `ca`, `cs`, `da`, `de`, `el`, `en`, `en-GB`,
            `es`, `fi`, `fr`, `he`, `hi`, `hr`, `hu`, `id`, `it`, `ja`,
            `ko`, `ms`, `nb`, `nl`, `pl`, `pt`, `pr-BR`, `ro`, `ru`,
            `sv`, `th`, `tl`, `tr`, `vi`, `zh`, `zh-CN`, or `zh-HK.`.
        payee:
            The payee of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        rate_limits:
            The custom key-value pairs of Programmable Rate Limits. Keys correspond
            to `unique_name` fields defined when [creating your Rate
            Limit](https://www.twilio.com/docs/verify/api/service-rate-
            limits). Associated value pairs represent values in the
            request that you are rate limiting on. You may include
            multiple Rate Limit values in each request.
        send_digits:
            The digits to send after a phone call is answered, for example, to dial
            an extension. For more information, see the Programmable
            Voice documentation of
            [sendDigits](https://www.twilio.com/docs/voice/twiml/number
            attributes-sendDigits).
        template_custom_substitutions:
            A stringified JSON object in which the keys are the template's special
            variables and the values are the variables substitutions.
        template_sid:
            The message
            [template](https://www.twilio.com/docs/verify/api/templates).
            If provided, will override the default template for the
            Service. SMS channel only.
        to:
            The phone number or [email](https://www.twilio.com/docs/verify/email) to
            verify. Phone numbers must be in [E.164
            format](https://www.twilio.com/docs/glossary/what-e164).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Verifications?](
    https://verify.twilio.com/v2/Services/{service_sid}/Verifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "amount": amount,
        "app_hash": app_hash,
        "channel": channel,
        "channel_configuration": channel_configuration,
        "custom_code": custom_code,
        "custom_friendly_name": custom_friendly_name,
        "custom_message": custom_message,
        "locale": locale,
        "payee": payee,
        "rate_limits": rate_limits,
        "send_digits": send_digits,
        "template_custom_substitutions": template_custom_substitutions,
        "template_sid": template_sid,
        "to": to,
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
async def get_v2_services_service_sid_verifications_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Verification.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}"  # noqa
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
async def post_v2_services_service_sid_verifications_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Update a Verification status.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The new status of the resource. Can be: `canceled` or `approved`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "status": status,
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
async def get_v2_services_service_sid_webhooks(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Webhooks for a Service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks"  # noqa
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
async def post_v2_services_service_sid_webhooks(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    event_types: list = None,
    friendly_name: str = None,
    status: str = None,
    version: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """
    Create a new Webhook for the Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        event_types:
            The array of events that this Webhook is subscribed to. Possible event
            types: `*, factor.deleted, factor.created, factor.verified,
            challenge.approved, challenge.denied`.
        friendly_name:
            The string that you assigned to describe the webhook. **This value
            should not contain PII.**.
        status:
            The webhook status. Default value is `enabled`. One of: `enabled` or
            `disabled`.
        version:
            The webhook version. Default value is `v2` which includes all the latest
            fields. Version `v1` is legacy and may be removed in the
            future.
        webhook_url:
            The URL associated with this Webhook.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "event_types": event_types,
        "friendly_name": friendly_name,
        "status": status,
        "version": version,
        "webhook_url": webhook_url,
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
async def delete_v2_services_service_sid_webhooks_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Webhook.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}"  # noqa
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
async def get_v2_services_service_sid_webhooks_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Webhook.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}"  # noqa
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
async def post_v2_services_service_sid_webhooks_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    event_types: list = None,
    friendly_name: str = None,
    status: str = None,
    version: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        event_types:
            The array of events that this Webhook is subscribed to. Possible event
            types: `*, factor.deleted, factor.created, factor.verified,
            challenge.approved, challenge.denied`.
        friendly_name:
            The string that you assigned to describe the webhook. **This value
            should not contain PII.**.
        status:
            The webhook status. Default value is `enabled`. One of: `enabled` or
            `disabled`.
        version:
            The webhook version. Default value is `v2` which includes all the latest
            fields. Version `v1` is legacy and may be removed in the
            future.
        webhook_url:
            The URL associated with this Webhook.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "event_types": event_types,
        "friendly_name": friendly_name,
        "status": status,
        "version": version,
        "webhook_url": webhook_url,
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
    Delete a specific Verification Service Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{sid}?](
    https://verify.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{sid}"  # noqa
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
    Fetch specific Verification Service Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{sid}?](
    https://verify.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{sid}"  # noqa
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
    code_length: int = None,
    custom_code_enabled: bool = None,
    default_template_sid: str = None,
    do_not_share_warning_enabled: bool = None,
    dtmf_input_required: bool = None,
    friendly_name: str = None,
    lookup_enabled: bool = None,
    psd2_enabled: bool = None,
    push_apn_credential_sid: str = None,
    push_fcm_credential_sid: str = None,
    push_include_date: bool = None,
    skip_sms_to_landlines: bool = None,
    totp_code_length: int = None,
    totp_issuer: str = None,
    totp_skew: int = None,
    totp_time_step: int = None,
    tts_name: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Verification Service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        code_length:
            The length of the verification code to generate. Must be an integer
            value between 4 and 10, inclusive.
        custom_code_enabled:
            Whether to allow sending verifications with a custom code instead of a
            randomly generated one. Not available for all customers.
        default_template_sid:
            The default message
            [template](https://www.twilio.com/docs/verify/api/templates).
            Will be used for all SMS verifications unless explicitly
            overriden. SMS channel only.
        do_not_share_warning_enabled:
            Whether to add a privacy warning at the end of an SMS. **Disabled by
            default and applies only for SMS.**.
        dtmf_input_required:
            Whether to ask the user to press a number before delivering the verify
            code in a phone call.
        friendly_name:
            A descriptive string that you create to describe the verification
            service. It can be up to 30 characters long. **This value
            should not contain PII.**.
        lookup_enabled:
            Whether to perform a lookup with each verification started and return
            info about the phone number.
        psd2_enabled:
            Whether to pass PSD2 transaction parameters when starting a
            verification.
        push_apn_credential_sid:
            Optional configuration for the Push factors. Set the APN Credential for
            this service. This will allow to send push notifications to
            iOS devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_fcm_credential_sid:
            Optional configuration for the Push factors. Set the FCM Credential for
            this service. This will allow to send push notifications to
            Android devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_include_date:
            Optional configuration for the Push factors. If true, include the date
            in the Challenge's response. Otherwise, the date is omitted
            from the response. See
            [Challenge](https://www.twilio.com/docs/verify/api/challenge)
            resource’s details parameter for more info. Default: false.
            **Deprecated** do not use this parameter.
        skip_sms_to_landlines:
            Whether to skip sending SMS verifications to landlines. Requires
            `lookup_enabled`.
        totp_code_length:
            Optional configuration for the TOTP factors. Number of digits for
            generated TOTP codes. Must be between 3 and 8, inclusive.
            Defaults to 6.
        totp_issuer:
            Optional configuration for the TOTP factors. Set TOTP Issuer for this
            service. This will allow to configure the issuer of the TOTP
            URI.
        totp_skew:
            Optional configuration for the TOTP factors. The number of time-steps,
            past and future, that are valid for validation of TOTP
            codes. Must be between 0 and 2, inclusive. Defaults to 1.
        totp_time_step:
            Optional configuration for the TOTP factors. Defines how often, in
            seconds, are TOTP codes generated. i.e, a new TOTP code is
            generated every time_step seconds. Must be between 20 and 60
            seconds, inclusive. Defaults to 30 seconds.
        tts_name:
            The name of an alternative text-to-speech service to use in phone calls.
            Applies only to TTS languages.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{sid}?](
    https://verify.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "code_length": code_length,
        "custom_code_enabled": custom_code_enabled,
        "default_template_sid": default_template_sid,
        "do_not_share_warning_enabled": do_not_share_warning_enabled,
        "dtmf_input_required": dtmf_input_required,
        "friendly_name": friendly_name,
        "lookup_enabled": lookup_enabled,
        "psd2_enabled": psd2_enabled,
        "push_apn_credential_sid": push_apn_credential_sid,
        "push_fcm_credential_sid": push_fcm_credential_sid,
        "push_include_date": push_include_date,
        "skip_sms_to_landlines": skip_sms_to_landlines,
        "totp_code_length": totp_code_length,
        "totp_issuer": totp_issuer,
        "totp_skew": totp_skew,
        "totp_time_step": totp_time_step,
        "tts_name": tts_name,
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
async def get_v2_templates(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all the available templates for a given Account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            String filter used to query templates with a given friendly name.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Templates?&friendly_name=%s&page_size=%s](
    https://verify.twilio.com/v2/Templates?&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Templates"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "friendly_name": friendly_name,
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
