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
async def get_v1_phone_numbers_phone_number(
    phone_number: str,
    twilio_credentials: "TwilioCredentials",
    country_code: str = None,
    type: list = None,
    add_ons: list = None,
    add_ons_data: dict = None,
) -> Dict[str, Any]:
    """


    Args:
        phone_number:
            Phone number used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        country_code:
            The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            of the phone number to fetch. This is used to specify the
            country when the phone number is provided in a national
            format.
        type:
            The type of information to return. Can be: `carrier` or `caller-name`.
            The default is null.  Carrier information costs $0.005 per
            phone number looked up.  Caller Name information is
            currently available only in the US and costs $0.01 per phone
            number looked up.  To retrieve both types on information,
            specify this parameter twice; once with `carrier` and once
            with `caller-name` as the value.
        add_ons:
            The `unique_name` of an Add-on you would like to invoke. Can be the
            `unique_name` of an Add-on that is installed on your
            account. You can specify multiple instances of this
            parameter to invoke multiple Add-ons. For more information
            about  Add-ons, see the [Add-ons
            documentation](https://www.twilio.com/docs/add-ons).
        add_ons_data:
            Data specific to the add-on you would like to invoke. The content and
            format of this value depends on the add-on.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://lookups.twilio.com/v1/PhoneNumbers/{phone_number}?&country_code=%s&type=%s&add_ons=%s&add_ons_data=%s](
    https://lookups.twilio.com/v1/PhoneNumbers/{phone_number}?&country_code=%s&type=%s&add_ons=%s&add_ons_data=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://lookups.twilio.com/v1/PhoneNumbers/{phone_number}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "country_code": country_code,
        "type": type,
        "add_ons": add_ons,
        "add_ons_data": add_ons_data,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
