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
async def get_v1_rate_plans(
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
    [https://wireless.twilio.com/v1/RatePlans?&page_size=%s](
    https://wireless.twilio.com/v1/RatePlans?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://wireless.twilio.com/v1/RatePlans"  # noqa

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
async def post_v1_rate_plans(
    twilio_credentials: "TwilioCredentials",
    data_enabled: bool = None,
    data_limit: int = None,
    data_metering: str = None,
    friendly_name: str = None,
    international_roaming: list = None,
    international_roaming_data_limit: int = None,
    messaging_enabled: bool = None,
    national_roaming_data_limit: int = None,
    national_roaming_enabled: bool = None,
    unique_name: str = None,
    voice_enabled: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        data_enabled:
            Whether SIMs can use GPRS/3G/4G/LTE data connectivity.
        data_limit:
            The total data usage (download and upload combined) in Megabytes that
            the Network allows during one month on the home network
            (T-Mobile USA). The metering period begins the day of
            activation and ends on the same day in the following month.
            Can be up to 2TB and the default value is `1000`.
        data_metering:
            The model used to meter data usage. Can be: `payg` and `quota-1`,
            `quota-10`, and `quota-50`. Learn more about the available
            [data metering
            models](https://www.twilio.com/docs/wireless/api/rateplan-
            resource
            payg-vs-quota-data-plans).
        friendly_name:
            A descriptive string that you create to describe the resource. It does
            not have to be unique.
        international_roaming:
            The list of services that SIMs capable of using GPRS/3G/4G/LTE data
            connectivity can use outside of the United States. Can
            contain: `data` and `messaging`.
        international_roaming_data_limit:
            The total data usage (download and upload combined) in Megabytes that
            the Network allows during one month when roaming outside the
            United States. Can be up to 2TB.
        messaging_enabled:
            Whether SIMs can make, send, and receive SMS using
            [Commands](https://www.twilio.com/docs/wireless/api/command-
            resource).
        national_roaming_data_limit:
            The total data usage (download and upload combined) in Megabytes that
            the Network allows during one month on non-home networks in
            the United States. The metering period begins the day of
            activation and ends on the same day in the following month.
            Can be up to 2TB. See [national
            roaming](https://www.twilio.com/docs/wireless/api/rateplan-
            resource
            national-roaming) for more info.
        national_roaming_enabled:
            Whether SIMs can roam on networks other than the home network (T-Mobile
            USA) in the United States. See [national
            roaming](https://www.twilio.com/docs/wireless/api/rateplan-
            resource
            national-roaming).
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used in place of the resource's `sid` in the URL to
            address the resource.
        voice_enabled:
            Deprecated.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/RatePlans?](
    https://wireless.twilio.com/v1/RatePlans?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://wireless.twilio.com/v1/RatePlans"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "data_enabled": data_enabled,
        "data_limit": data_limit,
        "data_metering": data_metering,
        "friendly_name": friendly_name,
        "international_roaming": international_roaming,
        "international_roaming_data_limit": international_roaming_data_limit,
        "messaging_enabled": messaging_enabled,
        "national_roaming_data_limit": national_roaming_data_limit,
        "national_roaming_enabled": national_roaming_enabled,
        "unique_name": unique_name,
        "voice_enabled": voice_enabled,
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
async def delete_v1_rate_plans_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/RatePlans/{sid}?](
    https://wireless.twilio.com/v1/RatePlans/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/RatePlans/{sid}"  # noqa
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
async def get_v1_rate_plans_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/RatePlans/{sid}?](
    https://wireless.twilio.com/v1/RatePlans/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/RatePlans/{sid}"  # noqa
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
async def post_v1_rate_plans_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It does
            not have to be unique.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used in place of the resource's `sid` in the URL to
            address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/RatePlans/{sid}?](
    https://wireless.twilio.com/v1/RatePlans/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/RatePlans/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "unique_name": unique_name,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
