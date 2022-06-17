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
async def get_v1_a2p_brand_registrations(
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
    [https://messaging.twilio.com/v1/a2p/BrandRegistrations?&page_size=%s](
    https://messaging.twilio.com/v1/a2p/BrandRegistrations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://messaging.twilio.com/v1/a2p/BrandRegistrations"  # noqa

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
async def post_v1_a2p_brand_registrations(
    twilio_credentials: "TwilioCredentials",
    a2_p_profile_bundle_sid: str = None,
    brand_type: str = None,
    customer_profile_bundle_sid: str = None,
    mock: bool = None,
    skip_automatic_sec_vet: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        a2_p_profile_bundle_sid:
            A2P Messaging Profile Bundle Sid.
        brand_type:
            Type of brand being created. One of: "STANDARD", "STARTER". STARTER is
            for low volume, starter use cases. STANDARD is for all other
            use cases.
        customer_profile_bundle_sid:
            Customer Profile Bundle Sid.
        mock:
            A boolean that specifies whether brand should be a mock or not. If true,
            brand will be registered as a mock brand. Defaults to false
            if no value is provided.
        skip_automatic_sec_vet:
            A flag to disable automatic secondary vetting for brands which it would
            otherwise be done.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/a2p/BrandRegistrations?](
    https://messaging.twilio.com/v1/a2p/BrandRegistrations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://messaging.twilio.com/v1/a2p/BrandRegistrations"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "a2_p_profile_bundle_sid": a2_p_profile_bundle_sid,
        "brand_type": brand_type,
        "customer_profile_bundle_sid": customer_profile_bundle_sid,
        "mock": mock,
        "skip_automatic_sec_vet": skip_automatic_sec_vet,
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
async def get_v1_a2p_brand_registrations_brand_sid_vettings(
    brand_sid: str,
    twilio_credentials: "TwilioCredentials",
    vetting_provider: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        brand_sid:
            Brand sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        vetting_provider:
            The third-party provider of the vettings to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/a2p/BrandRegistrations/{brand_sid}/Vettings?&vetting_provider=%s&page_size=%s](
    https://messaging.twilio.com/v1/a2p/BrandRegistrations/{brand_sid}/Vettings?&vetting_provider=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/a2p/BrandRegistrations/{brand_sid}/Vettings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "vetting_provider": vetting_provider,
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
async def post_v1_a2p_brand_registrations_brand_sid_vettings(
    brand_sid: str,
    twilio_credentials: "TwilioCredentials",
    vetting_id: str = None,
    vetting_provider: str = None,
) -> Dict[str, Any]:
    """


    Args:
        brand_sid:
            Brand sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        vetting_id:
            The unique ID of the vetting.
        vetting_provider:
            The third-party provider of the vettings to create .

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/a2p/BrandRegistrations/{brand_sid}/Vettings?](
    https://messaging.twilio.com/v1/a2p/BrandRegistrations/{brand_sid}/Vettings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/a2p/BrandRegistrations/{brand_sid}/Vettings"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "vetting_id": vetting_id,
        "vetting_provider": vetting_provider,
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
async def get_v1_a2p_brand_registrations_brand_sid_vettings_brand_vetting_sid(
    brand_sid: str,
    brand_vetting_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        brand_sid:
            Brand sid used in formatting the endpoint URL.
        brand_vetting_sid:
            Brand vetting sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/a2p/BrandRegistrations/{brand_sid}/Vettings/{brand_vetting_sid}?](
    https://messaging.twilio.com/v1/a2p/BrandRegistrations/{brand_sid}/Vettings/{brand_vetting_sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/a2p/BrandRegistrations/{brand_sid}/Vettings/{brand_vetting_sid}"  # noqa
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
async def get_v1_a2p_brand_registrations_sid(
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
    [https://messaging.twilio.com/v1/a2p/BrandRegistrations/{sid}?](
    https://messaging.twilio.com/v1/a2p/BrandRegistrations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/a2p/BrandRegistrations/{sid}"  # noqa
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
async def post_v1_a2p_brand_registrations_sid(
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
    [https://messaging.twilio.com/v1/a2p/BrandRegistrations/{sid}?](
    https://messaging.twilio.com/v1/a2p/BrandRegistrations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 202 | Accepted. |
    """  # noqa
    url = f"https://messaging.twilio.com/v1/a2p/BrandRegistrations/{sid}"  # noqa
    responses = {
        202: "Accepted.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result
