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
async def get_v2_regulatory_compliance_bundles(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    friendly_name: str = None,
    regulation_sid: str = None,
    iso_country: str = None,
    number_type: str = None,
    has_valid_until_date: bool = None,
    sort_by: str = None,
    sort_direction: str = None,
    valid_until_date: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Bundles for an account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The verification status of the Bundle resource. Please refer to [Bundle
            Statuses](https://www.twilio.com/docs/phone-
            numbers/regulatory/api/bundles
            bundle-statuses) for more details.
        friendly_name:
            The string that you assigned to describe the resource. The column can
            contain 255 variable characters.
        regulation_sid:
            The unique string of a [Regulation
            resource](https://www.twilio.com/docs/phone-
            numbers/regulatory/api/regulations) that is associated to
            the Bundle resource.
        iso_country:
            The 2-digit [ISO country
            code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of
            the Bundle's phone number country ownership request.
        number_type:
            The type of phone number of the Bundle's ownership request. Can be
            `local`, `mobile`, `national`, or `tollfree`.
        has_valid_until_date:
            Indicates that the Bundle is a valid Bundle until a specified expiration
            date.
        sort_by:
            Can be `valid-until` or `date-updated`. Defaults to `date-created`.
        sort_direction:
            Default is `DESC`. Can be `ASC` or `DESC`.
        valid_until_date:
            Date to filter Bundles having their `valid_until_date` before or after
            the specified date. Can be `ValidUntilDate>=` or
            `ValidUntilDate<=`. Both can be used in conjunction as well.
            [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the
            acceptable date format.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?&status=%s&friendly_name=%s&regulation_sid=%s&iso_country=%s&number_type=%s&has_valid_until_date=%s&sort_by=%s&sort_direction=%s&valid_until_date=%s&valid_until_date=%s&valid_until_date=%s&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?&status=%s&friendly_name=%s&regulation_sid=%s&iso_country=%s&number_type=%s&has_valid_until_date=%s&sort_by=%s&sort_direction=%s&valid_until_date=%s&valid_until_date=%s&valid_until_date=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "friendly_name": friendly_name,
        "regulation_sid": regulation_sid,
        "iso_country": iso_country,
        "number_type": number_type,
        "has_valid_until_date": has_valid_until_date,
        "sort_by": sort_by,
        "sort_direction": sort_direction,
        "valid_until_date": valid_until_date,
        "valid_until_date": valid_until_date,
        "valid_until_date": valid_until_date,
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
async def post_v2_regulatory_compliance_bundles(
    twilio_credentials: "TwilioCredentials",
    email: str = None,
    end_user_type: str = None,
    friendly_name: str = None,
    iso_country: str = None,
    number_type: str = None,
    regulation_sid: str = None,
    status_callback: str = None,
) -> Dict[str, Any]:
    """
    Create a new Bundle.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        email:
            The email address that will receive updates when the Bundle resource
            changes status.
        end_user_type:
            The [type of End User](https://www.twilio.com/docs/phone-
            numbers/regulatory/api/end-user-types) of the Bundle
            resource.
        friendly_name:
            The string that you assigned to describe the resource.
        iso_country:
            The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            of the Bundle's phone number country ownership request.
        number_type:
            The type of phone number of the Bundle's ownership request. Can be
            `local`, `mobile`, `national`, or `toll free`.
        regulation_sid:
            The unique string of a regulation that is associated to the Bundle
            resource.
        status_callback:
            The URL we call to inform your application of status changes.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "email": email,
        "end_user_type": end_user_type,
        "friendly_name": friendly_name,
        "iso_country": iso_country,
        "number_type": number_type,
        "regulation_sid": regulation_sid,
        "status_callback": status_callback,
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
async def get_v2_regulatory_compliance_bundles_bundle_sid_copies(
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Bundles Copies for a Bundle.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies"  # noqa
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
async def post_v2_regulatory_compliance_bundles_bundle_sid_copies(
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Creates a new copy of a Bundle. It will internally create copies of all the
    bundle items (identities and documents) of the original bundle.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The string that you assigned to describe the copied bundle.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Copies"  # noqa
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
async def get_v2_regulatory_compliance_bundles_bundle_sid_evaluations(  # noqa
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Evaluations associated to the Bundle resource.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations"  # noqa
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
async def post_v2_regulatory_compliance_bundles_bundle_sid_evaluations(  # noqa
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Creates an evaluation for a bundle.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations"  # noqa
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
async def get_v2_regulatory_compliance_bundles_bundle_sid_evaluations_sid(  # noqa
    bundle_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Evaluation Instance.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_bundles_bundle_sid_item_assignments(  # noqa
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Assigned Items for an account.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments"  # noqa
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
async def post_v2_regulatory_compliance_bundles_bundle_sid_item_assignments(  # noqa
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    object_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new Assigned Item.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        object_sid:
            The SID of an object bag that holds information of the different items.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "object_sid": object_sid,
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
async def delete_v2_regulatory_compliance_bundles_bundle_sid_item_assignments_sid(  # noqa
    bundle_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an Assignment Item Instance.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_bundles_bundle_sid_item_assignments_sid(  # noqa
    bundle_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Assigned Item Instance.

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}"  # noqa
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
async def post_v2_regulatory_compliance_bundles_bundle_sid_replace_items(  # noqa
    bundle_sid: str,
    twilio_credentials: "TwilioCredentials",
    from_bundle_sid: str = None,
) -> Dict[str, Any]:
    """
    Replaces all bundle items in the target bundle (specified in the path) with all
    the bundle items of the source bundle (specified by the from_bundle_sid body
    param).

    Args:
        bundle_sid:
            Bundle sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        from_bundle_sid:
            The source bundle sid to copy the item assignments from.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ReplaceItems?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ReplaceItems?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{bundle_sid}/ReplaceItems"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "from_bundle_sid": from_bundle_sid,
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
async def delete_v2_regulatory_compliance_bundles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Bundle.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_bundles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Bundle instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}"  # noqa
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
async def post_v2_regulatory_compliance_bundles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    email: str = None,
    friendly_name: str = None,
    status: str = None,
    status_callback: str = None,
) -> Dict[str, Any]:
    """
    Updates a Bundle in an account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        email:
            The email address that will receive updates when the Bundle resource
            changes status.
        friendly_name:
            The string that you assigned to describe the resource.
        status:
            The verification status of the Bundle resource.
        status_callback:
            The URL we call to inform your application of status changes.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "email": email,
        "friendly_name": friendly_name,
        "status": status,
        "status_callback": status_callback,
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
async def get_v2_regulatory_compliance_end_user_types(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all End-User Types.

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
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes"  # noqa

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
async def get_v2_regulatory_compliance_end_user_types_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific End-User Type Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://numbers.twilio.com/v2/RegulatoryCompliance/EndUserTypes/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_end_users(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all End User for an account.

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
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers"  # noqa

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
async def post_v2_regulatory_compliance_end_users(
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Create a new End User.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            The set of parameters that are the attributes of the End User resource
            which are derived End User Types.
        friendly_name:
            The string that you assigned to describe the resource.
        type:
            The type of end user of the Bundle resource - can be `individual` or
            `business`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
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
async def delete_v2_regulatory_compliance_end_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific End User.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_end_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific End User Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}"  # noqa
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
async def post_v2_regulatory_compliance_end_users_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update an existing End User.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            The set of parameters that are the attributes of the End User resource
            which are derived End User Types.
        friendly_name:
            The string that you assigned to describe the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
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
async def get_v2_regulatory_compliance_regulations(
    twilio_credentials: "TwilioCredentials",
    end_user_type: str = None,
    iso_country: str = None,
    number_type: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Regulations.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_user_type:
            The type of End User the regulation requires - can be `individual` or
            `business`.
        iso_country:
            The ISO country code of the phone number's country.
        number_type:
            The type of phone number that the regulatory requiremnt is restricting.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations?&end_user_type=%s&iso_country=%s&number_type=%s&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations?&end_user_type=%s&iso_country=%s&number_type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end_user_type": end_user_type,
        "iso_country": iso_country,
        "number_type": number_type,
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
async def get_v2_regulatory_compliance_regulations_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Regulation Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_supporting_document_types(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Supporting Document Types.

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
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes"  # noqa

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
async def get_v2_regulatory_compliance_supporting_document_types_sid(  # noqa
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Supporting Document Type Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocumentTypes/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_supporting_documents(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Supporting Document for an account.

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
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?&page_size=%s](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments"  # noqa
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
async def post_v2_regulatory_compliance_supporting_documents(
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
    type: str = None,
) -> Dict[str, Any]:
    """
    Create a new Supporting Document.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            The set of parameters that are the attributes of the Supporting
            Documents resource which are derived Supporting Document
            Types.
        friendly_name:
            The string that you assigned to describe the resource.
        type:
            The type of the Supporting Document.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments"  # noqa
    )

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "friendly_name": friendly_name,
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
async def delete_v2_regulatory_compliance_supporting_documents_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Supporting Document.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}"  # noqa
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
async def get_v2_regulatory_compliance_supporting_documents_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Supporting Document Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}"  # noqa
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
async def post_v2_regulatory_compliance_supporting_documents_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update an existing Supporting Document.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            The set of parameters that are the attributes of the Supporting Document
            resource which are derived Supporting Document Types.
        friendly_name:
            The string that you assigned to describe the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?](
    https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "attributes": attributes,
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
