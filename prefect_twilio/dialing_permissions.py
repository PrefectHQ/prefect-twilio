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
async def post_v1_dialing_permissions_bulk_country_updates(
    twilio_credentials: "TwilioCredentials",
    update_request: str = None,
) -> Dict[str, Any]:
    """
    Create a bulk update request to change voice dialing country permissions of one
    or more countries identified by the corresponding [ISO country
    code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        update_request:
            URL encoded JSON array of update objects. example : `[ { "iso_code":
            "GB", "low_risk_numbers_enabled": "true",
            "high_risk_special_numbers_enabled":"true",
            "high_risk_tollfraud_numbers_enabled": "false" } ]`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/DialingPermissions/BulkCountryUpdates?](
    https://voice.twilio.com/v1/DialingPermissions/BulkCountryUpdates?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://voice.twilio.com/v1/DialingPermissions/BulkCountryUpdates"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "update_request": update_request,
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
async def get_v1_dialing_permissions_countries(
    twilio_credentials: "TwilioCredentials",
    iso_code: str = None,
    continent: str = None,
    country_code: str = None,
    low_risk_numbers_enabled: bool = None,
    high_risk_special_numbers_enabled: bool = None,
    high_risk_tollfraud_numbers_enabled: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve all voice dialing country permissions for this account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        iso_code:
            Filter to retrieve the country permissions by specifying the [ISO
            country
            code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        continent:
            Filter to retrieve the country permissions by specifying the continent.
        country_code:
            Filter the results by specified [country
            codes](https://www.itu.int/itudoc/itu-t/ob-
            lists/icc/e164_763.html).
        low_risk_numbers_enabled:
            Filter to retrieve the country permissions with dialing to low-risk
            numbers enabled. Can be: `true` or `false`.
        high_risk_special_numbers_enabled:
            Filter to retrieve the country permissions with dialing to high-risk
            special service numbers enabled. Can be: `true` or `false`.
        high_risk_tollfraud_numbers_enabled:
            Filter to retrieve the country permissions with dialing to high-risk
            [toll fraud](https://www.twilio.com/learn/voice-and-
            video/toll-fraud) numbers enabled. Can be: `true` or
            `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/DialingPermissions/Countries?&iso_code=%s&continent=%s&country_code=%s&low_risk_numbers_enabled=%s&high_risk_special_numbers_enabled=%s&high_risk_tollfraud_numbers_enabled=%s&page_size=%s](
    https://voice.twilio.com/v1/DialingPermissions/Countries?&iso_code=%s&continent=%s&country_code=%s&low_risk_numbers_enabled=%s&high_risk_special_numbers_enabled=%s&high_risk_tollfraud_numbers_enabled=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://voice.twilio.com/v1/DialingPermissions/Countries"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "iso_code": iso_code,
        "continent": continent,
        "country_code": country_code,
        "low_risk_numbers_enabled": low_risk_numbers_enabled,
        "high_risk_special_numbers_enabled": high_risk_special_numbers_enabled,
        "high_risk_tollfraud_numbers_enabled": high_risk_tollfraud_numbers_enabled,
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
async def get_v1_dialing_permissions_countries_iso_code(
    iso_code: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve voice dialing country permissions identified by the given ISO country
    code.

    Args:
        iso_code:
            Iso code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}?](
    https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}"  # noqa
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
async def get_v1_dialing_permissions_countries_iso_code_high_risk_special_prefixes(
    iso_code: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Fetch the high-risk special services prefixes from the country resource
    corresponding to the [ISO country
    code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

    Args:
        iso_code:
            Iso code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}/HighRiskSpecialPrefixes?&page_size=%s](
    https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}/HighRiskSpecialPrefixes?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/DialingPermissions/Countries/{iso_code}/HighRiskSpecialPrefixes"  # noqa
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
