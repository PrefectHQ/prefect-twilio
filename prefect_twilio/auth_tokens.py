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
async def post_v1_auth_tokens_promote(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Promote the secondary Auth Token to primary. After promoting the new token, all
    requests to Twilio using your old primary Auth Token will result in an
    error.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/AuthTokens/Promote?](
    https://accounts.twilio.com/v1/AuthTokens/Promote?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/AuthTokens/Promote"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def delete_v1_auth_tokens_secondary(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete the secondary Auth Token from your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/AuthTokens/Secondary?](
    https://accounts.twilio.com/v1/AuthTokens/Secondary?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/AuthTokens/Secondary"  # noqa

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
async def post_v1_auth_tokens_secondary(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Create a new secondary Auth Token.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/AuthTokens/Secondary?](
    https://accounts.twilio.com/v1/AuthTokens/Secondary?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/AuthTokens/Secondary"  # noqa

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
