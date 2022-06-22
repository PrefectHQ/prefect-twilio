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
async def get_v1_services(
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
    [https://sync.twilio.com/v1/Services?&page_size=%s](
    https://sync.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://sync.twilio.com/v1/Services"  # noqa

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
async def post_v1_services(
    twilio_credentials: "TwilioCredentials",
    acl_enabled: bool = None,
    friendly_name: str = None,
    reachability_debouncing_enabled: bool = None,
    reachability_debouncing_window: int = None,
    reachability_webhooks_enabled: bool = None,
    webhook_url: str = None,
    webhooks_from_rest_enabled: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        acl_enabled:
            Whether token identities in the Service must be granted access to Sync
            objects by using the
            [Permissions](https://www.twilio.com/docs/sync/api/sync-
            permissions) resource.
        friendly_name:
            A string that you assign to describe the resource.
        reachability_debouncing_enabled:
            Whether every `endpoint_disconnected` event should occur after a
            configurable delay. The default is `false`, where the
            `endpoint_disconnected` event occurs immediately after
            disconnection. When `true`, intervening reconnections can
            prevent the `endpoint_disconnected` event.
        reachability_debouncing_window:
            The reachability event delay in milliseconds if
            `reachability_debouncing_enabled` = `true`.  Must be between
            1,000 and 30,000 and defaults to 5,000. This is the number
            of milliseconds after the last running client disconnects,
            and a Sync identity is declared offline, before the
            `webhook_url` is called if all endpoints remain offline. A
            reconnection from the same identity by any endpoint during
            this interval prevents the call to `webhook_url`.
        reachability_webhooks_enabled:
            Whether the service instance should call `webhook_url` when client
            endpoints connect to Sync. The default is `false`.
        webhook_url:
            The URL we should call when Sync objects are manipulated.
        webhooks_from_rest_enabled:
            Whether the Service instance should call `webhook_url` when the REST API
            is used to update Sync objects. The default is `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services?](
    https://sync.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://sync.twilio.com/v1/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "acl_enabled": acl_enabled,
        "friendly_name": friendly_name,
        "reachability_debouncing_enabled": reachability_debouncing_enabled,
        "reachability_debouncing_window": reachability_debouncing_window,
        "reachability_webhooks_enabled": reachability_webhooks_enabled,
        "webhook_url": webhook_url,
        "webhooks_from_rest_enabled": webhooks_from_rest_enabled,
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
async def get_v1_services_service_sid_documents(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Documents?&page_size=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Documents?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Documents"  # noqa
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
async def post_v1_services_service_sid_documents(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    data: str = None,
    ttl: int = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        data:
            A JSON string that represents an arbitrary, schema-less object that the
            Sync Document stores. Can be up to 16 KiB in length.
        ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Sync Document expires and
            is deleted (the Sync Document's time-to-live).
        unique_name:
            An application-defined string that uniquely identifies the Sync Document.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Documents?](
    https://sync.twilio.com/v1/Services/{service_sid}/Documents?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Documents"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "data": data,
        "ttl": ttl,
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


@task
async def get_v1_services_service_sid_documents_document_sid_permissions(  # noqa
    service_sid: str,
    document_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Permissions applying to a Sync Document.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        document_sid:
            Document sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions?&page_size=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions"  # noqa
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
async def delete_v1_services_service_sid_documents_document_sid_permissions_identity(  # noqa
    service_sid: str,
    document_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Sync Document Permission.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        document_sid:
            Document sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}"  # noqa
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
async def get_v1_services_service_sid_documents_document_sid_permissions_identity(  # noqa
    service_sid: str,
    document_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Sync Document Permission.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        document_sid:
            Document sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}"  # noqa
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
async def post_v1_services_service_sid_documents_document_sid_permissions_identity(  # noqa
    service_sid: str,
    document_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    manage: bool = None,
    read: bool = None,
    write: bool = None,
) -> Dict[str, Any]:
    """
    Update an identity's access to a specific Sync Document.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        document_sid:
            Document sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        manage:
            Whether the identity can delete the Sync Document. Default value is
            `false`.
        read:
            Whether the identity can read the Sync Document. Default value is
            `false`.
        write:
            Whether the identity can update the Sync Document. Default value is
            `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "manage": manage,
        "read": read,
        "write": write,
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
async def delete_v1_services_service_sid_documents_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Documents/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Documents/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Documents/{sid}"  # noqa
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
async def get_v1_services_service_sid_documents_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Documents/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Documents/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Documents/{sid}"  # noqa
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
async def post_v1_services_service_sid_documents_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
    data: str = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            The If-Match HTTP request header.
        data:
            A JSON string that represents an arbitrary, schema-less object that the
            Sync Document stores. Can be up to 16 KiB in length.
        ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Sync Document expires and
            is deleted (time-to-live).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Documents/{sid}?&if_match=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Documents/{sid}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Documents/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    data = {
        "data": data,
        "ttl": ttl,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_services_service_sid_lists(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists?&page_size=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists"  # noqa
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
async def post_v1_services_service_sid_lists(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    collection_ttl: int = None,
    ttl: int = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        collection_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Sync List expires (time-to-
            live) and is deleted.
        ttl:
            Alias for collection_ttl. If both are provided, this value is ignored.
        unique_name:
            An application-defined string that uniquely identifies the resource.
            This value must be unique within its Service and it can be
            up to 320 characters long. The `unique_name` value can be
            used as an alternative to the `sid` in the URL path to
            address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists?](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "collection_ttl": collection_ttl,
        "ttl": ttl,
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


@task
async def get_v1_services_service_sid_lists_list_sid_items(
    service_sid: str,
    list_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    from_: str = None,
    bounds: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        list_sid:
            List sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            How to order the List Items returned by their `index` value. Can be:
            `asc` (ascending) or `desc` (descending) and the default is
            ascending.
        from_:
            The `index` of the first Sync List Item resource to read. See also
            `bounds`.
        bounds:
            Whether to include the List Item referenced by the `from` parameter. Can
            be: `inclusive` to include the List Item referenced by the
            `from` parameter or `exclusive` to start with the next List
            Item. The default value is `inclusive`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items?&order=%s&from_=%s&bounds=%s&page_size=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items?&order=%s&from_=%s&bounds=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
        "from_": from_,
        "bounds": bounds,
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
async def post_v1_services_service_sid_lists_list_sid_items(
    service_sid: str,
    list_sid: str,
    twilio_credentials: "TwilioCredentials",
    collection_ttl: int = None,
    data: str = None,
    item_ttl: int = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        list_sid:
            List sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        collection_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the List Item's parent Sync
            List expires (time-to-live) and is deleted.
        data:
            A JSON string that represents an arbitrary, schema-less object that the
            List Item stores. Can be up to 16 KiB in length.
        item_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the List Item expires (time-to-
            live) and is deleted.
        ttl:
            An alias for `item_ttl`. If both parameters are provided, this value is
            ignored.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items?](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "collection_ttl": collection_ttl,
        "data": data,
        "item_ttl": item_ttl,
        "ttl": ttl,
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
async def delete_v1_services_service_sid_lists_list_sid_items_index(
    service_sid: str,
    list_sid: str,
    index: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        list_sid:
            List sid used in formatting the endpoint URL.
        index:
            Index used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            If provided, applies this mutation if (and only if) the “revision” field
            of this [map item] matches the provided value. This matches
            the semantics of (and is implemented with) the HTTP [If-
            Match header](https://developer.mozilla.org/en-
            US/docs/Web/HTTP/Headers/If-Match).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}?&if_match=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v1_services_service_sid_lists_list_sid_items_index(
    service_sid: str,
    list_sid: str,
    index: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        list_sid:
            List sid used in formatting the endpoint URL.
        index:
            Index used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}"  # noqa
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
async def post_v1_services_service_sid_lists_list_sid_items_index(
    service_sid: str,
    list_sid: str,
    index: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
    collection_ttl: int = None,
    data: str = None,
    item_ttl: int = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        list_sid:
            List sid used in formatting the endpoint URL.
        index:
            Index used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            If provided, applies this mutation if (and only if) the “revision” field
            of this [map item] matches the provided value. This matches
            the semantics of (and is implemented with) the HTTP [If-
            Match header](https://developer.mozilla.org/en-
            US/docs/Web/HTTP/Headers/If-Match).
        collection_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the List Item's parent Sync
            List expires (time-to-live) and is deleted. This parameter
            can only be used when the List Item's `data` or `ttl` is
            updated in the same request.
        data:
            A JSON string that represents an arbitrary, schema-less object that the
            List Item stores. Can be up to 16 KiB in length.
        item_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the List Item expires (time-to-
            live) and is deleted.
        ttl:
            An alias for `item_ttl`. If both parameters are provided, this value is
            ignored.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}?&if_match=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    data = {
        "collection_ttl": collection_ttl,
        "data": data,
        "item_ttl": item_ttl,
        "ttl": ttl,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_services_service_sid_lists_list_sid_permissions(
    service_sid: str,
    list_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Permissions applying to a Sync List.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        list_sid:
            List sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions?&page_size=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions"  # noqa
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
async def delete_v1_services_service_sid_lists_list_sid_permissions_identity(  # noqa
    service_sid: str,
    list_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Sync List Permission.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        list_sid:
            List sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}"  # noqa
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
async def get_v1_services_service_sid_lists_list_sid_permissions_identity(  # noqa
    service_sid: str,
    list_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Sync List Permission.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        list_sid:
            List sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}"  # noqa
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
async def post_v1_services_service_sid_lists_list_sid_permissions_identity(  # noqa
    service_sid: str,
    list_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    manage: bool = None,
    read: bool = None,
    write: bool = None,
) -> Dict[str, Any]:
    """
    Update an identity's access to a specific Sync List.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        list_sid:
            List sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        manage:
            Whether the identity can delete the Sync List. Default value is `false`.
        read:
            Whether the identity can read the Sync List and its Items. Default value
            is `false`.
        write:
            Whether the identity can create, update, and delete Items in the Sync
            List. Default value is `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "manage": manage,
        "read": read,
        "write": write,
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
async def delete_v1_services_service_sid_lists_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{sid}"  # noqa
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
async def get_v1_services_service_sid_lists_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{sid}"  # noqa
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
async def post_v1_services_service_sid_lists_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    collection_ttl: int = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        collection_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Sync List expires (time-to-
            live) and is deleted.
        ttl:
            An alias for `collection_ttl`. If both are provided, this value is
            ignored.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Lists/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Lists/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Lists/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "collection_ttl": collection_ttl,
        "ttl": ttl,
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
async def get_v1_services_service_sid_maps(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps?&page_size=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps"  # noqa
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
async def post_v1_services_service_sid_maps(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    collection_ttl: int = None,
    ttl: int = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        collection_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Sync Map expires (time-to-
            live) and is deleted.
        ttl:
            An alias for `collection_ttl`. If both parameters are provided, this
            value is ignored.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used as an alternative to the `sid` in the URL path
            to address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps?](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "collection_ttl": collection_ttl,
        "ttl": ttl,
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


@task
async def get_v1_services_service_sid_maps_map_sid_items(
    service_sid: str,
    map_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    from_: str = None,
    bounds: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        map_sid:
            Map sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            How to order the Map Items returned by their `key` value. Can be: `asc`
            (ascending) or `desc` (descending) and the default is
            ascending. Map Items are [ordered
            lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order)
            by Item key.
        from_:
            The `key` of the first Sync Map Item resource to read. See also
            `bounds`.
        bounds:
            Whether to include the Map Item referenced by the `from` parameter. Can
            be: `inclusive` to include the Map Item referenced by the
            `from` parameter or `exclusive` to start with the next Map
            Item. The default value is `inclusive`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items?&order=%s&from_=%s&bounds=%s&page_size=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items?&order=%s&from_=%s&bounds=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
        "from_": from_,
        "bounds": bounds,
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
async def post_v1_services_service_sid_maps_map_sid_items(
    service_sid: str,
    map_sid: str,
    twilio_credentials: "TwilioCredentials",
    collection_ttl: int = None,
    data: str = None,
    item_ttl: int = None,
    key: str = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        map_sid:
            Map sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        collection_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Map Item's parent Sync Map
            expires (time-to-live) and is deleted.
        data:
            A JSON string that represents an arbitrary, schema-less object that the
            Map Item stores. Can be up to 16 KiB in length.
        item_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Map Item expires (time-to-
            live) and is deleted.
        key:
            The unique, user-defined key for the Map Item. Can be up to 320
            characters long.
        ttl:
            An alias for `item_ttl`. If both parameters are provided, this value is
            ignored.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items?](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "collection_ttl": collection_ttl,
        "data": data,
        "item_ttl": item_ttl,
        "key": key,
        "ttl": ttl,
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
async def delete_v1_services_service_sid_maps_map_sid_items_key(
    service_sid: str,
    map_sid: str,
    key: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        map_sid:
            Map sid used in formatting the endpoint URL.
        key:
            Key used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            If provided, applies this mutation if (and only if) the “revision” field
            of this [map item] matches the provided value. This matches
            the semantics of (and is implemented with) the HTTP [If-
            Match header](https://developer.mozilla.org/en-
            US/docs/Web/HTTP/Headers/If-Match).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}?&if_match=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v1_services_service_sid_maps_map_sid_items_key(
    service_sid: str,
    map_sid: str,
    key: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        map_sid:
            Map sid used in formatting the endpoint URL.
        key:
            Key used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}"  # noqa
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
async def post_v1_services_service_sid_maps_map_sid_items_key(
    service_sid: str,
    map_sid: str,
    key: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
    collection_ttl: int = None,
    data: str = None,
    item_ttl: int = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        map_sid:
            Map sid used in formatting the endpoint URL.
        key:
            Key used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            If provided, applies this mutation if (and only if) the “revision” field
            of this [map item] matches the provided value. This matches
            the semantics of (and is implemented with) the HTTP [If-
            Match header](https://developer.mozilla.org/en-
            US/docs/Web/HTTP/Headers/If-Match).
        collection_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Map Item's parent Sync Map
            expires (time-to-live) and is deleted. This parameter can
            only be used when the Map Item's `data` or `ttl` is updated
            in the same request.
        data:
            A JSON string that represents an arbitrary, schema-less object that the
            Map Item stores. Can be up to 16 KiB in length.
        item_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Map Item expires (time-to-
            live) and is deleted.
        ttl:
            An alias for `item_ttl`. If both parameters are provided, this value is
            ignored.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}?&if_match=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    data = {
        "collection_ttl": collection_ttl,
        "data": data,
        "item_ttl": item_ttl,
        "ttl": ttl,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_services_service_sid_maps_map_sid_permissions(
    service_sid: str,
    map_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Permissions applying to a Sync Map.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        map_sid:
            Map sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions?&page_size=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions"  # noqa
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
async def delete_v1_services_service_sid_maps_map_sid_permissions_identity(  # noqa
    service_sid: str,
    map_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Sync Map Permission.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        map_sid:
            Map sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}"  # noqa
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
async def get_v1_services_service_sid_maps_map_sid_permissions_identity(  # noqa
    service_sid: str,
    map_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Sync Map Permission.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        map_sid:
            Map sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}"  # noqa
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
async def post_v1_services_service_sid_maps_map_sid_permissions_identity(  # noqa
    service_sid: str,
    map_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    manage: bool = None,
    read: bool = None,
    write: bool = None,
) -> Dict[str, Any]:
    """
    Update an identity's access to a specific Sync Map.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        map_sid:
            Map sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        manage:
            Whether the identity can delete the Sync Map. Default value is `false`.
        read:
            Whether the identity can read the Sync Map and its Items. Default value
            is `false`.
        write:
            Whether the identity can create, update, and delete Items in the Sync
            Map. Default value is `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "manage": manage,
        "read": read,
        "write": write,
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
async def delete_v1_services_service_sid_maps_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{sid}"  # noqa
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
async def get_v1_services_service_sid_maps_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{sid}"  # noqa
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
async def post_v1_services_service_sid_maps_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    collection_ttl: int = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        collection_ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Sync Map expires (time-to-
            live) and is deleted.
        ttl:
            An alias for `collection_ttl`. If both parameters are provided, this
            value is ignored.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Maps/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Maps/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Maps/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "collection_ttl": collection_ttl,
        "ttl": ttl,
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
async def get_v1_services_service_sid_streams(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Streams in a Service Instance.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Streams?&page_size=%s](
    https://sync.twilio.com/v1/Services/{service_sid}/Streams?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Streams"  # noqa
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
async def post_v1_services_service_sid_streams(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    ttl: int = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Stream.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Stream expires and is
            deleted (time-to-live).
        unique_name:
            An application-defined string that uniquely identifies the resource.
            This value must be unique within its Service and it can be
            up to 320 characters long. The `unique_name` value can be
            used as an alternative to the `sid` in the URL path to
            address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Streams?](
    https://sync.twilio.com/v1/Services/{service_sid}/Streams?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Streams"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "ttl": ttl,
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


@task
async def delete_v1_services_service_sid_streams_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Stream.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Streams/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Streams/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Streams/{sid}"  # noqa
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
async def get_v1_services_service_sid_streams_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Stream.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Streams/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Streams/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Streams/{sid}"  # noqa
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
async def post_v1_services_service_sid_streams_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    ttl: int = None,
) -> Dict[str, Any]:
    """
    Update a specific Stream.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ttl:
            How long, [in seconds](https://www.twilio.com/docs/sync/limits
            sync-payload-limits), before the Stream expires and is
            deleted (time-to-live).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Streams/{sid}?](
    https://sync.twilio.com/v1/Services/{service_sid}/Streams/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Streams/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "ttl": ttl,
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
async def post_v1_services_service_sid_streams_stream_sid_messages(  # noqa
    service_sid: str,
    stream_sid: str,
    twilio_credentials: "TwilioCredentials",
    data: str = None,
) -> Dict[str, Any]:
    """
    Create a new Stream Message.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        stream_sid:
            Stream sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        data:
            A JSON string that represents an arbitrary, schema-less object that
            makes up the Stream Message body. Can be up to 4 KiB in
            length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{service_sid}/Streams/{stream_sid}/Messages?](
    https://sync.twilio.com/v1/Services/{service_sid}/Streams/{stream_sid}/Messages?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{service_sid}/Streams/{stream_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "data": data,
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
async def delete_v1_services_sid(
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
    [https://sync.twilio.com/v1/Services/{sid}?](
    https://sync.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{sid}"  # noqa
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
async def get_v1_services_sid(
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
    [https://sync.twilio.com/v1/Services/{sid}?](
    https://sync.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{sid}"  # noqa
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
async def post_v1_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    acl_enabled: bool = None,
    friendly_name: str = None,
    reachability_debouncing_enabled: bool = None,
    reachability_debouncing_window: int = None,
    reachability_webhooks_enabled: bool = None,
    webhook_url: str = None,
    webhooks_from_rest_enabled: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        acl_enabled:
            Whether token identities in the Service must be granted access to Sync
            objects by using the
            [Permissions](https://www.twilio.com/docs/sync/api/sync-
            permissions) resource.
        friendly_name:
            A string that you assign to describe the resource.
        reachability_debouncing_enabled:
            Whether every `endpoint_disconnected` event should occur after a
            configurable delay. The default is `false`, where the
            `endpoint_disconnected` event occurs immediately after
            disconnection. When `true`, intervening reconnections can
            prevent the `endpoint_disconnected` event.
        reachability_debouncing_window:
            The reachability event delay in milliseconds if
            `reachability_debouncing_enabled` = `true`.  Must be between
            1,000 and 30,000 and defaults to 5,000. This is the number
            of milliseconds after the last running client disconnects,
            and a Sync identity is declared offline, before the webhook
            is called if all endpoints remain offline. A reconnection
            from the same identity by any endpoint during this interval
            prevents the webhook from being called.
        reachability_webhooks_enabled:
            Whether the service instance should call `webhook_url` when client
            endpoints connect to Sync. The default is `false`.
        webhook_url:
            The URL we should call when Sync objects are manipulated.
        webhooks_from_rest_enabled:
            Whether the Service instance should call `webhook_url` when the REST API
            is used to update Sync objects. The default is `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://sync.twilio.com/v1/Services/{sid}?](
    https://sync.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://sync.twilio.com/v1/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "acl_enabled": acl_enabled,
        "friendly_name": friendly_name,
        "reachability_debouncing_enabled": reachability_debouncing_enabled,
        "reachability_debouncing_window": reachability_debouncing_window,
        "reachability_webhooks_enabled": reachability_webhooks_enabled,
        "webhook_url": webhook_url,
        "webhooks_from_rest_enabled": webhooks_from_rest_enabled,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
