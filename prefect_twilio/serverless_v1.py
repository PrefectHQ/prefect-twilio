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
async def get_v1_services_service_sid_assets_asset_sid_versions_sid(  # noqa
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
async def get_v1_services_service_sid_environments_environment_sid_deployments(  # noqa
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
async def post_v1_services_service_sid_environments_environment_sid_deployments(  # noqa
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
async def get_v1_services_service_sid_environments_environment_sid_deployments_sid(  # noqa
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
async def get_v1_services_service_sid_environments_environment_sid_logs(  # noqa
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
async def get_v1_services_service_sid_environments_environment_sid_logs_sid(  # noqa
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
async def get_v1_services_service_sid_environments_environment_sid_variables(  # noqa
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
async def post_v1_services_service_sid_environments_environment_sid_variables(  # noqa
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
async def delete_v1_services_service_sid_environments_environment_sid_variables_sid(  # noqa
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
async def get_v1_services_service_sid_environments_environment_sid_variables_sid(  # noqa
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
async def post_v1_services_service_sid_environments_environment_sid_variables_sid(  # noqa
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
async def get_v1_services_service_sid_functions_function_sid_versions(  # noqa
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
async def get_v1_services_service_sid_functions_function_sid_versions_sid(  # noqa
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
async def get_v1_services_service_sid_functions_function_sid_versions_sid_content(  # noqa
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
