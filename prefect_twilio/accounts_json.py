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
async def get_2010_04_01_accounts_json(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieves a collection of Accounts belonging to the account used to make the
    request.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            Only return the Account resources with friendly names that exactly match
            this name.
        status:
            Only return Account resources with the given status. Can be `closed`,
            `suspended` or `active`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts.json?&friendly_name=%s&status=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts.json?&friendly_name=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://api.twilio.com/2010-04-01/Accounts.json"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "friendly_name": friendly_name,
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
async def post_2010_04_01_accounts_json(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Twilio Subaccount from the account making the request.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A human readable description of the account to create, defaults to
            `SubAccount Created at {YYYY-MM-DD HH:MM meridian}`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts.json?](
    https://api.twilio.com/2010-04-01/Accounts.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://api.twilio.com/2010-04-01/Accounts.json"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
