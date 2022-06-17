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
async def get_v1_interactions_interaction_sid_channels_channel_sid_invites(
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
async def post_v1_interactions_interaction_sid_channels_channel_sid_invites(
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
async def get_v1_interactions_interaction_sid_channels_channel_sid_participants(
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
async def post_v1_interactions_interaction_sid_channels_channel_sid_participants(
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
async def post_v1_interactions_interaction_sid_channels_channel_sid_participants_sid(
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
