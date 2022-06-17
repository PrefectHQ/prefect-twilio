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
async def get_v1_schemas_id(
    id: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific schema with its nested versions.

    Args:
        id:
            Id used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Schemas/{id}?](
    https://events.twilio.com/v1/Schemas/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Schemas/{id}"  # noqa
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
async def get_v1_schemas_id_versions(
    id: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a paginated list of versions of the schema.

    Args:
        id:
            Id used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Schemas/{id}/Versions?&page_size=%s](
    https://events.twilio.com/v1/Schemas/{id}/Versions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Schemas/{id}/Versions"  # noqa
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
async def get_v1_schemas_id_versions_schema_version(
    id: str,
    schema_version: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific schema and version.

    Args:
        id:
            Id used in formatting the endpoint URL.
        schema_version:
            Schema version used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Schemas/{id}/Versions/{schema_version}?](
    https://events.twilio.com/v1/Schemas/{id}/Versions/{schema_version}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Schemas/{id}/Versions/{schema_version}"  # noqa
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
async def get_v1_sinks(
    twilio_credentials: "TwilioCredentials",
    in_use: bool = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a paginated list of Sinks belonging to the account used to make the
    request.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        in_use:
            A boolean query parameter filtering the results to return sinks used/not
            used by a subscription.
        status:
            A String query parameter filtering the results by status `initialized`,
            `validating`, `active` or `failed`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks?&in_use=%s&status=%s&page_size=%s](
    https://events.twilio.com/v1/Sinks?&in_use=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://events.twilio.com/v1/Sinks"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "in_use": in_use,
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
async def post_v1_sinks(
    twilio_credentials: "TwilioCredentials",
    description: str = None,
    sink_configuration: str = None,
    sink_type: str = None,
) -> Dict[str, Any]:
    """
    Create a new Sink.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            A human readable description for the Sink **This value should not
            contain PII.**.
        sink_configuration:
            The information required for Twilio to connect to the provided Sink
            encoded as JSON.
        sink_type:
            The Sink type. Can only be "kinesis" or "webhook" currently.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks?](
    https://events.twilio.com/v1/Sinks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://events.twilio.com/v1/Sinks"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "description": description,
        "sink_configuration": sink_configuration,
        "sink_type": sink_type,
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
async def delete_v1_sinks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Sink.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}?](
    https://events.twilio.com/v1/Sinks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}"  # noqa
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
async def get_v1_sinks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Sink.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}?](
    https://events.twilio.com/v1/Sinks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}"  # noqa
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
async def post_v1_sinks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    description: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Sink.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            A human readable description for the Sink **This value should not
            contain PII.**.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}?](
    https://events.twilio.com/v1/Sinks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "description": description,
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
async def post_v1_sinks_sid_test(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Create a new Sink Test Event for the given Sink.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}/Test?](
    https://events.twilio.com/v1/Sinks/{sid}/Test?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}/Test"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_v1_sinks_sid_validate(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    test_id: str = None,
) -> Dict[str, Any]:
    """
    Validate that a test event for a Sink was received.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        test_id:
            A 34 character string that uniquely identifies the test event for a Sink
            being validated.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Sinks/{sid}/Validate?](
    https://events.twilio.com/v1/Sinks/{sid}/Validate?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Sinks/{sid}/Validate"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "test_id": test_id,
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
async def get_v1_subscriptions(
    twilio_credentials: "TwilioCredentials",
    sink_sid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a paginated list of Subscriptions belonging to the account used to make
    the request.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        sink_sid:
            The SID of the sink that the list of Subscriptions should be filtered
            by.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions?&sink_sid=%s&page_size=%s](
    https://events.twilio.com/v1/Subscriptions?&sink_sid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://events.twilio.com/v1/Subscriptions"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "sink_sid": sink_sid,
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
async def post_v1_subscriptions(
    twilio_credentials: "TwilioCredentials",
    description: str = None,
    sink_sid: str = None,
    types: list = None,
) -> Dict[str, Any]:
    """
    Create a new Subscription.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            A human readable description for the Subscription **This value should
            not contain PII.**.
        sink_sid:
            The SID of the sink that events selected by this subscription should be
            sent to. Sink must be active for the subscription to be
            created.
        types:
            An array of objects containing the subscribed Event Types.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions?](
    https://events.twilio.com/v1/Subscriptions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://events.twilio.com/v1/Subscriptions"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "description": description,
        "sink_sid": sink_sid,
        "types": types,
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
async def delete_v1_subscriptions_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Subscription.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions/{sid}?](
    https://events.twilio.com/v1/Subscriptions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Subscriptions/{sid}"  # noqa
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
async def get_v1_subscriptions_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Subscription.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions/{sid}?](
    https://events.twilio.com/v1/Subscriptions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Subscriptions/{sid}"  # noqa
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
async def post_v1_subscriptions_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    description: str = None,
    sink_sid: str = None,
) -> Dict[str, Any]:
    """
    Update a Subscription.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            A human readable description for the Subscription.
        sink_sid:
            The SID of the sink that events selected by this subscription should be
            sent to. Sink must be active for the subscription to be
            created.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions/{sid}?](
    https://events.twilio.com/v1/Subscriptions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Subscriptions/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "description": description,
        "sink_sid": sink_sid,
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
async def get_v1_subscriptions_subscription_sid_subscribed_events(  # noqa
    subscription_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Subscribed Event types for a Subscription.

    Args:
        subscription_sid:
            Subscription sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents?&page_size=%s](
    https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents"  # noqa
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
async def post_v1_subscriptions_subscription_sid_subscribed_events(  # noqa
    subscription_sid: str,
    twilio_credentials: "TwilioCredentials",
    schema_version: int = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Create a new Subscribed Event type for the subscription.

    Args:
        subscription_sid:
            Subscription sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        schema_version:
            The schema version that the subscription should use.
        type:
            Type of event being subscribed to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents?](
    https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "schema_version": schema_version,
        "type": type,
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
async def delete_v1_subscriptions_subscription_sid_subscribed_events_type(  # noqa
    subscription_sid: str,
    type: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an event type from a subscription.

    Args:
        subscription_sid:
            Subscription sid used in formatting the endpoint URL.
        type:
            Type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}?](
    https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}"  # noqa
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
async def get_v1_subscriptions_subscription_sid_subscribed_events_type(  # noqa
    subscription_sid: str,
    type: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Read an Event for a Subscription.

    Args:
        subscription_sid:
            Subscription sid used in formatting the endpoint URL.
        type:
            Type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}?](
    https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}"  # noqa
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
async def post_v1_subscriptions_subscription_sid_subscribed_events_type(  # noqa
    subscription_sid: str,
    type: str,
    twilio_credentials: "TwilioCredentials",
    schema_version: int = None,
) -> Dict[str, Any]:
    """
    Update an Event for a Subscription.

    Args:
        subscription_sid:
            Subscription sid used in formatting the endpoint URL.
        type:
            Type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        schema_version:
            The schema version that the subscription should use.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}?](
    https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "schema_version": schema_version,
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
async def get_v1_types(
    twilio_credentials: "TwilioCredentials",
    schema_id: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a paginated list of all the available Event Types.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        schema_id:
            A string parameter filtering the results to return only the Event Types
            using a given schema.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Types?&schema_id=%s&page_size=%s](
    https://events.twilio.com/v1/Types?&schema_id=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://events.twilio.com/v1/Types"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "schema_id": schema_id,
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
async def get_v1_types_type(
    type: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Event Type.

    Args:
        type:
            Type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://events.twilio.com/v1/Types/{type}?](
    https://events.twilio.com/v1/Types/{type}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://events.twilio.com/v1/Types/{type}"  # noqa
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
