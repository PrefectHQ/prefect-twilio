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
async def delete_v1_exports_jobs_job_sid(
    job_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        job_sid:
            Job sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://bulkexports.twilio.com/v1/Exports/Jobs/{job_sid}?](
    https://bulkexports.twilio.com/v1/Exports/Jobs/{job_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://bulkexports.twilio.com/v1/Exports/Jobs/{job_sid}"  # noqa
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
async def get_v1_exports_jobs_job_sid(
    job_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        job_sid:
            Job sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://bulkexports.twilio.com/v1/Exports/Jobs/{job_sid}?](
    https://bulkexports.twilio.com/v1/Exports/Jobs/{job_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://bulkexports.twilio.com/v1/Exports/Jobs/{job_sid}"  # noqa
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
async def get_v1_exports_resource_type(
    resource_type: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Export.

    Args:
        resource_type:
            Resource type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://bulkexports.twilio.com/v1/Exports/{resource_type}?](
    https://bulkexports.twilio.com/v1/Exports/{resource_type}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://bulkexports.twilio.com/v1/Exports/{resource_type}"  # noqa
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
async def get_v1_exports_resource_type_configuration(
    resource_type: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Export Configuration.

    Args:
        resource_type:
            Resource type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://bulkexports.twilio.com/v1/Exports/{resource_type}/Configuration?](
    https://bulkexports.twilio.com/v1/Exports/{resource_type}/Configuration?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://bulkexports.twilio.com/v1/Exports/{resource_type}/Configuration"  # noqa
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
async def post_v1_exports_resource_type_configuration(
    resource_type: str,
    twilio_credentials: "TwilioCredentials",
    enabled: bool = None,
    webhook_method: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Export Configuration.

    Args:
        resource_type:
            Resource type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        enabled:
            If true, Twilio will automatically generate every day's file when the
            day is over.
        webhook_method:
            Sets whether Twilio should call a webhook URL when the automatic
            generation is complete, using GET or POST. The actual
            destination is set in the webhook_url.
        webhook_url:
            Stores the URL destination for the method specified in webhook_method.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://bulkexports.twilio.com/v1/Exports/{resource_type}/Configuration?](
    https://bulkexports.twilio.com/v1/Exports/{resource_type}/Configuration?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://bulkexports.twilio.com/v1/Exports/{resource_type}/Configuration"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "enabled": enabled,
        "webhook_method": webhook_method,
        "webhook_url": webhook_url,
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
async def get_v1_exports_resource_type_days(
    resource_type: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Days for a resource.

    Args:
        resource_type:
            Resource type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://bulkexports.twilio.com/v1/Exports/{resource_type}/Days?&page_size=%s](
    https://bulkexports.twilio.com/v1/Exports/{resource_type}/Days?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://bulkexports.twilio.com/v1/Exports/{resource_type}/Days"  # noqa
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
async def get_v1_exports_resource_type_days_day(
    resource_type: str,
    day: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Day.

    Args:
        resource_type:
            Resource type used in formatting the endpoint URL.
        day:
            Day used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://bulkexports.twilio.com/v1/Exports/{resource_type}/Days/{day}?](
    https://bulkexports.twilio.com/v1/Exports/{resource_type}/Days/{day}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 307 | Temporary Redirect. |
    """  # noqa
    url = (
        f"https://bulkexports.twilio.com/v1/Exports/{resource_type}/Days/{day}"  # noqa
    )
    responses = {
        307: "Temporary Redirect.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_v1_exports_resource_type_jobs(
    resource_type: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        resource_type:
            Resource type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://bulkexports.twilio.com/v1/Exports/{resource_type}/Jobs?&page_size=%s](
    https://bulkexports.twilio.com/v1/Exports/{resource_type}/Jobs?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://bulkexports.twilio.com/v1/Exports/{resource_type}/Jobs"  # noqa
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
async def post_v1_exports_resource_type_jobs(
    resource_type: str,
    twilio_credentials: "TwilioCredentials",
    email: str = None,
    end_day: str = None,
    friendly_name: str = None,
    start_day: str = None,
    webhook_method: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        resource_type:
            Resource type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        email:
            The optional email to send the completion notification to. You can set
            both webhook, and email, or one or the other. If you set
            neither, the job will run but you will have to query to
            determine your job's status.
        end_day:
            The end day for the custom export specified as a string in the format of
            yyyy-mm-dd. End day is inclusive and must be 2 days earlier
            than the current UTC day.
        friendly_name:
            The friendly name specified when creating the job.
        start_day:
            The start day for the custom export specified as a string in the format
            of yyyy-mm-dd.
        webhook_method:
            This is the method used to call the webhook on completion of the job. If
            this is supplied, `WebhookUrl` must also be supplied.
        webhook_url:
            The optional webhook url called on completion of the job. If this is
            supplied, `WebhookMethod` must also be supplied. If you set
            neither webhook nor email, you will have to check your job's
            status manually.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://bulkexports.twilio.com/v1/Exports/{resource_type}/Jobs?](
    https://bulkexports.twilio.com/v1/Exports/{resource_type}/Jobs?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://bulkexports.twilio.com/v1/Exports/{resource_type}/Jobs"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "email": email,
        "end_day": end_day,
        "friendly_name": friendly_name,
        "start_day": start_day,
        "webhook_method": webhook_method,
        "webhook_url": webhook_url,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
