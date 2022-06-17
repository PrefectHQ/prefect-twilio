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
async def get_v1_voice_settings(
    twilio_credentials: "TwilioCredentials",
    subaccount_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        subaccount_sid:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/Settings?&subaccount_sid=%s](
    https://insights.twilio.com/v1/Voice/Settings?&subaccount_sid=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://insights.twilio.com/v1/Voice/Settings"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "subaccount_sid": subaccount_sid,
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
async def post_v1_voice_settings(
    twilio_credentials: "TwilioCredentials",
    advanced_features: bool = None,
    subaccount_sid: str = None,
    voice_trace: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        advanced_features:

        subaccount_sid:

        voice_trace:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/Settings?](
    https://insights.twilio.com/v1/Voice/Settings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://insights.twilio.com/v1/Voice/Settings"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "advanced_features": advanced_features,
        "subaccount_sid": subaccount_sid,
        "voice_trace": voice_trace,
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
async def get_v1_voice_summaries(
    twilio_credentials: "TwilioCredentials",
    from_: str = None,
    to: str = None,
    from_carrier: str = None,
    to_carrier: str = None,
    from_country_code: str = None,
    to_country_code: str = None,
    branded: bool = None,
    verified_caller: bool = None,
    has_tag: bool = None,
    start_time: str = None,
    end_time: str = None,
    call_type: str = None,
    call_state: str = None,
    direction: str = None,
    processing_state: str = None,
    sort_by: str = None,
    subaccount: str = None,
    abnormal_session: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        from_:

        to:

        from_carrier:

        to_carrier:

        from_country_code:

        to_country_code:

        branded:

        verified_caller:

        has_tag:

        start_time:

        end_time:

        call_type:

        call_state:

        direction:

        processing_state:

        sort_by:

        subaccount:

        abnormal_session:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/Summaries?&from_=%s&to=%s&from_carrier=%s&to_carrier=%s&from_country_code=%s&to_country_code=%s&branded=%s&verified_caller=%s&has_tag=%s&start_time=%s&end_time=%s&call_type=%s&call_state=%s&direction=%s&processing_state=%s&sort_by=%s&subaccount=%s&abnormal_session=%s&page_size=%s](
    https://insights.twilio.com/v1/Voice/Summaries?&from_=%s&to=%s&from_carrier=%s&to_carrier=%s&from_country_code=%s&to_country_code=%s&branded=%s&verified_caller=%s&has_tag=%s&start_time=%s&end_time=%s&call_type=%s&call_state=%s&direction=%s&processing_state=%s&sort_by=%s&subaccount=%s&abnormal_session=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://insights.twilio.com/v1/Voice/Summaries"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "from_": from_,
        "to": to,
        "from_carrier": from_carrier,
        "to_carrier": to_carrier,
        "from_country_code": from_country_code,
        "to_country_code": to_country_code,
        "branded": branded,
        "verified_caller": verified_caller,
        "has_tag": has_tag,
        "start_time": start_time,
        "end_time": end_time,
        "call_type": call_type,
        "call_state": call_state,
        "direction": direction,
        "processing_state": processing_state,
        "sort_by": sort_by,
        "subaccount": subaccount,
        "abnormal_session": abnormal_session,
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
async def get_v1_voice_call_sid_annotation(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Annotation?](
    https://insights.twilio.com/v1/Voice/{call_sid}/Annotation?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Annotation"  # noqa
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
async def post_v1_voice_call_sid_annotation(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    answered_by: str = None,
    call_score: int = None,
    comment: str = None,
    connectivity_issue: str = None,
    incident: str = None,
    quality_issues: str = None,
    spam: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        answered_by:

        call_score:

        comment:

        connectivity_issue:

        incident:

        quality_issues:

        spam:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Annotation?](
    https://insights.twilio.com/v1/Voice/{call_sid}/Annotation?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Annotation"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "answered_by": answered_by,
        "call_score": call_score,
        "comment": comment,
        "connectivity_issue": connectivity_issue,
        "incident": incident,
        "quality_issues": quality_issues,
        "spam": spam,
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
async def get_v1_voice_call_sid_events(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    edge: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        edge:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Events?&edge=%s&page_size=%s](
    https://insights.twilio.com/v1/Voice/{call_sid}/Events?&edge=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Events"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "edge": edge,
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
async def get_v1_voice_call_sid_metrics(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    edge: str = None,
    direction: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        edge:

        direction:

        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Metrics?&edge=%s&direction=%s&page_size=%s](
    https://insights.twilio.com/v1/Voice/{call_sid}/Metrics?&edge=%s&direction=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Metrics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "edge": edge,
        "direction": direction,
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
async def get_v1_voice_call_sid_summary(
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    processing_state: str = None,
) -> Dict[str, Any]:
    """


    Args:
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        processing_state:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://insights.twilio.com/v1/Voice/{call_sid}/Summary?&processing_state=%s](
    https://insights.twilio.com/v1/Voice/{call_sid}/Summary?&processing_state=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{call_sid}/Summary"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "processing_state": processing_state,
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
async def get_v1_voice_sid(
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
    [https://insights.twilio.com/v1/Voice/{sid}?](
    https://insights.twilio.com/v1/Voice/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://insights.twilio.com/v1/Voice/{sid}"  # noqa
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
async def get_v1_voice_countries(
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
    [https://pricing.twilio.com/v1/Voice/Countries?&page_size=%s](
    https://pricing.twilio.com/v1/Voice/Countries?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://pricing.twilio.com/v1/Voice/Countries"  # noqa

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
async def get_v1_voice_countries_iso_country(
    iso_country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        iso_country:
            Iso country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v1/Voice/Countries/{iso_country}?](
    https://pricing.twilio.com/v1/Voice/Countries/{iso_country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v1/Voice/Countries/{iso_country}"  # noqa
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
async def get_v1_voice_numbers_number(
    number: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        number:
            Number used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v1/Voice/Numbers/{number}?](
    https://pricing.twilio.com/v1/Voice/Numbers/{number}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v1/Voice/Numbers/{number}"  # noqa
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
async def get_v2_voice_countries(
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
    [https://pricing.twilio.com/v2/Voice/Countries?&page_size=%s](
    https://pricing.twilio.com/v2/Voice/Countries?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://pricing.twilio.com/v2/Voice/Countries"  # noqa

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
async def get_v2_voice_countries_iso_country(
    iso_country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Country.

    Args:
        iso_country:
            Iso country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Voice/Countries/{iso_country}?](
    https://pricing.twilio.com/v2/Voice/Countries/{iso_country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Voice/Countries/{iso_country}"  # noqa
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
async def get_v2_voice_numbers_destination_number(
    destination_number: str,
    twilio_credentials: "TwilioCredentials",
    origination_number: str = None,
) -> Dict[str, Any]:
    """
    Fetch pricing information for a specific destination and, optionally,
    origination phone number.

    Args:
        destination_number:
            Destination number used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        origination_number:
            The origination phone number, in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format, for which to fetch the origin-based voice pricing
            information. E.164 format consists of a + followed by the
            country code and subscriber number.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://pricing.twilio.com/v2/Voice/Numbers/{destination_number}?&origination_number=%s](
    https://pricing.twilio.com/v2/Voice/Numbers/{destination_number}?&origination_number=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://pricing.twilio.com/v2/Voice/Numbers/{destination_number}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "origination_number": origination_number,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
