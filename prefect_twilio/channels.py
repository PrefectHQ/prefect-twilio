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
