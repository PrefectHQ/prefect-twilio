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
async def get_v1_flows(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Flows.

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
    [https://studio.twilio.com/v1/Flows?&page_size=%s](
    https://studio.twilio.com/v1/Flows?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://studio.twilio.com/v1/Flows"  # noqa

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
async def get_v1_flows_flow_sid_engagements(
    flow_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Engagements for the Flow.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements?&page_size=%s](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements"  # noqa
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
async def post_v1_flows_flow_sid_engagements(
    flow_sid: str,
    twilio_credentials: "TwilioCredentials",
    from_: str = None,
    parameters: str = None,
    to: str = None,
) -> Dict[str, Any]:
    """
    Triggers a new Engagement for the Flow.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        from_:
            The Twilio phone number to send messages or initiate calls from during
            the Flow Engagement. Available as variable
            `{{flow.channel.address}}`.
        parameters:
            A JSON string we will add to your flow's context and that you can access
            as variables inside your flow. For example, if you pass in
            `Parameters={'name':'Zeke'}` then inside a widget you can
            reference the variable `{{flow.data.name}}` which will
            return the string 'Zeke'. Note: the JSON value must
            explicitly be passed as a string, not as a hash object.
            Depending on your particular HTTP library, you may need to
            add quotes or URL encode your JSON string.
        to:
            The Contact phone number to start a Studio Flow Engagement, available as
            variable `{{contact.channel.address}}`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "from_": from_,
        "parameters": parameters,
        "to": to,
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
async def get_v1_flows_flow_sid_engagements_engagement_sid_context(  # noqa
    flow_sid: str,
    engagement_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve the most recent context for an Engagement.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        engagement_sid:
            Engagement sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Context?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Context?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Context"  # noqa
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
async def get_v1_flows_flow_sid_engagements_engagement_sid_steps(
    flow_sid: str,
    engagement_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Steps for an Engagement.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        engagement_sid:
            Engagement sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps?&page_size=%s](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps"  # noqa
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
async def get_v1_flows_flow_sid_engagements_engagement_sid_steps_sid(  # noqa
    flow_sid: str,
    engagement_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a Step.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        engagement_sid:
            Engagement sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps/{sid}?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps/{sid}"  # noqa
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
async def get_v1_flows_flow_sid_engagements_engagement_sid_steps_step_sid_context(  # noqa
    flow_sid: str,
    engagement_sid: str,
    step_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve the context for an Engagement Step.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        engagement_sid:
            Engagement sid used in formatting the endpoint URL.
        step_sid:
            Step sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps/{step_sid}/Context?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps/{step_sid}/Context?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps/{step_sid}/Context"  # noqa
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
async def delete_v1_flows_flow_sid_engagements_sid(
    flow_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete this Engagement and all Steps relating to it.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{sid}?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{sid}"  # noqa
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
async def get_v1_flows_flow_sid_engagements_sid(
    flow_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve an Engagement.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{sid}?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Engagements/{sid}"  # noqa
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
async def get_v1_flows_flow_sid_executions(
    flow_sid: str,
    twilio_credentials: "TwilioCredentials",
    date_created_from: str = None,
    date_created_to: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Executions for the Flow.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created_from:
            Only show Execution resources starting on or after this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time,
            given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        date_created_to:
            Only show Execution resources starting before this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time,
            given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Executions?&date_created_from=%s&date_created_to=%s&page_size=%s](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Executions?&date_created_from=%s&date_created_to=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Executions"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created_from": date_created_from,
        "date_created_to": date_created_to,
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
async def post_v1_flows_flow_sid_executions(
    flow_sid: str,
    twilio_credentials: "TwilioCredentials",
    from_: str = None,
    parameters: str = None,
    to: str = None,
) -> Dict[str, Any]:
    """
    Triggers a new Execution for the Flow.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        from_:
            The Twilio phone number to send messages or initiate calls from during
            the Flow's Execution. Available as variable
            `{{flow.channel.address}}`. For SMS, this can also be a
            Messaging Service SID.
        parameters:
            JSON data that will be added to the Flow's context and that can be
            accessed as variables inside your Flow. For example, if you
            pass in `Parameters={"name":"Zeke"}`, a widget in your Flow
            can reference the variable `{{flow.data.name}}`, which
            returns "Zeke". Note: the JSON value must explicitly be
            passed as a string, not as a hash object. Depending on your
            particular HTTP library, you may need to add quotes or URL
            encode the JSON string.
        to:
            The Contact phone number to start a Studio Flow Execution, available as
            variable `{{contact.channel.address}}`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Executions?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Executions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Executions"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "from_": from_,
        "parameters": parameters,
        "to": to,
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
async def get_v1_flows_flow_sid_executions_execution_sid_context(
    flow_sid: str,
    execution_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve the most recent context for an Execution.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        execution_sid:
            Execution sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Context?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Context?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Context"  # noqa
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
async def get_v1_flows_flow_sid_executions_execution_sid_steps(
    flow_sid: str,
    execution_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Steps for an Execution.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        execution_sid:
            Execution sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Steps?&page_size=%s](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Steps?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Steps"  # noqa
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
async def get_v1_flows_flow_sid_executions_execution_sid_steps_sid(  # noqa
    flow_sid: str,
    execution_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a Step.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        execution_sid:
            Execution sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{sid}?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{sid}"  # noqa
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
async def get_v1_flows_flow_sid_executions_execution_sid_steps_step_sid_context(  # noqa
    flow_sid: str,
    execution_sid: str,
    step_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve the context for an Execution Step.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        execution_sid:
            Execution sid used in formatting the endpoint URL.
        step_sid:
            Step sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{step_sid}/Context?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{step_sid}/Context?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{step_sid}/Context"  # noqa
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
async def delete_v1_flows_flow_sid_executions_sid(
    flow_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete the Execution and all Steps relating to it.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{sid}?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{sid}"  # noqa
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
async def get_v1_flows_flow_sid_executions_sid(
    flow_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve an Execution.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{sid}?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{sid}"  # noqa
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
async def post_v1_flows_flow_sid_executions_sid(
    flow_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Update the status of an Execution to `ended`.

    Args:
        flow_sid:
            Flow sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The status of the Execution. Can only be `ended`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{sid}?](
    https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{flow_sid}/Executions/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "status": status,
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
async def delete_v1_flows_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Flow.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{sid}?](
    https://studio.twilio.com/v1/Flows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{sid}"  # noqa
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
async def get_v1_flows_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Flow.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://studio.twilio.com/v1/Flows/{sid}?](
    https://studio.twilio.com/v1/Flows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://studio.twilio.com/v1/Flows/{sid}"  # noqa
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
