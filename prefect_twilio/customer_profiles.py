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
async def get_v1_customer_profiles(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    friendly_name: str = None,
    policy_sid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Customer-Profiles for an account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The verification status of the Customer-Profile resource.
        friendly_name:
            The string that you assigned to describe the resource.
        policy_sid:
            The unique string of a policy that is associated to the Customer-Profile
            resource.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles?&status=%s&friendly_name=%s&policy_sid=%s&page_size=%s](
    https://trusthub.twilio.com/v1/CustomerProfiles?&status=%s&friendly_name=%s&policy_sid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://trusthub.twilio.com/v1/CustomerProfiles"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "friendly_name": friendly_name,
        "policy_sid": policy_sid,
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
async def post_v1_customer_profiles(
    twilio_credentials: "TwilioCredentials",
    email: str = None,
    friendly_name: str = None,
    policy_sid: str = None,
    status_callback: str = None,
) -> Dict[str, Any]:
    """
    Create a new Customer-Profile.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        email:
            The email address that will receive updates when the Customer-Profile
            resource changes status.
        friendly_name:
            The string that you assigned to describe the resource.
        policy_sid:
            The unique string of a policy that is associated to the Customer-Profile
            resource.
        status_callback:
            The URL we call to inform your application of status changes.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles?](
    https://trusthub.twilio.com/v1/CustomerProfiles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://trusthub.twilio.com/v1/CustomerProfiles"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "email": email,
        "friendly_name": friendly_name,
        "policy_sid": policy_sid,
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
async def get_v1_customer_profiles_customer_profile_sid_channel_endpoint_assignments(
    customer_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    channel_endpoint_sid: str = None,
    channel_endpoint_sids: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Assigned Items for an account.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        channel_endpoint_sid:
            The SID of an channel endpoint.
        channel_endpoint_sids:
            comma separated list of channel endpoint sids.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments?&channel_endpoint_sid=%s&channel_endpoint_sids=%s&page_size=%s](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments?&channel_endpoint_sid=%s&channel_endpoint_sids=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "channel_endpoint_sid": channel_endpoint_sid,
        "channel_endpoint_sids": channel_endpoint_sids,
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
async def post_v1_customer_profiles_customer_profile_sid_channel_endpoint_assignments(
    customer_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    channel_endpoint_sid: str = None,
    channel_endpoint_type: str = None,
) -> Dict[str, Any]:
    """
    Create a new Assigned Item.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        channel_endpoint_sid:
            The SID of an channel endpoint.
        channel_endpoint_type:
            The type of channel endpoint. eg: phone-number.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "channel_endpoint_sid": channel_endpoint_sid,
        "channel_endpoint_type": channel_endpoint_type,
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
async def delete_v1_customer_profiles_customer_profile_sid_channel_endpoint_assignments_sid(
    customer_profile_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an Assignment Item Instance.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments/{sid}?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments/{sid}"  # noqa
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
async def get_v1_customer_profiles_customer_profile_sid_channel_endpoint_assignments_sid(
    customer_profile_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Assigned Item Instance.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments/{sid}?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments/{sid}"  # noqa
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
async def get_v1_customer_profiles_customer_profile_sid_entity_assignments(
    customer_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Assigned Items for an account.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments?&page_size=%s](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments"  # noqa
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
async def post_v1_customer_profiles_customer_profile_sid_entity_assignments(
    customer_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    object_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new Assigned Item.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        object_sid:
            The SID of an object bag that holds information of the different items.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments"  # noqa
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
async def delete_v1_customer_profiles_customer_profile_sid_entity_assignments_sid(
    customer_profile_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an Assignment Item Instance.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments/{sid}?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments/{sid}"  # noqa
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
async def get_v1_customer_profiles_customer_profile_sid_entity_assignments_sid(
    customer_profile_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Assigned Item Instance.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments/{sid}?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments/{sid}"  # noqa
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
async def get_v1_customer_profiles_customer_profile_sid_evaluations(
    customer_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Evaluations associated to the customer_profile resource.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/Evaluations?&page_size=%s](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/Evaluations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/Evaluations"  # noqa
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
async def post_v1_customer_profiles_customer_profile_sid_evaluations(
    customer_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    policy_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new Evaluation.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        policy_sid:
            The unique string of a policy that is associated to the customer_profile
            resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/Evaluations?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/Evaluations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/Evaluations"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "policy_sid": policy_sid,
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
async def get_v1_customer_profiles_customer_profile_sid_evaluations_sid(
    customer_profile_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Evaluation Instance.

    Args:
        customer_profile_sid:
            Customer profile sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/Evaluations/{sid}?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/Evaluations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{customer_profile_sid}/Evaluations/{sid}"  # noqa
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
async def delete_v1_customer_profiles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Customer-Profile.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{sid}?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{sid}"  # noqa
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
async def get_v1_customer_profiles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Customer-Profile instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{sid}?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{sid}"  # noqa
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
async def post_v1_customer_profiles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    email: str = None,
    friendly_name: str = None,
    status: str = None,
    status_callback: str = None,
) -> Dict[str, Any]:
    """
    Updates a Customer-Profile in an account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        email:
            The email address that will receive updates when the Customer-Profile
            resource changes status.
        friendly_name:
            The string that you assigned to describe the resource.
        status:
            The verification status of the Customer-Profile resource.
        status_callback:
            The URL we call to inform your application of status changes.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://trusthub.twilio.com/v1/CustomerProfiles/{sid}?](
    https://trusthub.twilio.com/v1/CustomerProfiles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://trusthub.twilio.com/v1/CustomerProfiles/{sid}"  # noqa
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
