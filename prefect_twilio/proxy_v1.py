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
async def get_v1_services_service_sid_sessions_session_sid_interactions(  # noqa
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
async def delete_v1_services_service_sid_sessions_session_sid_interactions_sid(  # noqa
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
async def get_v1_services_service_sid_sessions_session_sid_interactions_sid(  # noqa
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
async def get_v1_services_service_sid_sessions_session_sid_participants(  # noqa
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
async def post_v1_services_service_sid_sessions_session_sid_participants(  # noqa
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
async def get_v1_services_service_sid_sessions_session_sid_participants_participant_sid_message_interactions(  # noqa
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
async def post_v1_services_service_sid_sessions_session_sid_participants_participant_sid_message_interactions(  # noqa
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
async def get_v1_services_service_sid_sessions_session_sid_participants_participant_sid_message_interactions_sid(  # noqa
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
async def delete_v1_services_service_sid_sessions_session_sid_participants_sid(  # noqa
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
async def get_v1_services_service_sid_sessions_session_sid_participants_sid(  # noqa
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
