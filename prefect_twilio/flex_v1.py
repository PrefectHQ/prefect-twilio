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
async def get_v1_channels(
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
    [https://flex-api.twilio.com/v1/Channels?&page_size=%s](
    https://flex-api.twilio.com/v1/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://flex-api.twilio.com/v1/Channels"  # noqa

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
async def post_v1_channels(
    twilio_credentials: "TwilioCredentials",
    chat_friendly_name: str = None,
    chat_unique_name: str = None,
    chat_user_friendly_name: str = None,
    flex_flow_sid: str = None,
    identity: str = None,
    long_lived: bool = None,
    pre_engagement_data: str = None,
    target: str = None,
    task_attributes: str = None,
    task_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        chat_friendly_name:
            The chat channel's friendly name.
        chat_unique_name:
            The chat channel's unique name.
        chat_user_friendly_name:
            The chat participant's friendly name.
        flex_flow_sid:
            The SID of the Flex Flow.
        identity:
            The `identity` value that uniquely identifies the new resource's chat
            User.
        long_lived:
            Whether to create the channel as long-lived.
        pre_engagement_data:
            The pre-engagement data.
        target:
            The Target Contact Identity, for example the phone number of an SMS.
        task_attributes:
            The Task attributes to be added for the TaskRouter Task.
        task_sid:
            The SID of the TaskRouter Task. Only valid when integration type is
            `task`. `null` for integration types `studio` & `external`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/Channels?](
    https://flex-api.twilio.com/v1/Channels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://flex-api.twilio.com/v1/Channels"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "chat_friendly_name": chat_friendly_name,
        "chat_unique_name": chat_unique_name,
        "chat_user_friendly_name": chat_user_friendly_name,
        "flex_flow_sid": flex_flow_sid,
        "identity": identity,
        "long_lived": long_lived,
        "pre_engagement_data": pre_engagement_data,
        "target": target,
        "task_attributes": task_attributes,
        "task_sid": task_sid,
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
async def delete_v1_channels_sid(
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
    [https://flex-api.twilio.com/v1/Channels/{sid}?](
    https://flex-api.twilio.com/v1/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Channels/{sid}"  # noqa
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
async def get_v1_channels_sid(
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
    [https://flex-api.twilio.com/v1/Channels/{sid}?](
    https://flex-api.twilio.com/v1/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Channels/{sid}"  # noqa
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


@task
async def get_v1_flex_flows(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The `friendly_name` of the Flex Flow resources to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/FlexFlows?&friendly_name=%s&page_size=%s](
    https://flex-api.twilio.com/v1/FlexFlows?&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://flex-api.twilio.com/v1/FlexFlows"  # noqa

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
async def post_v1_flex_flows(
    twilio_credentials: "TwilioCredentials",
    channel_type: str = None,
    chat_service_sid: str = None,
    contact_identity: str = None,
    enabled: bool = None,
    friendly_name: str = None,
    integration_channel: str = None,
    integration_creation_on_message: bool = None,
    integration_flow_sid: str = None,
    integration_priority: int = None,
    integration_retry_count: int = None,
    integration_timeout: int = None,
    integration_url: str = None,
    integration_workflow_sid: str = None,
    integration_workspace_sid: str = None,
    integration_type: str = None,
    janitor_enabled: bool = None,
    long_lived: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        channel_type:
            The channel type. One of `web`, `facebook`, `sms`, `whatsapp`, `line` or
            `custom`. By default, Studio’s Send to Flex widget passes it
            on to the Task attributes for Tasks created based on this
            Flex Flow. The Task attributes will be used by the Flex UI
            to render the respective Task as appropriate (applying
            channel-specific design and length limits). If `channelType`
            is `facebook`, `whatsapp` or `line`, the Send to Flex widget
            should set the Task Channel to Programmable Chat.
        chat_service_sid:
            The SID of the chat service.
        contact_identity:
            The channel contact's Identity.
        enabled:
            Whether the new Flex Flow is enabled.
        friendly_name:
            A descriptive string that you create to describe the Flex Flow resource.
        integration_channel:
            The Task Channel SID (TCXXXX) or unique name (e.g., `sms`) to use for
            the Task that will be created. Applicable and required when
            `integrationType` is `task`. The default value is `default`.
        integration_creation_on_message:
            In the context of outbound messaging, defines whether to create a Task
            immediately (and therefore reserve the conversation to
            current agent), or delay Task creation until the customer
            sends the first response. Set to false to create
            immediately, true to delay Task creation. This setting is
            only applicable for outbound messaging.
        integration_flow_sid:
            The SID of the Studio Flow. Required when `integrationType` is `studio`.
        integration_priority:
            The Task priority of a new Task. The default priority is 0. Optional
            when `integrationType` is `task`, not applicable otherwise.
        integration_retry_count:
            The number of times to retry the Studio Flow or webhook in case of
            failure. Takes integer values from 0 to 3 with the default
            being 3. Optional when `integrationType` is `studio` or
            `external`, not applicable otherwise.
        integration_timeout:
            The Task timeout in seconds for a new Task. Default is 86,400 seconds
            (24 hours). Optional when `integrationType` is `task`, not
            applicable otherwise.
        integration_url:
            The URL of the external webhook. Required when `integrationType` is
            `external`.
        integration_workflow_sid:
            The Workflow SID for a new Task. Required when `integrationType` is
            `task`.
        integration_workspace_sid:
            The Workspace SID for a new Task. Required when `integrationType` is
            `task`.
        integration_type:
            The software that will handle inbound messages. [Integration
            Type](https://www.twilio.com/docs/flex/developer/messaging/manage-
            flows
            integration-types) can be: `studio`, `external`, or `task`.
        janitor_enabled:
            When enabled, the Messaging Channel Janitor will remove active Proxy
            sessions if the associated Task is deleted outside of the
            Flex UI. Defaults to `false`.
        long_lived:
            When enabled, Flex will keep the chat channel active so that it may be
            used for subsequent interactions with a contact identity.
            Defaults to `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/FlexFlows?](
    https://flex-api.twilio.com/v1/FlexFlows?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://flex-api.twilio.com/v1/FlexFlows"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "channel_type": channel_type,
        "chat_service_sid": chat_service_sid,
        "contact_identity": contact_identity,
        "enabled": enabled,
        "friendly_name": friendly_name,
        "integration_channel": integration_channel,
        "integration_creation_on_message": integration_creation_on_message,
        "integration_flow_sid": integration_flow_sid,
        "integration_priority": integration_priority,
        "integration_retry_count": integration_retry_count,
        "integration_timeout": integration_timeout,
        "integration_url": integration_url,
        "integration_workflow_sid": integration_workflow_sid,
        "integration_workspace_sid": integration_workspace_sid,
        "integration_type": integration_type,
        "janitor_enabled": janitor_enabled,
        "long_lived": long_lived,
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
async def delete_v1_flex_flows_sid(
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
    [https://flex-api.twilio.com/v1/FlexFlows/{sid}?](
    https://flex-api.twilio.com/v1/FlexFlows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/FlexFlows/{sid}"  # noqa
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
async def get_v1_flex_flows_sid(
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
    [https://flex-api.twilio.com/v1/FlexFlows/{sid}?](
    https://flex-api.twilio.com/v1/FlexFlows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/FlexFlows/{sid}"  # noqa
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
async def post_v1_flex_flows_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    channel_type: str = None,
    chat_service_sid: str = None,
    contact_identity: str = None,
    enabled: bool = None,
    friendly_name: str = None,
    integration_channel: str = None,
    integration_creation_on_message: bool = None,
    integration_flow_sid: str = None,
    integration_priority: int = None,
    integration_retry_count: int = None,
    integration_timeout: int = None,
    integration_url: str = None,
    integration_workflow_sid: str = None,
    integration_workspace_sid: str = None,
    integration_type: str = None,
    janitor_enabled: bool = None,
    long_lived: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        channel_type:
            The channel type. One of `web`, `facebook`, `sms`, `whatsapp`, `line` or
            `custom`. By default, Studio’s Send to Flex widget passes it
            on to the Task attributes for Tasks created based on this
            Flex Flow. The Task attributes will be used by the Flex UI
            to render the respective Task as appropriate (applying
            channel-specific design and length limits). If `channelType`
            is `facebook`, `whatsapp` or `line`, the Send to Flex widget
            should set the Task Channel to Programmable Chat.
        chat_service_sid:
            The SID of the chat service.
        contact_identity:
            The channel contact's Identity.
        enabled:
            Whether the new Flex Flow is enabled.
        friendly_name:
            A descriptive string that you create to describe the Flex Flow resource.
        integration_channel:
            The Task Channel SID (TCXXXX) or unique name (e.g., `sms`) to use for
            the Task that will be created. Applicable and required when
            `integrationType` is `task`. The default value is `default`.
        integration_creation_on_message:
            In the context of outbound messaging, defines whether to create a Task
            immediately (and therefore reserve the conversation to
            current agent), or delay Task creation until the customer
            sends the first response. Set to false to create
            immediately, true to delay Task creation. This setting is
            only applicable for outbound messaging.
        integration_flow_sid:
            The SID of the Studio Flow. Required when `integrationType` is `studio`.
        integration_priority:
            The Task priority of a new Task. The default priority is 0. Optional
            when `integrationType` is `task`, not applicable otherwise.
        integration_retry_count:
            The number of times to retry the Studio Flow or webhook in case of
            failure. Takes integer values from 0 to 3 with the default
            being 3. Optional when `integrationType` is `studio` or
            `external`, not applicable otherwise.
        integration_timeout:
            The Task timeout in seconds for a new Task. Default is 86,400 seconds
            (24 hours). Optional when `integrationType` is `task`, not
            applicable otherwise.
        integration_url:
            The URL of the external webhook. Required when `integrationType` is
            `external`.
        integration_workflow_sid:
            The Workflow SID for a new Task. Required when `integrationType` is
            `task`.
        integration_workspace_sid:
            The Workspace SID for a new Task. Required when `integrationType` is
            `task`.
        integration_type:
            The software that will handle inbound messages. [Integration
            Type](https://www.twilio.com/docs/flex/developer/messaging/manage-
            flows
            integration-types) can be: `studio`, `external`, or `task`.
        janitor_enabled:
            When enabled, the Messaging Channel Janitor will remove active Proxy
            sessions if the associated Task is deleted outside of the
            Flex UI. Defaults to `false`.
        long_lived:
            When enabled, Flex will keep the chat channel active so that it may be
            used for subsequent interactions with a contact identity.
            Defaults to `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/FlexFlows/{sid}?](
    https://flex-api.twilio.com/v1/FlexFlows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/FlexFlows/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "channel_type": channel_type,
        "chat_service_sid": chat_service_sid,
        "contact_identity": contact_identity,
        "enabled": enabled,
        "friendly_name": friendly_name,
        "integration_channel": integration_channel,
        "integration_creation_on_message": integration_creation_on_message,
        "integration_flow_sid": integration_flow_sid,
        "integration_priority": integration_priority,
        "integration_retry_count": integration_retry_count,
        "integration_timeout": integration_timeout,
        "integration_url": integration_url,
        "integration_workflow_sid": integration_workflow_sid,
        "integration_workspace_sid": integration_workspace_sid,
        "integration_type": integration_type,
        "janitor_enabled": janitor_enabled,
        "long_lived": long_lived,
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
async def post_v1_interactions(
    twilio_credentials: "TwilioCredentials",
    channel: str = None,
    routing: str = None,
) -> Dict[str, Any]:
    """
    Create a new Interaction.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        channel:
            The Interaction's channel.
        routing:
            The Interaction's routing logic.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/Interactions?](
    https://flex-api.twilio.com/v1/Interactions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://flex-api.twilio.com/v1/Interactions"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "channel": channel,
        "routing": routing,
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
async def get_v1_interactions_interaction_sid_channels(
    interaction_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all Channels for an Interaction.

    Args:
        interaction_sid:
            Interaction sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels?&page_size=%s](
    https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels"  # noqa
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
async def get_v1_interactions_interaction_sid_channels_channel_sid_invites(  # noqa
    interaction_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all Invites for a Channel.

    Args:
        interaction_sid:
            Interaction sid used in formatting the endpoint URL.
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
    [https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Invites?&page_size=%s](
    https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Invites?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Invites"  # noqa
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
async def post_v1_interactions_interaction_sid_channels_channel_sid_invites(  # noqa
    interaction_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    routing: str = None,
) -> Dict[str, Any]:
    """
    Invite an Agent or a TaskQueue to a Channel.

    Args:
        interaction_sid:
            Interaction sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        routing:
            The Interaction's routing logic.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Invites?](
    https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Invites?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "routing": routing,
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
async def get_v1_interactions_interaction_sid_channels_channel_sid_participants(  # noqa
    interaction_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all Participants for a Channel.

    Args:
        interaction_sid:
            Interaction sid used in formatting the endpoint URL.
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
    [https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants?&page_size=%s](
    https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants"  # noqa
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
async def post_v1_interactions_interaction_sid_channels_channel_sid_participants(  # noqa
    interaction_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    media_properties: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Add a Participant to a Channel.

    Args:
        interaction_sid:
            Interaction sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        media_properties:
            JSON representing the Media Properties for the new Participant.
        type:
            Participant type.  Can be: `agent`, `customer`, `supervisor`, `external`
            or `unknown`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants?](
    https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "media_properties": media_properties,
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
async def post_v1_interactions_interaction_sid_channels_channel_sid_participants_sid(  # noqa
    interaction_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Update an existing Channel Participant.

    Args:
        interaction_sid:
            Interaction sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The Participant's status. Can be: `closed` or `wrapup`.  Participant
            must be an agent.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants/{sid}?](
    https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants/{sid}"  # noqa
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
async def get_v1_interactions_interaction_sid_channels_sid(
    interaction_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Channel for an Interaction.

    Args:
        interaction_sid:
            Interaction sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{sid}?](
    https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{sid}"  # noqa
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
async def post_v1_interactions_interaction_sid_channels_sid(
    interaction_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    routing: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """
    Update an existing Interaction.

    Args:
        interaction_sid:
            Interaction sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        routing:
            Optional. The state of associated tasks. If not specified, all tasks
            will be set to `wrapping`.
        status:
            Required. Indicates the Interaction channel's status. When a channel is
            set to `closed`, all tasks are put in the `wrapping` state
            by default unless the Routing status is set to `closed` in
            which case the tasks will be `completed`. Value: `closed`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{sid}?](
    https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Interactions/{interaction_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "routing": routing,
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
async def get_v1_interactions_sid(
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
    [https://flex-api.twilio.com/v1/Interactions/{sid}?](
    https://flex-api.twilio.com/v1/Interactions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/Interactions/{sid}"  # noqa
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
async def get_v1_web_channels(
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
    [https://flex-api.twilio.com/v1/WebChannels?&page_size=%s](
    https://flex-api.twilio.com/v1/WebChannels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://flex-api.twilio.com/v1/WebChannels"  # noqa

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
async def post_v1_web_channels(
    twilio_credentials: "TwilioCredentials",
    chat_friendly_name: str = None,
    chat_unique_name: str = None,
    customer_friendly_name: str = None,
    flex_flow_sid: str = None,
    identity: str = None,
    pre_engagement_data: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        chat_friendly_name:
            The chat channel's friendly name.
        chat_unique_name:
            The chat channel's unique name.
        customer_friendly_name:
            The chat participant's friendly name.
        flex_flow_sid:
            The SID of the Flex Flow.
        identity:
            The chat identity.
        pre_engagement_data:
            The pre-engagement data.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/WebChannels?](
    https://flex-api.twilio.com/v1/WebChannels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://flex-api.twilio.com/v1/WebChannels"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "chat_friendly_name": chat_friendly_name,
        "chat_unique_name": chat_unique_name,
        "customer_friendly_name": customer_friendly_name,
        "flex_flow_sid": flex_flow_sid,
        "identity": identity,
        "pre_engagement_data": pre_engagement_data,
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
async def delete_v1_web_channels_sid(
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
    [https://flex-api.twilio.com/v1/WebChannels/{sid}?](
    https://flex-api.twilio.com/v1/WebChannels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/WebChannels/{sid}"  # noqa
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
async def get_v1_web_channels_sid(
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
    [https://flex-api.twilio.com/v1/WebChannels/{sid}?](
    https://flex-api.twilio.com/v1/WebChannels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/WebChannels/{sid}"  # noqa
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
async def post_v1_web_channels_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    chat_status: str = None,
    post_engagement_data: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        chat_status:
            The chat status. Can only be `inactive`.
        post_engagement_data:
            The post-engagement data.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://flex-api.twilio.com/v1/WebChannels/{sid}?](
    https://flex-api.twilio.com/v1/WebChannels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://flex-api.twilio.com/v1/WebChannels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "chat_status": chat_status,
        "post_engagement_data": post_engagement_data,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
