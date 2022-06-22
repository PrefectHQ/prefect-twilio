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
async def get_v1_alerts(
    twilio_credentials: "TwilioCredentials",
    log_level: str = None,
    start_date: str = None,
    end_date: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        log_level:
            Only show alerts for this log-level.  Can be: `error`, `warning`,
            `notice`, or `debug`.
        start_date:
            Only include alerts that occurred on or after this date and time.
            Specify the date and time in GMT and format as `YYYY-MM-DD`
            or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30
            days are not supported.
        end_date:
            Only include alerts that occurred on or before this date and time.
            Specify the date and time in GMT and format as `YYYY-MM-DD`
            or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30
            days are not supported.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://monitor.twilio.com/v1/Alerts?&log_level=%s&start_date=%s&end_date=%s&page_size=%s](
    https://monitor.twilio.com/v1/Alerts?&log_level=%s&start_date=%s&end_date=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://monitor.twilio.com/v1/Alerts"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "log_level": log_level,
        "start_date": start_date,
        "end_date": end_date,
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
async def get_v1_alerts_sid(
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
    [https://monitor.twilio.com/v1/Alerts/{sid}?](
    https://monitor.twilio.com/v1/Alerts/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://monitor.twilio.com/v1/Alerts/{sid}"  # noqa
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
async def get_v1_events(
    twilio_credentials: "TwilioCredentials",
    actor_sid: str = None,
    event_type: str = None,
    resource_sid: str = None,
    source_ip_address: str = None,
    start_date: str = None,
    end_date: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Returns a list of events in the account, sorted by event-date.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        actor_sid:
            Only include events initiated by this Actor. Useful for auditing actions
            taken by specific users or API credentials.
        event_type:
            Only include events of this [Event
            Type](https://www.twilio.com/docs/usage/monitor-events
            event-types).
        resource_sid:
            Only include events that refer to this resource. Useful for discovering
            the history of a specific resource.
        source_ip_address:
            Only include events that originated from this IP address. Useful for
            tracking suspicious activity originating from the API or the
            Twilio Console.
        start_date:
            Only include events that occurred on or after this date. Specify the
            date in GMT and [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        end_date:
            Only include events that occurred on or before this date. Specify the
            date in GMT and [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://monitor.twilio.com/v1/Events?&actor_sid=%s&event_type=%s&resource_sid=%s&source_ip_address=%s&start_date=%s&end_date=%s&page_size=%s](
    https://monitor.twilio.com/v1/Events?&actor_sid=%s&event_type=%s&resource_sid=%s&source_ip_address=%s&start_date=%s&end_date=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://monitor.twilio.com/v1/Events"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "actor_sid": actor_sid,
        "event_type": event_type,
        "resource_sid": resource_sid,
        "source_ip_address": source_ip_address,
        "start_date": start_date,
        "end_date": end_date,
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
async def get_v1_events_sid(
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
    [https://monitor.twilio.com/v1/Events/{sid}?](
    https://monitor.twilio.com/v1/Events/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://monitor.twilio.com/v1/Events/{sid}"  # noqa
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
