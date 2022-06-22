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
    [https://notify.twilio.com/v1/Credentials?&page_size=%s](
    https://notify.twilio.com/v1/Credentials?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://notify.twilio.com/v1/Credentials"  # noqa

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
            [GCM only] The `Server key` of your project from Firebase console under
            Settings / Cloud messaging.
        certificate:
            [APN only] The URL-encoded representation of the certificate. Strip
            everything outside of the headers, e.g. `-----BEGIN
            CERTIFICATE-----
            MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END
            CERTIFICATE-----`.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        private_key:
            [APN only] The URL-encoded representation of the private key. Strip
            everything outside of the headers, e.g. `-----BEGIN RSA
            PRIVATE KEY-----
            MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\n.
            -----END RSA PRIVATE KEY-----`.
        sandbox:
            [APN only] Whether to send the credential to sandbox APNs. Can be `true`
            to send to sandbox APNs or `false` to send to production.
        secret:
            [FCM only] The `Server key` of your project from Firebase console under
            Settings / Cloud messaging.
        type:
            The Credential type. Can be: `gcm`, `fcm`, or `apn`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Credentials?](
    https://notify.twilio.com/v1/Credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://notify.twilio.com/v1/Credentials"  # noqa

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
    [https://notify.twilio.com/v1/Credentials/{sid}?](
    https://notify.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Credentials/{sid}"  # noqa
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
    [https://notify.twilio.com/v1/Credentials/{sid}?](
    https://notify.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Credentials/{sid}"  # noqa
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
            [GCM only] The `Server key` of your project from Firebase console under
            Settings / Cloud messaging.
        certificate:
            [APN only] The URL-encoded representation of the certificate. Strip
            everything outside of the headers, e.g. `-----BEGIN
            CERTIFICATE-----
            MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END
            CERTIFICATE-----`.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        private_key:
            [APN only] The URL-encoded representation of the private key. Strip
            everything outside of the headers, e.g. `-----BEGIN RSA
            PRIVATE KEY-----
            MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\n.
            -----END RSA PRIVATE KEY-----`.
        sandbox:
            [APN only] Whether to send the credential to sandbox APNs. Can be `true`
            to send to sandbox APNs or `false` to send to production.
        secret:
            [FCM only] The `Server key` of your project from Firebase console under
            Settings / Cloud messaging.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Credentials/{sid}?](
    https://notify.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Credentials/{sid}"  # noqa
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
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The string that identifies the Service resources to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services?&friendly_name=%s&page_size=%s](
    https://notify.twilio.com/v1/Services?&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://notify.twilio.com/v1/Services"  # noqa

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


@task
async def post_v1_services(
    twilio_credentials: "TwilioCredentials",
    alexa_skill_id: str = None,
    apn_credential_sid: str = None,
    default_alexa_notification_protocol_version: str = None,
    default_apn_notification_protocol_version: str = None,
    default_fcm_notification_protocol_version: str = None,
    default_gcm_notification_protocol_version: str = None,
    delivery_callback_enabled: bool = None,
    delivery_callback_url: str = None,
    facebook_messenger_page_id: str = None,
    fcm_credential_sid: str = None,
    friendly_name: str = None,
    gcm_credential_sid: str = None,
    log_enabled: bool = None,
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        alexa_skill_id:
            Deprecated.
        apn_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for APN Bindings.
        default_alexa_notification_protocol_version:
            Deprecated.
        default_apn_notification_protocol_version:
            The protocol version to use for sending APNS notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        default_fcm_notification_protocol_version:
            The protocol version to use for sending FCM notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        default_gcm_notification_protocol_version:
            The protocol version to use for sending GCM notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        delivery_callback_enabled:
            Callback configuration that enables delivery callbacks, default false.
        delivery_callback_url:
            URL to send delivery status callback.
        facebook_messenger_page_id:
            Deprecated.
        fcm_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for FCM Bindings.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        gcm_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for GCM Bindings.
        log_enabled:
            Whether to log notifications. Can be: `true` or `false` and the default
            is `true`.
        messaging_service_sid:
            The SID of the [Messaging Service](https://www.twilio.com/docs/sms/send-
            messages
            messaging-services) to use for SMS Bindings. This parameter
            must be set in order to send SMS notifications.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services?](
    https://notify.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://notify.twilio.com/v1/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "alexa_skill_id": alexa_skill_id,
        "apn_credential_sid": apn_credential_sid,
        "default_alexa_notification_protocol_version": default_alexa_notification_protocol_version,  # noqa
        "default_apn_notification_protocol_version": default_apn_notification_protocol_version,  # noqa
        "default_fcm_notification_protocol_version": default_fcm_notification_protocol_version,  # noqa
        "default_gcm_notification_protocol_version": default_gcm_notification_protocol_version,  # noqa
        "delivery_callback_enabled": delivery_callback_enabled,
        "delivery_callback_url": delivery_callback_url,
        "facebook_messenger_page_id": facebook_messenger_page_id,
        "fcm_credential_sid": fcm_credential_sid,
        "friendly_name": friendly_name,
        "gcm_credential_sid": gcm_credential_sid,
        "log_enabled": log_enabled,
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
async def get_v1_services_service_sid_bindings(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    start_date: str = None,
    end_date: str = None,
    identity: list = None,
    tag: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.
        identity:
            The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s
            `identity` value of the resources to read.
        tag:
            Only list Bindings that have all of the specified Tags. The following
            implicit tags are available: `all`, `apn`, `fcm`, `gcm`,
            `sms`, `facebook-messenger`. Up to 5 tags are allowed.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services/{service_sid}/Bindings?&start_date=%s&end_date=%s&identity=%s&tag=%s&page_size=%s](
    https://notify.twilio.com/v1/Services/{service_sid}/Bindings?&start_date=%s&end_date=%s&identity=%s&tag=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Bindings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "start_date": start_date,
        "end_date": end_date,
        "identity": identity,
        "tag": tag,
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
async def post_v1_services_service_sid_bindings(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    address: str = None,
    binding_type: str = None,
    credential_sid: str = None,
    endpoint: str = None,
    identity: str = None,
    notification_protocol_version: str = None,
    tag: list = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        address:
            The channel-specific address. For APNS, the device token. For FCM and
            GCM, the registration token. For SMS, a phone number in
            E.164 format. For Facebook Messenger, the Messenger ID of
            the user or a phone number in E.164 format.
        binding_type:
            The transport technology to use for the Binding. Can be: `apn`, `fcm`,
            `gcm`, `sms`, or `facebook-messenger`.
        credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) resource to be used to send notifications to this
            Binding. If present, this overrides the Credential specified
            in the Service resource. Applies to only `apn`, `fcm`, and
            `gcm` type Bindings.
        endpoint:
            Deprecated.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/notify/api/service-
            resource). Up to 20 Bindings can be created for the same
            Identity in a given Service.
        notification_protocol_version:
            The protocol version to use to send the notification. This defaults to
            the value of `default_xxxx_notification_protocol_version`
            for the protocol in the
            [Service](https://www.twilio.com/docs/notify/api/service-
            resource). The current version is `"3"` for `apn`, `fcm`,
            and `gcm` type Bindings. The parameter is not applicable to
            `sms` and `facebook-messenger` type Bindings as the data
            format is fixed.
        tag:
            A tag that can be used to select the Bindings to notify. Repeat this
            parameter to specify more than one tag, up to a total of 20
            tags.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services/{service_sid}/Bindings?](
    https://notify.twilio.com/v1/Services/{service_sid}/Bindings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Bindings"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "address": address,
        "binding_type": binding_type,
        "credential_sid": credential_sid,
        "endpoint": endpoint,
        "identity": identity,
        "notification_protocol_version": notification_protocol_version,
        "tag": tag,
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
async def delete_v1_services_service_sid_bindings_sid(
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
    [https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}?](
    https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def get_v1_services_service_sid_bindings_sid(
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
    [https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}?](
    https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def post_v1_services_service_sid_notifications(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    action: str = None,
    alexa: str = None,
    apn: str = None,
    body: str = None,
    data: str = None,
    delivery_callback_url: str = None,
    facebook_messenger: str = None,
    fcm: str = None,
    gcm: str = None,
    identity: list = None,
    priority: str = None,
    segment: list = None,
    sms: str = None,
    sound: str = None,
    tag: list = None,
    title: str = None,
    to_binding: list = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        action:
            The actions to display for the notification. For APNS, translates to the
            `aps.category` value. For GCM, translates to the
            `data.twi_action` value. For SMS, this parameter is not
            supported and is omitted from deliveries to those channels.
        alexa:
            Deprecated.
        apn:
            The APNS-specific payload that overrides corresponding attributes in the
            generic payload for APNS Bindings. This property maps to the
            APNS `Payload` item, therefore the `aps` key must be used to
            change standard attributes. Adds custom key-value pairs to
            the root of the dictionary. See the [APNS
            documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html)
            for more details. We reserve keys that start with `twi_` for
            future use. Custom keys that start with `twi_` are not
            allowed.
        body:
            The notification text. For FCM and GCM, translates to `data.twi_body`.
            For APNS, translates to `aps.alert.body`. For SMS,
            translates to `body`. SMS requires either this `body` value,
            or `media_urls` attribute defined in the `sms` parameter of
            the notification.
        data:
            The custom key-value pairs of the notification's payload. For FCM and
            GCM, this value translates to `data` in the FCM and GCM
            payloads. FCM and GCM [reserve certain
            keys](https://firebase.google.com/docs/cloud-messaging/http-
            server-ref) that cannot be used in those channels. For APNS,
            attributes of `data` are inserted into the APNS payload as
            custom properties outside of the `aps` dictionary. In all
            channels, we reserve keys that start with `twi_` for future
            use. Custom keys that start with `twi_` are not allowed and
            are rejected as 400 Bad request with no delivery attempted.
            For SMS, this parameter is not supported and is omitted from
            deliveries to those channels.
        delivery_callback_url:
            URL to send webhooks.
        facebook_messenger:
            Deprecated.
        fcm:
            The FCM-specific payload that overrides corresponding attributes in the
            generic payload for FCM Bindings. This property maps to the
            root JSON dictionary. See the [FCM
            documentation](https://firebase.google.com/docs/cloud-
            messaging/http-server-ref
            downstream) for more details. Target parameters `to`,
            `registration_ids`, `condition`, and `notification_key` are
            not allowed in this parameter. We reserve keys that start
            with `twi_` for future use. Custom keys that start with
            `twi_` are not allowed. FCM also [reserves certain
            keys](https://firebase.google.com/docs/cloud-messaging/http-
            server-ref), which cannot be used in that channel.
        gcm:
            The GCM-specific payload that overrides corresponding attributes in the
            generic payload for GCM Bindings.  This property maps to the
            root JSON dictionary. See the [GCM
            documentation](https://firebase.google.com/docs/cloud-
            messaging/http-server-ref) for more details. Target
            parameters `to`, `registration_ids`, and `notification_key`
            are not allowed. We reserve keys that start with `twi_` for
            future use. Custom keys that start with `twi_` are not
            allowed. GCM also [reserves certain
            keys](https://firebase.google.com/docs/cloud-messaging/http-
            server-ref).
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/notify/api/service-
            resource). Delivery will be attempted only to Bindings with
            an Identity in this list. No more than 20 items are allowed
            in this list.
        priority:
            The priority of the notification. Can be: `low` or `high` and the
            default is `high`. A value of `low` optimizes the client
            app's battery consumption; however, notifications may be
            delivered with unspecified delay. For FCM and GCM, `low`
            priority is the same as `Normal` priority. For APNS `low`
            priority is the same as `5`. A value of `high` sends the
            notification immediately, and can wake up a sleeping device.
            For FCM and GCM, `high` is the same as `High` priority. For
            APNS, `high` is a priority `10`. SMS does not support this
            property.
        segment:
            The Segment resource is deprecated. Use the `tag` parameter, instead.
        sms:
            The SMS-specific payload that overrides corresponding attributes in the
            generic payload for SMS Bindings.  Each attribute in this
            value maps to the corresponding `form` parameter of the
            Twilio [Message](https://www.twilio.com/docs/sms/send-
            messages) resource.  These parameters of the Message
            resource are supported in snake case format: `body`,
            `media_urls`, `status_callback`, and `max_price`.  The
            `status_callback` parameter overrides the corresponding
            parameter in the messaging service, if configured. The
            `media_urls` property expects a JSON array.
        sound:
            The name of the sound to be played for the notification. For FCM and
            GCM, this Translates to `data.twi_sound`.  For APNS, this
            translates to `aps.sound`.  SMS does not support this
            property.
        tag:
            A tag that selects the Bindings to notify. Repeat this parameter to
            specify more than one tag, up to a total of 5 tags. The
            implicit tag `all` is available to notify all Bindings in a
            Service instance. Similarly, the implicit tags `apn`, `fcm`,
            `gcm`, `sms` and `facebook-messenger` are available to
            notify all Bindings in a specific channel.
        title:
            The notification title. For FCM and GCM, this translates to the
            `data.twi_title` value. For APNS, this translates to the
            `aps.alert.title` value. SMS does not support this property.
            This field is not visible on iOS phones and tablets but
            appears on Apple Watch and Android devices.
        to_binding:
            The destination address specified as a JSON string.  Multiple
            `to_binding` parameters can be included but the total size
            of the request entity should not exceed 1MB. This is
            typically sufficient for 10,000 phone numbers.
        ttl:
            How long, in seconds, the notification is valid. Can be an integer
            between 0 and 2,419,200, which is 4 weeks, the default and
            the maximum supported time to live (TTL). Delivery should be
            attempted if the device is offline until the TTL elapses.
            Zero means that the notification delivery is attempted
            immediately, only once, and is not stored for future
            delivery. SMS does not support this property.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services/{service_sid}/Notifications?](
    https://notify.twilio.com/v1/Services/{service_sid}/Notifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Notifications"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "action": action,
        "alexa": alexa,
        "apn": apn,
        "body": body,
        "data": data,
        "delivery_callback_url": delivery_callback_url,
        "facebook_messenger": facebook_messenger,
        "fcm": fcm,
        "gcm": gcm,
        "identity": identity,
        "priority": priority,
        "segment": segment,
        "sms": sms,
        "sound": sound,
        "tag": tag,
        "title": title,
        "to_binding": to_binding,
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
    [https://notify.twilio.com/v1/Services/{sid}?](
    https://notify.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{sid}"  # noqa
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
    [https://notify.twilio.com/v1/Services/{sid}?](
    https://notify.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{sid}"  # noqa
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
    alexa_skill_id: str = None,
    apn_credential_sid: str = None,
    default_alexa_notification_protocol_version: str = None,
    default_apn_notification_protocol_version: str = None,
    default_fcm_notification_protocol_version: str = None,
    default_gcm_notification_protocol_version: str = None,
    delivery_callback_enabled: bool = None,
    delivery_callback_url: str = None,
    facebook_messenger_page_id: str = None,
    fcm_credential_sid: str = None,
    friendly_name: str = None,
    gcm_credential_sid: str = None,
    log_enabled: bool = None,
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        alexa_skill_id:
            Deprecated.
        apn_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for APN Bindings.
        default_alexa_notification_protocol_version:
            Deprecated.
        default_apn_notification_protocol_version:
            The protocol version to use for sending APNS notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        default_fcm_notification_protocol_version:
            The protocol version to use for sending FCM notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        default_gcm_notification_protocol_version:
            The protocol version to use for sending GCM notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        delivery_callback_enabled:
            Callback configuration that enables delivery callbacks, default false.
        delivery_callback_url:
            URL to send delivery status callback.
        facebook_messenger_page_id:
            Deprecated.
        fcm_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for FCM Bindings.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        gcm_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for GCM Bindings.
        log_enabled:
            Whether to log notifications. Can be: `true` or `false` and the default
            is `true`.
        messaging_service_sid:
            The SID of the [Messaging Service](https://www.twilio.com/docs/sms/send-
            messages
            messaging-services) to use for SMS Bindings. This parameter
            must be set in order to send SMS notifications.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services/{sid}?](
    https://notify.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "alexa_skill_id": alexa_skill_id,
        "apn_credential_sid": apn_credential_sid,
        "default_alexa_notification_protocol_version": default_alexa_notification_protocol_version,  # noqa
        "default_apn_notification_protocol_version": default_apn_notification_protocol_version,  # noqa
        "default_fcm_notification_protocol_version": default_fcm_notification_protocol_version,  # noqa
        "default_gcm_notification_protocol_version": default_gcm_notification_protocol_version,  # noqa
        "delivery_callback_enabled": delivery_callback_enabled,
        "delivery_callback_url": delivery_callback_url,
        "facebook_messenger_page_id": facebook_messenger_page_id,
        "fcm_credential_sid": fcm_credential_sid,
        "friendly_name": friendly_name,
        "gcm_credential_sid": gcm_credential_sid,
        "log_enabled": log_enabled,
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
