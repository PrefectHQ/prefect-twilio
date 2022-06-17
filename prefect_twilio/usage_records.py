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
async def get_v1_usage_records(
    twilio_credentials: "TwilioCredentials",
    sim: str = None,
    fleet: str = None,
    network: str = None,
    iso_country: str = None,
    group: str = None,
    granularity: str = None,
    start_time: str = None,
    end_time: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List UsageRecords.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        sim:
            SID or unique name of a Sim resource. Only show UsageRecords
            representing usage incurred by this Super SIM.
        fleet:
            SID or unique name of a Fleet resource. Only show UsageRecords
            representing usage for Super SIMs belonging to this Fleet
            resource at the time the usage occurred.
        network:
            SID of a Network resource. Only show UsageRecords representing usage on
            this network.
        iso_country:
            Alpha-2 ISO Country Code. Only show UsageRecords representing usage in
            this country.
        group:
            Dimension over which to aggregate usage records. Can be: `sim`, `fleet`,
            `network`, `isoCountry`. Default is to not aggregate across
            any of these dimensions, UsageRecords will be aggregated
            into the time buckets described by the `Granularity`
            parameter.
        granularity:
            Time-based grouping that UsageRecords should be aggregated by. Can be:
            `hour`, `day`, or `all`. Default is `all`. `all` returns one
            UsageRecord that describes the usage for the entire period.
        start_time:
            Only include usage that occurred at or after this time, specified in
            [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
            Default is one month before the `end_time`.
        end_time:
            Only include usage that occurred before this time (exclusive), specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format. Default is the current time.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/UsageRecords?&sim=%s&fleet=%s&network=%s&iso_country=%s&group=%s&granularity=%s&start_time=%s&end_time=%s&page_size=%s](
    https://supersim.twilio.com/v1/UsageRecords?&sim=%s&fleet=%s&network=%s&iso_country=%s&group=%s&granularity=%s&start_time=%s&end_time=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/UsageRecords"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "sim": sim,
        "fleet": fleet,
        "network": network,
        "iso_country": iso_country,
        "group": group,
        "granularity": granularity,
        "start_time": start_time,
        "end_time": end_time,
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
async def get_v1_usage_records(
    twilio_credentials: "TwilioCredentials",
    end: str = None,
    start: str = None,
    granularity: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end:
            Only include usage that has occurred on or before this date. Format is
            [ISO 8601](https://www.iso.org/iso-8601-date-and-time-
            format.html).
        start:
            Only include usage that has occurred on or after this date. Format is
            [ISO 8601](https://www.iso.org/iso-8601-date-and-time-
            format.html).
        granularity:
            How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`.
            A value of `all` returns one Usage Record that describes the
            usage for the entire period.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/UsageRecords?&end=%s&start=%s&granularity=%s&page_size=%s](
    https://wireless.twilio.com/v1/UsageRecords?&end=%s&start=%s&granularity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://wireless.twilio.com/v1/UsageRecords"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end": end,
        "start": start,
        "granularity": granularity,
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
