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
async def get_v1_deactivations(
    twilio_credentials: "TwilioCredentials",
    date: str = None,
) -> Dict[str, Any]:
    """
    Fetch a list of all United States numbers that have been deactivated on a
    specific date.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date:
            The request will return a list of all United States Phone Numbers that
            were deactivated on the day specified by this parameter.
            This date should be specified in YYYY-MM-DD format.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Deactivations?&date=%s](
    https://messaging.twilio.com/v1/Deactivations?&date=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 307 | Temporary Redirect. |
    """  # noqa
    url = "https://messaging.twilio.com/v1/Deactivations"  # noqa

    responses = {
        307: "Temporary Redirect.",  # noqa
    }

    params = {
        "date": date,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
