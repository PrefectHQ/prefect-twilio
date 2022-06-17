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


@task
async def get_v1_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a frontline user.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://frontline-api.twilio.com/v1/Users/{sid}?](
    https://frontline-api.twilio.com/v1/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://frontline-api.twilio.com/v1/Users/{sid}"  # noqa
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
    avatar: str = None,
    friendly_name: str = None,
    is_available: bool = None,
    state: str = None,
) -> Dict[str, Any]:
    """
    Update an existing frontline user.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        avatar:
            The avatar URL which will be shown in Frontline application.
        friendly_name:
            The string that you assigned to describe the User.
        is_available:
            Whether the User is available for new conversations. Set to `false` to
            prevent User from receiving new inbound conversations if you
            are using [Pool
            Routing](https://www.twilio.com/docs/frontline/handle-
            incoming-conversations
            3-pool-routing).
        state:
            Current state of this user. Can be either `active` or `deactivated`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://frontline-api.twilio.com/v1/Users/{sid}?](
    https://frontline-api.twilio.com/v1/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://frontline-api.twilio.com/v1/Users/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "avatar": avatar,
        "friendly_name": friendly_name,
        "is_available": is_available,
        "state": state,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
