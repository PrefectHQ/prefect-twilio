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
async def get_v2_attempts(
    twilio_credentials: "TwilioCredentials",
    date_created_after: str = None,
    date_created_before: str = None,
    channel_data_to: str = None,
    country: str = None,
    channel: str = None,
    verify_service_sid: str = None,
    verification_sid: str = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all the verification attempts for a given Account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created_after:
            Datetime filter used to query Verification Attempts created after this
            datetime. Given as GMT in RFC 2822 format.
        date_created_before:
            Datetime filter used to query Verification Attempts created before this
            datetime. Given as GMT in RFC 2822 format.
        channel_data_to:
            Destination of a verification. It is phone number in E.164 format.
        country:
            Filter used to query Verification Attempts sent to the specified
            destination country.
        channel:
            Filter used to query Verification Attempts by communication channel.
            Valid values are `SMS` and `CALL`.
        verify_service_sid:
            Filter used to query Verification Attempts by verify service. Only
            attempts of the provided SID will be returned.
        verification_sid:
            Filter used to return all the Verification Attempts of a single
            verification. Only attempts of the provided verification SID
            will be returned.
        status:
            Filter used to query Verification Attempts by conversion status. Valid
            values are `UNCONVERTED`, for attempts that were not
            converted, and `CONVERTED`, for attempts that were
            confirmed.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Attempts?&date_created_after=%s&date_created_before=%s&channel_data_to=%s&country=%s&channel=%s&verify_service_sid=%s&verification_sid=%s&status=%s&page_size=%s](
    https://verify.twilio.com/v2/Attempts?&date_created_after=%s&date_created_before=%s&channel_data_to=%s&country=%s&channel=%s&verify_service_sid=%s&verification_sid=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Attempts"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "channel_data_to": channel_data_to,
        "country": country,
        "channel": channel,
        "verify_service_sid": verify_service_sid,
        "verification_sid": verification_sid,
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
async def get_v2_attempts_summary(
    twilio_credentials: "TwilioCredentials",
    verify_service_sid: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    country: str = None,
    channel: str = None,
    destination_prefix: str = None,
) -> Dict[str, Any]:
    """
    Get a summary of how many attempts were made and how many were converted.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        verify_service_sid:
            Filter used to consider only Verification Attempts of the given verify
            service on the summary aggregation.
        date_created_after:
            Datetime filter used to consider only Verification Attempts created
            after this datetime on the summary aggregation. Given as GMT
            in RFC 2822 format.
        date_created_before:
            Datetime filter used to consider only Verification Attempts created
            before this datetime on the summary aggregation. Given as
            GMT in RFC 2822 format.
        country:
            Filter used to consider only Verification Attempts sent to the specified
            destination country on the summary aggregation.
        channel:
            Filter Verification Attempts considered on the summary aggregation by
            communication channel. Valid values are `SMS` and `CALL`.
        destination_prefix:
            Filter the Verification Attempts considered on the summary aggregation
            by Destination prefix. It is the prefix of a phone number in
            E.164 format.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Attempts/Summary?&verify_service_sid=%s&date_created_after=%s&date_created_before=%s&country=%s&channel=%s&destination_prefix=%s](
    https://verify.twilio.com/v2/Attempts/Summary?&verify_service_sid=%s&date_created_after=%s&date_created_before=%s&country=%s&channel=%s&destination_prefix=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Attempts/Summary"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "verify_service_sid": verify_service_sid,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "country": country,
        "channel": channel,
        "destination_prefix": destination_prefix,
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
async def get_v2_attempts_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific verification attempt.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Attempts/{sid}?](
    https://verify.twilio.com/v2/Attempts/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Attempts/{sid}"  # noqa
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
