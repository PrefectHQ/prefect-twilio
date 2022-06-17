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
    [https://chat.twilio.com/v1/Services?&page_size=%s](
    https://chat.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://chat.twilio.com/v1/Services"  # noqa

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
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services?](
    https://chat.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://chat.twilio.com/v1/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v1_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    type: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        type:
            The visibility of the Channels to read. Can be: `public` or `private`
            and defaults to `public`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels?&type=%s&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels?&type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "type": type,
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
async def post_v1_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    type: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        type:
            The visibility of the channel. Can be: `public` or `private` and
            defaults to `public`.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL. This value must be 64
            characters or less in length and be unique within the
            Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "type": type,
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
async def get_v1_services_service_sid_channels_channel_sid_invites(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)'s
            `identity` value of the resources to read. See [access
            tokens](https://www.twilio.com/docs/api/chat/guides/create-
            tokens) for more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v1_services_service_sid_channels_channel_sid_invites(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/api/chat/rest/v1/user)
            within the
            [Service](https://www.twilio.com/docs/api/chat/rest/v1/service).
            See [access
            tokens](https://www.twilio.com/docs/api/chat/guides/create-
            tokens) for more info.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            assigned to the new member.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v1_services_service_sid_channels_channel_sid_invites_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_invites_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_members(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)'s
            `identity` value of the resources to read. See [access
            tokens](https://www.twilio.com/docs/api/chat/guides/create-
            tokens) for more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v1_services_service_sid_channels_channel_sid_members(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/api/chat/rest/v1/user)
            within the
            [Service](https://www.twilio.com/docs/api/chat/rest/services).
            See [access
            tokens](https://www.twilio.com/docs/api/chat/guides/create-
            tokens) for more details.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            to assign to the member. The default roles are those
            specified on the
            [Service](https://www.twilio.com/docs/chat/api/services).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v1_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
async def post_v1_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    last_consumed_message_index: int = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        last_consumed_message_index:
            The index of the last
            [Message](https://www.twilio.com/docs/api/chat/rest/messages)
            that the Member has read within the
            [Channel](https://www.twilio.com/docs/api/chat/rest/channels).
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            to assign to the member. The default roles are those
            specified on the
            [Service](https://www.twilio.com/docs/chat/api/services).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "last_consumed_message_index": last_consumed_message_index,
        "role_sid": role_sid,
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
async def get_v1_services_service_sid_channels_channel_sid_messages(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            The sort order of the returned messages. Can be: `asc` (ascending) or
            `desc` (descending) with `asc` as the default.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
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
async def post_v1_services_service_sid_channels_channel_sid_messages(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    body: str = None,
    from_: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            A valid JSON string that contains application-specific data.
        body:
            The message to send to the channel. Can also be an empty string or
            `null`, which sets the value as an empty string. You can
            send structured data in the body by serializing it as a
            string.
        from_:
            The [identity](https://www.twilio.com/docs/api/chat/guides/identity) of
            the new message's author. The default value is `system`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "body": body,
        "from_": from_,
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
async def delete_v1_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
async def post_v1_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    body: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            A valid JSON string that contains application-specific data.
        body:
            The message to send to the channel. Can also be an empty string or
            `null`, which sets the value as an empty string. You can
            send structured data in the body by serializing it as a
            string.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
        "body": body,
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
async def delete_v1_services_service_sid_channels_sid(
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_sid(
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
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
async def post_v1_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL. This value must be 64
            characters or less in length and be unique within the
            Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
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


@task
async def get_v1_services_service_sid_roles(
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles?&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles"  # noqa
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
async def post_v1_services_service_sid_roles(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    permission: list = None,
    type: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        permission:
            A permission that you grant to the new role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. The values
            for this parameter depend on the role's `type` and are
            described in the documentation.
        type:
            The type of role. Can be: `channel` for
            [Channel](https://www.twilio.com/docs/chat/api/channels)
            roles or `deployment` for
            [Service](https://www.twilio.com/docs/chat/api/services)
            roles.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles?](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "permission": permission,
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
async def delete_v1_services_service_sid_roles_sid(
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
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
async def get_v1_services_service_sid_roles_sid(
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
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
async def post_v1_services_service_sid_roles_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    permission: list = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        permission:
            A permission that you grant to the role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. The values
            for this parameter depend on the role's `type` and are
            described in the documentation.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "permission": permission,
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
async def get_v1_services_service_sid_users(
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Users?&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users"  # noqa
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
async def post_v1_services_service_sid_users(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the new resource. This
            value is often used for display purposes.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/api/chat/rest/v1/user)
            within the
            [Service](https://www.twilio.com/docs/api/chat/rest/v1/service).
            This value is often a username or email address. See the
            Identity documentation for more details.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            assigned to the new User.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Users?](
    https://chat.twilio.com/v1/Services/{service_sid}/Users?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v1_services_service_sid_users_sid(
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
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
async def get_v1_services_service_sid_users_sid(
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
    [https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
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
async def post_v1_services_service_sid_users_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the resource. It is
            often used for display purposes.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles)
            assigned to this user.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "role_sid": role_sid,
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
async def get_v1_services_service_sid_users_user_sid_channels(
    service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all Channels for a given User.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s](
    https://chat.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels"  # noqa
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
    [https://chat.twilio.com/v1/Services/{sid}?](
    https://chat.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{sid}"  # noqa
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
    [https://chat.twilio.com/v1/Services/{sid}?](
    https://chat.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{sid}"  # noqa
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
    consumption_report_interval: int = None,
    default_channel_creator_role_sid: str = None,
    default_channel_role_sid: str = None,
    default_service_role_sid: str = None,
    friendly_name: str = None,
    limits_channel_members: int = None,
    limits_user_channels: int = None,
    notifications_added_to_channel_enabled: bool = None,
    notifications_added_to_channel_template: str = None,
    notifications_invited_to_channel_enabled: bool = None,
    notifications_invited_to_channel_template: str = None,
    notifications_new_message_enabled: bool = None,
    notifications_new_message_template: str = None,
    notifications_removed_from_channel_enabled: bool = None,
    notifications_removed_from_channel_template: str = None,
    post_webhook_url: str = None,
    pre_webhook_url: str = None,
    reachability_enabled: bool = None,
    read_status_enabled: bool = None,
    typing_indicator_timeout: int = None,
    webhook_filters: list = None,
    webhook_method: str = None,
    webhooks_on_channel_add_method: str = None,
    webhooks_on_channel_add_url: str = None,
    webhooks_on_channel_added_method: str = None,
    webhooks_on_channel_added_url: str = None,
    webhooks_on_channel_destroy_method: str = None,
    webhooks_on_channel_destroy_url: str = None,
    webhooks_on_channel_destroyed_method: str = None,
    webhooks_on_channel_destroyed_url: str = None,
    webhooks_on_channel_update_method: str = None,
    webhooks_on_channel_update_url: str = None,
    webhooks_on_channel_updated_method: str = None,
    webhooks_on_channel_updated_url: str = None,
    webhooks_on_member_add_method: str = None,
    webhooks_on_member_add_url: str = None,
    webhooks_on_member_added_method: str = None,
    webhooks_on_member_added_url: str = None,
    webhooks_on_member_remove_method: str = None,
    webhooks_on_member_remove_url: str = None,
    webhooks_on_member_removed_method: str = None,
    webhooks_on_member_removed_url: str = None,
    webhooks_on_message_remove_method: str = None,
    webhooks_on_message_remove_url: str = None,
    webhooks_on_message_removed_method: str = None,
    webhooks_on_message_removed_url: str = None,
    webhooks_on_message_send_method: str = None,
    webhooks_on_message_send_url: str = None,
    webhooks_on_message_sent_method: str = None,
    webhooks_on_message_sent_url: str = None,
    webhooks_on_message_update_method: str = None,
    webhooks_on_message_update_url: str = None,
    webhooks_on_message_updated_method: str = None,
    webhooks_on_message_updated_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        consumption_report_interval:
            DEPRECATED. The interval in seconds between consumption reports
            submission batches from client endpoints.
        default_channel_creator_role_sid:
            The channel role assigned to a channel creator when they join a new
            channel. See the [Roles
            endpoint](https://www.twilio.com/docs/chat/api/roles) for
            more details.
        default_channel_role_sid:
            The channel role assigned to users when they are added to a channel. See
            the [Roles
            endpoint](https://www.twilio.com/docs/chat/api/roles) for
            more details.
        default_service_role_sid:
            The service role assigned to users when they are added to the service.
            See the [Roles
            endpoint](https://www.twilio.com/docs/chat/api/roles) for
            more details.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        limits_channel_members:
            The maximum number of Members that can be added to Channels within this
            Service. Can be up to 1,000.
        limits_user_channels:
            The maximum number of Channels Users can be a Member of within this
            Service. Can be up to 1,000.
        notifications_added_to_channel_enabled:
            Whether to send a notification when a member is added to a channel. Can
            be: `true` or `false` and the default is `false`.
        notifications_added_to_channel_template:
            The template to use to create the notification text displayed when a
            member is added to a channel and
            `notifications.added_to_channel.enabled` is `true`.
        notifications_invited_to_channel_enabled:
            Whether to send a notification when a user is invited to a channel. Can
            be: `true` or `false` and the default is `false`.
        notifications_invited_to_channel_template:
            The template to use to create the notification text displayed when a
            user is invited to a channel and
            `notifications.invited_to_channel.enabled` is `true`.
        notifications_new_message_enabled:
            Whether to send a notification when a new message is added to a channel.
            Can be: `true` or `false` and the default is `false`.
        notifications_new_message_template:
            The template to use to create the notification text displayed when a new
            message is added to a channel and
            `notifications.new_message.enabled` is `true`.
        notifications_removed_from_channel_enabled:
            Whether to send a notification to a user when they are removed from a
            channel. Can be: `true` or `false` and the default is
            `false`.
        notifications_removed_from_channel_template:
            The template to use to create the notification text displayed to a user
            when they are removed from a channel and
            `notifications.removed_from_channel.enabled` is `true`.
        post_webhook_url:
            The URL for post-event webhooks, which are called by using the
            `webhook_method`. See [Webhook
            Events](https://www.twilio.com/docs/api/chat/webhooks) for
            more details.
        pre_webhook_url:
            The URL for pre-event webhooks, which are called by using the
            `webhook_method`. See [Webhook
            Events](https://www.twilio.com/docs/api/chat/webhooks) for
            more details.
        reachability_enabled:
            Whether to enable the [Reachability
            Indicator](https://www.twilio.com/docs/chat/reachability-
            indicator) for this Service instance. The default is
            `false`.
        read_status_enabled:
            Whether to enable the [Message Consumption
            Horizon](https://www.twilio.com/docs/chat/consumption-
            horizon) feature. The default is `true`.
        typing_indicator_timeout:
            How long in seconds after a `started typing` event until clients should
            assume that user is no longer typing, even if no `ended
            typing` message was received.  The default is 5 seconds.
        webhook_filters:
            The list of WebHook events that are enabled for this Service instance.
            See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.
        webhook_method:
            The HTTP method to use for calls to the `pre_webhook_url` and
            `post_webhook_url` webhooks.  Can be: `POST` or `GET` and
            the default is `POST`. See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.
        webhooks_on_channel_add_method:
            The HTTP method to use when calling the `webhooks.on_channel_add.url`.
        webhooks_on_channel_add_url:
            The URL of the webhook to call in response to the `on_channel_add` event
            using the `webhooks.on_channel_add.method` HTTP method.
        webhooks_on_channel_added_method:
            The URL of the webhook to call in response to the `on_channel_added`
            event`.
        webhooks_on_channel_added_url:
            The URL of the webhook to call in response to the `on_channel_added`
            event using the `webhooks.on_channel_added.method` HTTP
            method.
        webhooks_on_channel_destroy_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_destroy.url`.
        webhooks_on_channel_destroy_url:
            The URL of the webhook to call in response to the `on_channel_destroy`
            event using the `webhooks.on_channel_destroy.method` HTTP
            method.
        webhooks_on_channel_destroyed_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_destroyed.url`.
        webhooks_on_channel_destroyed_url:
            The URL of the webhook to call in response to the `on_channel_added`
            event using the `webhooks.on_channel_destroyed.method` HTTP
            method.
        webhooks_on_channel_update_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_update.url`.
        webhooks_on_channel_update_url:
            The URL of the webhook to call in response to the `on_channel_update`
            event using the `webhooks.on_channel_update.method` HTTP
            method.
        webhooks_on_channel_updated_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_updated.url`.
        webhooks_on_channel_updated_url:
            The URL of the webhook to call in response to the `on_channel_updated`
            event using the `webhooks.on_channel_updated.method` HTTP
            method.
        webhooks_on_member_add_method:
            The HTTP method to use when calling the `webhooks.on_member_add.url`.
        webhooks_on_member_add_url:
            The URL of the webhook to call in response to the `on_member_add` event
            using the `webhooks.on_member_add.method` HTTP method.
        webhooks_on_member_added_method:
            The HTTP method to use when calling the
            `webhooks.on_channel_updated.url`.
        webhooks_on_member_added_url:
            The URL of the webhook to call in response to the `on_channel_updated`
            event using the `webhooks.on_channel_updated.method` HTTP
            method.
        webhooks_on_member_remove_method:
            The HTTP method to use when calling the `webhooks.on_member_remove.url`.
        webhooks_on_member_remove_url:
            The URL of the webhook to call in response to the `on_member_remove`
            event using the `webhooks.on_member_remove.method` HTTP
            method.
        webhooks_on_member_removed_method:
            The HTTP method to use when calling the
            `webhooks.on_member_removed.url`.
        webhooks_on_member_removed_url:
            The URL of the webhook to call in response to the `on_member_removed`
            event using the `webhooks.on_member_removed.method` HTTP
            method.
        webhooks_on_message_remove_method:
            The HTTP method to use when calling the
            `webhooks.on_message_remove.url`.
        webhooks_on_message_remove_url:
            The URL of the webhook to call in response to the `on_message_remove`
            event using the `webhooks.on_message_remove.method` HTTP
            method.
        webhooks_on_message_removed_method:
            The HTTP method to use when calling the
            `webhooks.on_message_removed.url`.
        webhooks_on_message_removed_url:
            The URL of the webhook to call in response to the `on_message_removed`
            event using the `webhooks.on_message_removed.method` HTTP
            method.
        webhooks_on_message_send_method:
            The HTTP method to use when calling the `webhooks.on_message_send.url`.
        webhooks_on_message_send_url:
            The URL of the webhook to call in response to the `on_message_send`
            event using the `webhooks.on_message_send.method` HTTP
            method.
        webhooks_on_message_sent_method:
            The URL of the webhook to call in response to the `on_message_sent`
            event`.
        webhooks_on_message_sent_url:
            The URL of the webhook to call in response to the `on_message_sent`
            event using the `webhooks.on_message_sent.method` HTTP
            method.
        webhooks_on_message_update_method:
            The HTTP method to use when calling the
            `webhooks.on_message_update.url`.
        webhooks_on_message_update_url:
            The URL of the webhook to call in response to the `on_message_update`
            event using the `webhooks.on_message_update.method` HTTP
            method.
        webhooks_on_message_updated_method:
            The HTTP method to use when calling the
            `webhooks.on_message_updated.url`.
        webhooks_on_message_updated_url:
            The URL of the webhook to call in response to the `on_message_updated`
            event using the `webhooks.on_message_updated.method` HTTP
            method.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v1/Services/{sid}?](
    https://chat.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v1/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "consumption_report_interval": consumption_report_interval,
        "default_channel_creator_role_sid": default_channel_creator_role_sid,
        "default_channel_role_sid": default_channel_role_sid,
        "default_service_role_sid": default_service_role_sid,
        "friendly_name": friendly_name,
        "limits_channel_members": limits_channel_members,
        "limits_user_channels": limits_user_channels,
        "notifications_added_to_channel_enabled": notifications_added_to_channel_enabled,  # noqa
        "notifications_added_to_channel_template": notifications_added_to_channel_template,  # noqa
        "notifications_invited_to_channel_enabled": notifications_invited_to_channel_enabled,  # noqa
        "notifications_invited_to_channel_template": notifications_invited_to_channel_template,  # noqa
        "notifications_new_message_enabled": notifications_new_message_enabled,
        "notifications_new_message_template": notifications_new_message_template,
        "notifications_removed_from_channel_enabled": notifications_removed_from_channel_enabled,  # noqa
        "notifications_removed_from_channel_template": notifications_removed_from_channel_template,  # noqa
        "post_webhook_url": post_webhook_url,
        "pre_webhook_url": pre_webhook_url,
        "reachability_enabled": reachability_enabled,
        "read_status_enabled": read_status_enabled,
        "typing_indicator_timeout": typing_indicator_timeout,
        "webhook_filters": webhook_filters,
        "webhook_method": webhook_method,
        "webhooks_on_channel_add_method": webhooks_on_channel_add_method,
        "webhooks_on_channel_add_url": webhooks_on_channel_add_url,
        "webhooks_on_channel_added_method": webhooks_on_channel_added_method,
        "webhooks_on_channel_added_url": webhooks_on_channel_added_url,
        "webhooks_on_channel_destroy_method": webhooks_on_channel_destroy_method,
        "webhooks_on_channel_destroy_url": webhooks_on_channel_destroy_url,
        "webhooks_on_channel_destroyed_method": webhooks_on_channel_destroyed_method,  # noqa
        "webhooks_on_channel_destroyed_url": webhooks_on_channel_destroyed_url,
        "webhooks_on_channel_update_method": webhooks_on_channel_update_method,
        "webhooks_on_channel_update_url": webhooks_on_channel_update_url,
        "webhooks_on_channel_updated_method": webhooks_on_channel_updated_method,
        "webhooks_on_channel_updated_url": webhooks_on_channel_updated_url,
        "webhooks_on_member_add_method": webhooks_on_member_add_method,
        "webhooks_on_member_add_url": webhooks_on_member_add_url,
        "webhooks_on_member_added_method": webhooks_on_member_added_method,
        "webhooks_on_member_added_url": webhooks_on_member_added_url,
        "webhooks_on_member_remove_method": webhooks_on_member_remove_method,
        "webhooks_on_member_remove_url": webhooks_on_member_remove_url,
        "webhooks_on_member_removed_method": webhooks_on_member_removed_method,
        "webhooks_on_member_removed_url": webhooks_on_member_removed_url,
        "webhooks_on_message_remove_method": webhooks_on_message_remove_method,
        "webhooks_on_message_remove_url": webhooks_on_message_remove_url,
        "webhooks_on_message_removed_method": webhooks_on_message_removed_method,
        "webhooks_on_message_removed_url": webhooks_on_message_removed_url,
        "webhooks_on_message_send_method": webhooks_on_message_send_method,
        "webhooks_on_message_send_url": webhooks_on_message_send_url,
        "webhooks_on_message_sent_method": webhooks_on_message_sent_method,
        "webhooks_on_message_sent_url": webhooks_on_message_sent_url,
        "webhooks_on_message_update_method": webhooks_on_message_update_method,
        "webhooks_on_message_update_url": webhooks_on_message_update_url,
        "webhooks_on_message_updated_method": webhooks_on_message_updated_method,
        "webhooks_on_message_updated_url": webhooks_on_message_updated_url,
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
async def get_v2_services(
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
    [https://chat.twilio.com/v2/Services?&page_size=%s](
    https://chat.twilio.com/v2/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://chat.twilio.com/v2/Services"  # noqa

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
async def post_v2_services(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the new resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services?](
    https://chat.twilio.com/v2/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://chat.twilio.com/v2/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v2_services_service_sid_bindings(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    binding_type: list = None,
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_type:
            The push technology used by the Binding resources to read.  Can be:
            `apn`, `gcm`, or `fcm`.  See [push notification
            configuration](https://www.twilio.com/docs/chat/push-
            notification-configuration) for more info.
        identity:
            The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s
            `identity` value of the resources to read. See [access
            tokens](https://www.twilio.com/docs/chat/create-tokens) for
            more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Bindings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "binding_type": binding_type,
        "identity": identity,
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
async def delete_v2_services_service_sid_bindings_sid(
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_bindings_sid(
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    type: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        type:
            The visibility of the Channels to read. Can be: `public` or `private`
            and defaults to `public`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels?&type=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels?&type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "type": type,
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
async def post_v2_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    created_by: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    type: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A valid JSON string that contains application-specific data.
        created_by:
            The `identity` of the User that created the channel. Default is:
            `system`.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            Note that this should only be used in cases where a Channel
            is being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated. The
            default value is `null`. Note that this parameter should
            only be used in cases where a Channel is being recreated
            from a backup/separate source  and where a Message was
            previously updated.
        friendly_name:
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        type:
            The visibility of the channel. Can be: `public` or `private` and
            defaults to `public`.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the Channel
            resource's `sid` in the URL. This value must be 64
            characters or less in length and be unique within the
            Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "created_by": created_by,
        "date_created": date_created,
        "date_updated": date_updated,
        "friendly_name": friendly_name,
        "type": type,
        "unique_name": unique_name,
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
async def get_v2_services_service_sid_channels_channel_sid_invites(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s
            `identity` value of the resources to read. See [access
            tokens](https://www.twilio.com/docs/chat/create-tokens) for
            more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v2_services_service_sid_channels_channel_sid_invites(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource). See [access
            tokens](https://www.twilio.com/docs/chat/create-tokens) for
            more info.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) assigned to the new member.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v2_services_service_sid_channels_channel_sid_invites_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels_channel_sid_invites_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels_channel_sid_members(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s
            `identity` value of the Member resources to read. See
            [access tokens](https://www.twilio.com/docs/chat/create-
            tokens) for more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v2_services_service_sid_channels_channel_sid_members(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    identity: str = None,
    last_consumed_message_index: int = None,
    last_consumption_timestamp: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A valid JSON string that contains application-specific data.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            Note that this parameter should only be used when a Member
            is being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated. The
            default value is `null`. Note that this parameter should
            only be used when a Member is being recreated from a
            backup/separate source and where a Member was previously
            updated.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource). See [access
            tokens](https://www.twilio.com/docs/chat/create-tokens) for
            more info.
        last_consumed_message_index:
            The index of the last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) in the
            [Channel](https://www.twilio.com/docs/chat/channels) that
            the Member has read. This parameter should only be used when
            recreating a Member from a backup/separate source.
        last_consumption_timestamp:
            The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the
            last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) read event for the Member within the
            [Channel](https://www.twilio.com/docs/chat/channels).
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) to assign to the member. The default roles are
            those specified on the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "identity": identity,
        "last_consumed_message_index": last_consumed_message_index,
        "last_consumption_timestamp": last_consumption_timestamp,
        "role_sid": role_sid,
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
async def delete_v2_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v2_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    last_consumed_message_index: int = None,
    last_consumption_timestamp: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A valid JSON string that contains application-specific data.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            Note that this parameter should only be used when a Member
            is being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated.
        last_consumed_message_index:
            The index of the last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) that the Member has read within the
            [Channel](https://www.twilio.com/docs/chat/channels).
        last_consumption_timestamp:
            The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the
            last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) read event for the Member within the
            [Channel](https://www.twilio.com/docs/chat/channels).
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) to assign to the member. The default roles are
            those specified on the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "last_consumed_message_index": last_consumed_message_index,
        "last_consumption_timestamp": last_consumption_timestamp,
        "role_sid": role_sid,
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
async def get_v2_services_service_sid_channels_channel_sid_messages(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            The sort order of the returned messages. Can be: `asc` (ascending) or
            `desc` (descending) with `asc` as the default.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
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
async def post_v2_services_service_sid_channels_channel_sid_messages(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
    from_: str = None,
    last_updated_by: str = None,
    media_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A valid JSON string that contains application-specific data.
        body:
            The message to send to the channel. Can be an empty string or `null`,
            which sets the value as an empty string. You can send
            structured data in the body by serializing it as a string.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            This parameter should only be used when a Chat's history is
            being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated.
        from_:
            The [Identity](https://www.twilio.com/docs/chat/identity) of the new
            message's author. The default value is `system`.
        last_updated_by:
            The [Identity](https://www.twilio.com/docs/chat/identity) of the User
            who last updated the Message, if applicable.
        media_sid:
            The SID of the [Media](https://www.twilio.com/docs/chat/rest/media) to
            attach to the new Message.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
        "from_": from_,
        "last_updated_by": last_updated_by,
        "media_sid": media_sid,
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
async def delete_v2_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v2_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
    from_: str = None,
    last_updated_by: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A valid JSON string that contains application-specific data.
        body:
            The message to send to the channel. Can be an empty string or `null`,
            which sets the value as an empty string. You can send
            structured data in the body by serializing it as a string.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            This parameter should only be used when a Chat's history is
            being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated.
        from_:
            The [Identity](https://www.twilio.com/docs/chat/identity) of the
            message's author.
        last_updated_by:
            The [Identity](https://www.twilio.com/docs/chat/identity) of the User
            who last updated the Message, if applicable.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
        "from_": from_,
        "last_updated_by": last_updated_by,
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
async def get_v2_services_service_sid_channels_channel_sid_webhooks(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_retry_count: int = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:
            The events that cause us to call the Channel Webhook. Used when `type`
            is `webhook`. This parameter takes only one event. To
            specify more than one event, repeat this parameter for each
            event. For the list of possible events, see [Webhook Event
            Triggers](https://www.twilio.com/docs/chat/webhook-events
            webhook-event-trigger).
        configuration_flow_sid:
            The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-
            api/flow) to call when an event in `configuration.filters`
            occurs. Used only when `type` is `studio`.
        configuration_method:
            The HTTP method used to call `configuration.url`. Can be: `GET` or
            `POST` and the default is `POST`.
        configuration_retry_count:
            The number of times to retry the webhook if the first attempt fails. Can
            be an integer between 0 and 3, inclusive, and the default is
            0.
        configuration_triggers:
            A string that will cause us to call the webhook when it is present in a
            message body. This parameter takes only one trigger string.
            To specify more than one, repeat this parameter for each
            trigger string up to a total of 5 trigger strings. Used only
            when `type` = `trigger`.
        configuration_url:
            The URL of the webhook to call using the `configuration.method`.
        type:
            The type of webhook. Can be: `webhook`, `studio`, or `trigger`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_retry_count": configuration_retry_count,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
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
async def delete_v2_services_service_sid_channels_channel_sid_webhooks_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels_channel_sid_webhooks_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_retry_count: int = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:
            The events that cause us to call the Channel Webhook. Used when `type`
            is `webhook`. This parameter takes only one event. To
            specify more than one event, repeat this parameter for each
            event. For the list of possible events, see [Webhook Event
            Triggers](https://www.twilio.com/docs/chat/webhook-events
            webhook-event-trigger).
        configuration_flow_sid:
            The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-
            api/flow) to call when an event in `configuration.filters`
            occurs. Used only when `type` = `studio`.
        configuration_method:
            The HTTP method used to call `configuration.url`. Can be: `GET` or
            `POST` and the default is `POST`.
        configuration_retry_count:
            The number of times to retry the webhook if the first attempt fails. Can
            be an integer between 0 and 3, inclusive, and the default is
            0.
        configuration_triggers:
            A string that will cause us to call the webhook when it is present in a
            message body. This parameter takes only one trigger string.
            To specify more than one, repeat this parameter for each
            trigger string up to a total of 5 trigger strings. Used only
            when `type` = `trigger`.
        configuration_url:
            The URL of the webhook to call using the `configuration.method`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_retry_count": configuration_retry_count,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
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
async def delete_v2_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v2_services_service_sid_channels_sid(
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    created_by: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A valid JSON string that contains application-specific data.
        created_by:
            The `identity` of the User that created the channel. Default is:
            `system`.
        date_created:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was created. The
            default value is the current time set by the Chat service.
            Note that this should only be used in cases where a Channel
            is being recreated from a backup/separate source.
        date_updated:
            The date, specified in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format, to
            assign to the resource as the date it was last updated.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 256 characters long.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL. This value must be 256
            characters or less in length and unique within the Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "created_by": created_by,
        "date_created": date_created,
        "date_updated": date_updated,
        "friendly_name": friendly_name,
        "unique_name": unique_name,
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
async def get_v2_services_service_sid_roles(
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles?&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles"  # noqa
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
async def post_v2_services_service_sid_roles(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    permission: list = None,
    type: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        permission:
            A permission that you grant to the new role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. The values
            for this parameter depend on the role's `type`.
        type:
            The type of role. Can be: `channel` for
            [Channel](https://www.twilio.com/docs/chat/channels) roles
            or `deployment` for
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource) roles.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles?](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "permission": permission,
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
async def delete_v2_services_service_sid_roles_sid(
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
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
async def get_v2_services_service_sid_roles_sid(
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
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
async def post_v2_services_service_sid_roles_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    permission: list = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        permission:
            A permission that you grant to the role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. Note that
            the update action replaces all previously assigned
            permissions with those defined in the update action. To
            remove a permission, do not include it in the subsequent
            update action. The values for this parameter depend on the
            role's `type`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "permission": permission,
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
async def get_v2_services_service_sid_users(
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users?&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users"  # noqa
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
async def post_v2_services_service_sid_users(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the new resource. This
            value is often used for display purposes.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/chat/rest/service-
            resource). This value is often a username or email address.
            See the Identity documentation for more info.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) to assign to the new User.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v2_services_service_sid_users_sid(
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
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
async def get_v2_services_service_sid_users_sid(
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
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
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
async def post_v2_services_service_sid_users_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A valid JSON string that contains application-specific data.
        friendly_name:
            A descriptive string that you create to describe the resource. It is
            often used for display purposes.
        role_sid:
            The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-
            resource) to assign to the User.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "role_sid": role_sid,
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
async def get_v2_services_service_sid_users_user_sid_bindings(
    service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    binding_type: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_type:
            The push technology used by the User Binding resources to read. Can be:
            `apn`, `gcm`, or `fcm`.  See [push notification
            configuration](https://www.twilio.com/docs/chat/push-
            notification-configuration) for more info.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings?&binding_type=%s&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings?&binding_type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "binding_type": binding_type,
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
async def delete_v2_services_service_sid_users_user_sid_bindings_sid(
    service_sid: str,
    user_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_users_user_sid_bindings_sid(
    service_sid: str,
    user_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_users_user_sid_channels(
    service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all Channels for a given User.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels"  # noqa
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
async def delete_v2_services_service_sid_users_user_sid_channels_channel_sid(
    service_sid: str,
    user_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Removes User from selected Channel.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v2_services_service_sid_users_user_sid_channels_channel_sid(
    service_sid: str,
    user_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
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
async def post_v2_services_service_sid_users_user_sid_channels_channel_sid(
    service_sid: str,
    user_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    last_consumed_message_index: int = None,
    last_consumption_timestamp: str = None,
    notification_level: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        last_consumed_message_index:
            The index of the last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) in the
            [Channel](https://www.twilio.com/docs/chat/channels) that
            the Member has read.
        last_consumption_timestamp:
            The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the
            last
            [Message](https://www.twilio.com/docs/chat/rest/message-
            resource) read event for the Member within the
            [Channel](https://www.twilio.com/docs/chat/channels).
        notification_level:
            The push notification level to assign to the User Channel. Can be:
            `default` or `muted`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "last_consumed_message_index": last_consumed_message_index,
        "last_consumption_timestamp": last_consumption_timestamp,
        "notification_level": notification_level,
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
async def delete_v2_services_sid(
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
    [https://chat.twilio.com/v2/Services/{sid}?](
    https://chat.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{sid}"  # noqa
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
async def get_v2_services_sid(
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
    [https://chat.twilio.com/v2/Services/{sid}?](
    https://chat.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{sid}"  # noqa
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
async def post_v2_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    consumption_report_interval: int = None,
    default_channel_creator_role_sid: str = None,
    default_channel_role_sid: str = None,
    default_service_role_sid: str = None,
    friendly_name: str = None,
    limits_channel_members: int = None,
    limits_user_channels: int = None,
    media_compatibility_message: str = None,
    notifications_added_to_channel_enabled: bool = None,
    notifications_added_to_channel_sound: str = None,
    notifications_added_to_channel_template: str = None,
    notifications_invited_to_channel_enabled: bool = None,
    notifications_invited_to_channel_sound: str = None,
    notifications_invited_to_channel_template: str = None,
    notifications_log_enabled: bool = None,
    notifications_new_message_badge_count_enabled: bool = None,
    notifications_new_message_enabled: bool = None,
    notifications_new_message_sound: str = None,
    notifications_new_message_template: str = None,
    notifications_removed_from_channel_enabled: bool = None,
    notifications_removed_from_channel_sound: str = None,
    notifications_removed_from_channel_template: str = None,
    post_webhook_retry_count: int = None,
    post_webhook_url: str = None,
    pre_webhook_retry_count: int = None,
    pre_webhook_url: str = None,
    reachability_enabled: bool = None,
    read_status_enabled: bool = None,
    typing_indicator_timeout: int = None,
    webhook_filters: list = None,
    webhook_method: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        consumption_report_interval:
            DEPRECATED. The interval in seconds between consumption reports
            submission batches from client endpoints.
        default_channel_creator_role_sid:
            The channel role assigned to a channel creator when they join a new
            channel. See the [Role
            resource](https://www.twilio.com/docs/chat/rest/role-
            resource) for more info about roles.
        default_channel_role_sid:
            The channel role assigned to users when they are added to a channel. See
            the [Role
            resource](https://www.twilio.com/docs/chat/rest/role-
            resource) for more info about roles.
        default_service_role_sid:
            The service role assigned to users when they are added to the service.
            See the [Role
            resource](https://www.twilio.com/docs/chat/rest/role-
            resource) for more info about roles.
        friendly_name:
            A descriptive string that you create to describe the resource.
        limits_channel_members:
            The maximum number of Members that can be added to Channels within this
            Service. Can be up to 1,000.
        limits_user_channels:
            The maximum number of Channels Users can be a Member of within this
            Service. Can be up to 1,000.
        media_compatibility_message:
            The message to send when a media message has no text. Can be used as
            placeholder message.
        notifications_added_to_channel_enabled:
            Whether to send a notification when a member is added to a channel. The
            default is `false`.
        notifications_added_to_channel_sound:
            The name of the sound to play when a member is added to a channel and
            `notifications.added_to_channel.enabled` is `true`.
        notifications_added_to_channel_template:
            The template to use to create the notification text displayed when a
            member is added to a channel and
            `notifications.added_to_channel.enabled` is `true`.
        notifications_invited_to_channel_enabled:
            Whether to send a notification when a user is invited to a channel. The
            default is `false`.
        notifications_invited_to_channel_sound:
            The name of the sound to play when a user is invited to a channel and
            `notifications.invited_to_channel.enabled` is `true`.
        notifications_invited_to_channel_template:
            The template to use to create the notification text displayed when a
            user is invited to a channel and
            `notifications.invited_to_channel.enabled` is `true`.
        notifications_log_enabled:
            Whether to log notifications. The default is `false`.
        notifications_new_message_badge_count_enabled:
            Whether the new message badge is enabled. The default is `false`.
        notifications_new_message_enabled:
            Whether to send a notification when a new message is added to a channel.
            The default is `false`.
        notifications_new_message_sound:
            The name of the sound to play when a new message is added to a channel
            and `notifications.new_message.enabled` is `true`.
        notifications_new_message_template:
            The template to use to create the notification text displayed when a new
            message is added to a channel and
            `notifications.new_message.enabled` is `true`.
        notifications_removed_from_channel_enabled:
            Whether to send a notification to a user when they are removed from a
            channel. The default is `false`.
        notifications_removed_from_channel_sound:
            The name of the sound to play to a user when they are removed from a
            channel and `notifications.removed_from_channel.enabled` is
            `true`.
        notifications_removed_from_channel_template:
            The template to use to create the notification text displayed to a user
            when they are removed from a channel and
            `notifications.removed_from_channel.enabled` is `true`.
        post_webhook_retry_count:
            The number of times to retry a call to the `post_webhook_url` if the
            request times out (after 5 seconds) or it receives a 429,
            503, or 504 HTTP response. The default is 0, which means the
            call won't be retried.
        post_webhook_url:
            The URL for post-event webhooks, which are called by using the
            `webhook_method`. See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.
        pre_webhook_retry_count:
            The number of times to retry a call to the `pre_webhook_url` if the
            request times out (after 5 seconds) or it receives a 429,
            503, or 504 HTTP response. Default retry count is 0 times,
            which means the call won't be retried.
        pre_webhook_url:
            The URL for pre-event webhooks, which are called by using the
            `webhook_method`. See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.
        reachability_enabled:
            Whether to enable the [Reachability
            Indicator](https://www.twilio.com/docs/chat/reachability-
            indicator) for this Service instance. The default is
            `false`.
        read_status_enabled:
            Whether to enable the [Message Consumption
            Horizon](https://www.twilio.com/docs/chat/consumption-
            horizon) feature. The default is `true`.
        typing_indicator_timeout:
            How long in seconds after a `started typing` event until clients should
            assume that user is no longer typing, even if no `ended
            typing` message was received.  The default is 5 seconds.
        webhook_filters:
            The list of webhook events that are enabled for this Service instance.
            See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.
        webhook_method:
            The HTTP method to use for calls to the `pre_webhook_url` and
            `post_webhook_url` webhooks.  Can be: `POST` or `GET` and
            the default is `POST`. See [Webhook
            Events](https://www.twilio.com/docs/chat/webhook-events) for
            more details.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v2/Services/{sid}?](
    https://chat.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v2/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "consumption_report_interval": consumption_report_interval,
        "default_channel_creator_role_sid": default_channel_creator_role_sid,
        "default_channel_role_sid": default_channel_role_sid,
        "default_service_role_sid": default_service_role_sid,
        "friendly_name": friendly_name,
        "limits_channel_members": limits_channel_members,
        "limits_user_channels": limits_user_channels,
        "media_compatibility_message": media_compatibility_message,
        "notifications_added_to_channel_enabled": notifications_added_to_channel_enabled,  # noqa
        "notifications_added_to_channel_sound": notifications_added_to_channel_sound,  # noqa
        "notifications_added_to_channel_template": notifications_added_to_channel_template,  # noqa
        "notifications_invited_to_channel_enabled": notifications_invited_to_channel_enabled,  # noqa
        "notifications_invited_to_channel_sound": notifications_invited_to_channel_sound,  # noqa
        "notifications_invited_to_channel_template": notifications_invited_to_channel_template,  # noqa
        "notifications_log_enabled": notifications_log_enabled,
        "notifications_new_message_badge_count_enabled": notifications_new_message_badge_count_enabled,  # noqa
        "notifications_new_message_enabled": notifications_new_message_enabled,
        "notifications_new_message_sound": notifications_new_message_sound,
        "notifications_new_message_template": notifications_new_message_template,
        "notifications_removed_from_channel_enabled": notifications_removed_from_channel_enabled,  # noqa
        "notifications_removed_from_channel_sound": notifications_removed_from_channel_sound,  # noqa
        "notifications_removed_from_channel_template": notifications_removed_from_channel_template,  # noqa
        "post_webhook_retry_count": post_webhook_retry_count,
        "post_webhook_url": post_webhook_url,
        "pre_webhook_retry_count": pre_webhook_retry_count,
        "pre_webhook_url": pre_webhook_url,
        "reachability_enabled": reachability_enabled,
        "read_status_enabled": read_status_enabled,
        "typing_indicator_timeout": typing_indicator_timeout,
        "webhook_filters": webhook_filters,
        "webhook_method": webhook_method,
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
async def post_v3_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    messaging_service_sid: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Channel.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        messaging_service_sid:
            The unique ID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) this
            channel belongs to.
        type:
            TThe Type for this Channel to migrate to. Can only be `private`.
            Migration to 'public' is not allowed.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://chat.twilio.com/v3/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://chat.twilio.com/v3/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://chat.twilio.com/v3/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "messaging_service_sid": messaging_service_sid,
        "type": type,
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
async def get_v1_services(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all conversation services on your account.

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
    [https://conversations.twilio.com/v1/Services?&page_size=%s](
    https://conversations.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Services"  # noqa

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
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new conversation service on your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The human-readable name of this service, limited to 256 characters.
            Optional.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services?](
    https://conversations.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v1_services_chat_service_sid_bindings(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    binding_type: list = None,
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all push notification bindings in the conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_type:
            The push technology used by the Binding resources to read.  Can be:
            `apn`, `gcm`, or `fcm`.  See [push notification
            configuration](https://www.twilio.com/docs/chat/push-
            notification-configuration) for more info.
        identity:
            The identity of a [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource) this binding belongs to. See [access
            tokens](https://www.twilio.com/docs/conversations/create-
            tokens) for more details.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "binding_type": binding_type,
        "identity": identity,
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
async def delete_v1_services_chat_service_sid_bindings_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove a push notification binding from the conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_bindings_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a push notification binding from the conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Bindings/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_configuration(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the configuration of a conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration"  # noqa
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
async def post_v1_services_chat_service_sid_configuration(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    default_chat_service_role_sid: str = None,
    default_conversation_creator_role_sid: str = None,
    default_conversation_role_sid: str = None,
    reachability_enabled: bool = None,
) -> Dict[str, Any]:
    """
    Update configuration settings of a conversation service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        default_chat_service_role_sid:
            The service-level role assigned to users when they are added to the
            service. See the [Conversation
            Role](https://www.twilio.com/docs/conversations/api/role-
            resource) for more info about roles.
        default_conversation_creator_role_sid:
            The conversation-level role assigned to a conversation creator when they
            join a new conversation. See the [Conversation
            Role](https://www.twilio.com/docs/conversations/api/role-
            resource) for more info about roles.
        default_conversation_role_sid:
            The conversation-level role assigned to users when they are added to a
            conversation. See the [Conversation
            Role](https://www.twilio.com/docs/conversations/api/role-
            resource) for more info about roles.
        reachability_enabled:
            Whether the [Reachability
            Indicator](https://www.twilio.com/docs/chat/reachability-
            indicator) is enabled for this Conversations Service. The
            default is `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "default_chat_service_role_sid": default_chat_service_role_sid,
        "default_conversation_creator_role_sid": default_conversation_creator_role_sid,  # noqa
        "default_conversation_role_sid": default_conversation_role_sid,
        "reachability_enabled": reachability_enabled,
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
async def get_v1_services_chat_service_sid_configuration_notifications(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch push notification service settings.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications"  # noqa
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
async def post_v1_services_chat_service_sid_configuration_notifications(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    added_to_conversation_enabled: bool = None,
    added_to_conversation_sound: str = None,
    added_to_conversation_template: str = None,
    log_enabled: bool = None,
    new_message_badge_count_enabled: bool = None,
    new_message_enabled: bool = None,
    new_message_sound: str = None,
    new_message_template: str = None,
    new_message_with_media_enabled: bool = None,
    new_message_with_media_template: str = None,
    removed_from_conversation_enabled: bool = None,
    removed_from_conversation_sound: str = None,
    removed_from_conversation_template: str = None,
) -> Dict[str, Any]:
    """
    Update push notification service settings.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        added_to_conversation_enabled:
            Whether to send a notification when a participant is added to a
            conversation. The default is `false`.
        added_to_conversation_sound:
            The name of the sound to play when a participant is added to a
            conversation and `added_to_conversation.enabled` is `true`.
        added_to_conversation_template:
            The template to use to create the notification text displayed when a
            participant is added to a conversation and
            `added_to_conversation.enabled` is `true`.
        log_enabled:
            Weather the notification logging is enabled.
        new_message_badge_count_enabled:
            Whether the new message badge is enabled. The default is `false`.
        new_message_enabled:
            Whether to send a notification when a new message is added to a
            conversation. The default is `false`.
        new_message_sound:
            The name of the sound to play when a new message is added to a
            conversation and `new_message.enabled` is `true`.
        new_message_template:
            The template to use to create the notification text displayed when a new
            message is added to a conversation and `new_message.enabled`
            is `true`.
        new_message_with_media_enabled:
            Whether to send a notification when a new message with media/file
            attachments is added to a conversation. The default is
            `false`.
        new_message_with_media_template:
            The template to use to create the notification text displayed when a new
            message with media/file attachments is added to a
            conversation and `new_message.attachments.enabled` is
            `true`.
        removed_from_conversation_enabled:
            Whether to send a notification to a user when they are removed from a
            conversation. The default is `false`.
        removed_from_conversation_sound:
            The name of the sound to play to a user when they are removed from a
            conversation and `removed_from_conversation.enabled` is
            `true`.
        removed_from_conversation_template:
            The template to use to create the notification text displayed to a user
            when they are removed from a conversation and
            `removed_from_conversation.enabled` is `true`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Notifications"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "added_to_conversation_enabled": added_to_conversation_enabled,
        "added_to_conversation_sound": added_to_conversation_sound,
        "added_to_conversation_template": added_to_conversation_template,
        "log_enabled": log_enabled,
        "new_message_badge_count_enabled": new_message_badge_count_enabled,
        "new_message_enabled": new_message_enabled,
        "new_message_sound": new_message_sound,
        "new_message_template": new_message_template,
        "new_message_with_media_enabled": new_message_with_media_enabled,
        "new_message_with_media_template": new_message_with_media_template,
        "removed_from_conversation_enabled": removed_from_conversation_enabled,
        "removed_from_conversation_sound": removed_from_conversation_sound,
        "removed_from_conversation_template": removed_from_conversation_template,
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
async def get_v1_services_chat_service_sid_configuration_webhooks(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific service webhook configuration.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks"  # noqa
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
async def post_v1_services_chat_service_sid_configuration_webhooks(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    filters: list = None,
    method: str = None,
    post_webhook_url: str = None,
    pre_webhook_url: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Webhook.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        filters:
            The list of events that your configured webhook targets will receive.
            Events not configured here will not fire. Possible values
            are `onParticipantAdd`, `onParticipantAdded`,
            `onDeliveryUpdated`, `onConversationUpdated`,
            `onConversationRemove`, `onParticipantRemove`,
            `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`,
            `onParticipantUpdated`, `onConversationAdded`,
            `onMessageAdded`, `onConversationAdd`,
            `onConversationRemoved`, `onParticipantUpdate`,
            `onMessageRemove`, `onMessageUpdated`,
            `onParticipantRemoved`, `onMessageUpdate` or
            `onConversationStateUpdated`.
        method:
            The HTTP method to be used when sending a webhook request. One of `GET`
            or `POST`.
        post_webhook_url:
            The absolute url the post-event webhook request should be sent to.
        pre_webhook_url:
            The absolute url the pre-event webhook request should be sent to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Configuration/Webhooks"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "filters": filters,
        "method": method,
        "post_webhook_url": post_webhook_url,
        "pre_webhook_url": pre_webhook_url,
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
async def get_v1_services_chat_service_sid_conversations(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of conversations in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations"  # noqa
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
async def post_v1_services_chat_service_sid_conversations(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    messaging_service_sid: str = None,
    state: str = None,
    timers_closed: str = None,
    timers_inactive: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new conversation in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        friendly_name:
            The human-readable name of this conversation, limited to 256 characters.
            Optional.
        messaging_service_sid:
            The unique ID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) this
            conversation belongs to.
        state:
            Current state of this conversation. Can be either `active`, `inactive`
            or `closed` and defaults to `active`.
        timers_closed:
            ISO8601 duration when conversation will be switched to `closed` state.
            Minimum value for this timer is 10 minutes.
        timers_inactive:
            ISO8601 duration when conversation will be switched to `inactive` state.
            Minimum value for this timer is 1 minute.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "friendly_name": friendly_name,
        "messaging_service_sid": messaging_service_sid,
        "state": state,
        "timers_closed": timers_closed,
        "timers_inactive": timers_inactive,
        "unique_name": unique_name,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_messages(
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all messages in the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:
            The sort order of the returned messages. Can be: `asc` (ascending) or
            `desc` (descending), with `asc` as the default.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages?&order=%s&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_messages(
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    author: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
    media_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new message to the conversation in a specific service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A string metadata field you can use to store any data you wish. The
            string value must contain structurally valid JSON if
            specified.  **Note** that if the attributes are not set "{}"
            will be returned.
        author:
            The channel specific identifier of the message's author. Defaults to
            `system`.
        body:
            The content of the message, can be up to 1,600 characters long.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated. `null` if the message has
            not been edited.
        media_sid:
            The Media SID to be attached to the new Message.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "author": author,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
        "media_sid": media_sid,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_messages_message_sid_receipts(
    chat_service_sid: str,
    conversation_sid: str,
    message_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all delivery and read receipts of the conversation message.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        message_sid:
            Message sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts"  # noqa
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_messages_message_sid_receipts_sid(
    chat_service_sid: str,
    conversation_sid: str,
    message_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the delivery and read receipts of the conversation message.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        message_sid:
            Message sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}"  # noqa
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
async def delete_v1_services_chat_service_sid_conversations_conversation_sid_messages_sid(
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a message from the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_messages_sid(
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a message from the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_messages_sid(
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    author: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
) -> Dict[str, Any]:
    """
    Update an existing message in the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            A string metadata field you can use to store any data you wish. The
            string value must contain structurally valid JSON if
            specified.  **Note** that if the attributes are not set "{}"
            will be returned.
        author:
            The channel specific identifier of the message's author. Defaults to
            `system`.
        body:
            The content of the message, can be up to 1,600 characters long.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated. `null` if the message has
            not been edited.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "author": author,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_participants(
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all participants of the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_participants(
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    identity: str = None,
    messaging_binding_address: str = None,
    messaging_binding_projected_address: str = None,
    messaging_binding_proxy_address: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new participant to the conversation in a specific service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversation SDK to communicate.
            Limited to 256 characters.
        messaging_binding_address:
            The address of the participant's device, e.g. a phone or WhatsApp
            number. Together with the Proxy address, this determines a
            participant uniquely. This field (with proxy_address) is
            only null when the participant is interacting from an SDK
            endpoint (see the 'identity' field).
        messaging_binding_projected_address:
            The address of the Twilio phone number that is used in Group MMS.
            Communication mask for the Conversation participant with
            Identity.
        messaging_binding_proxy_address:
            The address of the Twilio phone number (or WhatsApp number) that the
            participant is in contact with. This field, together with
            participant address, is only null when the participant is
            interacting from an SDK endpoint (see the 'identity' field).
        role_sid:
            The SID of a conversation-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the participant.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "identity": identity,
        "messaging_binding_address": messaging_binding_address,
        "messaging_binding_projected_address": messaging_binding_projected_address,
        "messaging_binding_proxy_address": messaging_binding_proxy_address,
        "role_sid": role_sid,
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
async def delete_v1_services_chat_service_sid_conversations_conversation_sid_participants_sid(
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a participant from the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_participants_sid(
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a participant of the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_participants_sid(
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    identity: str = None,
    last_read_message_index: int = None,
    last_read_timestamp: str = None,
    messaging_binding_projected_address: str = None,
    messaging_binding_proxy_address: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Update an existing participant in the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversation SDK to communicate.
            Limited to 256 characters.
        last_read_message_index:
            Index of last “read” message in the
            [Conversation](https://www.twilio.com/docs/conversations/api/conversation-
            resource) for the Participant.
        last_read_timestamp:
            Timestamp of last “read” message in the
            [Conversation](https://www.twilio.com/docs/conversations/api/conversation-
            resource) for the Participant.
        messaging_binding_projected_address:
            The address of the Twilio phone number that is used in Group MMS. 'null'
            value will remove it.
        messaging_binding_proxy_address:
            The address of the Twilio phone number that the participant is in
            contact with. 'null' value will remove it.
        role_sid:
            The SID of a conversation-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the participant.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Participants/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "identity": identity,
        "last_read_message_index": last_read_message_index,
        "last_read_timestamp": last_read_timestamp,
        "messaging_binding_projected_address": messaging_binding_projected_address,
        "messaging_binding_proxy_address": messaging_binding_proxy_address,
        "role_sid": role_sid,
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_webhooks(
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all webhooks scoped to the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_webhooks(
    chat_service_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_replay_after: int = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
    target: str = None,
) -> Dict[str, Any]:
    """
    Create a new webhook scoped to the conversation in a specific service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:
            The list of events, firing webhook event for this Conversation.
        configuration_flow_sid:
            The studio flow SID, where the webhook should be sent to.
        configuration_method:
            The HTTP method to be used when sending a webhook request.
        configuration_replay_after:
            The message index for which and it's successors the webhook will be
            replayed. Not set by default.
        configuration_triggers:
            The list of keywords, firing webhook event for this Conversation.
        configuration_url:
            The absolute url the webhook request should be sent to.
        target:
            The target of this webhook: `webhook`, `studio`, `trigger`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_replay_after": configuration_replay_after,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
        "target": target,
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
async def delete_v1_services_chat_service_sid_conversations_conversation_sid_webhooks_sid(
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an existing webhook scoped to the conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_conversations_conversation_sid_webhooks_sid(
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the configuration of a conversation-scoped webhook.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_conversation_sid_webhooks_sid(
    chat_service_sid: str,
    conversation_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
) -> Dict[str, Any]:
    """
    Update an existing conversation-scoped webhook.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:
            The list of events, firing webhook event for this Conversation.
        configuration_flow_sid:
            The studio flow SID, where the webhook should be sent to.
        configuration_method:
            The HTTP method to be used when sending a webhook request.
        configuration_triggers:
            The list of keywords, firing webhook event for this Conversation.
        configuration_url:
            The absolute url the webhook request should be sent to.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
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
async def delete_v1_services_chat_service_sid_conversations_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a conversation from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v1_services_chat_service_sid_conversations_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a conversation from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_conversations_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    messaging_service_sid: str = None,
    state: str = None,
    timers_closed: str = None,
    timers_inactive: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Update an existing conversation in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            An optional string metadata field you can use to store any data you
            wish. The string value must contain structurally valid JSON
            if specified.  **Note** that if the attributes are not set
            "{}" will be returned.
        date_created:
            The date that this resource was created.
        date_updated:
            The date that this resource was last updated.
        friendly_name:
            The human-readable name of this conversation, limited to 256 characters.
            Optional.
        messaging_service_sid:
            The unique ID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) this
            conversation belongs to.
        state:
            Current state of this conversation. Can be either `active`, `inactive`
            or `closed` and defaults to `active`.
        timers_closed:
            ISO8601 duration when conversation will be switched to `closed` state.
            Minimum value for this timer is 10 minutes.
        timers_inactive:
            ISO8601 duration when conversation will be switched to `inactive` state.
            Minimum value for this timer is 1 minute.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used to address the resource in place of the
            resource's `sid` in the URL.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Conversations/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "friendly_name": friendly_name,
        "messaging_service_sid": messaging_service_sid,
        "state": state,
        "timers_closed": timers_closed,
        "timers_inactive": timers_inactive,
        "unique_name": unique_name,
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
async def get_v1_services_chat_service_sid_participant_conversations(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    address: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Conversations that this Participant belongs to by
    identity or by address. Only one parameter should be specified.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversations SDK to communicate.
            Limited to 256 characters.
        address:
            A unique string identifier for the conversation participant who's not a
            Conversation User. This parameter could be found in
            messaging_binding.address field of Participant resource. It
            should be url-encoded.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/ParticipantConversations?&identity=%s&address=%s&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/ParticipantConversations?&identity=%s&address=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/ParticipantConversations"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
        "address": address,
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
async def get_v1_services_chat_service_sid_roles(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all user roles in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles"  # noqa
    )
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
async def post_v1_services_chat_service_sid_roles(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    permission: list = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Create a new user role in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the new resource. It
            can be up to 64 characters long.
        permission:
            A permission that you grant to the new role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. The values
            for this parameter depend on the role's `type`.
        type:
            The type of role. Can be: `conversation` for
            [Conversation](https://www.twilio.com/docs/conversations/api/conversation-
            resource) roles or `service` for [Conversation
            Service](https://www.twilio.com/docs/conversations/api/service-
            resource) roles.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles"  # noqa
    )
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "permission": permission,
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
async def delete_v1_services_chat_service_sid_roles_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove a user role from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}"  # noqa
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
async def get_v1_services_chat_service_sid_roles_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a user role from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_roles_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    permission: list = None,
) -> Dict[str, Any]:
    """
    Update an existing user role in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        permission:
            A permission that you grant to the role. Only one permission can be
            granted per parameter. To assign more than one permission,
            repeat this parameter for each permission value. Note that
            the update action replaces all previously assigned
            permissions with those defined in the update action. To
            remove a permission, do not include it in the subsequent
            update action. The values for this parameter depend on the
            role's `type`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Roles/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "permission": permission,
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
async def get_v1_services_chat_service_sid_users(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all conversation users in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users"  # noqa
    )
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
async def post_v1_services_chat_service_sid_users(
    chat_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new conversation user to your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            The JSON Object string that stores application-specific data. If
            attributes have not been set, `{}` is returned.
        friendly_name:
            The string that you assigned to describe the resource.
        identity:
            The application-defined string that uniquely identifies the resource's
            User within the [Conversation
            Service](https://www.twilio.com/docs/conversations/api/service-
            resource). This value is often a username or an email
            address, and is case-sensitive.
        role_sid:
            The SID of a service-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the user.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users"  # noqa
    )
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v1_services_chat_service_sid_users_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """
    Remove a conversation user from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v1_services_chat_service_sid_users_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a conversation user from your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}"  # noqa
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
async def post_v1_services_chat_service_sid_users_sid(
    chat_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """
    Update an existing conversation user in your service.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:
            The JSON Object string that stores application-specific data. If
            attributes have not been set, `{}` is returned.
        friendly_name:
            The string that you assigned to describe the resource.
        role_sid:
            The SID of a service-level
            [Role](https://www.twilio.com/docs/conversations/api/role-
            resource) to assign to the user.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "role_sid": role_sid,
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
async def get_v1_services_chat_service_sid_users_user_sid_conversations(
    chat_service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all User Conversations for the User.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations?&page_size=%s](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations"  # noqa
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
async def delete_v1_services_chat_service_sid_users_user_sid_conversations_conversation_sid(
    chat_service_sid: str,
    user_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific User Conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}"  # noqa
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
async def get_v1_services_chat_service_sid_users_user_sid_conversations_conversation_sid(
    chat_service_sid: str,
    user_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific User Conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}"  # noqa
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
async def post_v1_services_chat_service_sid_users_user_sid_conversations_conversation_sid(
    chat_service_sid: str,
    user_sid: str,
    conversation_sid: str,
    twilio_credentials: "TwilioCredentials",
    last_read_message_index: int = None,
    last_read_timestamp: str = None,
    notification_level: str = None,
) -> Dict[str, Any]:
    """
    Update a specific User Conversation.

    Args:
        chat_service_sid:
            Chat service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        conversation_sid:
            Conversation sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        last_read_message_index:
            The index of the last Message in the Conversation that the Participant
            has read.
        last_read_timestamp:
            The date of the last message read in conversation by the user, given in
            ISO 8601 format.
        notification_level:
            The Notification Level of this User Conversation. One of `default` or
            `muted`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?](
    https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "last_read_message_index": last_read_message_index,
        "last_read_timestamp": last_read_timestamp,
        "notification_level": notification_level,
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
    Remove a conversation service with all its nested resources from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{sid}?](
    https://conversations.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{sid}"  # noqa
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
    Fetch a conversation service from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/Services/{sid}?](
    https://conversations.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://conversations.twilio.com/v1/Services/{sid}"  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services?&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v1/Services"  # noqa

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
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services?](
    https://ip-messaging.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v1/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v1_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    type: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        type:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels?&type=%s&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels?&type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "type": type,
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
async def post_v1_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    type: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:

        friendly_name:

        type:

        unique_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "type": type,
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
async def get_v1_services_service_sid_channels_channel_sid_invites(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v1_services_service_sid_channels_channel_sid_invites(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v1_services_service_sid_channels_channel_sid_invites_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_invites_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_members(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v1_services_service_sid_channels_channel_sid_members(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v1_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
async def post_v1_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    last_consumed_message_index: int = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        last_consumed_message_index:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "last_consumed_message_index": last_consumed_message_index,
        "role_sid": role_sid,
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
async def get_v1_services_service_sid_channels_channel_sid_messages(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
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
async def post_v1_services_service_sid_channels_channel_sid_messages(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    body: str = None,
    from_: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:

        body:

        from_:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "body": body,
        "from_": from_,
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
async def delete_v1_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
async def post_v1_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    body: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:

        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
        "body": body,
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
async def delete_v1_services_service_sid_channels_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
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
async def get_v1_services_service_sid_channels_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
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
async def post_v1_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:

        friendly_name:

        unique_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
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


@task
async def get_v1_services_service_sid_roles(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles?&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles"  # noqa
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
async def post_v1_services_service_sid_roles(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    permission: list = None,
    type: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:

        permission:

        type:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "permission": permission,
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
async def delete_v1_services_service_sid_roles_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
    )
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
async def get_v1_services_service_sid_roles_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
    )
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
async def post_v1_services_service_sid_roles_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    permission: list = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        permission:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Roles/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "permission": permission,
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
async def get_v1_services_service_sid_users(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users?&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users"  # noqa
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
async def post_v1_services_service_sid_users(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:

        friendly_name:

        identity:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v1_services_service_sid_users_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
    )
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
async def get_v1_services_service_sid_users_sid(
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
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
    )
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
async def post_v1_services_service_sid_users_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:

        friendly_name:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "role_sid": role_sid,
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
async def get_v1_services_service_sid_users_user_sid_channels(
    service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s](
    https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{service_sid}/Users/{user_sid}/Channels"  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{sid}"  # noqa
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
    [https://ip-messaging.twilio.com/v1/Services/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{sid}"  # noqa
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
    consumption_report_interval: int = None,
    default_channel_creator_role_sid: str = None,
    default_channel_role_sid: str = None,
    default_service_role_sid: str = None,
    friendly_name: str = None,
    limits_channel_members: int = None,
    limits_user_channels: int = None,
    notifications_added_to_channel_enabled: bool = None,
    notifications_added_to_channel_template: str = None,
    notifications_invited_to_channel_enabled: bool = None,
    notifications_invited_to_channel_template: str = None,
    notifications_new_message_enabled: bool = None,
    notifications_new_message_template: str = None,
    notifications_removed_from_channel_enabled: bool = None,
    notifications_removed_from_channel_template: str = None,
    post_webhook_url: str = None,
    pre_webhook_url: str = None,
    reachability_enabled: bool = None,
    read_status_enabled: bool = None,
    typing_indicator_timeout: int = None,
    webhook_filters: list = None,
    webhook_method: str = None,
    webhooks_on_channel_add_method: str = None,
    webhooks_on_channel_add_url: str = None,
    webhooks_on_channel_added_method: str = None,
    webhooks_on_channel_added_url: str = None,
    webhooks_on_channel_destroy_method: str = None,
    webhooks_on_channel_destroy_url: str = None,
    webhooks_on_channel_destroyed_method: str = None,
    webhooks_on_channel_destroyed_url: str = None,
    webhooks_on_channel_update_method: str = None,
    webhooks_on_channel_update_url: str = None,
    webhooks_on_channel_updated_method: str = None,
    webhooks_on_channel_updated_url: str = None,
    webhooks_on_member_add_method: str = None,
    webhooks_on_member_add_url: str = None,
    webhooks_on_member_added_method: str = None,
    webhooks_on_member_added_url: str = None,
    webhooks_on_member_remove_method: str = None,
    webhooks_on_member_remove_url: str = None,
    webhooks_on_member_removed_method: str = None,
    webhooks_on_member_removed_url: str = None,
    webhooks_on_message_remove_method: str = None,
    webhooks_on_message_remove_url: str = None,
    webhooks_on_message_removed_method: str = None,
    webhooks_on_message_removed_url: str = None,
    webhooks_on_message_send_method: str = None,
    webhooks_on_message_send_url: str = None,
    webhooks_on_message_sent_method: str = None,
    webhooks_on_message_sent_url: str = None,
    webhooks_on_message_update_method: str = None,
    webhooks_on_message_update_url: str = None,
    webhooks_on_message_updated_method: str = None,
    webhooks_on_message_updated_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        consumption_report_interval:

        default_channel_creator_role_sid:

        default_channel_role_sid:

        default_service_role_sid:

        friendly_name:

        limits_channel_members:

        limits_user_channels:

        notifications_added_to_channel_enabled:

        notifications_added_to_channel_template:

        notifications_invited_to_channel_enabled:

        notifications_invited_to_channel_template:

        notifications_new_message_enabled:

        notifications_new_message_template:

        notifications_removed_from_channel_enabled:

        notifications_removed_from_channel_template:

        post_webhook_url:

        pre_webhook_url:

        reachability_enabled:

        read_status_enabled:

        typing_indicator_timeout:

        webhook_filters:

        webhook_method:

        webhooks_on_channel_add_method:

        webhooks_on_channel_add_url:

        webhooks_on_channel_added_method:

        webhooks_on_channel_added_url:

        webhooks_on_channel_destroy_method:

        webhooks_on_channel_destroy_url:

        webhooks_on_channel_destroyed_method:

        webhooks_on_channel_destroyed_url:

        webhooks_on_channel_update_method:

        webhooks_on_channel_update_url:

        webhooks_on_channel_updated_method:

        webhooks_on_channel_updated_url:

        webhooks_on_member_add_method:

        webhooks_on_member_add_url:

        webhooks_on_member_added_method:

        webhooks_on_member_added_url:

        webhooks_on_member_remove_method:

        webhooks_on_member_remove_url:

        webhooks_on_member_removed_method:

        webhooks_on_member_removed_url:

        webhooks_on_message_remove_method:

        webhooks_on_message_remove_url:

        webhooks_on_message_removed_method:

        webhooks_on_message_removed_url:

        webhooks_on_message_send_method:

        webhooks_on_message_send_url:

        webhooks_on_message_sent_method:

        webhooks_on_message_sent_url:

        webhooks_on_message_update_method:

        webhooks_on_message_update_url:

        webhooks_on_message_updated_method:

        webhooks_on_message_updated_url:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v1/Services/{sid}?](
    https://ip-messaging.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v1/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "consumption_report_interval": consumption_report_interval,
        "default_channel_creator_role_sid": default_channel_creator_role_sid,
        "default_channel_role_sid": default_channel_role_sid,
        "default_service_role_sid": default_service_role_sid,
        "friendly_name": friendly_name,
        "limits_channel_members": limits_channel_members,
        "limits_user_channels": limits_user_channels,
        "notifications_added_to_channel_enabled": notifications_added_to_channel_enabled,  # noqa
        "notifications_added_to_channel_template": notifications_added_to_channel_template,  # noqa
        "notifications_invited_to_channel_enabled": notifications_invited_to_channel_enabled,  # noqa
        "notifications_invited_to_channel_template": notifications_invited_to_channel_template,  # noqa
        "notifications_new_message_enabled": notifications_new_message_enabled,
        "notifications_new_message_template": notifications_new_message_template,
        "notifications_removed_from_channel_enabled": notifications_removed_from_channel_enabled,  # noqa
        "notifications_removed_from_channel_template": notifications_removed_from_channel_template,  # noqa
        "post_webhook_url": post_webhook_url,
        "pre_webhook_url": pre_webhook_url,
        "reachability_enabled": reachability_enabled,
        "read_status_enabled": read_status_enabled,
        "typing_indicator_timeout": typing_indicator_timeout,
        "webhook_filters": webhook_filters,
        "webhook_method": webhook_method,
        "webhooks_on_channel_add_method": webhooks_on_channel_add_method,
        "webhooks_on_channel_add_url": webhooks_on_channel_add_url,
        "webhooks_on_channel_added_method": webhooks_on_channel_added_method,
        "webhooks_on_channel_added_url": webhooks_on_channel_added_url,
        "webhooks_on_channel_destroy_method": webhooks_on_channel_destroy_method,
        "webhooks_on_channel_destroy_url": webhooks_on_channel_destroy_url,
        "webhooks_on_channel_destroyed_method": webhooks_on_channel_destroyed_method,  # noqa
        "webhooks_on_channel_destroyed_url": webhooks_on_channel_destroyed_url,
        "webhooks_on_channel_update_method": webhooks_on_channel_update_method,
        "webhooks_on_channel_update_url": webhooks_on_channel_update_url,
        "webhooks_on_channel_updated_method": webhooks_on_channel_updated_method,
        "webhooks_on_channel_updated_url": webhooks_on_channel_updated_url,
        "webhooks_on_member_add_method": webhooks_on_member_add_method,
        "webhooks_on_member_add_url": webhooks_on_member_add_url,
        "webhooks_on_member_added_method": webhooks_on_member_added_method,
        "webhooks_on_member_added_url": webhooks_on_member_added_url,
        "webhooks_on_member_remove_method": webhooks_on_member_remove_method,
        "webhooks_on_member_remove_url": webhooks_on_member_remove_url,
        "webhooks_on_member_removed_method": webhooks_on_member_removed_method,
        "webhooks_on_member_removed_url": webhooks_on_member_removed_url,
        "webhooks_on_message_remove_method": webhooks_on_message_remove_method,
        "webhooks_on_message_remove_url": webhooks_on_message_remove_url,
        "webhooks_on_message_removed_method": webhooks_on_message_removed_method,
        "webhooks_on_message_removed_url": webhooks_on_message_removed_url,
        "webhooks_on_message_send_method": webhooks_on_message_send_method,
        "webhooks_on_message_send_url": webhooks_on_message_send_url,
        "webhooks_on_message_sent_method": webhooks_on_message_sent_method,
        "webhooks_on_message_sent_url": webhooks_on_message_sent_url,
        "webhooks_on_message_update_method": webhooks_on_message_update_method,
        "webhooks_on_message_update_url": webhooks_on_message_update_url,
        "webhooks_on_message_updated_method": webhooks_on_message_updated_method,
        "webhooks_on_message_updated_url": webhooks_on_message_updated_url,
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
async def get_v2_services(
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
    [https://ip-messaging.twilio.com/v2/Services?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v2/Services"  # noqa

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
async def post_v2_services(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services?](
    https://ip-messaging.twilio.com/v2/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://ip-messaging.twilio.com/v2/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v2_services_service_sid_bindings(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    binding_type: list = None,
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_type:

        identity:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings?&binding_type=%s&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "binding_type": binding_type,
        "identity": identity,
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
async def delete_v2_services_service_sid_bindings_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_bindings_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    type: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        type:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels?&type=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels?&type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "type": type,
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
async def post_v2_services_service_sid_channels(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    created_by: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    type: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        created_by:

        date_created:

        date_updated:

        friendly_name:

        type:

        unique_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "created_by": created_by,
        "date_created": date_created,
        "date_updated": date_updated,
        "friendly_name": friendly_name,
        "type": type,
        "unique_name": unique_name,
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
async def get_v2_services_service_sid_channels_channel_sid_invites(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v2_services_service_sid_channels_channel_sid_invites(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v2_services_service_sid_channels_channel_sid_invites_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels_channel_sid_invites_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels_channel_sid_members(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&identity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
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
async def post_v2_services_service_sid_channels_channel_sid_members(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    identity: str = None,
    last_consumed_message_index: int = None,
    last_consumption_timestamp: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        date_created:

        date_updated:

        identity:

        last_consumed_message_index:

        last_consumption_timestamp:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "identity": identity,
        "last_consumed_message_index": last_consumed_message_index,
        "last_consumption_timestamp": last_consumption_timestamp,
        "role_sid": role_sid,
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
async def delete_v2_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v2_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_members_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    date_created: str = None,
    date_updated: str = None,
    last_consumed_message_index: int = None,
    last_consumption_timestamp: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        date_created:

        date_updated:

        last_consumed_message_index:

        last_consumption_timestamp:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "date_created": date_created,
        "date_updated": date_updated,
        "last_consumed_message_index": last_consumed_message_index,
        "last_consumption_timestamp": last_consumption_timestamp,
        "role_sid": role_sid,
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
async def get_v2_services_service_sid_channels_channel_sid_messages(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        order:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "order": order,
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
async def post_v2_services_service_sid_channels_channel_sid_messages(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
    from_: str = None,
    last_updated_by: str = None,
    media_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        body:

        date_created:

        date_updated:

        from_:

        last_updated_by:

        media_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
        "from_": from_,
        "last_updated_by": last_updated_by,
        "media_sid": media_sid,
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
async def delete_v2_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v2_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_messages_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    body: str = None,
    date_created: str = None,
    date_updated: str = None,
    from_: str = None,
    last_updated_by: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        body:

        date_created:

        date_updated:

        from_:

        last_updated_by:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "body": body,
        "date_created": date_created,
        "date_updated": date_updated,
        "from_": from_,
        "last_updated_by": last_updated_by,
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
async def get_v2_services_service_sid_channels_channel_sid_webhooks(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks(
    service_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_retry_count: int = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:

        configuration_flow_sid:

        configuration_method:

        configuration_retry_count:

        configuration_triggers:

        configuration_url:

        type:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_retry_count": configuration_retry_count,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
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
async def delete_v2_services_service_sid_channels_channel_sid_webhooks_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
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
async def get_v2_services_service_sid_channels_channel_sid_webhooks_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_channel_sid_webhooks_sid(
    service_sid: str,
    channel_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    configuration_filters: list = None,
    configuration_flow_sid: str = None,
    configuration_method: str = None,
    configuration_retry_count: int = None,
    configuration_triggers: list = None,
    configuration_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        configuration_filters:

        configuration_flow_sid:

        configuration_method:

        configuration_retry_count:

        configuration_triggers:

        configuration_url:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "configuration_filters": configuration_filters,
        "configuration_flow_sid": configuration_flow_sid,
        "configuration_method": configuration_method,
        "configuration_retry_count": configuration_retry_count,
        "configuration_triggers": configuration_triggers,
        "configuration_url": configuration_url,
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
async def delete_v2_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
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
async def get_v2_services_service_sid_channels_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
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
async def post_v2_services_service_sid_channels_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    created_by: str = None,
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        created_by:

        date_created:

        date_updated:

        friendly_name:

        unique_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "created_by": created_by,
        "date_created": date_created,
        "date_updated": date_updated,
        "friendly_name": friendly_name,
        "unique_name": unique_name,
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
async def get_v2_services_service_sid_roles(
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
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles"  # noqa
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
async def post_v2_services_service_sid_roles(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    permission: list = None,
    type: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:

        permission:

        type:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "permission": permission,
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
async def delete_v2_services_service_sid_roles_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
    )
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
async def get_v2_services_service_sid_roles_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
    )
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
async def post_v2_services_service_sid_roles_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    permission: list = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        permission:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Roles/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "permission": permission,
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
async def get_v2_services_service_sid_users(
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
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users"  # noqa
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
async def post_v2_services_service_sid_users(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    identity: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        friendly_name:

        identity:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "identity": identity,
        "role_sid": role_sid,
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
async def delete_v2_services_service_sid_users_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
    )
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
async def get_v2_services_service_sid_users_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
    )
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
async def post_v2_services_service_sid_users_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    x_twilio_webhook_enabled: str = None,
    attributes: str = None,
    friendly_name: str = None,
    role_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        x_twilio_webhook_enabled:
            The X-Twilio-Webhook-Enabled HTTP request header.
        attributes:

        friendly_name:

        role_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}?&x_twilio_webhook_enabled=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "x_twilio_webhook_enabled": x_twilio_webhook_enabled,
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
        "role_sid": role_sid,
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
async def get_v2_services_service_sid_users_user_sid_bindings(
    service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    binding_type: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_type:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings?&binding_type=%s&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings?&binding_type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "binding_type": binding_type,
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
async def delete_v2_services_service_sid_users_user_sid_bindings_sid(
    service_sid: str,
    user_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_users_user_sid_bindings_sid(
    service_sid: str,
    user_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}"  # noqa
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
async def get_v2_services_service_sid_users_user_sid_channels(
    service_sid: str,
    user_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels"  # noqa
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
async def delete_v2_services_service_sid_users_user_sid_channels_channel_sid(
    service_sid: str,
    user_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
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
async def get_v2_services_service_sid_users_user_sid_channels_channel_sid(
    service_sid: str,
    user_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
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
async def post_v2_services_service_sid_users_user_sid_channels_channel_sid(
    service_sid: str,
    user_sid: str,
    channel_sid: str,
    twilio_credentials: "TwilioCredentials",
    last_consumed_message_index: int = None,
    last_consumption_timestamp: str = None,
    notification_level: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        user_sid:
            User sid used in formatting the endpoint URL.
        channel_sid:
            Channel sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        last_consumed_message_index:

        last_consumption_timestamp:

        notification_level:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?](
    https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "last_consumed_message_index": last_consumed_message_index,
        "last_consumption_timestamp": last_consumption_timestamp,
        "notification_level": notification_level,
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
async def delete_v2_services_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{sid}"  # noqa
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
async def get_v2_services_sid(
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
    [https://ip-messaging.twilio.com/v2/Services/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{sid}"  # noqa
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
async def post_v2_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    consumption_report_interval: int = None,
    default_channel_creator_role_sid: str = None,
    default_channel_role_sid: str = None,
    default_service_role_sid: str = None,
    friendly_name: str = None,
    limits_channel_members: int = None,
    limits_user_channels: int = None,
    media_compatibility_message: str = None,
    notifications_added_to_channel_enabled: bool = None,
    notifications_added_to_channel_sound: str = None,
    notifications_added_to_channel_template: str = None,
    notifications_invited_to_channel_enabled: bool = None,
    notifications_invited_to_channel_sound: str = None,
    notifications_invited_to_channel_template: str = None,
    notifications_log_enabled: bool = None,
    notifications_new_message_badge_count_enabled: bool = None,
    notifications_new_message_enabled: bool = None,
    notifications_new_message_sound: str = None,
    notifications_new_message_template: str = None,
    notifications_removed_from_channel_enabled: bool = None,
    notifications_removed_from_channel_sound: str = None,
    notifications_removed_from_channel_template: str = None,
    post_webhook_retry_count: int = None,
    post_webhook_url: str = None,
    pre_webhook_retry_count: int = None,
    pre_webhook_url: str = None,
    reachability_enabled: bool = None,
    read_status_enabled: bool = None,
    typing_indicator_timeout: int = None,
    webhook_filters: list = None,
    webhook_method: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        consumption_report_interval:

        default_channel_creator_role_sid:

        default_channel_role_sid:

        default_service_role_sid:

        friendly_name:

        limits_channel_members:

        limits_user_channels:

        media_compatibility_message:

        notifications_added_to_channel_enabled:

        notifications_added_to_channel_sound:

        notifications_added_to_channel_template:

        notifications_invited_to_channel_enabled:

        notifications_invited_to_channel_sound:

        notifications_invited_to_channel_template:

        notifications_log_enabled:

        notifications_new_message_badge_count_enabled:

        notifications_new_message_enabled:

        notifications_new_message_sound:

        notifications_new_message_template:

        notifications_removed_from_channel_enabled:

        notifications_removed_from_channel_sound:

        notifications_removed_from_channel_template:

        post_webhook_retry_count:

        post_webhook_url:

        pre_webhook_retry_count:

        pre_webhook_url:

        reachability_enabled:

        read_status_enabled:

        typing_indicator_timeout:

        webhook_filters:

        webhook_method:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://ip-messaging.twilio.com/v2/Services/{sid}?](
    https://ip-messaging.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://ip-messaging.twilio.com/v2/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "consumption_report_interval": consumption_report_interval,
        "default_channel_creator_role_sid": default_channel_creator_role_sid,
        "default_channel_role_sid": default_channel_role_sid,
        "default_service_role_sid": default_service_role_sid,
        "friendly_name": friendly_name,
        "limits_channel_members": limits_channel_members,
        "limits_user_channels": limits_user_channels,
        "media_compatibility_message": media_compatibility_message,
        "notifications_added_to_channel_enabled": notifications_added_to_channel_enabled,  # noqa
        "notifications_added_to_channel_sound": notifications_added_to_channel_sound,  # noqa
        "notifications_added_to_channel_template": notifications_added_to_channel_template,  # noqa
        "notifications_invited_to_channel_enabled": notifications_invited_to_channel_enabled,  # noqa
        "notifications_invited_to_channel_sound": notifications_invited_to_channel_sound,  # noqa
        "notifications_invited_to_channel_template": notifications_invited_to_channel_template,  # noqa
        "notifications_log_enabled": notifications_log_enabled,
        "notifications_new_message_badge_count_enabled": notifications_new_message_badge_count_enabled,  # noqa
        "notifications_new_message_enabled": notifications_new_message_enabled,
        "notifications_new_message_sound": notifications_new_message_sound,
        "notifications_new_message_template": notifications_new_message_template,
        "notifications_removed_from_channel_enabled": notifications_removed_from_channel_enabled,  # noqa
        "notifications_removed_from_channel_sound": notifications_removed_from_channel_sound,  # noqa
        "notifications_removed_from_channel_template": notifications_removed_from_channel_template,  # noqa
        "post_webhook_retry_count": post_webhook_retry_count,
        "post_webhook_url": post_webhook_url,
        "pre_webhook_retry_count": pre_webhook_retry_count,
        "pre_webhook_url": pre_webhook_url,
        "reachability_enabled": reachability_enabled,
        "read_status_enabled": read_status_enabled,
        "typing_indicator_timeout": typing_indicator_timeout,
        "webhook_filters": webhook_filters,
        "webhook_method": webhook_method,
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
    [https://messaging.twilio.com/v1/Services?&page_size=%s](
    https://messaging.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://messaging.twilio.com/v1/Services"  # noqa

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
    area_code_geomatch: bool = None,
    fallback_method: str = None,
    fallback_to_long_code: bool = None,
    fallback_url: str = None,
    friendly_name: str = None,
    inbound_method: str = None,
    inbound_request_url: str = None,
    mms_converter: bool = None,
    scan_message_content: str = None,
    smart_encoding: bool = None,
    status_callback: str = None,
    sticky_sender: bool = None,
    synchronous_validation: bool = None,
    use_inbound_webhook_on_number: bool = None,
    usecase: str = None,
    validity_period: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        area_code_geomatch:
            Whether to enable [Area Code
            Geomatch](https://www.twilio.com/docs/sms/services
            area-code-geomatch) on the Service Instance.
        fallback_method:
            The HTTP method we should use to call `fallback_url`. Can be: `GET` or
            `POST`.
        fallback_to_long_code:
            Whether to enable [Fallback to Long
            Code](https://www.twilio.com/docs/sms/services
            fallback-to-long-code) for messages sent through the Service
            instance.
        fallback_url:
            The URL that we call using `fallback_method` if an error occurs while
            retrieving or executing the TwiML from the Inbound Request
            URL. If the `use_inbound_webhook_on_number` field is enabled
            then the webhook url defined on the phone number will
            override the `fallback_url` defined for the Messaging
            Service.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        inbound_method:
            The HTTP method we should use to call `inbound_request_url`. Can be
            `GET` or `POST` and the default is `POST`.
        inbound_request_url:
            The URL we call using `inbound_method` when a message is received by any
            phone number or short code in the Service. When this
            property is `null`, receiving inbound messages is disabled.
            All messages sent to the Twilio phone number or short code
            will not be logged and received on the Account. If the
            `use_inbound_webhook_on_number` field is enabled then the
            webhook url defined on the phone number will override the
            `inbound_request_url` defined for the Messaging Service.
        mms_converter:
            Whether to enable the [MMS
            Converter](https://www.twilio.com/docs/sms/services
            mms-converter) for messages sent through the Service
            instance.
        scan_message_content:
            Reserved.
        smart_encoding:
            Whether to enable [Smart
            Encoding](https://www.twilio.com/docs/sms/services
            smart-encoding) for messages sent through the Service
            instance.
        status_callback:
            The URL we should call to [pass status
            updates](https://www.twilio.com/docs/sms/api/message-
            resource
            message-status-values) about message delivery.
        sticky_sender:
            Whether to enable [Sticky
            Sender](https://www.twilio.com/docs/sms/services
            sticky-sender) on the Service instance.
        synchronous_validation:
            Reserved.
        use_inbound_webhook_on_number:
            A boolean value that indicates either the webhook url configured on the
            phone number will be used or
            `inbound_request_url`/`fallback_url` url will be called when
            a message is received from the phone number. If this field
            is enabled then the webhook url defined on the phone number
            will override the `inbound_request_url`/`fallback_url`
            defined for the Messaging Service.
        usecase:
            A string that describes the scenario in which the Messaging Service will
            be used. Examples: [notification, marketing, verification,
            poll ..].
        validity_period:
            How long, in seconds, messages sent from the Service are valid. Can be
            an integer from `1` to `14,400`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services?](
    https://messaging.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://messaging.twilio.com/v1/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "area_code_geomatch": area_code_geomatch,
        "fallback_method": fallback_method,
        "fallback_to_long_code": fallback_to_long_code,
        "fallback_url": fallback_url,
        "friendly_name": friendly_name,
        "inbound_method": inbound_method,
        "inbound_request_url": inbound_request_url,
        "mms_converter": mms_converter,
        "scan_message_content": scan_message_content,
        "smart_encoding": smart_encoding,
        "status_callback": status_callback,
        "sticky_sender": sticky_sender,
        "synchronous_validation": synchronous_validation,
        "use_inbound_webhook_on_number": use_inbound_webhook_on_number,
        "usecase": usecase,
        "validity_period": validity_period,
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
async def post_v1_services_preregistered_usa2p(
    twilio_credentials: "TwilioCredentials",
    campaign_id: str = None,
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        campaign_id:
            ID of the preregistered campaign.
        messaging_service_sid:
            The SID of the [Messaging
            Service](https://www.twilio.com/docs/messaging/services/api)
            that the resource is associated with.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/PreregisteredUsa2p?](
    https://messaging.twilio.com/v1/Services/PreregisteredUsa2p?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://messaging.twilio.com/v1/Services/PreregisteredUsa2p"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "campaign_id": campaign_id,
        "messaging_service_sid": messaging_service_sid,
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
async def get_v1_services_usecases(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/Usecases?](
    https://messaging.twilio.com/v1/Services/Usecases?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://messaging.twilio.com/v1/Services/Usecases"  # noqa

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
async def get_v1_services_messaging_service_sid_compliance_usa2p(
    messaging_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        messaging_service_sid:
            Messaging service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p?&page_size=%s](
    https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p"  # noqa
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
async def post_v1_services_messaging_service_sid_compliance_usa2p(
    messaging_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    brand_registration_sid: str = None,
    description: str = None,
    has_embedded_links: bool = None,
    has_embedded_phone: bool = None,
    message_samples: list = None,
    us_app_to_person_usecase: str = None,
) -> Dict[str, Any]:
    """


    Args:
        messaging_service_sid:
            Messaging service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        brand_registration_sid:
            A2P Brand Registration SID.
        description:
            A short description of what this SMS campaign does.
        has_embedded_links:
            Indicates that this SMS campaign will send messages that contain links.
        has_embedded_phone:
            Indicates that this SMS campaign will send messages that contain phone
            numbers.
        message_samples:
            Message samples, at least 2 and up to 5 sample messages, <=1024 chars
            each.
        us_app_to_person_usecase:
            A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..].

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p?](
    https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "brand_registration_sid": brand_registration_sid,
        "description": description,
        "has_embedded_links": has_embedded_links,
        "has_embedded_phone": has_embedded_phone,
        "message_samples": message_samples,
        "us_app_to_person_usecase": us_app_to_person_usecase,
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
async def get_v1_services_messaging_service_sid_compliance_usa2p_usecases(
    messaging_service_sid: str,
    twilio_credentials: "TwilioCredentials",
    brand_registration_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        messaging_service_sid:
            Messaging service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        brand_registration_sid:
            The unique string to identify the A2P brand.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p/Usecases?&brand_registration_sid=%s](
    https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p/Usecases?&brand_registration_sid=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p/Usecases"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "brand_registration_sid": brand_registration_sid,
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
async def delete_v1_services_messaging_service_sid_compliance_usa2p_sid(
    messaging_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        messaging_service_sid:
            Messaging service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}?](
    https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}"  # noqa
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
async def get_v1_services_messaging_service_sid_compliance_usa2p_sid(
    messaging_service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        messaging_service_sid:
            Messaging service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}?](
    https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}"  # noqa
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
async def get_v1_services_service_sid_alpha_senders(
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
    [https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders?&page_size=%s](
    https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders"  # noqa
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
async def post_v1_services_service_sid_alpha_senders(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    alpha_sender: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        alpha_sender:
            The Alphanumeric Sender ID string. Can be up to 11 characters long.
            Valid characters are A-Z, a-z, 0-9, space, and hyphen `-`.
            This value cannot contain only numbers.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders?](
    https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "alpha_sender": alpha_sender,
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
async def delete_v1_services_service_sid_alpha_senders_sid(
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
    [https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders/{sid}?](
    https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders/{sid}"  # noqa
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
async def get_v1_services_service_sid_alpha_senders_sid(
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
    [https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders/{sid}?](
    https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/AlphaSenders/{sid}"  # noqa
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
async def get_v1_services_service_sid_phone_numbers(
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
    [https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers?&page_size=%s](
    https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers"  # noqa
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
async def post_v1_services_service_sid_phone_numbers(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    phone_number_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        phone_number_sid:
            The SID of the Phone Number being added to the Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers?](
    https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "phone_number_sid": phone_number_sid,
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
async def delete_v1_services_service_sid_phone_numbers_sid(
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
    [https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?](
    https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}"  # noqa
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
async def get_v1_services_service_sid_phone_numbers_sid(
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
    [https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?](
    https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}"  # noqa
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
async def get_v1_services_service_sid_short_codes(
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
    [https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes?&page_size=%s](
    https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes"  # noqa
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
async def post_v1_services_service_sid_short_codes(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    short_code_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        short_code_sid:
            The SID of the ShortCode resource being added to the Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes?](
    https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "short_code_sid": short_code_sid,
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
async def delete_v1_services_service_sid_short_codes_sid(
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
    [https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?](
    https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}"  # noqa
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
async def get_v1_services_service_sid_short_codes_sid(
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
    [https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?](
    https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}"  # noqa
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
    [https://messaging.twilio.com/v1/Services/{sid}?](
    https://messaging.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{sid}"  # noqa
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
    [https://messaging.twilio.com/v1/Services/{sid}?](
    https://messaging.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{sid}"  # noqa
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
    area_code_geomatch: bool = None,
    fallback_method: str = None,
    fallback_to_long_code: bool = None,
    fallback_url: str = None,
    friendly_name: str = None,
    inbound_method: str = None,
    inbound_request_url: str = None,
    mms_converter: bool = None,
    scan_message_content: str = None,
    smart_encoding: bool = None,
    status_callback: str = None,
    sticky_sender: bool = None,
    synchronous_validation: bool = None,
    use_inbound_webhook_on_number: bool = None,
    usecase: str = None,
    validity_period: int = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        area_code_geomatch:
            Whether to enable [Area Code
            Geomatch](https://www.twilio.com/docs/sms/services
            area-code-geomatch) on the Service Instance.
        fallback_method:
            The HTTP method we should use to call `fallback_url`. Can be: `GET` or
            `POST`.
        fallback_to_long_code:
            Whether to enable [Fallback to Long
            Code](https://www.twilio.com/docs/sms/services
            fallback-to-long-code) for messages sent through the Service
            instance.
        fallback_url:
            The URL that we call using `fallback_method` if an error occurs while
            retrieving or executing the TwiML from the Inbound Request
            URL. If the `use_inbound_webhook_on_number` field is enabled
            then the webhook url defined on the phone number will
            override the `fallback_url` defined for the Messaging
            Service.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        inbound_method:
            The HTTP method we should use to call `inbound_request_url`. Can be
            `GET` or `POST` and the default is `POST`.
        inbound_request_url:
            The URL we call using `inbound_method` when a message is received by any
            phone number or short code in the Service. When this
            property is `null`, receiving inbound messages is disabled.
            All messages sent to the Twilio phone number or short code
            will not be logged and received on the Account. If the
            `use_inbound_webhook_on_number` field is enabled then the
            webhook url defined on the phone number will override the
            `inbound_request_url` defined for the Messaging Service.
        mms_converter:
            Whether to enable the [MMS
            Converter](https://www.twilio.com/docs/sms/services
            mms-converter) for messages sent through the Service
            instance.
        scan_message_content:
            Reserved.
        smart_encoding:
            Whether to enable [Smart
            Encoding](https://www.twilio.com/docs/sms/services
            smart-encoding) for messages sent through the Service
            instance.
        status_callback:
            The URL we should call to [pass status
            updates](https://www.twilio.com/docs/sms/api/message-
            resource
            message-status-values) about message delivery.
        sticky_sender:
            Whether to enable [Sticky
            Sender](https://www.twilio.com/docs/sms/services
            sticky-sender) on the Service instance.
        synchronous_validation:
            Reserved.
        use_inbound_webhook_on_number:
            A boolean value that indicates either the webhook url configured on the
            phone number will be used or
            `inbound_request_url`/`fallback_url` url will be called when
            a message is received from the phone number. If this field
            is enabled then the webhook url defined on the phone number
            will override the `inbound_request_url`/`fallback_url`
            defined for the Messaging Service.
        usecase:
            A string that describes the scenario in which the Messaging Service will
            be used. Examples: [notification, marketing, verification,
            poll ..].
        validity_period:
            How long, in seconds, messages sent from the Service are valid. Can be
            an integer from `1` to `14,400`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Services/{sid}?](
    https://messaging.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "area_code_geomatch": area_code_geomatch,
        "fallback_method": fallback_method,
        "fallback_to_long_code": fallback_to_long_code,
        "fallback_url": fallback_url,
        "friendly_name": friendly_name,
        "inbound_method": inbound_method,
        "inbound_request_url": inbound_request_url,
        "mms_converter": mms_converter,
        "scan_message_content": scan_message_content,
        "smart_encoding": smart_encoding,
        "status_callback": status_callback,
        "sticky_sender": sticky_sender,
        "synchronous_validation": synchronous_validation,
        "use_inbound_webhook_on_number": use_inbound_webhook_on_number,
        "usecase": usecase,
        "validity_period": validity_period,
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
async def get_v1_services(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The string that identifies the Service resources to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services?&friendly_name=%s&page_size=%s](
    https://notify.twilio.com/v1/Services?&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://notify.twilio.com/v1/Services"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "friendly_name": friendly_name,
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
    alexa_skill_id: str = None,
    apn_credential_sid: str = None,
    default_alexa_notification_protocol_version: str = None,
    default_apn_notification_protocol_version: str = None,
    default_fcm_notification_protocol_version: str = None,
    default_gcm_notification_protocol_version: str = None,
    delivery_callback_enabled: bool = None,
    delivery_callback_url: str = None,
    facebook_messenger_page_id: str = None,
    fcm_credential_sid: str = None,
    friendly_name: str = None,
    gcm_credential_sid: str = None,
    log_enabled: bool = None,
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        alexa_skill_id:
            Deprecated.
        apn_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for APN Bindings.
        default_alexa_notification_protocol_version:
            Deprecated.
        default_apn_notification_protocol_version:
            The protocol version to use for sending APNS notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        default_fcm_notification_protocol_version:
            The protocol version to use for sending FCM notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        default_gcm_notification_protocol_version:
            The protocol version to use for sending GCM notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        delivery_callback_enabled:
            Callback configuration that enables delivery callbacks, default false.
        delivery_callback_url:
            URL to send delivery status callback.
        facebook_messenger_page_id:
            Deprecated.
        fcm_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for FCM Bindings.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        gcm_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for GCM Bindings.
        log_enabled:
            Whether to log notifications. Can be: `true` or `false` and the default
            is `true`.
        messaging_service_sid:
            The SID of the [Messaging Service](https://www.twilio.com/docs/sms/send-
            messages
            messaging-services) to use for SMS Bindings. This parameter
            must be set in order to send SMS notifications.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services?](
    https://notify.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://notify.twilio.com/v1/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "alexa_skill_id": alexa_skill_id,
        "apn_credential_sid": apn_credential_sid,
        "default_alexa_notification_protocol_version": default_alexa_notification_protocol_version,  # noqa
        "default_apn_notification_protocol_version": default_apn_notification_protocol_version,  # noqa
        "default_fcm_notification_protocol_version": default_fcm_notification_protocol_version,  # noqa
        "default_gcm_notification_protocol_version": default_gcm_notification_protocol_version,  # noqa
        "delivery_callback_enabled": delivery_callback_enabled,
        "delivery_callback_url": delivery_callback_url,
        "facebook_messenger_page_id": facebook_messenger_page_id,
        "fcm_credential_sid": fcm_credential_sid,
        "friendly_name": friendly_name,
        "gcm_credential_sid": gcm_credential_sid,
        "log_enabled": log_enabled,
        "messaging_service_sid": messaging_service_sid,
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
async def get_v1_services_service_sid_bindings(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    start_date: str = None,
    end_date: str = None,
    identity: list = None,
    tag: list = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.
        identity:
            The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s
            `identity` value of the resources to read.
        tag:
            Only list Bindings that have all of the specified Tags. The following
            implicit tags are available: `all`, `apn`, `fcm`, `gcm`,
            `sms`, `facebook-messenger`. Up to 5 tags are allowed.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services/{service_sid}/Bindings?&start_date=%s&end_date=%s&identity=%s&tag=%s&page_size=%s](
    https://notify.twilio.com/v1/Services/{service_sid}/Bindings?&start_date=%s&end_date=%s&identity=%s&tag=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Bindings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "start_date": start_date,
        "end_date": end_date,
        "identity": identity,
        "tag": tag,
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
async def post_v1_services_service_sid_bindings(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    address: str = None,
    binding_type: str = None,
    credential_sid: str = None,
    endpoint: str = None,
    identity: str = None,
    notification_protocol_version: str = None,
    tag: list = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        address:
            The channel-specific address. For APNS, the device token. For FCM and
            GCM, the registration token. For SMS, a phone number in
            E.164 format. For Facebook Messenger, the Messenger ID of
            the user or a phone number in E.164 format.
        binding_type:
            The transport technology to use for the Binding. Can be: `apn`, `fcm`,
            `gcm`, `sms`, or `facebook-messenger`.
        credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) resource to be used to send notifications to this
            Binding. If present, this overrides the Credential specified
            in the Service resource. Applies to only `apn`, `fcm`, and
            `gcm` type Bindings.
        endpoint:
            Deprecated.
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/notify/api/service-
            resource). Up to 20 Bindings can be created for the same
            Identity in a given Service.
        notification_protocol_version:
            The protocol version to use to send the notification. This defaults to
            the value of `default_xxxx_notification_protocol_version`
            for the protocol in the
            [Service](https://www.twilio.com/docs/notify/api/service-
            resource). The current version is `"3"` for `apn`, `fcm`,
            and `gcm` type Bindings. The parameter is not applicable to
            `sms` and `facebook-messenger` type Bindings as the data
            format is fixed.
        tag:
            A tag that can be used to select the Bindings to notify. Repeat this
            parameter to specify more than one tag, up to a total of 20
            tags.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services/{service_sid}/Bindings?](
    https://notify.twilio.com/v1/Services/{service_sid}/Bindings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Bindings"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "address": address,
        "binding_type": binding_type,
        "credential_sid": credential_sid,
        "endpoint": endpoint,
        "identity": identity,
        "notification_protocol_version": notification_protocol_version,
        "tag": tag,
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
async def delete_v1_services_service_sid_bindings_sid(
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
    [https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}?](
    https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def get_v1_services_service_sid_bindings_sid(
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
    [https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}?](
    https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Bindings/{sid}"  # noqa
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
async def post_v1_services_service_sid_notifications(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    action: str = None,
    alexa: str = None,
    apn: str = None,
    body: str = None,
    data: str = None,
    delivery_callback_url: str = None,
    facebook_messenger: str = None,
    fcm: str = None,
    gcm: str = None,
    identity: list = None,
    priority: str = None,
    segment: list = None,
    sms: str = None,
    sound: str = None,
    tag: list = None,
    title: str = None,
    to_binding: list = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        action:
            The actions to display for the notification. For APNS, translates to the
            `aps.category` value. For GCM, translates to the
            `data.twi_action` value. For SMS, this parameter is not
            supported and is omitted from deliveries to those channels.
        alexa:
            Deprecated.
        apn:
            The APNS-specific payload that overrides corresponding attributes in the
            generic payload for APNS Bindings. This property maps to the
            APNS `Payload` item, therefore the `aps` key must be used to
            change standard attributes. Adds custom key-value pairs to
            the root of the dictionary. See the [APNS
            documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html)
            for more details. We reserve keys that start with `twi_` for
            future use. Custom keys that start with `twi_` are not
            allowed.
        body:
            The notification text. For FCM and GCM, translates to `data.twi_body`.
            For APNS, translates to `aps.alert.body`. For SMS,
            translates to `body`. SMS requires either this `body` value,
            or `media_urls` attribute defined in the `sms` parameter of
            the notification.
        data:
            The custom key-value pairs of the notification's payload. For FCM and
            GCM, this value translates to `data` in the FCM and GCM
            payloads. FCM and GCM [reserve certain
            keys](https://firebase.google.com/docs/cloud-messaging/http-
            server-ref) that cannot be used in those channels. For APNS,
            attributes of `data` are inserted into the APNS payload as
            custom properties outside of the `aps` dictionary. In all
            channels, we reserve keys that start with `twi_` for future
            use. Custom keys that start with `twi_` are not allowed and
            are rejected as 400 Bad request with no delivery attempted.
            For SMS, this parameter is not supported and is omitted from
            deliveries to those channels.
        delivery_callback_url:
            URL to send webhooks.
        facebook_messenger:
            Deprecated.
        fcm:
            The FCM-specific payload that overrides corresponding attributes in the
            generic payload for FCM Bindings. This property maps to the
            root JSON dictionary. See the [FCM
            documentation](https://firebase.google.com/docs/cloud-
            messaging/http-server-ref
            downstream) for more details. Target parameters `to`,
            `registration_ids`, `condition`, and `notification_key` are
            not allowed in this parameter. We reserve keys that start
            with `twi_` for future use. Custom keys that start with
            `twi_` are not allowed. FCM also [reserves certain
            keys](https://firebase.google.com/docs/cloud-messaging/http-
            server-ref), which cannot be used in that channel.
        gcm:
            The GCM-specific payload that overrides corresponding attributes in the
            generic payload for GCM Bindings.  This property maps to the
            root JSON dictionary. See the [GCM
            documentation](https://firebase.google.com/docs/cloud-
            messaging/http-server-ref) for more details. Target
            parameters `to`, `registration_ids`, and `notification_key`
            are not allowed. We reserve keys that start with `twi_` for
            future use. Custom keys that start with `twi_` are not
            allowed. GCM also [reserves certain
            keys](https://firebase.google.com/docs/cloud-messaging/http-
            server-ref).
        identity:
            The `identity` value that uniquely identifies the new resource's
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            within the
            [Service](https://www.twilio.com/docs/notify/api/service-
            resource). Delivery will be attempted only to Bindings with
            an Identity in this list. No more than 20 items are allowed
            in this list.
        priority:
            The priority of the notification. Can be: `low` or `high` and the
            default is `high`. A value of `low` optimizes the client
            app's battery consumption; however, notifications may be
            delivered with unspecified delay. For FCM and GCM, `low`
            priority is the same as `Normal` priority. For APNS `low`
            priority is the same as `5`. A value of `high` sends the
            notification immediately, and can wake up a sleeping device.
            For FCM and GCM, `high` is the same as `High` priority. For
            APNS, `high` is a priority `10`. SMS does not support this
            property.
        segment:
            The Segment resource is deprecated. Use the `tag` parameter, instead.
        sms:
            The SMS-specific payload that overrides corresponding attributes in the
            generic payload for SMS Bindings.  Each attribute in this
            value maps to the corresponding `form` parameter of the
            Twilio [Message](https://www.twilio.com/docs/sms/send-
            messages) resource.  These parameters of the Message
            resource are supported in snake case format: `body`,
            `media_urls`, `status_callback`, and `max_price`.  The
            `status_callback` parameter overrides the corresponding
            parameter in the messaging service, if configured. The
            `media_urls` property expects a JSON array.
        sound:
            The name of the sound to be played for the notification. For FCM and
            GCM, this Translates to `data.twi_sound`.  For APNS, this
            translates to `aps.sound`.  SMS does not support this
            property.
        tag:
            A tag that selects the Bindings to notify. Repeat this parameter to
            specify more than one tag, up to a total of 5 tags. The
            implicit tag `all` is available to notify all Bindings in a
            Service instance. Similarly, the implicit tags `apn`, `fcm`,
            `gcm`, `sms` and `facebook-messenger` are available to
            notify all Bindings in a specific channel.
        title:
            The notification title. For FCM and GCM, this translates to the
            `data.twi_title` value. For APNS, this translates to the
            `aps.alert.title` value. SMS does not support this property.
            This field is not visible on iOS phones and tablets but
            appears on Apple Watch and Android devices.
        to_binding:
            The destination address specified as a JSON string.  Multiple
            `to_binding` parameters can be included but the total size
            of the request entity should not exceed 1MB. This is
            typically sufficient for 10,000 phone numbers.
        ttl:
            How long, in seconds, the notification is valid. Can be an integer
            between 0 and 2,419,200, which is 4 weeks, the default and
            the maximum supported time to live (TTL). Delivery should be
            attempted if the device is offline until the TTL elapses.
            Zero means that the notification delivery is attempted
            immediately, only once, and is not stored for future
            delivery. SMS does not support this property.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services/{service_sid}/Notifications?](
    https://notify.twilio.com/v1/Services/{service_sid}/Notifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{service_sid}/Notifications"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "action": action,
        "alexa": alexa,
        "apn": apn,
        "body": body,
        "data": data,
        "delivery_callback_url": delivery_callback_url,
        "facebook_messenger": facebook_messenger,
        "fcm": fcm,
        "gcm": gcm,
        "identity": identity,
        "priority": priority,
        "segment": segment,
        "sms": sms,
        "sound": sound,
        "tag": tag,
        "title": title,
        "to_binding": to_binding,
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
    [https://notify.twilio.com/v1/Services/{sid}?](
    https://notify.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{sid}"  # noqa
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
    [https://notify.twilio.com/v1/Services/{sid}?](
    https://notify.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{sid}"  # noqa
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
    alexa_skill_id: str = None,
    apn_credential_sid: str = None,
    default_alexa_notification_protocol_version: str = None,
    default_apn_notification_protocol_version: str = None,
    default_fcm_notification_protocol_version: str = None,
    default_gcm_notification_protocol_version: str = None,
    delivery_callback_enabled: bool = None,
    delivery_callback_url: str = None,
    facebook_messenger_page_id: str = None,
    fcm_credential_sid: str = None,
    friendly_name: str = None,
    gcm_credential_sid: str = None,
    log_enabled: bool = None,
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        alexa_skill_id:
            Deprecated.
        apn_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for APN Bindings.
        default_alexa_notification_protocol_version:
            Deprecated.
        default_apn_notification_protocol_version:
            The protocol version to use for sending APNS notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        default_fcm_notification_protocol_version:
            The protocol version to use for sending FCM notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        default_gcm_notification_protocol_version:
            The protocol version to use for sending GCM notifications. Can be
            overridden on a Binding by Binding basis when creating a
            [Binding](https://www.twilio.com/docs/notify/api/binding-
            resource) resource.
        delivery_callback_enabled:
            Callback configuration that enables delivery callbacks, default false.
        delivery_callback_url:
            URL to send delivery status callback.
        facebook_messenger_page_id:
            Deprecated.
        fcm_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for FCM Bindings.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        gcm_credential_sid:
            The SID of the
            [Credential](https://www.twilio.com/docs/notify/api/credential-
            resource) to use for GCM Bindings.
        log_enabled:
            Whether to log notifications. Can be: `true` or `false` and the default
            is `true`.
        messaging_service_sid:
            The SID of the [Messaging Service](https://www.twilio.com/docs/sms/send-
            messages
            messaging-services) to use for SMS Bindings. This parameter
            must be set in order to send SMS notifications.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://notify.twilio.com/v1/Services/{sid}?](
    https://notify.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://notify.twilio.com/v1/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "alexa_skill_id": alexa_skill_id,
        "apn_credential_sid": apn_credential_sid,
        "default_alexa_notification_protocol_version": default_alexa_notification_protocol_version,  # noqa
        "default_apn_notification_protocol_version": default_apn_notification_protocol_version,  # noqa
        "default_fcm_notification_protocol_version": default_fcm_notification_protocol_version,  # noqa
        "default_gcm_notification_protocol_version": default_gcm_notification_protocol_version,  # noqa
        "delivery_callback_enabled": delivery_callback_enabled,
        "delivery_callback_url": delivery_callback_url,
        "facebook_messenger_page_id": facebook_messenger_page_id,
        "fcm_credential_sid": fcm_credential_sid,
        "friendly_name": friendly_name,
        "gcm_credential_sid": gcm_credential_sid,
        "log_enabled": log_enabled,
        "messaging_service_sid": messaging_service_sid,
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
async def get_v1_services(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Services for Twilio Proxy. A maximum of 100 records will
    be returned per page.

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
    [https://proxy.twilio.com/v1/Services?&page_size=%s](
    https://proxy.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://proxy.twilio.com/v1/Services"  # noqa

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
    callback_url: str = None,
    chat_instance_sid: str = None,
    default_ttl: int = None,
    geo_match_level: str = None,
    intercept_callback_url: str = None,
    number_selection_behavior: str = None,
    out_of_session_callback_url: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Service for Twilio Proxy.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_url:
            The URL we should call when the interaction status changes.
        chat_instance_sid:
            The SID of the Chat Service Instance managed by Proxy Service. The Chat
            Service enables Proxy to forward SMS and channel messages to
            this chat instance. This is a one-to-one relationship.
        default_ttl:
            The default `ttl` value to set for Sessions created in the Service. The
            TTL (time to live) is measured in seconds after the
            Session's last create or last Interaction. The default value
            of `0` indicates an unlimited Session length. You can
            override a Session's default TTL value by setting its `ttl`
            value.
        geo_match_level:
            Where a proxy number must be located relative to the participant
            identifier. Can be: `country`, `area-code`, or `extended-
            area-code`. The default value is `country` and more specific
            areas than `country` are only available in North America.
        intercept_callback_url:
            The URL we call on each interaction. If we receive a 403 status, we
            block the interaction; otherwise the interaction continues.
        number_selection_behavior:
            The preference for Proxy Number selection in the Service instance. Can
            be: `prefer-sticky` or `avoid-sticky` and the default is
            `prefer-sticky`. `prefer-sticky` means that we will try and
            select the same Proxy Number for a given participant if they
            have previous
            [Sessions](https://www.twilio.com/docs/proxy/api/session),
            but we will not fail if that Proxy Number cannot be used.
            `avoid-sticky` means that we will try to use different Proxy
            Numbers as long as that is possible within a given pool
            rather than try and use a previously assigned number.
        out_of_session_callback_url:
            The URL we should call when an inbound call or SMS action occurs on a
            closed or non-existent Session. If your server (or a Twilio
            [function](https://www.twilio.com/functions)) responds with
            valid [TwiML](https://www.twilio.com/docs/voice/twiml), we
            will process it. This means it is possible, for example, to
            play a message for a call, send an automated text message
            response, or redirect a call to another Phone Number. See
            [Out-of-Session Callback Response
            Guide](https://www.twilio.com/docs/proxy/out-session-
            callback-response-guide) for more information.
        unique_name:
            An application-defined string that uniquely identifies the resource.
            This value must be 191 characters or fewer in length and be
            unique. **This value should not have PII.**.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services?](
    https://proxy.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://proxy.twilio.com/v1/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "callback_url": callback_url,
        "chat_instance_sid": chat_instance_sid,
        "default_ttl": default_ttl,
        "geo_match_level": geo_match_level,
        "intercept_callback_url": intercept_callback_url,
        "number_selection_behavior": number_selection_behavior,
        "out_of_session_callback_url": out_of_session_callback_url,
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
async def get_v1_services_service_sid_phone_numbers(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Phone Numbers in the Proxy Number Pool for a Service. A
    maximum of 100 records will be returned per page.

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
    [https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers?&page_size=%s](
    https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers"  # noqa
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
async def post_v1_services_service_sid_phone_numbers(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    is_reserved: bool = None,
    phone_number: str = None,
    sid: str = None,
) -> Dict[str, Any]:
    """
    Add a Phone Number to a Service's Proxy Number Pool.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        is_reserved:
            Whether the new phone number should be reserved and not be assigned to a
            participant using proxy pool logic. See [Reserved Phone
            Numbers](https://www.twilio.com/docs/proxy/reserved-phone-
            numbers) for more information.
        phone_number:
            The phone number in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format.  E.164 phone numbers consist of a + followed by the
            country code and subscriber number without punctuation
            characters. For example, +14155551234.
        sid:
            The SID of a Twilio
            [IncomingPhoneNumber](https://www.twilio.com/docs/phone-
            numbers/api/incomingphonenumber-resource) resource that
            represents the Twilio Number you would like to assign to
            your Proxy Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers?](
    https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "is_reserved": is_reserved,
        "phone_number": phone_number,
        "sid": sid,
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
async def delete_v1_services_service_sid_phone_numbers_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Phone Number from a Service.

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
    [https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}"  # noqa
    )
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
async def get_v1_services_service_sid_phone_numbers_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Phone Number.

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
    [https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}"  # noqa
    )
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
async def post_v1_services_service_sid_phone_numbers_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    is_reserved: bool = None,
) -> Dict[str, Any]:
    """
    Update a specific Proxy Number.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        is_reserved:
            Whether the phone number should be reserved and not be assigned to a
            participant using proxy pool logic. See [Reserved Phone
            Numbers](https://www.twilio.com/docs/proxy/reserved-phone-
            numbers) for more information.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://proxy.twilio.com/v1/Services/{service_sid}/PhoneNumbers/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "is_reserved": is_reserved,
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
async def get_v1_services_service_sid_sessions(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Sessions for the Service. A maximum of 100 records will
    be returned per page.

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
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions?&page_size=%s](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions"  # noqa
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
async def post_v1_services_service_sid_sessions(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    date_expiry: str = None,
    fail_on_participant_conflict: bool = None,
    mode: str = None,
    participants: list = None,
    status: str = None,
    ttl: int = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Session.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_expiry:
            The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the
            Session should expire. If this is value is present, it
            overrides the `ttl` value.
        fail_on_participant_conflict:
            [Experimental] For accounts with the ProxyAllowParticipantConflict
            account flag, setting to true enables per-request opt-in to
            allowing Proxy to reject a Session create (with
            Participants) request that could cause the same
            Identifier/ProxyIdentifier pair to be active in multiple
            Sessions. Depending on the context, this could be a 409
            error (Twilio error code 80623) or a 400 error (Twilio error
            code 80604). If not provided, requests will be allowed to
            succeed and a Debugger notification (80802) will be emitted.
            Having multiple, active Participants with the same
            Identifier/ProxyIdentifier pair causes calls and messages
            from affected Participants to be routed incorrectly. Please
            note, the default behavior for accounts without the
            ProxyAllowParticipantConflict flag is to reject the request
            as described.  This will eventually be the default for all
            accounts.
        mode:
            The Mode of the Session. Can be: `message-only`, `voice-only`, or
            `voice-and-message` and the default value is `voice-and-
            message`.
        participants:
            The Participant objects to include in the new session.
        status:
            The initial status of the Session. Can be: `open`, `in-progress`,
            `closed`, `failed`, or `unknown`. The default is `open` on
            create.
        ttl:
            The time, in seconds, when the session will expire. The time is measured
            from the last Session create or the Session's last
            Interaction.
        unique_name:
            An application-defined string that uniquely identifies the resource.
            This value must be 191 characters or fewer in length and be
            unique. **This value should not have PII.**.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "date_expiry": date_expiry,
        "fail_on_participant_conflict": fail_on_participant_conflict,
        "mode": mode,
        "participants": participants,
        "status": status,
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
async def get_v1_services_service_sid_sessions_session_sid_interactions(
    service_sid: str,
    session_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Interactions for a Session. A maximum of 100 records will
    be returned per page.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions?&page_size=%s](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions"  # noqa
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
async def delete_v1_services_service_sid_sessions_session_sid_interactions_sid(
    service_sid: str,
    session_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Interaction.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions/{sid}"  # noqa
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
async def get_v1_services_service_sid_sessions_session_sid_interactions_sid(
    service_sid: str,
    session_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a list of Interactions for a given
    [Session](https://www.twilio.com/docs/proxy/api/session).

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions/{sid}"  # noqa
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
async def get_v1_services_service_sid_sessions_session_sid_participants(
    service_sid: str,
    session_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Participants in a Session.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants?&page_size=%s](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants"  # noqa
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
async def post_v1_services_service_sid_sessions_session_sid_participants(
    service_sid: str,
    session_sid: str,
    twilio_credentials: "TwilioCredentials",
    fail_on_participant_conflict: bool = None,
    friendly_name: str = None,
    identifier: str = None,
    proxy_identifier: str = None,
    proxy_identifier_sid: str = None,
) -> Dict[str, Any]:
    """
    Add a new Participant to the Session.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        fail_on_participant_conflict:
            [Experimental] For accounts with the ProxyAllowParticipantConflict
            account flag, setting to true enables per-request opt-in to
            allowing Proxy to reject a Participant create request that
            could cause the same Identifier/ProxyIdentifier pair to be
            active in multiple Sessions. Depending on the context, this
            could be a 409 error (Twilio error code 80623) or a 400
            error (Twilio error code 80604). If not provided, requests
            will be allowed to succeed and a Debugger notification
            (80802) will be emitted. Having multiple, active
            Participants with the same Identifier/ProxyIdentifier pair
            causes calls and messages from affected Participants to be
            routed incorrectly. Please note, the default behavior for
            accounts without the ProxyAllowParticipantConflict flag is
            to reject the request as described.  This will eventually be
            the default for all accounts.
        friendly_name:
            The string that you assigned to describe the participant. This value
            must be 255 characters or fewer. **This value should not
            have PII.**.
        identifier:
            The phone number of the Participant.
        proxy_identifier:
            The proxy phone number to use for the Participant. If not specified,
            Proxy will select a number from the pool.
        proxy_identifier_sid:
            The SID of the Proxy Identifier to assign to the Participant.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "fail_on_participant_conflict": fail_on_participant_conflict,
        "friendly_name": friendly_name,
        "identifier": identifier,
        "proxy_identifier": proxy_identifier,
        "proxy_identifier_sid": proxy_identifier_sid,
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
async def get_v1_services_service_sid_sessions_session_sid_participants_participant_sid_message_interactions(
    service_sid: str,
    session_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions?&page_size=%s](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions"  # noqa
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
async def post_v1_services_service_sid_sessions_session_sid_participants_participant_sid_message_interactions(
    service_sid: str,
    session_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
    body: str = None,
    media_url: list = None,
) -> Dict[str, Any]:
    """
    Create a new message Interaction to send directly from your system to one
    [Participant](https://www.twilio.com/docs/proxy/api/participant).  The
    `inbound` properties for the Interaction will always be empty.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        body:
            The message to send to the participant.
        media_url:
            Reserved. Not currently supported.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "body": body,
        "media_url": media_url,
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
async def get_v1_services_service_sid_sessions_session_sid_participants_participant_sid_message_interactions_sid(
    service_sid: str,
    session_sid: str,
    participant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions/{sid}"  # noqa
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
async def delete_v1_services_service_sid_sessions_session_sid_participants_sid(
    service_sid: str,
    session_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Participant. This is a soft-delete. The participant remains
    associated with the session and cannot be re-added. Participants are only
    permanently deleted when the
    [Session](https://www.twilio.com/docs/proxy/api/session) is deleted.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}"  # noqa
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
async def get_v1_services_service_sid_sessions_session_sid_participants_sid(
    service_sid: str,
    session_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Participant.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        session_sid:
            Session sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}"  # noqa
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
async def delete_v1_services_service_sid_sessions_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Session.

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
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{sid}"  # noqa
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
async def get_v1_services_service_sid_sessions_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Session.

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
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{sid}"  # noqa
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
async def post_v1_services_service_sid_sessions_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    date_expiry: str = None,
    fail_on_participant_conflict: bool = None,
    status: str = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """
    Update a specific Session.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_expiry:
            The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the
            Session should expire. If this is value is present, it
            overrides the `ttl` value.
        fail_on_participant_conflict:
            [Experimental] For accounts with the ProxyAllowParticipantConflict
            account flag, setting to true enables per-request opt-in to
            allowing Proxy to return a 400 error (Twilio error code
            80604) when a request to set a Session to in-progress would
            cause Participants with the same Identifier/ProxyIdentifier
            pair to be active in multiple Sessions. If not provided,
            requests will be allowed to succeed, and a Debugger
            notification (80801) will be emitted. Having multiple,
            active Participants with the same Identifier/ProxyIdentifier
            pair causes calls and messages from affected Participants to
            be routed incorrectly. Please note, the default behavior for
            accounts without the ProxyAllowParticipantConflict flag is
            to reject the request as described.  This will eventually be
            the default for all accounts.
        status:
            The new status of the resource. Can be: `in-progress` to re-open a
            session or `closed` to close a session.
        ttl:
            The time, in seconds, when the session will expire. The time is measured
            from the last Session create or the Session's last
            Interaction.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/Sessions/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "date_expiry": date_expiry,
        "fail_on_participant_conflict": fail_on_participant_conflict,
        "status": status,
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
async def get_v1_services_service_sid_short_codes(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Short Codes in the Proxy Number Pool for the Service. A
    maximum of 100 records will be returned per page.

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
    [https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes?&page_size=%s](
    https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes"  # noqa
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
async def post_v1_services_service_sid_short_codes(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    sid: str = None,
) -> Dict[str, Any]:
    """
    Add a Short Code to the Proxy Number Pool for the Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        sid:
            The SID of a Twilio
            [ShortCode](https://www.twilio.com/docs/sms/api/short-code)
            resource that represents the short code you would like to
            assign to your Proxy Service.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes?](
    https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "sid": sid,
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
async def delete_v1_services_service_sid_short_codes_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Short Code from a Service.

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
    [https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}"  # noqa
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
async def get_v1_services_service_sid_short_codes_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Short Code.

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
    [https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}"  # noqa
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
async def post_v1_services_service_sid_short_codes_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    is_reserved: bool = None,
) -> Dict[str, Any]:
    """
    Update a specific Short Code.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        is_reserved:
            Whether the short code should be reserved and not be assigned to a
            participant using proxy pool logic. See [Reserved Phone
            Numbers](https://www.twilio.com/docs/proxy/reserved-phone-
            numbers) for more information.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?](
    https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{service_sid}/ShortCodes/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "is_reserved": is_reserved,
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
    Delete a specific Service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{sid}?](
    https://proxy.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{sid}"  # noqa
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
    Fetch a specific Service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{sid}?](
    https://proxy.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{sid}"  # noqa
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
    callback_url: str = None,
    chat_instance_sid: str = None,
    default_ttl: int = None,
    geo_match_level: str = None,
    intercept_callback_url: str = None,
    number_selection_behavior: str = None,
    out_of_session_callback_url: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_url:
            The URL we should call when the interaction status changes.
        chat_instance_sid:
            The SID of the Chat Service Instance managed by Proxy Service. The Chat
            Service enables Proxy to forward SMS and channel messages to
            this chat instance. This is a one-to-one relationship.
        default_ttl:
            The default `ttl` value to set for Sessions created in the Service. The
            TTL (time to live) is measured in seconds after the
            Session's last create or last Interaction. The default value
            of `0` indicates an unlimited Session length. You can
            override a Session's default TTL value by setting its `ttl`
            value.
        geo_match_level:
            Where a proxy number must be located relative to the participant
            identifier. Can be: `country`, `area-code`, or `extended-
            area-code`. The default value is `country` and more specific
            areas than `country` are only available in North America.
        intercept_callback_url:
            The URL we call on each interaction. If we receive a 403 status, we
            block the interaction; otherwise the interaction continues.
        number_selection_behavior:
            The preference for Proxy Number selection in the Service instance. Can
            be: `prefer-sticky` or `avoid-sticky` and the default is
            `prefer-sticky`. `prefer-sticky` means that we will try and
            select the same Proxy Number for a given participant if they
            have previous
            [Sessions](https://www.twilio.com/docs/proxy/api/session),
            but we will not fail if that Proxy Number cannot be used.
            `avoid-sticky` means that we will try to use different Proxy
            Numbers as long as that is possible within a given pool
            rather than try and use a previously assigned number.
        out_of_session_callback_url:
            The URL we should call when an inbound call or SMS action occurs on a
            closed or non-existent Session. If your server (or a Twilio
            [function](https://www.twilio.com/functions)) responds with
            valid [TwiML](https://www.twilio.com/docs/voice/twiml), we
            will process it. This means it is possible, for example, to
            play a message for a call, send an automated text message
            response, or redirect a call to another Phone Number. See
            [Out-of-Session Callback Response
            Guide](https://www.twilio.com/docs/proxy/out-session-
            callback-response-guide) for more information.
        unique_name:
            An application-defined string that uniquely identifies the resource.
            This value must be 191 characters or fewer in length and be
            unique. **This value should not have PII.**.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://proxy.twilio.com/v1/Services/{sid}?](
    https://proxy.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://proxy.twilio.com/v1/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "callback_url": callback_url,
        "chat_instance_sid": chat_instance_sid,
        "default_ttl": default_ttl,
        "geo_match_level": geo_match_level,
        "intercept_callback_url": intercept_callback_url,
        "number_selection_behavior": number_selection_behavior,
        "out_of_session_callback_url": out_of_session_callback_url,
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
async def get_v1_services(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Services.

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
    [https://serverless.twilio.com/v1/Services?&page_size=%s](
    https://serverless.twilio.com/v1/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://serverless.twilio.com/v1/Services"  # noqa

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
    friendly_name: str = None,
    include_credentials: bool = None,
    ui_editable: bool = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Service resource.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the Service resource.
            It can be a maximum of 255 characters.
        include_credentials:
            Whether to inject Account credentials into a function invocation
            context. The default value is `true`.
        ui_editable:
            Whether the Service's properties and subresources can be edited via the
            UI. The default value is `false`.
        unique_name:
            A user-defined string that uniquely identifies the Service resource. It
            can be used as an alternative to the `sid` in the URL path
            to address the Service resource. This value must be 50
            characters or less in length and be unique.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services?](
    https://serverless.twilio.com/v1/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://serverless.twilio.com/v1/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "include_credentials": include_credentials,
        "ui_editable": ui_editable,
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
async def get_v1_services_service_sid_assets(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Assets.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Assets?&page_size=%s](
    https://serverless.twilio.com/v1/Services/{service_sid}/Assets?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Assets"  # noqa
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
async def post_v1_services_service_sid_assets(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Asset resource.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the Asset resource. It
            can be a maximum of 255 characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Assets?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Assets?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Assets"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v1_services_service_sid_assets_asset_sid_versions(
    service_sid: str,
    asset_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Asset Versions.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        asset_sid:
            Asset sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{asset_sid}/Versions?&page_size=%s](
    https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{asset_sid}/Versions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{asset_sid}/Versions"  # noqa
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
async def get_v1_services_service_sid_assets_asset_sid_versions_sid(
    service_sid: str,
    asset_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Asset Version.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        asset_sid:
            Asset sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{asset_sid}/Versions/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{asset_sid}/Versions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{asset_sid}/Versions/{sid}"  # noqa
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
async def delete_v1_services_service_sid_assets_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete an Asset resource.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{sid}"  # noqa
    )
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
async def get_v1_services_service_sid_assets_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Asset resource.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{sid}"  # noqa
    )
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
async def post_v1_services_service_sid_assets_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Asset resource.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the Asset resource. It
            can be a maximum of 255 characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://serverless.twilio.com/v1/Services/{service_sid}/Assets/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v1_services_service_sid_builds(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Builds.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Builds?&page_size=%s](
    https://serverless.twilio.com/v1/Services/{service_sid}/Builds?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Builds"  # noqa
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
async def post_v1_services_service_sid_builds(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    asset_versions: list = None,
    dependencies: str = None,
    function_versions: list = None,
    runtime: str = None,
) -> Dict[str, Any]:
    """
    Create a new Build resource. At least one function version or asset version is
    required.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        asset_versions:
            The list of Asset Version resource SIDs to include in the Build.
        dependencies:
            A list of objects that describe the Dependencies included in the Build.
            Each object contains the `name` and `version` of the
            dependency.
        function_versions:
            The list of the Function Version resource SIDs to include in the Build.
        runtime:
            The Runtime version that will be used to run the Build resource when it
            is deployed.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Builds?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Builds?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Builds"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "asset_versions": asset_versions,
        "dependencies": dependencies,
        "function_versions": function_versions,
        "runtime": runtime,
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
async def delete_v1_services_service_sid_builds_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Build resource.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Builds/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Builds/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://serverless.twilio.com/v1/Services/{service_sid}/Builds/{sid}"  # noqa
    )
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
async def get_v1_services_service_sid_builds_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Build resource.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Builds/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Builds/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://serverless.twilio.com/v1/Services/{service_sid}/Builds/{sid}"  # noqa
    )
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
async def get_v1_services_service_sid_builds_sid_status(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Build resource.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Builds/{sid}/Status?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Builds/{sid}/Status?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Builds/{sid}/Status"  # noqa
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
async def get_v1_services_service_sid_environments(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all environments.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments?&page_size=%s](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments"  # noqa
    )
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
async def post_v1_services_service_sid_environments(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    domain_suffix: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new environment.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        domain_suffix:
            A URL-friendly name that represents the environment and forms part of
            the domain name. It can be a maximum of 16 characters.
        unique_name:
            A user-defined string that uniquely identifies the Environment resource.
            It can be a maximum of 100 characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments"  # noqa
    )
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "domain_suffix": domain_suffix,
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
async def get_v1_services_service_sid_environments_environment_sid_deployments(
    service_sid: str,
    environment_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Deployments.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments?&page_size=%s](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments"  # noqa
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
async def post_v1_services_service_sid_environments_environment_sid_deployments(
    service_sid: str,
    environment_sid: str,
    twilio_credentials: "TwilioCredentials",
    build_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new Deployment.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        build_sid:
            The SID of the Build for the Deployment.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "build_sid": build_sid,
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
async def get_v1_services_service_sid_environments_environment_sid_deployments_sid(
    service_sid: str,
    environment_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Deployment.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments/{sid}"  # noqa
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
async def get_v1_services_service_sid_environments_environment_sid_logs(
    service_sid: str,
    environment_sid: str,
    twilio_credentials: "TwilioCredentials",
    function_sid: str = None,
    start_date: str = None,
    end_date: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all logs.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        function_sid:
            The SID of the function whose invocation produced the Log resources to
            read.
        start_date:
            The date/time (in GMT, ISO 8601) after which the Log resources must have
            been created. Defaults to 1 day prior to current date/time.
        end_date:
            The date/time (in GMT, ISO 8601) before which the Log resources must
            have been created. Defaults to current date/time.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Logs?&function_sid=%s&start_date=%s&end_date=%s&page_size=%s](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Logs?&function_sid=%s&start_date=%s&end_date=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Logs"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "function_sid": function_sid,
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
async def get_v1_services_service_sid_environments_environment_sid_logs_sid(
    service_sid: str,
    environment_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific log.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Logs/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Logs/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Logs/{sid}"  # noqa
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
async def get_v1_services_service_sid_environments_environment_sid_variables(
    service_sid: str,
    environment_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Variables.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables?&page_size=%s](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables"  # noqa
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
async def post_v1_services_service_sid_environments_environment_sid_variables(
    service_sid: str,
    environment_sid: str,
    twilio_credentials: "TwilioCredentials",
    key: str = None,
    value: str = None,
) -> Dict[str, Any]:
    """
    Create a new Variable.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        key:
            A string by which the Variable resource can be referenced. It can be a
            maximum of 128 characters.
        value:
            A string that contains the actual value of the Variable. It can be a
            maximum of 450 bytes in size.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "key": key,
        "value": value,
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
async def delete_v1_services_service_sid_environments_environment_sid_variables_sid(
    service_sid: str,
    environment_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Variable.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}"  # noqa
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
async def get_v1_services_service_sid_environments_environment_sid_variables_sid(
    service_sid: str,
    environment_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Variable.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}"  # noqa
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
async def post_v1_services_service_sid_environments_environment_sid_variables_sid(
    service_sid: str,
    environment_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    key: str = None,
    value: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Variable.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        environment_sid:
            Environment sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        key:
            A string by which the Variable resource can be referenced. It can be a
            maximum of 128 characters.
        value:
            A string that contains the actual value of the Variable. It can be a
            maximum of 450 bytes in size.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "key": key,
        "value": value,
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
async def delete_v1_services_service_sid_environments_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific environment.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{sid}"  # noqa
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
async def get_v1_services_service_sid_environments_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific environment.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Environments/{sid}"  # noqa
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
async def get_v1_services_service_sid_functions(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Functions.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Functions?&page_size=%s](
    https://serverless.twilio.com/v1/Services/{service_sid}/Functions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Functions"  # noqa
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
async def post_v1_services_service_sid_functions(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Function resource.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the Function resource.
            It can be a maximum of 255 characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Functions?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Functions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Functions"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v1_services_service_sid_functions_function_sid_versions(
    service_sid: str,
    function_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Function Version resources.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        function_sid:
            Function sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions?&page_size=%s](
    https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions"  # noqa
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
async def get_v1_services_service_sid_functions_function_sid_versions_sid(
    service_sid: str,
    function_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Function Version resource.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        function_sid:
            Function sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}"  # noqa
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
async def get_v1_services_service_sid_functions_function_sid_versions_sid_content(
    service_sid: str,
    function_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a the content of a specific Function Version resource.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        function_sid:
            Function sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}/Content?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}/Content?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}/Content"  # noqa
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
async def delete_v1_services_service_sid_functions_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Function resource.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{sid}"  # noqa
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
async def get_v1_services_service_sid_functions_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a specific Function resource.

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
    [https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{sid}"  # noqa
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
async def post_v1_services_service_sid_functions_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Function resource.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the Function resource.
            It can be a maximum of 255 characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{sid}?](
    https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{service_sid}/Functions/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
    Delete a Service resource.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{sid}?](
    https://serverless.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{sid}"  # noqa
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
    Retrieve a specific Service resource.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{sid}?](
    https://serverless.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{sid}"  # noqa
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
    friendly_name: str = None,
    include_credentials: bool = None,
    ui_editable: bool = None,
) -> Dict[str, Any]:
    """
    Update a specific Service resource.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the Service resource.
            It can be a maximum of 255 characters.
        include_credentials:
            Whether to inject Account credentials into a function invocation
            context.
        ui_editable:
            Whether the Service resource's properties and subresources can be edited
            via the UI. The default value is `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://serverless.twilio.com/v1/Services/{sid}?](
    https://serverless.twilio.com/v1/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://serverless.twilio.com/v1/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "include_credentials": include_credentials,
        "ui_editable": ui_editable,
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
async def get_v1_services_service_sid_documents_document_sid_permissions(
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
async def delete_v1_services_service_sid_documents_document_sid_permissions_identity(
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
async def get_v1_services_service_sid_documents_document_sid_permissions_identity(
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
async def post_v1_services_service_sid_documents_document_sid_permissions_identity(
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
async def delete_v1_services_service_sid_lists_list_sid_permissions_identity(
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
async def get_v1_services_service_sid_lists_list_sid_permissions_identity(
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
async def post_v1_services_service_sid_lists_list_sid_permissions_identity(
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
async def delete_v1_services_service_sid_maps_map_sid_permissions_identity(
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
async def get_v1_services_service_sid_maps_map_sid_permissions_identity(
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
async def post_v1_services_service_sid_maps_map_sid_permissions_identity(
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
async def post_v1_services_service_sid_streams_stream_sid_messages(
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


@task
async def get_v2_services(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Verification Services for an account.

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
    [https://verify.twilio.com/v2/Services?&page_size=%s](
    https://verify.twilio.com/v2/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Services"  # noqa

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
async def post_v2_services(
    twilio_credentials: "TwilioCredentials",
    code_length: int = None,
    custom_code_enabled: bool = None,
    default_template_sid: str = None,
    do_not_share_warning_enabled: bool = None,
    dtmf_input_required: bool = None,
    friendly_name: str = None,
    lookup_enabled: bool = None,
    psd2_enabled: bool = None,
    push_apn_credential_sid: str = None,
    push_fcm_credential_sid: str = None,
    push_include_date: bool = None,
    skip_sms_to_landlines: bool = None,
    totp_code_length: int = None,
    totp_issuer: str = None,
    totp_skew: int = None,
    totp_time_step: int = None,
    tts_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Verification Service.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        code_length:
            The length of the verification code to generate. Must be an integer
            value between 4 and 10, inclusive.
        custom_code_enabled:
            Whether to allow sending verifications with a custom code instead of a
            randomly generated one. Not available for all customers.
        default_template_sid:
            The default message
            [template](https://www.twilio.com/docs/verify/api/templates).
            Will be used for all SMS verifications unless explicitly
            overriden. SMS channel only.
        do_not_share_warning_enabled:
            Whether to add a security warning at the end of an SMS verification
            body. Disabled by default and applies only to SMS. Example
            SMS body: `Your AppName verification code is: 1234. Don’t
            share this code with anyone; our employees will never ask
            for the code`.
        dtmf_input_required:
            Whether to ask the user to press a number before delivering the verify
            code in a phone call.
        friendly_name:
            A descriptive string that you create to describe the verification
            service. It can be up to 30 characters long. **This value
            should not contain PII.**.
        lookup_enabled:
            Whether to perform a lookup with each verification started and return
            info about the phone number.
        psd2_enabled:
            Whether to pass PSD2 transaction parameters when starting a
            verification.
        push_apn_credential_sid:
            Optional configuration for the Push factors. Set the APN Credential for
            this service. This will allow to send push notifications to
            iOS devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_fcm_credential_sid:
            Optional configuration for the Push factors. Set the FCM Credential for
            this service. This will allow to send push notifications to
            Android devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_include_date:
            Optional configuration for the Push factors. If true, include the date
            in the Challenge's response. Otherwise, the date is omitted
            from the response. See
            [Challenge](https://www.twilio.com/docs/verify/api/challenge)
            resource’s details parameter for more info. Default: false.
            **Deprecated** do not use this parameter. This timestamp
            value is the same one as the one found in `date_created`,
            please use that one instead.
        skip_sms_to_landlines:
            Whether to skip sending SMS verifications to landlines. Requires
            `lookup_enabled`.
        totp_code_length:
            Optional configuration for the TOTP factors. Number of digits for
            generated TOTP codes. Must be between 3 and 8, inclusive.
            Defaults to 6.
        totp_issuer:
            Optional configuration for the TOTP factors. Set TOTP Issuer for this
            service. This will allow to configure the issuer of the TOTP
            URI. Defaults to the service friendly name if not provided.
        totp_skew:
            Optional configuration for the TOTP factors. The number of time-steps,
            past and future, that are valid for validation of TOTP
            codes. Must be between 0 and 2, inclusive. Defaults to 1.
        totp_time_step:
            Optional configuration for the TOTP factors. Defines how often, in
            seconds, are TOTP codes generated. i.e, a new TOTP code is
            generated every time_step seconds. Must be between 20 and 60
            seconds, inclusive. Defaults to 30 seconds.
        tts_name:
            The name of an alternative text-to-speech service to use in phone calls.
            Applies only to TTS languages.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services?](
    https://verify.twilio.com/v2/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "code_length": code_length,
        "custom_code_enabled": custom_code_enabled,
        "default_template_sid": default_template_sid,
        "do_not_share_warning_enabled": do_not_share_warning_enabled,
        "dtmf_input_required": dtmf_input_required,
        "friendly_name": friendly_name,
        "lookup_enabled": lookup_enabled,
        "psd2_enabled": psd2_enabled,
        "push_apn_credential_sid": push_apn_credential_sid,
        "push_fcm_credential_sid": push_fcm_credential_sid,
        "push_include_date": push_include_date,
        "skip_sms_to_landlines": skip_sms_to_landlines,
        "totp_code_length": totp_code_length,
        "totp_issuer": totp_issuer,
        "totp_skew": totp_skew,
        "totp_time_step": totp_time_step,
        "tts_name": tts_name,
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
async def post_v2_services_service_sid_access_tokens(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    factor_friendly_name: str = None,
    factor_type: str = None,
    identity: str = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """
    Create a new enrollment Access Token for the Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        factor_friendly_name:
            The friendly name of the factor that is going to be created with this
            access token.
        factor_type:
            The Type of this Factor. Eg. `push`.
        identity:
            The unique external identifier for the Entity of the Service. This
            identifier should be immutable, not PII, and generated by
            your external system, such as your user's UUID, GUID, or
            SID.
        ttl:
            How long, in seconds, the access token is valid. Can be an integer
            between 60 and 300. Default is 60.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens?](
    https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "factor_friendly_name": factor_friendly_name,
        "factor_type": factor_type,
        "identity": identity,
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
async def get_v2_services_service_sid_access_tokens_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an Access Token for the Entity.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens/{sid}"  # noqa
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
async def get_v2_services_service_sid_entities(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Entities for a Service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities"  # noqa
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
async def post_v2_services_service_sid_entities(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
) -> Dict[str, Any]:
    """
    Create a new Entity for the Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The unique external identifier for the Entity of the Service. This
            identifier should be immutable, not PII, length between 8
            and 64 characters, and generated by your external system,
            such as your user's UUID, GUID, or SID. It can only contain
            dash (-) separated alphanumeric characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
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
async def delete_v2_services_service_sid_entities_identity(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}"  # noqa
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
async def get_v2_services_service_sid_entities_identity(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}"  # noqa
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
async def get_v2_services_service_sid_entities_identity_challenges(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    factor_sid: str = None,
    status: str = None,
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Challenges for a Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        factor_sid:
            The unique SID identifier of the Factor.
        status:
            The Status of the Challenges to fetch. One of `pending`, `expired`,
            `approved` or `denied`.
        order:
            The desired sort order of the Challenges list. One of `asc` or `desc`
            for ascending and descending respectively. Defaults to
            `asc`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?&factor_sid=%s&status=%s&order=%s&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?&factor_sid=%s&status=%s&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "factor_sid": factor_sid,
        "status": status,
        "order": order,
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
async def post_v2_services_service_sid_entities_identity_challenges(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    auth_payload: str = None,
    details_fields: list = None,
    details_message: str = None,
    expiration_date: str = None,
    factor_sid: str = None,
    hidden_details: str = None,
) -> Dict[str, Any]:
    """
    Create a new Challenge for the Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auth_payload:
            Optional payload used to verify the Challenge upon creation. Only used
            with a Factor of type `totp` to carry the TOTP code that
            needs to be verified. For `TOTP` this value must be between
            3 and 8 characters long.
        details_fields:
            A list of objects that describe the Fields included in the Challenge.
            Each object contains the label and value of the field, the
            label can be up to 36 characters in length and the value can
            be up to 128 characters in length. Used when `factor_type`
            is `push`. There can be up to 20 details fields.
        details_message:
            Shown to the user when the push notification arrives. Required when
            `factor_type` is `push`. Can be up to 256 characters in
            length.
        expiration_date:
            The date-time when this Challenge expires, given in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format. The
            default value is five (5) minutes after Challenge creation.
            The max value is sixty (60) minutes after creation.
        factor_sid:
            The unique SID identifier of the Factor.
        hidden_details:
            Details provided to give context about the Challenge. Not shown to the
            end user. It must be a stringified JSON with only strings
            values eg. `{"ip": "172.168.1.234"}`. Can be up to 1024
            characters in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "auth_payload": auth_payload,
        "details_fields": details_fields,
        "details_message": details_message,
        "expiration_date": expiration_date,
        "factor_sid": factor_sid,
        "hidden_details": hidden_details,
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
async def post_v2_services_service_sid_entities_identity_challenges_challenge_sid_notifications(
    service_sid: str,
    identity: str,
    challenge_sid: str,
    twilio_credentials: "TwilioCredentials",
    ttl: int = None,
) -> Dict[str, Any]:
    """
    Create a new Notification for the corresponding Challenge.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        challenge_sid:
            Challenge sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ttl:
            How long, in seconds, the notification is valid. Can be an integer
            between 0 and 300. Default is 300. Delivery is attempted
            until the TTL elapses, even if the device is offline. 0
            means that the notification delivery is attempted
            immediately, only once, and is not stored for future
            delivery.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications"  # noqa
    responses = {
        201: "Created.",  # noqa
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
async def get_v2_services_service_sid_entities_identity_challenges_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Challenge.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}"  # noqa
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
async def post_v2_services_service_sid_entities_identity_challenges_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    auth_payload: str = None,
    metadata: str = None,
) -> Dict[str, Any]:
    """
    Verify a specific Challenge.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auth_payload:
            The optional payload needed to verify the Challenge. E.g., a TOTP would
            use the numeric code. For `TOTP` this value must be between
            3 and 8 characters long. For `Push` this value can be up to
            5456 characters in length.
        metadata:
            Custom metadata associated with the challenge. This is added by the
            Device/SDK directly to allow for the inclusion of device
            information. It must be a stringified JSON with only strings
            values eg. `{"os": "Android"}`. Can be up to 1024 characters
            in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "auth_payload": auth_payload,
        "metadata": metadata,
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
async def get_v2_services_service_sid_entities_identity_factors(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Factors for an Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors"  # noqa
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
async def post_v2_services_service_sid_entities_identity_factors(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    binding_alg: str = None,
    binding_public_key: str = None,
    binding_secret: str = None,
    config_alg: str = None,
    config_app_id: str = None,
    config_code_length: int = None,
    config_notification_platform: str = None,
    config_notification_token: str = None,
    config_sdk_version: str = None,
    config_skew: int = None,
    config_time_step: int = None,
    factor_type: str = None,
    friendly_name: str = None,
    metadata: str = None,
) -> Dict[str, Any]:
    """
    Create a new Factor for the Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_alg:
            The algorithm used when `factor_type` is `push`. Algorithm supported:
            `ES256`.
        binding_public_key:
            The Ecdsa public key in PKIX, ASN.1 DER format encoded in Base64.
            Required when `factor_type` is `push`.
        binding_secret:
            The shared secret for TOTP factors encoded in Base32. This can be
            provided when creating the Factor, otherwise it will be
            generated.  Used when `factor_type` is `totp`.
        config_alg:
            The algorithm used to derive the TOTP codes. Can be `sha1`, `sha256` or
            `sha512`. Defaults to `sha1`.  Used when `factor_type` is
            `totp`.
        config_app_id:
            The ID that uniquely identifies your app in the Google or Apple store,
            such as `com.example.myapp`. It can be up to 100 characters
            long.  Required when `factor_type` is `push`.
        config_code_length:
            Number of digits for generated TOTP codes. Must be between 3 and 8,
            inclusive. The default value is defined at the service level
            in the property `totp.code_length`. If not configured
            defaults to 6.  Used when `factor_type` is `totp`.
        config_notification_platform:
            The transport technology used to generate the Notification Token. Can be
            `apn`, `fcm` or `none`.  Required when `factor_type` is
            `push`.
        config_notification_token:
            For APN, the device token. For FCM, the registration token. It is used
            to send the push notifications. Must be between 32 and 255
            characters long.  Required when `factor_type` is `push`.
        config_sdk_version:
            The Verify Push SDK version used to configure the factor  Required when
            `factor_type` is `push`.
        config_skew:
            The number of time-steps, past and future, that are valid for validation
            of TOTP codes. Must be between 0 and 2, inclusive. The
            default value is defined at the service level in the
            property `totp.skew`. If not configured defaults to 1.  Used
            when `factor_type` is `totp`.
        config_time_step:
            Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP
            code is generated every time_step seconds. Must be between
            20 and 60 seconds, inclusive. The default value is defined
            at the service level in the property `totp.time_step`.
            Defaults to 30 seconds if not configured.  Used when
            `factor_type` is `totp`.
        factor_type:
            The Type of this Factor. Currently `push` and `totp` are supported.
        friendly_name:
            The friendly name of this Factor. This can be any string up to 64
            characters, meant for humans to distinguish between Factors.
            For `factor_type` `push`, this could be a device name. For
            `factor_type` `totp`, this value is used as the “account
            name” in constructing the `binding.uri` property. At the
            same time, we recommend avoiding providing PII.
        metadata:
            Custom metadata associated with the factor. This is added by the
            Device/SDK directly to allow for the inclusion of device
            information. It must be a stringified JSON with only strings
            values eg. `{"os": "Android"}`. Can be up to 1024 characters
            in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "binding_alg": binding_alg,
        "binding_public_key": binding_public_key,
        "binding_secret": binding_secret,
        "config_alg": config_alg,
        "config_app_id": config_app_id,
        "config_code_length": config_code_length,
        "config_notification_platform": config_notification_platform,
        "config_notification_token": config_notification_token,
        "config_sdk_version": config_sdk_version,
        "config_skew": config_skew,
        "config_time_step": config_time_step,
        "factor_type": factor_type,
        "friendly_name": friendly_name,
        "metadata": metadata,
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
async def delete_v2_services_service_sid_entities_identity_factors_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}"  # noqa
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
async def get_v2_services_service_sid_entities_identity_factors_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}"  # noqa
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
async def post_v2_services_service_sid_entities_identity_factors_sid(
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    auth_payload: str = None,
    config_alg: str = None,
    config_code_length: int = None,
    config_notification_platform: str = None,
    config_notification_token: str = None,
    config_sdk_version: str = None,
    config_skew: int = None,
    config_time_step: int = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Factor. This endpoint can be used to Verify a Factor if passed
    an `AuthPayload` param.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auth_payload:
            The optional payload needed to verify the Factor for the first time.
            E.g. for a TOTP, the numeric code.
        config_alg:
            The algorithm used to derive the TOTP codes. Can be `sha1`, `sha256` or
            `sha512`.
        config_code_length:
            Number of digits for generated TOTP codes. Must be between 3 and 8,
            inclusive.
        config_notification_platform:
            The transport technology used to generate the Notification Token. Can be
            `apn`, `fcm` or `none`.  Required when `factor_type` is
            `push`.
        config_notification_token:
            For APN, the device token. For FCM, the registration token. It is used
            to send the push notifications. Required when `factor_type`
            is `push`. If specified, this value must be between 32 and
            255 characters long.
        config_sdk_version:
            The Verify Push SDK version used to configure the factor.
        config_skew:
            The number of time-steps, past and future, that are valid for validation
            of TOTP codes. Must be between 0 and 2, inclusive.
        config_time_step:
            Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP
            code is generated every time_step seconds. Must be between
            20 and 60 seconds, inclusive.
        friendly_name:
            The new friendly name of this Factor. It can be up to 64 characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "auth_payload": auth_payload,
        "config_alg": config_alg,
        "config_code_length": config_code_length,
        "config_notification_platform": config_notification_platform,
        "config_notification_token": config_notification_token,
        "config_sdk_version": config_sdk_version,
        "config_skew": config_skew,
        "config_time_step": config_time_step,
        "friendly_name": friendly_name,
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
async def get_v2_services_service_sid_messaging_configurations(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Messaging Configurations for a Service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations"  # noqa
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
async def post_v2_services_service_sid_messaging_configurations(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    country: str = None,
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new MessagingConfiguration for a service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        country:
            The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            country code of the country this configuration will be
            applied to. If this is a global configuration, Country will
            take the value `all`.
        messaging_service_sid:
            The SID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) to be
            used to send SMS to the country of this configuration.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "country": country,
        "messaging_service_sid": messaging_service_sid,
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
async def delete_v2_services_service_sid_messaging_configurations_country(
    service_sid: str,
    country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific MessagingConfiguration.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        country:
            Country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}"  # noqa
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
async def get_v2_services_service_sid_messaging_configurations_country(
    service_sid: str,
    country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific MessagingConfiguration.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        country:
            Country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}"  # noqa
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
async def post_v2_services_service_sid_messaging_configurations_country(
    service_sid: str,
    country: str,
    twilio_credentials: "TwilioCredentials",
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """
    Update a specific MessagingConfiguration.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        country:
            Country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        messaging_service_sid:
            The SID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) to be
            used to send SMS to the country of this configuration.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "messaging_service_sid": messaging_service_sid,
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
async def get_v2_services_service_sid_rate_limits(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Rate Limits for a service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits"  # noqa
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
async def post_v2_services_service_sid_rate_limits(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    description: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Rate Limit for a Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            Description of this Rate Limit.
        unique_name:
            Provides a unique and addressable name to be assigned to this Rate
            Limit, assigned by the developer, to be optionally used in
            addition to SID. **This value should not contain PII.**.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "description": description,
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
async def get_v2_services_service_sid_rate_limits_rate_limit_sid_buckets(
    service_sid: str,
    rate_limit_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Buckets for a Rate Limit.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets"  # noqa
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
async def post_v2_services_service_sid_rate_limits_rate_limit_sid_buckets(
    service_sid: str,
    rate_limit_sid: str,
    twilio_credentials: "TwilioCredentials",
    interval: int = None,
    max: int = None,
) -> Dict[str, Any]:
    """
    Create a new Bucket for a Rate Limit.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        interval:
            Number of seconds that the rate limit will be enforced over.
        max:
            Maximum number of requests permitted in during the interval.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "interval": interval,
        "max": max,
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
async def delete_v2_services_service_sid_rate_limits_rate_limit_sid_buckets_sid(
    service_sid: str,
    rate_limit_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Bucket.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}"  # noqa
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
async def get_v2_services_service_sid_rate_limits_rate_limit_sid_buckets_sid(
    service_sid: str,
    rate_limit_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Bucket.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}"  # noqa
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
async def post_v2_services_service_sid_rate_limits_rate_limit_sid_buckets_sid(
    service_sid: str,
    rate_limit_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    interval: int = None,
    max: int = None,
) -> Dict[str, Any]:
    """
    Update a specific Bucket.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        interval:
            Number of seconds that the rate limit will be enforced over.
        max:
            Maximum number of requests permitted in during the interval.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "interval": interval,
        "max": max,
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
async def delete_v2_services_service_sid_rate_limits_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Rate Limit.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}"  # noqa
    )
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
async def get_v2_services_service_sid_rate_limits_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Rate Limit.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}"  # noqa
    )
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
async def post_v2_services_service_sid_rate_limits_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    description: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Rate Limit.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            Description of this Rate Limit.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}"  # noqa
    )
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
async def post_v2_services_service_sid_verification_check(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    amount: str = None,
    code: str = None,
    payee: str = None,
    to: str = None,
    verification_sid: str = None,
) -> Dict[str, Any]:
    """
    challenge a specific Verification Check.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        amount:
            The amount of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        code:
            The 4-10 character string being verified.
        payee:
            The payee of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        to:
            The phone number or [email](https://www.twilio.com/docs/verify/email) to
            verify. Either this parameter or the `verification_sid` must
            be specified. Phone numbers must be in [E.164
            format](https://www.twilio.com/docs/glossary/what-e164).
        verification_sid:
            A SID that uniquely identifies the Verification Check. Either this
            parameter or the `to` phone
            number/[email](https://www.twilio.com/docs/verify/email)
            must be specified.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/VerificationCheck?](
    https://verify.twilio.com/v2/Services/{service_sid}/VerificationCheck?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/VerificationCheck"  # noqa
    )
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "amount": amount,
        "code": code,
        "payee": payee,
        "to": to,
        "verification_sid": verification_sid,
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
async def post_v2_services_service_sid_verifications(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    amount: str = None,
    app_hash: str = None,
    channel: str = None,
    channel_configuration: str = None,
    custom_code: str = None,
    custom_friendly_name: str = None,
    custom_message: str = None,
    locale: str = None,
    payee: str = None,
    rate_limits: str = None,
    send_digits: str = None,
    template_custom_substitutions: str = None,
    template_sid: str = None,
    to: str = None,
) -> Dict[str, Any]:
    """
    Create a new Verification using a Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        amount:
            The amount of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        app_hash:
            Your [App Hash](https://developers.google.com/identity/sms-
            retriever/verify
            computing_your_apps_hash_string) to be appended at the end
            of your verification SMS body. Applies only to SMS. Example
            SMS body: `<
            > Your AppName verification code is: 1234 He42w354ol9`.
        channel:
            The verification method to use. Can be:
            [`email`](https://www.twilio.com/docs/verify/email), `sms`,
            `whatsapp` or `call`.
        channel_configuration:
            [`email`](https://www.twilio.com/docs/verify/email) channel
            configuration in json format. The fields 'from' and
            'from_name' are optional but if included the 'from' field
            must have a valid email address.
        custom_code:
            A pre-generated code to use for verification. The code can be between 4
            and 10 characters, inclusive.
        custom_friendly_name:
            A custom user defined friendly name that overwrites the existing one in
            the verification message.
        custom_message:
            The text of a custom message to use for the verification.
        locale:
            The locale to use for the verification SMS, WhatsApp or call. Can be:
            `af`, `ar`, `ca`, `cs`, `da`, `de`, `el`, `en`, `en-GB`,
            `es`, `fi`, `fr`, `he`, `hi`, `hr`, `hu`, `id`, `it`, `ja`,
            `ko`, `ms`, `nb`, `nl`, `pl`, `pt`, `pr-BR`, `ro`, `ru`,
            `sv`, `th`, `tl`, `tr`, `vi`, `zh`, `zh-CN`, or `zh-HK.`.
        payee:
            The payee of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        rate_limits:
            The custom key-value pairs of Programmable Rate Limits. Keys correspond
            to `unique_name` fields defined when [creating your Rate
            Limit](https://www.twilio.com/docs/verify/api/service-rate-
            limits). Associated value pairs represent values in the
            request that you are rate limiting on. You may include
            multiple Rate Limit values in each request.
        send_digits:
            The digits to send after a phone call is answered, for example, to dial
            an extension. For more information, see the Programmable
            Voice documentation of
            [sendDigits](https://www.twilio.com/docs/voice/twiml/number
            attributes-sendDigits).
        template_custom_substitutions:
            A stringified JSON object in which the keys are the template's special
            variables and the values are the variables substitutions.
        template_sid:
            The message
            [template](https://www.twilio.com/docs/verify/api/templates).
            If provided, will override the default template for the
            Service. SMS channel only.
        to:
            The phone number or [email](https://www.twilio.com/docs/verify/email) to
            verify. Phone numbers must be in [E.164
            format](https://www.twilio.com/docs/glossary/what-e164).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Verifications?](
    https://verify.twilio.com/v2/Services/{service_sid}/Verifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "amount": amount,
        "app_hash": app_hash,
        "channel": channel,
        "channel_configuration": channel_configuration,
        "custom_code": custom_code,
        "custom_friendly_name": custom_friendly_name,
        "custom_message": custom_message,
        "locale": locale,
        "payee": payee,
        "rate_limits": rate_limits,
        "send_digits": send_digits,
        "template_custom_substitutions": template_custom_substitutions,
        "template_sid": template_sid,
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
async def get_v2_services_service_sid_verifications_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Verification.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}"  # noqa
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
async def post_v2_services_service_sid_verifications_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Update a Verification status.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The new status of the resource. Can be: `canceled` or `approved`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}"  # noqa
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
async def get_v2_services_service_sid_webhooks(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Webhooks for a Service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks"  # noqa
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
async def post_v2_services_service_sid_webhooks(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    event_types: list = None,
    friendly_name: str = None,
    status: str = None,
    version: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """
    Create a new Webhook for the Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        event_types:
            The array of events that this Webhook is subscribed to. Possible event
            types: `*, factor.deleted, factor.created, factor.verified,
            challenge.approved, challenge.denied`.
        friendly_name:
            The string that you assigned to describe the webhook. **This value
            should not contain PII.**.
        status:
            The webhook status. Default value is `enabled`. One of: `enabled` or
            `disabled`.
        version:
            The webhook version. Default value is `v2` which includes all the latest
            fields. Version `v1` is legacy and may be removed in the
            future.
        webhook_url:
            The URL associated with this Webhook.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "event_types": event_types,
        "friendly_name": friendly_name,
        "status": status,
        "version": version,
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
async def delete_v2_services_service_sid_webhooks_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Webhook.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}"  # noqa
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
async def get_v2_services_service_sid_webhooks_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Webhook.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}"  # noqa
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
async def post_v2_services_service_sid_webhooks_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    event_types: list = None,
    friendly_name: str = None,
    status: str = None,
    version: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        event_types:
            The array of events that this Webhook is subscribed to. Possible event
            types: `*, factor.deleted, factor.created, factor.verified,
            challenge.approved, challenge.denied`.
        friendly_name:
            The string that you assigned to describe the webhook. **This value
            should not contain PII.**.
        status:
            The webhook status. Default value is `enabled`. One of: `enabled` or
            `disabled`.
        version:
            The webhook version. Default value is `v2` which includes all the latest
            fields. Version `v1` is legacy and may be removed in the
            future.
        webhook_url:
            The URL associated with this Webhook.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "event_types": event_types,
        "friendly_name": friendly_name,
        "status": status,
        "version": version,
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
async def delete_v2_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Verification Service Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{sid}?](
    https://verify.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{sid}"  # noqa
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
async def get_v2_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Verification Service Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{sid}?](
    https://verify.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{sid}"  # noqa
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
async def post_v2_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    code_length: int = None,
    custom_code_enabled: bool = None,
    default_template_sid: str = None,
    do_not_share_warning_enabled: bool = None,
    dtmf_input_required: bool = None,
    friendly_name: str = None,
    lookup_enabled: bool = None,
    psd2_enabled: bool = None,
    push_apn_credential_sid: str = None,
    push_fcm_credential_sid: str = None,
    push_include_date: bool = None,
    skip_sms_to_landlines: bool = None,
    totp_code_length: int = None,
    totp_issuer: str = None,
    totp_skew: int = None,
    totp_time_step: int = None,
    tts_name: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Verification Service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        code_length:
            The length of the verification code to generate. Must be an integer
            value between 4 and 10, inclusive.
        custom_code_enabled:
            Whether to allow sending verifications with a custom code instead of a
            randomly generated one. Not available for all customers.
        default_template_sid:
            The default message
            [template](https://www.twilio.com/docs/verify/api/templates).
            Will be used for all SMS verifications unless explicitly
            overriden. SMS channel only.
        do_not_share_warning_enabled:
            Whether to add a privacy warning at the end of an SMS. **Disabled by
            default and applies only for SMS.**.
        dtmf_input_required:
            Whether to ask the user to press a number before delivering the verify
            code in a phone call.
        friendly_name:
            A descriptive string that you create to describe the verification
            service. It can be up to 30 characters long. **This value
            should not contain PII.**.
        lookup_enabled:
            Whether to perform a lookup with each verification started and return
            info about the phone number.
        psd2_enabled:
            Whether to pass PSD2 transaction parameters when starting a
            verification.
        push_apn_credential_sid:
            Optional configuration for the Push factors. Set the APN Credential for
            this service. This will allow to send push notifications to
            iOS devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_fcm_credential_sid:
            Optional configuration for the Push factors. Set the FCM Credential for
            this service. This will allow to send push notifications to
            Android devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_include_date:
            Optional configuration for the Push factors. If true, include the date
            in the Challenge's response. Otherwise, the date is omitted
            from the response. See
            [Challenge](https://www.twilio.com/docs/verify/api/challenge)
            resource’s details parameter for more info. Default: false.
            **Deprecated** do not use this parameter.
        skip_sms_to_landlines:
            Whether to skip sending SMS verifications to landlines. Requires
            `lookup_enabled`.
        totp_code_length:
            Optional configuration for the TOTP factors. Number of digits for
            generated TOTP codes. Must be between 3 and 8, inclusive.
            Defaults to 6.
        totp_issuer:
            Optional configuration for the TOTP factors. Set TOTP Issuer for this
            service. This will allow to configure the issuer of the TOTP
            URI.
        totp_skew:
            Optional configuration for the TOTP factors. The number of time-steps,
            past and future, that are valid for validation of TOTP
            codes. Must be between 0 and 2, inclusive. Defaults to 1.
        totp_time_step:
            Optional configuration for the TOTP factors. Defines how often, in
            seconds, are TOTP codes generated. i.e, a new TOTP code is
            generated every time_step seconds. Must be between 20 and 60
            seconds, inclusive. Defaults to 30 seconds.
        tts_name:
            The name of an alternative text-to-speech service to use in phone calls.
            Applies only to TTS languages.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{sid}?](
    https://verify.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "code_length": code_length,
        "custom_code_enabled": custom_code_enabled,
        "default_template_sid": default_template_sid,
        "do_not_share_warning_enabled": do_not_share_warning_enabled,
        "dtmf_input_required": dtmf_input_required,
        "friendly_name": friendly_name,
        "lookup_enabled": lookup_enabled,
        "psd2_enabled": psd2_enabled,
        "push_apn_credential_sid": push_apn_credential_sid,
        "push_fcm_credential_sid": push_fcm_credential_sid,
        "push_include_date": push_include_date,
        "skip_sms_to_landlines": skip_sms_to_landlines,
        "totp_code_length": totp_code_length,
        "totp_issuer": totp_issuer,
        "totp_skew": totp_skew,
        "totp_time_step": totp_time_step,
        "tts_name": tts_name,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
