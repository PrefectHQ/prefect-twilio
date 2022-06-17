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
async def get_v1_networks(
    twilio_credentials: "TwilioCredentials",
    iso_country: str = None,
    mcc: str = None,
    mnc: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Network resources.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        iso_country:
            The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            of the Network resources to read.
        mcc:
            The 'mobile country code' of a country. Network resources with this
            `mcc` in their `identifiers` will be read.
        mnc:
            The 'mobile network code' of a mobile operator network. Network
            resources with this `mnc` in their `identifiers` will be
            read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Networks?&iso_country=%s&mcc=%s&mnc=%s&page_size=%s](
    https://supersim.twilio.com/v1/Networks?&iso_country=%s&mcc=%s&mnc=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/Networks"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "iso_country": iso_country,
        "mcc": mcc,
        "mnc": mnc,
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
async def get_v1_networks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Network resource.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Networks/{sid}?](
    https://supersim.twilio.com/v1/Networks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Networks/{sid}"  # noqa
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
