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
async def get_v1_network_access_profiles(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Network Access Profiles from your account.

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
    [https://supersim.twilio.com/v1/NetworkAccessProfiles?&page_size=%s](
    https://supersim.twilio.com/v1/NetworkAccessProfiles?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/NetworkAccessProfiles"  # noqa

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
async def post_v1_network_access_profiles(
    twilio_credentials: "TwilioCredentials",
    networks: list = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Network Access Profile.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        networks:
            List of Network SIDs that this Network Access Profile will allow
            connections to.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used in place of the resource's `sid` in the URL to
            address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/NetworkAccessProfiles"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "networks": networks,
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
async def get_v1_network_access_profiles_network_access_profile_sid_networks(
    network_access_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Network Access Profile resource's Network resource.

    Args:
        network_access_profile_sid:
            Network access profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks?&page_size=%s](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks"  # noqa
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
async def post_v1_network_access_profiles_network_access_profile_sid_networks(
    network_access_profile_sid: str,
    twilio_credentials: "TwilioCredentials",
    network: str = None,
) -> Dict[str, Any]:
    """
    Add a Network resource to the Network Access Profile resource.

    Args:
        network_access_profile_sid:
            Network access profile sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        network:
            The SID of the Network resource to be added to the Network Access
            Profile resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "network": network,
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
async def delete_v1_network_access_profiles_network_access_profile_sid_networks_sid(
    network_access_profile_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove a Network resource from the Network Access Profile resource's.

    Args:
        network_access_profile_sid:
            Network access profile sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}"  # noqa
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
async def get_v1_network_access_profiles_network_access_profile_sid_networks_sid(
    network_access_profile_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Network Access Profile resource's Network resource.

    Args:
        network_access_profile_sid:
            Network access profile sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}"  # noqa
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
async def get_v1_network_access_profiles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Network Access Profile instance from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}"  # noqa
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
async def post_v1_network_access_profiles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Updates the given properties of a Network Access Profile in your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        unique_name:
            The new unique name of the Network Access Profile.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}?](
    https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/NetworkAccessProfiles/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
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
