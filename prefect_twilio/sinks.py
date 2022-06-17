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
async def get_v1_sinks(
    twilio_credentials: "TwilioCredentials",
    in_use: bool = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a paginated list of Sinks belonging to the account used to make the
    request.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        in_use:
            A boolean query parameter filtering the results to return sinks used/not
            used by a subscription.
        status:
            A String query parameter filtering the results by status `initialized`,
            `validating`, `active` or `failed`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks?&in_use=%s&status=%s&page_size=%s](
    https://events.twilio.com/v1/Sinks?&in_use=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://events.twilio.com/v1/Sinks"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "in_use": in_use,
        "status": status,
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
async def post_v1_sinks(
    twilio_credentials: "TwilioCredentials",
    description: str = None,
    sink_configuration: str = None,
    sink_type: str = None,
) -> Dict[str, Any]:
    """
    Create a new Sink.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            A human readable description for the Sink **This value should not
            contain PII.**.
        sink_configuration:
            The information required for Twilio to connect to the provided Sink
            encoded as JSON.
        sink_type:
            The Sink type. Can only be "kinesis" or "webhook" currently.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks?](
    https://events.twilio.com/v1/Sinks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://events.twilio.com/v1/Sinks"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "description": description,
        "sink_configuration": sink_configuration,
        "sink_type": sink_type,
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
async def delete_v1_sinks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Sink.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}?](
    https://events.twilio.com/v1/Sinks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}"  # noqa
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
async def get_v1_sinks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Sink.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}?](
    https://events.twilio.com/v1/Sinks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}"  # noqa
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
async def post_v1_sinks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    description: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Sink.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            A human readable description for the Sink **This value should not
            contain PII.**.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}?](
    https://events.twilio.com/v1/Sinks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "description": description,
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
async def post_v1_sinks_sid_test(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Create a new Sink Test Event for the given Sink.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}/Test?](
    https://events.twilio.com/v1/Sinks/{sid}/Test?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}/Test"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_v1_sinks_sid_validate(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    test_id: str = None,
) -> Dict[str, Any]:
    """
    Validate that a test event for a Sink was received.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        test_id:
            A 34 character string that uniquely identifies the test event for a Sink
            being validated.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}/Validate?](
    https://events.twilio.com/v1/Sinks/{sid}/Validate?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}/Validate"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "test_id": test_id,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
