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
async def get_v1_configuration(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the global configuration of conversations on your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Configuration?](
    https://conversations.twilio.com/v1/Configuration?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Configuration"  # noqa

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
async def post_v1_configuration(
    twilio_credentials: "TwilioCredentials",
    default_chat_service_sid: str = None,
    default_closed_timer: str = None,
    default_inactive_timer: str = None,
    default_messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """
    Update the global configuration of conversations on your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        default_chat_service_sid:
            The SID of the default [Conversation
            Service](https://www.twilio.com/docs/conversations/api/service-
            resource) to use when creating a conversation.
        default_closed_timer:
            Default ISO8601 duration when conversation will be switched to `closed`
            state. Minimum value for this timer is 10 minutes.
        default_inactive_timer:
            Default ISO8601 duration when conversation will be switched to
            `inactive` state. Minimum value for this timer is 1 minute.
        default_messaging_service_sid:
            The SID of the default [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) to
            use when creating a conversation.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Configuration?](
    https://conversations.twilio.com/v1/Configuration?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Configuration"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "default_chat_service_sid": default_chat_service_sid,
        "default_closed_timer": default_closed_timer,
        "default_inactive_timer": default_inactive_timer,
        "default_messaging_service_sid": default_messaging_service_sid,
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
async def get_v1_configuration_addresses(
    twilio_credentials: "TwilioCredentials",
    type: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of address configurations for an account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        type:
            Filter the address configurations by its type. This value can be one of:
            `whatsapp`, `sms`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Configuration/Addresses?&type=%s&page_size=%s](
    https://conversations.twilio.com/v1/Configuration/Addresses?&type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Configuration/Addresses"  # noqa

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
async def post_v1_configuration_addresses(
    twilio_credentials: "TwilioCredentials",
    address: str = None,
    auto_creation_conversation_service_sid: str = None,
    auto_creation_enabled: bool = None,
    auto_creation_studio_flow_sid: str = None,
    auto_creation_studio_retry_count: int = None,
    auto_creation_type: str = None,
    auto_creation_webhook_filters: list = None,
    auto_creation_webhook_method: str = None,
    auto_creation_webhook_url: str = None,
    friendly_name: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Create a new address configuration.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        address:
            The unique address to be configured. The address can be a whatsapp
            address or phone number.
        auto_creation_conversation_service_sid:
            Conversation Service for the auto-created conversation. If not set, the
            conversation is created in the default service.
        auto_creation_enabled:
            Enable/Disable auto-creating conversations for messages to this address.
        auto_creation_studio_flow_sid:
            For type `studio`, the studio flow SID where the webhook should be sent
            to.
        auto_creation_studio_retry_count:
            For type `studio`, number of times to retry the webhook request.
        auto_creation_type:
            Type of Auto Creation. Value can be one of `webhook`, `studio` or
            `default`.
        auto_creation_webhook_filters:
            The list of events, firing webhook event for this Conversation. Values
            can be any of the following: `onMessageAdded`,
            `onMessageUpdated`, `onMessageRemoved`,
            `onConversationUpdated`, `onConversationStateUpdated`,
            `onConversationRemoved`, `onParticipantAdded`,
            `onParticipantUpdated`, `onParticipantRemoved`,
            `onDeliveryUpdated`.
        auto_creation_webhook_method:
            For type `webhook`, the HTTP method to be used when sending a webhook
            request.
        auto_creation_webhook_url:
            For type `webhook`, the url for the webhook request.
        friendly_name:
            The human-readable name of this configuration, limited to 256
            characters. Optional.
        type:
            Type of Address. Value can be `whatsapp` or `sms`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Configuration/Addresses?](
    https://conversations.twilio.com/v1/Configuration/Addresses?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Configuration/Addresses"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "address": address,
        "auto_creation_conversation_service_sid": auto_creation_conversation_service_sid,  # noqa
        "auto_creation_enabled": auto_creation_enabled,
        "auto_creation_studio_flow_sid": auto_creation_studio_flow_sid,
        "auto_creation_studio_retry_count": auto_creation_studio_retry_count,
        "auto_creation_type": auto_creation_type,
        "auto_creation_webhook_filters": auto_creation_webhook_filters,
        "auto_creation_webhook_method": auto_creation_webhook_method,
        "auto_creation_webhook_url": auto_creation_webhook_url,
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
async def delete_v1_configuration_addresses_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an existing address configuration.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Configuration/Addresses/{sid}?](
    https://conversations.twilio.com/v1/Configuration/Addresses/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Configuration/Addresses/{sid}"  # noqa
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
async def get_v1_configuration_addresses_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an address configuration.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Configuration/Addresses/{sid}?](
    https://conversations.twilio.com/v1/Configuration/Addresses/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Configuration/Addresses/{sid}"  # noqa
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
async def post_v1_configuration_addresses_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    auto_creation_conversation_service_sid: str = None,
    auto_creation_enabled: bool = None,
    auto_creation_studio_flow_sid: str = None,
    auto_creation_studio_retry_count: int = None,
    auto_creation_type: str = None,
    auto_creation_webhook_filters: list = None,
    auto_creation_webhook_method: str = None,
    auto_creation_webhook_url: str = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update an existing address configuration.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auto_creation_conversation_service_sid:
            Conversation Service for the auto-created conversation. If not set, the
            conversation is created in the default service.
        auto_creation_enabled:
            Enable/Disable auto-creating conversations for messages to this address.
        auto_creation_studio_flow_sid:
            For type `studio`, the studio flow SID where the webhook should be sent
            to.
        auto_creation_studio_retry_count:
            For type `studio`, number of times to retry the webhook request.
        auto_creation_type:
            Type of Auto Creation. Value can be one of `webhook`, `studio` or
            `default`.
        auto_creation_webhook_filters:
            The list of events, firing webhook event for this Conversation. Values
            can be any of the following: `onMessageAdded`,
            `onMessageUpdated`, `onMessageRemoved`,
            `onConversationUpdated`, `onConversationStateUpdated`,
            `onConversationRemoved`, `onParticipantAdded`,
            `onParticipantUpdated`, `onParticipantRemoved`,
            `onDeliveryUpdated`.
        auto_creation_webhook_method:
            For type `webhook`, the HTTP method to be used when sending a webhook
            request.
        auto_creation_webhook_url:
            For type `webhook`, the url for the webhook request.
        friendly_name:
            The human-readable name of this configuration, limited to 256
            characters. Optional.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Configuration/Addresses/{sid}?](
    https://conversations.twilio.com/v1/Configuration/Addresses/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Configuration/Addresses/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "auto_creation_conversation_service_sid": auto_creation_conversation_service_sid,  # noqa
        "auto_creation_enabled": auto_creation_enabled,
        "auto_creation_studio_flow_sid": auto_creation_studio_flow_sid,
        "auto_creation_studio_retry_count": auto_creation_studio_retry_count,
        "auto_creation_type": auto_creation_type,
        "auto_creation_webhook_filters": auto_creation_webhook_filters,
        "auto_creation_webhook_method": auto_creation_webhook_method,
        "auto_creation_webhook_url": auto_creation_webhook_url,
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
async def get_v1_configuration_webhooks(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Configuration/Webhooks?](
    https://conversations.twilio.com/v1/Configuration/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Configuration/Webhooks"  # noqa

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
async def post_v1_configuration_webhooks(
    twilio_credentials: "TwilioCredentials",
    filters: list = None,
    method: str = None,
    post_webhook_url: str = None,
    pre_webhook_url: str = None,
    target: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        filters:
            The list of webhook event triggers that are enabled for this Service:
            `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`,
            `onConversationUpdated`, `onConversationRemoved`,
            `onParticipantAdded`, `onParticipantUpdated`,
            `onParticipantRemoved`.
        method:
            The HTTP method to be used when sending a webhook request.
        post_webhook_url:
            The absolute url the post-event webhook request should be sent to.
        pre_webhook_url:
            The absolute url the pre-event webhook request should be sent to.
        target:
            The routing target of the webhook.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Configuration/Webhooks?](
    https://conversations.twilio.com/v1/Configuration/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Configuration/Webhooks"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "filters": filters,
        "method": method,
        "post_webhook_url": post_webhook_url,
        "pre_webhook_url": pre_webhook_url,
        "target": target,
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
async def get_v1_configuration(
    twilio_credentials: "TwilioCredentials",
    ui_version: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ui_version:
            The Pinned UI version of the Configuration resource to fetch.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/Configuration?&ui_version=%s](
    https://flex-api.twilio.com/v1/Configuration?&ui_version=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://flex-api.twilio.com/v1/Configuration"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "ui_version": ui_version,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
