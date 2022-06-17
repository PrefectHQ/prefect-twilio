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
async def get_v1_sims(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    fleet: str = None,
    iccid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Super SIMs from your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The status of the Sim resources to read. Can be `new`, `ready`,
            `active`, `inactive`, or `scheduled`.
        fleet:
            The SID or unique name of the Fleet to which a list of Sims are
            assigned.
        iccid:
            The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module
            ICCID) associated with a Super SIM to filter the list by.
            Passing this parameter will always return a list containing
            zero or one SIMs.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims?&status=%s&fleet=%s&iccid=%s&page_size=%s](
    https://supersim.twilio.com/v1/Sims?&status=%s&fleet=%s&iccid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/Sims"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "fleet": fleet,
        "iccid": iccid,
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
async def post_v1_sims(
    twilio_credentials: "TwilioCredentials",
    iccid: str = None,
    registration_code: str = None,
) -> Dict[str, Any]:
    """
    Register a Super SIM to your Account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        iccid:
            The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module
            ICCID) of the Super SIM to be added to your Account.
        registration_code:
            The 10-digit code required to claim the Super SIM for your Account.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims?](
    https://supersim.twilio.com/v1/Sims?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/Sims"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "iccid": iccid,
        "registration_code": registration_code,
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
async def get_v1_sims_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Super SIM instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims/{sid}?](
    https://supersim.twilio.com/v1/Sims/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Sims/{sid}"  # noqa
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
async def post_v1_sims_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    account_sid: str = None,
    callback_method: str = None,
    callback_url: str = None,
    fleet: str = None,
    status: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Updates the given properties of a Super SIM instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        account_sid:
            The SID of the Account to which the Sim resource should belong. The
            Account SID can only be that of the requesting Account or
            that of a Subaccount of the requesting Account. Only valid
            when the Sim resource's status is new.
        callback_method:
            The HTTP method we should use to call `callback_url`. Can be: `GET` or
            `POST` and the default is POST.
        callback_url:
            The URL we should call using the `callback_method` after an asynchronous
            update has finished.
        fleet:
            The SID or unique name of the Fleet to which the SIM resource should be
            assigned.
        status:
            The new status of the resource. Can be: `ready`, `active`, or
            `inactive`. See the [Super SIM Status
            Values](https://www.twilio.com/docs/iot/supersim/api/sim-
            resource
            status-values) for more info.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used in place of the resource's `sid` in the URL to
            address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims/{sid}?](
    https://supersim.twilio.com/v1/Sims/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 202 | Accepted. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Sims/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
        202: "Accepted.",  # noqa
    }

    data = {
        "account_sid": account_sid,
        "callback_method": callback_method,
        "callback_url": callback_url,
        "fleet": fleet,
        "status": status,
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
async def get_v1_sims_sim_sid_billing_periods(
    sim_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Billing Periods for a Super SIM.

    Args:
        sim_sid:
            Sim sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/Sims/{sim_sid}/BillingPeriods?&page_size=%s](
    https://supersim.twilio.com/v1/Sims/{sim_sid}/BillingPeriods?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/Sims/{sim_sid}/BillingPeriods"  # noqa
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
async def get_v1_sims(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    iccid: str = None,
    rate_plan: str = None,
    e_id: str = None,
    sim_registration_code: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Sim resources on your Account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Only return Sim resources with this status.
        iccid:
            Only return Sim resources with this ICCID. This will return a list with
            a maximum size of 1.
        rate_plan:
            The SID or unique name of a [RatePlan
            resource](https://www.twilio.com/docs/wireless/api/rateplan-
            resource). Only return Sim resources assigned to this
            RatePlan resource.
        e_id:
            Deprecated.
        sim_registration_code:
            Only return Sim resources with this registration code. This will return
            a list with a maximum size of 1.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Sims?&status=%s&iccid=%s&rate_plan=%s&e_id=%s&sim_registration_code=%s&page_size=%s](
    https://wireless.twilio.com/v1/Sims?&status=%s&iccid=%s&rate_plan=%s&e_id=%s&sim_registration_code=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://wireless.twilio.com/v1/Sims"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "iccid": iccid,
        "rate_plan": rate_plan,
        "e_id": e_id,
        "sim_registration_code": sim_registration_code,
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
async def delete_v1_sims_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Sim resource on your Account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Sims/{sid}?](
    https://wireless.twilio.com/v1/Sims/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/Sims/{sid}"  # noqa
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
async def get_v1_sims_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Sim resource on your Account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Sims/{sid}?](
    https://wireless.twilio.com/v1/Sims/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/Sims/{sid}"  # noqa
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
async def post_v1_sims_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    account_sid: str = None,
    callback_method: str = None,
    callback_url: str = None,
    commands_callback_method: str = None,
    commands_callback_url: str = None,
    friendly_name: str = None,
    rate_plan: str = None,
    reset_status: str = None,
    sms_fallback_method: str = None,
    sms_fallback_url: str = None,
    sms_method: str = None,
    sms_url: str = None,
    status: str = None,
    unique_name: str = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """
    Updates the given properties of a Sim resource on your Account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        account_sid:
            The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to
            which the Sim resource should belong. The Account SID can
            only be that of the requesting Account or that of a
            [Subaccount](https://www.twilio.com/docs/iam/api/subaccounts)
            of the requesting Account. Only valid when the Sim
            resource's status is `new`. For more information, see the
            [Move SIMs between Subaccounts
            documentation](https://www.twilio.com/docs/wireless/api/sim-
            resource
            move-sims-between-subaccounts).
        callback_method:
            The HTTP method we should use to call `callback_url`. Can be: `POST` or
            `GET`. The default is `POST`.
        callback_url:
            The URL we should call using the `callback_url` when the SIM has
            finished updating. When the SIM transitions from `new` to
            `ready` or from any status to `deactivated`, we call this
            URL when the status changes to an intermediate status
            (`ready` or `deactivated`) and again when the status changes
            to its final status (`active` or `canceled`).
        commands_callback_method:
            The HTTP method we should use to call `commands_callback_url`. Can be:
            `POST` or `GET`. The default is `POST`.
        commands_callback_url:
            The URL we should call using the `commands_callback_method` when the SIM
            sends a
            [Command](https://www.twilio.com/docs/wireless/api/command-
            resource). Your server should respond with an HTTP status
            code in the 200 range; any response body is ignored.
        friendly_name:
            A descriptive string that you create to describe the Sim resource. It
            does not need to be unique.
        rate_plan:
            The SID or unique name of the [RatePlan
            resource](https://www.twilio.com/docs/wireless/api/rateplan-
            resource) to which the Sim resource should be assigned.
        reset_status:
            Initiate a connectivity reset on the SIM. Set to `resetting` to initiate
            a connectivity reset on the SIM. No other value is valid.
        sms_fallback_method:
            The HTTP method we should use to call `sms_fallback_url`. Can be: `GET`
            or `POST`. Default is `POST`.
        sms_fallback_url:
            The URL we should call using the `sms_fallback_method` when an error
            occurs while retrieving or executing the TwiML requested
            from `sms_url`.
        sms_method:
            The HTTP method we should use to call `sms_url`. Can be: `GET` or
            `POST`. Default is `POST`.
        sms_url:
            The URL we should call using the `sms_method` when the SIM-connected
            device sends an SMS message that is not a
            [Command](https://www.twilio.com/docs/wireless/api/command-
            resource).
        status:
            The new status of the Sim resource. Can be: `ready`, `active`,
            `suspended`, or `deactivated`.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used in place of the `sid` in the URL path to address
            the resource.
        voice_fallback_method:
            Deprecated.
        voice_fallback_url:
            Deprecated.
        voice_method:
            Deprecated.
        voice_url:
            Deprecated.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Sims/{sid}?](
    https://wireless.twilio.com/v1/Sims/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/Sims/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "account_sid": account_sid,
        "callback_method": callback_method,
        "callback_url": callback_url,
        "commands_callback_method": commands_callback_method,
        "commands_callback_url": commands_callback_url,
        "friendly_name": friendly_name,
        "rate_plan": rate_plan,
        "reset_status": reset_status,
        "sms_fallback_method": sms_fallback_method,
        "sms_fallback_url": sms_fallback_url,
        "sms_method": sms_method,
        "sms_url": sms_url,
        "status": status,
        "unique_name": unique_name,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_url": voice_url,
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
async def get_v1_sims_sim_sid_data_sessions(
    sim_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        sim_sid:
            Sim sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Sims/{sim_sid}/DataSessions?&page_size=%s](
    https://wireless.twilio.com/v1/Sims/{sim_sid}/DataSessions?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/Sims/{sim_sid}/DataSessions"  # noqa
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
async def get_v1_sims_sim_sid_usage_records(
    sim_sid: str,
    twilio_credentials: "TwilioCredentials",
    end: str = None,
    start: str = None,
    granularity: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        sim_sid:
            Sim sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end:
            Only include usage that occurred on or before this date, specified in
            [ISO 8601](https://www.iso.org/iso-8601-date-and-time-
            format.html). The default is the current time.
        start:
            Only include usage that has occurred on or after this date, specified in
            [ISO 8601](https://www.iso.org/iso-8601-date-and-time-
            format.html). The default is one month before the `end`
            parameter value.
        granularity:
            How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`.
            The default is `all`. A value of `all` returns one Usage
            Record that describes the usage for the entire period.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://wireless.twilio.com/v1/Sims/{sim_sid}/UsageRecords?&end=%s&start=%s&granularity=%s&page_size=%s](
    https://wireless.twilio.com/v1/Sims/{sim_sid}/UsageRecords?&end=%s&start=%s&granularity=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://wireless.twilio.com/v1/Sims/{sim_sid}/UsageRecords"  # noqa
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
