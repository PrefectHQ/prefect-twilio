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
