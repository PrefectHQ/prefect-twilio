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
async def get_v1_conversations_conversation_sid_messages_message_sid_receipts(
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
async def get_v1_conversations_conversation_sid_messages_message_sid_receipts_sid(
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
