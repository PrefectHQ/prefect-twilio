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
async def get_v2_phone_numbers_phone_number(
    phone_number: str,
    twilio_credentials: "TwilioCredentials",
    fields: str = None,
    country_code: str = None,
) -> Dict[str, Any]:
    """


    Args:
        phone_number:
            Phone number used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        fields:
            A comma-separated list of fields to return. Possible values are
            caller_name, sim_swap, call_forwarding, live_activity,
            enhanced_line_type or line_type_intelligence.
        country_code:
            The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            used if the phone number provided is in national format.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://lookups.twilio.com/v2/PhoneNumbers/{phone_number}?&fields=%s&country_code=%s](
    https://lookups.twilio.com/v2/PhoneNumbers/{phone_number}?&fields=%s&country_code=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://lookups.twilio.com/v2/PhoneNumbers/{phone_number}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "fields": fields,
        "country_code": country_code,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
