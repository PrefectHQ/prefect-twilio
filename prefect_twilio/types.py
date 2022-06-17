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
async def get_v1_types(
    twilio_credentials: "TwilioCredentials",
    schema_id: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a paginated list of all the available Event Types.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        schema_id:
            A string parameter filtering the results to return only the Event Types
            using a given schema.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Types?&schema_id=%s&page_size=%s](
    https://events.twilio.com/v1/Types?&schema_id=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://events.twilio.com/v1/Types"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "schema_id": schema_id,
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
async def get_v1_types_type(
    type: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Event Type.

    Args:
        type:
            Type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Types/{type}?](
    https://events.twilio.com/v1/Types/{type}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Types/{type}"  # noqa
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
