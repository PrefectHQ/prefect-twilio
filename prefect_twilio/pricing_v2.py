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
async def get_v2_trunking_countries(
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
    [https://pricing.twilio.com/v2/Trunking/Countries?&page_size=%s](
    https://pricing.twilio.com/v2/Trunking/Countries?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://pricing.twilio.com/v2/Trunking/Countries"  # noqa

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
async def get_v2_trunking_countries_iso_country(
    iso_country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Country.

    Args:
        iso_country:
            Iso country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Trunking/Countries/{iso_country}?](
    https://pricing.twilio.com/v2/Trunking/Countries/{iso_country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Trunking/Countries/{iso_country}"  # noqa
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
async def get_v2_trunking_numbers_destination_number(
    destination_number: str,
    twilio_credentials: "TwilioCredentials",
    origination_number: str = None,
) -> Dict[str, Any]:
    """
    Fetch pricing information for a specific destination and, optionally,
    origination phone number.

    Args:
        destination_number:
            Destination number used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        origination_number:
            The origination phone number, in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format, for which to fetch the origin-based voice pricing
            information. E.164 format consists of a + followed by the
            country code and subscriber number.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Trunking/Numbers/{destination_number}?&origination_number=%s](
    https://pricing.twilio.com/v2/Trunking/Numbers/{destination_number}?&origination_number=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Trunking/Numbers/{destination_number}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "origination_number": origination_number,
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
async def get_v2_voice_countries(
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
    [https://pricing.twilio.com/v2/Voice/Countries?&page_size=%s](
    https://pricing.twilio.com/v2/Voice/Countries?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://pricing.twilio.com/v2/Voice/Countries"  # noqa

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
async def get_v2_voice_countries_iso_country(
    iso_country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Country.

    Args:
        iso_country:
            Iso country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Voice/Countries/{iso_country}?](
    https://pricing.twilio.com/v2/Voice/Countries/{iso_country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Voice/Countries/{iso_country}"  # noqa
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
async def get_v2_voice_numbers_destination_number(
    destination_number: str,
    twilio_credentials: "TwilioCredentials",
    origination_number: str = None,
) -> Dict[str, Any]:
    """
    Fetch pricing information for a specific destination and, optionally,
    origination phone number.

    Args:
        destination_number:
            Destination number used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        origination_number:
            The origination phone number, in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format, for which to fetch the origin-based voice pricing
            information. E.164 format consists of a + followed by the
            country code and subscriber number.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Voice/Numbers/{destination_number}?&origination_number=%s](
    https://pricing.twilio.com/v2/Voice/Numbers/{destination_number}?&origination_number=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Voice/Numbers/{destination_number}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "origination_number": origination_number,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
