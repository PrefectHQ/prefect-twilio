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
async def get_v1_conversations(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of conversations in your account's default service.

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
    [https://conversations.twilio.com/v1/Conversations?&page_size=%s](
    https://conversations.twilio.com/v1/Conversations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Conversations"  # noqa

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
async def post_v1_conversations(
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    messaging_service_sid: str = None,
    state: str = None,
    timers_closed: str = None,
    timers_inactive: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new conversation in your account's default service.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        friendly_name:
            The human-readable name of this conversation, limited to 256 characters.
            Optional.
        messaging_service_sid:
            The unique ID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) this
            conversation belongs to.
        state:
            Current state of this conversation. Can be either `active`, `inactive`
            or `closed` and defaults to `active`.
        timers_closed:
            ISO8601 duration when conversation will be switched to `closed` state.
            Minimum value for this timer is 10 minutes.
        timers_inactive:
            ISO8601 duration when conversation will be switched to `inactive` state.
            Minimum value for this timer is 1 minute.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Conversations?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Conversations"  # noqa

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
        "friendly_name": friendly_name,
        "messaging_service_sid": messaging_service_sid,
        "state": state,
        "timers_closed": timers_closed,
        "timers_inactive": timers_inactive,
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
async def get_v1_conversations_conversation_sid_messages(
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all messages in the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            The sort order of the returned messages. Can be: `asc` (ascending) or
            `desc` (descending), with `asc` as the default.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages?&order=%s&page_size=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages"  # noqa
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
async def post_v1_conversations_conversation_sid_messages(
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    author: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
    media_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new message to the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A string metadata field you can use to store any data you wish. The
            string value must contain structurally valid JSON if
            specified.  **Note** that if the attributes are not set "{}"
            will be returned.
        author:
            The channel specific identifier of the message's author. Defaults to
            `system`.
        body:
            The content of the message, can be up to 1,600 characters long.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated. `null` if the message has
            not been edited.
        media_sid:
            The Media SID to be attached to the new Message.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "author": author,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
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
async def get_v1_conversations_conversation_sid_messages_message_sid_receipts(  # noqa
    conversation_sid: str,
    message_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all delivery and read receipts of the conversation message.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        message_sid:
            Message sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts?&page_size=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts"  # noqa
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
async def get_v1_conversations_conversation_sid_messages_message_sid_receipts_sid(  # noqa
    conversation_sid: str,
    message_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the delivery and read receipts of the conversation message.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        message_sid:
            Message sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}?](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}"  # noqa
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
async def delete_v1_conversations_conversation_sid_messages_sid(
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a message from the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
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
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{sid}"  # noqa
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
async def get_v1_conversations_conversation_sid_messages_sid(
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a message from the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{sid}?](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{sid}"  # noqa
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
async def post_v1_conversations_conversation_sid_messages_sid(
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    author: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
) -> Dict[str, Any]:
    """
    Update an existing message in the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A string metadata field you can use to store any data you wish. The
            string value must contain structurally valid JSON if
            specified.  **Note** that if the attributes are not set "{}"
            will be returned.
        author:
            The channel specific identifier of the message's author. Defaults to
            `system`.
        body:
            The content of the message, can be up to 1,600 characters long.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated. `null` if the message has
            not been edited.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Messages/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "author": author,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
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
async def get_v1_conversations_conversation_sid_participants(
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all participants of the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants?&page_size=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants"  # noqa
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
async def post_v1_conversations_conversation_sid_participants(
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    identity: str = None,
    messaging_binding_address: str = None,
    messaging_binding_projected_address: str = None,
    messaging_binding_proxy_address: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new participant to the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversations SDK to communicate.
            Limited to 256 characters.
        messaging_binding_address:
            The address of the participant's device, e.g. a phone or WhatsApp
            number. Together with the Proxy address, this determines a
            participant uniquely. This field (with proxy_address) is
            only null when the participant is interacting from an SDK
            endpoint (see the 'identity' field).
        messaging_binding_projected_address:
            The address of the Twilio phone number that is used in Group MMS.
            Communication mask for the Conversation participant with
            Identity.
        messaging_binding_proxy_address:
            The address of the Twilio phone number (or WhatsApp number) that the
            participant is in contact with. This field, together with
            participant address, is only null when the participant is
            interacting from an SDK endpoint (see the 'identity' field).
        role_sid:
            The SID of a conversation-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the participant.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants"  # noqa
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
        "messaging_binding_address": messaging_binding_address,
        "messaging_binding_projected_address": messaging_binding_projected_address,
        "messaging_binding_proxy_address": messaging_binding_proxy_address,
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
async def delete_v1_conversations_conversation_sid_participants_sid(
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a participant from the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
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
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants/{sid}"  # noqa
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
async def get_v1_conversations_conversation_sid_participants_sid(
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a participant of the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants/{sid}?](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants/{sid}"  # noqa
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
async def post_v1_conversations_conversation_sid_participants_sid(
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    identity: str = None,
    last_read_message_index: int = None,
    last_read_timestamp: str = None,
    messaging_binding_projected_address: str = None,
    messaging_binding_proxy_address: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Update an existing participant in the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversations SDK to communicate.
            Limited to 256 characters.
        last_read_message_index:
            Index of last “read” message in the
            [Conversation](https://www.twilio.com/docs/conversations/api/conversation-
            resource) for the Participant.
        last_read_timestamp:
            Timestamp of last “read” message in the
            [Conversation](https://www.twilio.com/docs/conversations/api/conversation-
            resource) for the Participant.
        messaging_binding_projected_address:
            The address of the Twilio phone number that is used in Group MMS. 'null'
            value will remove it.
        messaging_binding_proxy_address:
            The address of the Twilio phone number that the participant is in
            contact with. 'null' value will remove it.
        role_sid:
            The SID of a conversation-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the participant.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Participants/{sid}"  # noqa
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
        "identity": identity,
        "last_read_message_index": last_read_message_index,
        "last_read_timestamp": last_read_timestamp,
        "messaging_binding_projected_address": messaging_binding_projected_address,
        "messaging_binding_proxy_address": messaging_binding_proxy_address,
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
async def get_v1_conversations_conversation_sid_webhooks(
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all webhooks scoped to the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks?&page_size=%s](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks"  # noqa
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
async def post_v1_conversations_conversation_sid_webhooks(
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_replay_after: int = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
    target: str = None,
) -> Dict[str, Any]:
    """
    Create a new webhook scoped to the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:
            The list of events, firing webhook event for this Conversation.
        configuration_flow_sid:
            The studio flow SID, where the webhook should be sent to.
        configuration_method:
            The HTTP method to be used when sending a webhook request.
        configuration_replay_after:
            The message index for which and it's successors the webhook will be
            replayed. Not set by default.
        configuration_triggers:
            The list of keywords, firing webhook event for this Conversation.
        configuration_url:
            The absolute url the webhook request should be sent to.
        target:
            The target of this webhook: `webhook`, `studio`, `trigger`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks?](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_replay_after": configuration_replay_after,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
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
async def delete_v1_conversations_conversation_sid_webhooks_sid(
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an existing webhook scoped to the conversation.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks/{sid}?](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks/{sid}"  # noqa
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
async def get_v1_conversations_conversation_sid_webhooks_sid(
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the configuration of a conversation-scoped webhook.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks/{sid}?](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks/{sid}"  # noqa
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
async def post_v1_conversations_conversation_sid_webhooks_sid(
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
) -> Dict[str, Any]:
    """
    Update an existing conversation-scoped webhook.

    Args:
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:
            The list of events, firing webhook event for this Conversation.
        configuration_flow_sid:
            The studio flow SID, where the webhook should be sent to.
        configuration_method:
            The HTTP method to be used when sending a webhook request.
        configuration_triggers:
            The list of keywords, firing webhook event for this Conversation.
        configuration_url:
            The absolute url the webhook request should be sent to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks/{sid}?](
    https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{conversation_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
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
async def delete_v1_conversations_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a conversation from your account's default service.

    Args:
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
    [https://conversations.twilio.com/v1/Conversations/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Conversations/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{sid}"  # noqa
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
async def get_v1_conversations_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a conversation from your account's default service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{sid}?](
    https://conversations.twilio.com/v1/Conversations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{sid}"  # noqa
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
async def post_v1_conversations_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    messaging_service_sid: str = None,
    state: str = None,
    timers_closed: str = None,
    timers_inactive: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Update an existing conversation in your account's default service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        friendly_name:
            The human-readable name of this conversation, limited to 256 characters.
            Optional.
        messaging_service_sid:
            The unique ID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) this
            conversation belongs to.
        state:
            Current state of this conversation. Can be either `active`, `inactive`
            or `closed` and defaults to `active`.
        timers_closed:
            ISO8601 duration when conversation will be switched to `closed` state.
            Minimum value for this timer is 10 minutes.
        timers_inactive:
            ISO8601 duration when conversation will be switched to `inactive` state.
            Minimum value for this timer is 1 minute.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Conversations/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Conversations/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Conversations/{sid}"  # noqa
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
        "friendly_name": friendly_name,
        "messaging_service_sid": messaging_service_sid,
        "state": state,
        "timers_closed": timers_closed,
        "timers_inactive": timers_inactive,
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
async def get_v1_credentials(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all push notification credentials on your account.

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
    [https://conversations.twilio.com/v1/Credentials?&page_size=%s](
    https://conversations.twilio.com/v1/Credentials?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Credentials"  # noqa

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
    Add a new push notification credential to your account.

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
            `fcm`, `gcm`, or `apn`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Credentials?](
    https://conversations.twilio.com/v1/Credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Credentials"  # noqa

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
    Remove a push notification credential from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Credentials/{sid}?](
    https://conversations.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Credentials/{sid}"  # noqa
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
    Fetch a push notification credential from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Credentials/{sid}?](
    https://conversations.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Credentials/{sid}"  # noqa
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
    type: str = None,
) -> Dict[str, Any]:
    """
    Update an existing push notification credential on your account.

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
            `fcm`, `gcm`, or `apn`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Credentials/{sid}?](
    https://conversations.twilio.com/v1/Credentials/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Credentials/{sid}"  # noqa
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
async def get_v1_participant_conversations(
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    address: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Conversations that this Participant belongs to by
    identity or by address. Only one parameter should be specified.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversations SDK to communicate.
            Limited to 256 characters.
        address:
            A unique string identifier for the conversation participant who's not a
            Conversation User. This parameter could be found in
            messaging_binding.address field of Participant resource. It
            should be url-encoded.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/ParticipantConversations?&identity=%s&address=%s&page_size=%s](
    https://conversations.twilio.com/v1/ParticipantConversations?&identity=%s&address=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/ParticipantConversations"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
        "address": address,
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
async def get_v1_roles(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all user roles in your account's default service.

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
    [https://conversations.twilio.com/v1/Roles?&page_size=%s](
    https://conversations.twilio.com/v1/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Roles"  # noqa

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
async def post_v1_roles(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    permission: list = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Create a new user role in your account's default service.

    Args:
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
            The type of role. Can be: `conversation` for
            [Conversation](https://www.twilio.com/docs/conversations/api/conversation-
            resource) roles or `service` for [Conversation
            Service](https://www.twilio.com/docs/conversations/api/service-
            resource) roles.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Roles?](
    https://conversations.twilio.com/v1/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Roles"  # noqa

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
async def delete_v1_roles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove a user role from your account's default service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Roles/{sid}?](
    https://conversations.twilio.com/v1/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Roles/{sid}"  # noqa
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
async def get_v1_roles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a user role from your account's default service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Roles/{sid}?](
    https://conversations.twilio.com/v1/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Roles/{sid}"  # noqa
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
async def post_v1_roles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    permission: list = None,
) -> Dict[str, Any]:
    """
    Update an existing user role in your account's default service.

    Args:
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
    [https://conversations.twilio.com/v1/Roles/{sid}?](
    https://conversations.twilio.com/v1/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Roles/{sid}"  # noqa
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
async def get_v1_services(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all conversation services on your account.

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
    [https://conversations.twilio.com/v1/Services?&page_size=%s](
    https://conversations.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Services"  # noqa

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
    Create a new conversation service on your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The human-readable name of this service, limited to 256 characters.
            Optional.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services?](
    https://conversations.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Services"  # noqa

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
async def get_v1_services_chat_service_sid_bindings(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    binding_type: list = None,
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all push notification bindings in the conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_type:
            The push technology used by the Binding resources to read.  Can be:
            `apn`, `gcm`, or `fcm`.  See [push notification
            configuration](https://www.twilio.com/docs/chat/push-
            notification-configuration) for more info.
        identity:
            The identity of a [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource) this binding belongs to. See [access
            tokens](https://www.twilio.com/docs/conversations/create-
            tokens) for more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings"  # noqa
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
async def delete_v1_services_chat_service_sid_bindings_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove a push notification binding from the conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_bindings_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a push notification binding from the conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_configuration(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the configuration of a conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration"  # noqa
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
async def post_v1_services_chat_service_sid_configuration(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    default_chat_service_role_sid: str = None,
    default_conversation_creator_role_sid: str = None,
    default_conversation_role_sid: str = None,
    reachability_enabled: bool = None,
) -> Dict[str, Any]:
    """
    Update configuration settings of a conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        default_chat_service_role_sid:
            The service-level role assigned to users when they are added to the
            service. See the [Conversation
            Role](https://www.twilio.com/docs/conversations/api/role-
            resource) for more info about roles.
        default_conversation_creator_role_sid:
            The conversation-level role assigned to a conversation creator when they
            join a new conversation. See the [Conversation
            Role](https://www.twilio.com/docs/conversations/api/role-
            resource) for more info about roles.
        default_conversation_role_sid:
            The conversation-level role assigned to users when they are added to a
            conversation. See the [Conversation
            Role](https://www.twilio.com/docs/conversations/api/role-
            resource) for more info about roles.
        reachability_enabled:
            Whether the [Reachability
            Indicator](https://www.twilio.com/docs/chat/reachability-
            indicator) is enabled for this Conversations Service. The
            default is `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "default_chat_service_role_sid": default_chat_service_role_sid,
        "default_conversation_creator_role_sid": default_conversation_creator_role_sid,  # noqa
        "default_conversation_role_sid": default_conversation_role_sid,
        "reachability_enabled": reachability_enabled,
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
async def get_v1_services_chat_service_sid_configuration_notifications(  # noqa
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch push notification service settings.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications"  # noqa
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
async def post_v1_services_chat_service_sid_configuration_notifications(  # noqa
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    added_to_conversation_enabled: bool = None,
    added_to_conversation_sound: str = None,
    added_to_conversation_template: str = None,
    log_enabled: bool = None,
    new_message_badge_count_enabled: bool = None,
    new_message_enabled: bool = None,
    new_message_sound: str = None,
    new_message_template: str = None,
    new_message_with_media_enabled: bool = None,
    new_message_with_media_template: str = None,
    removed_from_conversation_enabled: bool = None,
    removed_from_conversation_sound: str = None,
    removed_from_conversation_template: str = None,
) -> Dict[str, Any]:
    """
    Update push notification service settings.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        added_to_conversation_enabled:
            Whether to send a notification when a participant is added to a
            conversation. The default is `false`.
        added_to_conversation_sound:
            The name of the sound to play when a participant is added to a
            conversation and `added_to_conversation.enabled` is `true`.
        added_to_conversation_template:
            The template to use to create the notification text displayed when a
            participant is added to a conversation and
            `added_to_conversation.enabled` is `true`.
        log_enabled:
            Weather the notification logging is enabled.
        new_message_badge_count_enabled:
            Whether the new message badge is enabled. The default is `false`.
        new_message_enabled:
            Whether to send a notification when a new message is added to a
            conversation. The default is `false`.
        new_message_sound:
            The name of the sound to play when a new message is added to a
            conversation and `new_message.enabled` is `true`.
        new_message_template:
            The template to use to create the notification text displayed when a new
            message is added to a conversation and `new_message.enabled`
            is `true`.
        new_message_with_media_enabled:
            Whether to send a notification when a new message with media/file
            attachments is added to a conversation. The default is
            `false`.
        new_message_with_media_template:
            The template to use to create the notification text displayed when a new
            message with media/file attachments is added to a
            conversation and `new_message.attachments.enabled` is
            `true`.
        removed_from_conversation_enabled:
            Whether to send a notification to a user when they are removed from a
            conversation. The default is `false`.
        removed_from_conversation_sound:
            The name of the sound to play to a user when they are removed from a
            conversation and `removed_from_conversation.enabled` is
            `true`.
        removed_from_conversation_template:
            The template to use to create the notification text displayed to a user
            when they are removed from a conversation and
            `removed_from_conversation.enabled` is `true`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "added_to_conversation_enabled": added_to_conversation_enabled,
        "added_to_conversation_sound": added_to_conversation_sound,
        "added_to_conversation_template": added_to_conversation_template,
        "log_enabled": log_enabled,
        "new_message_badge_count_enabled": new_message_badge_count_enabled,
        "new_message_enabled": new_message_enabled,
        "new_message_sound": new_message_sound,
        "new_message_template": new_message_template,
        "new_message_with_media_enabled": new_message_with_media_enabled,
        "new_message_with_media_template": new_message_with_media_template,
        "removed_from_conversation_enabled": removed_from_conversation_enabled,
        "removed_from_conversation_sound": removed_from_conversation_sound,
        "removed_from_conversation_template": removed_from_conversation_template,
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
async def get_v1_services_chat_service_sid_configuration_webhooks(  # noqa
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific service webhook configuration.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks"  # noqa
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
async def post_v1_services_chat_service_sid_configuration_webhooks(  # noqa
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    filters: list = None,
    method: str = None,
    post_webhook_url: str = None,
    pre_webhook_url: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Webhook.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        filters:
            The list of events that your configured webhook targets will receive.
            Events not configured here will not fire. Possible values
            are `onParticipantAdd`, `onParticipantAdded`,
            `onDeliveryUpdated`, `onConversationUpdated`,
            `onConversationRemove`, `onParticipantRemove`,
            `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`,
            `onParticipantUpdated`, `onConversationAdded`,
            `onMessageAdded`, `onConversationAdd`,
            `onConversationRemoved`, `onParticipantUpdate`,
            `onMessageRemove`, `onMessageUpdated`,
            `onParticipantRemoved`, `onMessageUpdate` or
            `onConversationStateUpdated`.
        method:
            The HTTP method to be used when sending a webhook request. One of `GET`
            or `POST`.
        post_webhook_url:
            The absolute url the post-event webhook request should be sent to.
        pre_webhook_url:
            The absolute url the pre-event webhook request should be sent to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "filters": filters,
        "method": method,
        "post_webhook_url": post_webhook_url,
        "pre_webhook_url": pre_webhook_url,
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
async def get_v1_services_chat_service_sid_conversations(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of conversations in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations"  # noqa
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
async def post_v1_services_chat_service_sid_conversations(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    messaging_service_sid: str = None,
    state: str = None,
    timers_closed: str = None,
    timers_inactive: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new conversation in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        friendly_name:
            The human-readable name of this conversation, limited to 256 characters.
            Optional.
        messaging_service_sid:
            The unique ID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) this
            conversation belongs to.
        state:
            Current state of this conversation. Can be either `active`, `inactive`
            or `closed` and defaults to `active`.
        timers_closed:
            ISO8601 duration when conversation will be switched to `closed` state.
            Minimum value for this timer is 10 minutes.
        timers_inactive:
            ISO8601 duration when conversation will be switched to `inactive` state.
            Minimum value for this timer is 1 minute.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations"  # noqa
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
        "friendly_name": friendly_name,
        "messaging_service_sid": messaging_service_sid,
        "state": state,
        "timers_closed": timers_closed,
        "timers_inactive": timers_inactive,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_messages(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all messages in the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            The sort order of the returned messages. Can be: `asc` (ascending) or
            `desc` (descending), with `asc` as the default.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages?&order=%s&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_messages(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    author: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
    media_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new message to the conversation in a specific service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A string metadata field you can use to store any data you wish. The
            string value must contain structurally valid JSON if
            specified.  **Note** that if the attributes are not set "{}"
            will be returned.
        author:
            The channel specific identifier of the message's author. Defaults to
            `system`.
        body:
            The content of the message, can be up to 1,600 characters long.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated. `null` if the message has
            not been edited.
        media_sid:
            The Media SID to be attached to the new Message.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "author": author,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_messages_message_sid_receipts(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    message_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all delivery and read receipts of the conversation message.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        message_sid:
            Message sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts"  # noqa
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_messages_message_sid_receipts_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    message_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the delivery and read receipts of the conversation message.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        message_sid:
            Message sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}"  # noqa
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
async def delete_v1_services_chat_service_sid_conversations_conversation_sid_messages_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a message from the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
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
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_messages_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a message from the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_messages_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    author: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
) -> Dict[str, Any]:
    """
    Update an existing message in the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A string metadata field you can use to store any data you wish. The
            string value must contain structurally valid JSON if
            specified.  **Note** that if the attributes are not set "{}"
            will be returned.
        author:
            The channel specific identifier of the message's author. Defaults to
            `system`.
        body:
            The content of the message, can be up to 1,600 characters long.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated. `null` if the message has
            not been edited.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "author": author,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_participants(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all participants of the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_participants(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    identity: str = None,
    messaging_binding_address: str = None,
    messaging_binding_projected_address: str = None,
    messaging_binding_proxy_address: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new participant to the conversation in a specific service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversation SDK to communicate.
            Limited to 256 characters.
        messaging_binding_address:
            The address of the participant's device, e.g. a phone or WhatsApp
            number. Together with the Proxy address, this determines a
            participant uniquely. This field (with proxy_address) is
            only null when the participant is interacting from an SDK
            endpoint (see the 'identity' field).
        messaging_binding_projected_address:
            The address of the Twilio phone number that is used in Group MMS.
            Communication mask for the Conversation participant with
            Identity.
        messaging_binding_proxy_address:
            The address of the Twilio phone number (or WhatsApp number) that the
            participant is in contact with. This field, together with
            participant address, is only null when the participant is
            interacting from an SDK endpoint (see the 'identity' field).
        role_sid:
            The SID of a conversation-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the participant.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants"  # noqa
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
        "messaging_binding_address": messaging_binding_address,
        "messaging_binding_projected_address": messaging_binding_projected_address,
        "messaging_binding_proxy_address": messaging_binding_proxy_address,
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
async def delete_v1_services_chat_service_sid_conversations_conversation_sid_participants_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a participant from the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
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
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_participants_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a participant of the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_participants_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    identity: str = None,
    last_read_message_index: int = None,
    last_read_timestamp: str = None,
    messaging_binding_projected_address: str = None,
    messaging_binding_proxy_address: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Update an existing participant in the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversation SDK to communicate.
            Limited to 256 characters.
        last_read_message_index:
            Index of last “read” message in the
            [Conversation](https://www.twilio.com/docs/conversations/api/conversation-
            resource) for the Participant.
        last_read_timestamp:
            Timestamp of last “read” message in the
            [Conversation](https://www.twilio.com/docs/conversations/api/conversation-
            resource) for the Participant.
        messaging_binding_projected_address:
            The address of the Twilio phone number that is used in Group MMS. 'null'
            value will remove it.
        messaging_binding_proxy_address:
            The address of the Twilio phone number that the participant is in
            contact with. 'null' value will remove it.
        role_sid:
            The SID of a conversation-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the participant.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}"  # noqa
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
        "identity": identity,
        "last_read_message_index": last_read_message_index,
        "last_read_timestamp": last_read_timestamp,
        "messaging_binding_projected_address": messaging_binding_projected_address,
        "messaging_binding_proxy_address": messaging_binding_proxy_address,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_webhooks(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all webhooks scoped to the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_webhooks(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_replay_after: int = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
    target: str = None,
) -> Dict[str, Any]:
    """
    Create a new webhook scoped to the conversation in a specific service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:
            The list of events, firing webhook event for this Conversation.
        configuration_flow_sid:
            The studio flow SID, where the webhook should be sent to.
        configuration_method:
            The HTTP method to be used when sending a webhook request.
        configuration_replay_after:
            The message index for which and it's successors the webhook will be
            replayed. Not set by default.
        configuration_triggers:
            The list of keywords, firing webhook event for this Conversation.
        configuration_url:
            The absolute url the webhook request should be sent to.
        target:
            The target of this webhook: `webhook`, `studio`, `trigger`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_replay_after": configuration_replay_after,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
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
async def delete_v1_services_chat_service_sid_conversations_conversation_sid_webhooks_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an existing webhook scoped to the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_webhooks_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the configuration of a conversation-scoped webhook.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_webhooks_sid(  # noqa
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
) -> Dict[str, Any]:
    """
    Update an existing conversation-scoped webhook.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:
            The list of events, firing webhook event for this Conversation.
        configuration_flow_sid:
            The studio flow SID, where the webhook should be sent to.
        configuration_method:
            The HTTP method to be used when sending a webhook request.
        configuration_triggers:
            The list of keywords, firing webhook event for this Conversation.
        configuration_url:
            The absolute url the webhook request should be sent to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
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
async def delete_v1_services_chat_service_sid_conversations_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a conversation from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
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
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_conversations_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a conversation from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    messaging_service_sid: str = None,
    state: str = None,
    timers_closed: str = None,
    timers_inactive: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Update an existing conversation in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        friendly_name:
            The human-readable name of this conversation, limited to 256 characters.
            Optional.
        messaging_service_sid:
            The unique ID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) this
            conversation belongs to.
        state:
            Current state of this conversation. Can be either `active`, `inactive`
            or `closed` and defaults to `active`.
        timers_closed:
            ISO8601 duration when conversation will be switched to `closed` state.
            Minimum value for this timer is 10 minutes.
        timers_inactive:
            ISO8601 duration when conversation will be switched to `inactive` state.
            Minimum value for this timer is 1 minute.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}"  # noqa
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
        "friendly_name": friendly_name,
        "messaging_service_sid": messaging_service_sid,
        "state": state,
        "timers_closed": timers_closed,
        "timers_inactive": timers_inactive,
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
async def get_v1_services_chat_service_sid_participant_conversations(  # noqa
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    address: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Conversations that this Participant belongs to by
    identity or by address. Only one parameter should be specified.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversations SDK to communicate.
            Limited to 256 characters.
        address:
            A unique string identifier for the conversation participant who's not a
            Conversation User. This parameter could be found in
            messaging_binding.address field of Participant resource. It
            should be url-encoded.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/ParticipantConversations?&identity=%s&address=%s&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/ParticipantConversations?&identity=%s&address=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/ParticipantConversations"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
        "address": address,
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
async def get_v1_services_chat_service_sid_roles(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all user roles in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles"  # noqa
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
async def post_v1_services_chat_service_sid_roles(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    permission: list = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Create a new user role in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
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
            The type of role. Can be: `conversation` for
            [Conversation](https://www.twilio.com/docs/conversations/api/conversation-
            resource) roles or `service` for [Conversation
            Service](https://www.twilio.com/docs/conversations/api/service-
            resource) roles.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles"  # noqa
    )
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
async def delete_v1_services_chat_service_sid_roles_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove a user role from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_roles_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a user role from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_roles_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    permission: list = None,
) -> Dict[str, Any]:
    """
    Update an existing user role in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
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
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_users(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all conversation users in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users"  # noqa
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
async def post_v1_services_chat_service_sid_users(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new conversation user to your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            The JSON Object string that stores application-specific data. If
            attributes have not been set, `{}` is returned.
        friendly_name:
            The string that you assigned to describe the resource.
        identity:
            The application-defined string that uniquely identifies the resource's
            User within the [Conversation
            Service](https://www.twilio.com/docs/conversations/api/service-
            resource). This value is often a username or an email
            address, and is case-sensitive.
        role_sid:
            The SID of a service-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the user.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users"  # noqa
    )
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
async def delete_v1_services_chat_service_sid_users_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a conversation user from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
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
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_users_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a conversation user from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_users_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Update an existing conversation user in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            The JSON Object string that stores application-specific data. If
            attributes have not been set, `{}` is returned.
        friendly_name:
            The string that you assigned to describe the resource.
        role_sid:
            The SID of a service-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the user.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_users_user_sid_conversations(  # noqa
    chat_service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all User Conversations for the User.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
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
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations"  # noqa
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
async def delete_v1_services_chat_service_sid_users_user_sid_conversations_conversation_sid(  # noqa
    chat_service_sid: str,
    user_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific User Conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}"  # noqa
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
async def get_v1_services_chat_service_sid_users_user_sid_conversations_conversation_sid(  # noqa
    chat_service_sid: str,
    user_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific User Conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}"  # noqa
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
async def post_v1_services_chat_service_sid_users_user_sid_conversations_conversation_sid(  # noqa
    chat_service_sid: str,
    user_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    last_read_message_index: int = None,
    last_read_timestamp: str = None,
    notification_level: str = None,
) -> Dict[str, Any]:
    """
    Update a specific User Conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        last_read_message_index:
            The index of the last Message in the Conversation that the Participant
            has read.
        last_read_timestamp:
            The date of the last message read in conversation by the user, given in
            ISO 8601 format.
        notification_level:
            The Notification Level of this User Conversation. One of `default` or
            `muted`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "last_read_message_index": last_read_message_index,
        "last_read_timestamp": last_read_timestamp,
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
async def delete_v1_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove a conversation service with all its nested resources from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{sid}?](
    https://conversations.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{sid}"  # noqa
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
    Fetch a conversation service from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{sid}?](
    https://conversations.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{sid}"  # noqa
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
async def get_v1_users(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all conversation users in your account's default service.

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
    [https://conversations.twilio.com/v1/Users?&page_size=%s](
    https://conversations.twilio.com/v1/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Users"  # noqa

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
async def post_v1_users(
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new conversation user to your account's default service.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            The JSON Object string that stores application-specific data. If
            attributes have not been set, `{}` is returned.
        friendly_name:
            The string that you assigned to describe the resource.
        identity:
            The application-defined string that uniquely identifies the resource's
            User within the [Conversation
            Service](https://www.twilio.com/docs/conversations/api/service-
            resource). This value is often a username or an email
            address, and is case-sensitive.
        role_sid:
            The SID of a service-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the user.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Users?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Users?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Users"  # noqa

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
async def delete_v1_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a conversation user from your account's default service.

    Args:
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
    [https://conversations.twilio.com/v1/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Users/{sid}"  # noqa
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
async def get_v1_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a conversation user from your account's default service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Users/{sid}?](
    https://conversations.twilio.com/v1/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Users/{sid}"  # noqa
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
async def post_v1_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Update an existing conversation user in your account's default service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            The JSON Object string that stores application-specific data. If
            attributes have not been set, `{}` is returned.
        friendly_name:
            The string that you assigned to describe the resource.
        role_sid:
            The SID of a service-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the user.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Users/{sid}"  # noqa
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
async def get_v1_users_user_sid_conversations(
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all User Conversations for the User.

    Args:
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
    [https://conversations.twilio.com/v1/Users/{user_sid}/Conversations?&page_size=%s](
    https://conversations.twilio.com/v1/Users/{user_sid}/Conversations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Users/{user_sid}/Conversations"  # noqa
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
async def delete_v1_users_user_sid_conversations_conversation_sid(
    user_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific User Conversation.

    Args:
        user_sid:
            User sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Users/{user_sid}/Conversations/{conversation_sid}?](
    https://conversations.twilio.com/v1/Users/{user_sid}/Conversations/{conversation_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Users/{user_sid}/Conversations/{conversation_sid}"  # noqa
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
async def get_v1_users_user_sid_conversations_conversation_sid(
    user_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific User Conversation.

    Args:
        user_sid:
            User sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Users/{user_sid}/Conversations/{conversation_sid}?](
    https://conversations.twilio.com/v1/Users/{user_sid}/Conversations/{conversation_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Users/{user_sid}/Conversations/{conversation_sid}"  # noqa
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
async def post_v1_users_user_sid_conversations_conversation_sid(
    user_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    last_read_message_index: int = None,
    last_read_timestamp: str = None,
    notification_level: str = None,
) -> Dict[str, Any]:
    """
    Update a specific User Conversation.

    Args:
        user_sid:
            User sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        last_read_message_index:
            The index of the last Message in the Conversation that the Participant
            has read.
        last_read_timestamp:
            The date of the last message read in conversation by the user, given in
            ISO 8601 format.
        notification_level:
            The Notification Level of this User Conversation. One of `default` or
            `muted`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Users/{user_sid}/Conversations/{conversation_sid}?](
    https://conversations.twilio.com/v1/Users/{user_sid}/Conversations/{conversation_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Users/{user_sid}/Conversations/{conversation_sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "last_read_message_index": last_read_message_index,
        "last_read_timestamp": last_read_timestamp,
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
