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
