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
async def get_2010_04_01_accounts_account_sid_addresses_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    customer_name: str = None,
    friendly_name: str = None,
    iso_country: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        customer_name:
            The `customer_name` of the Address resources to read.
        friendly_name:
            The string that identifies the Address resources to read.
        iso_country:
            The ISO country code of the Address resources to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses.json?&customer_name=%s&friendly_name=%s&iso_country=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses.json?&customer_name=%s&friendly_name=%s&iso_country=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "customer_name": customer_name,
        "friendly_name": friendly_name,
        "iso_country": iso_country,
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
async def post_2010_04_01_accounts_account_sid_addresses_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    auto_correct_address: bool = None,
    city: str = None,
    customer_name: str = None,
    emergency_enabled: bool = None,
    friendly_name: str = None,
    iso_country: str = None,
    postal_code: str = None,
    region: str = None,
    street: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auto_correct_address:
            Whether we should automatically correct the address. Can be: `true` or
            `false` and the default is `true`. If empty or `true`, we
            will correct the address you provide if necessary. If
            `false`, we won't alter the address you provide.
        city:
            The city of the new address.
        customer_name:
            The name to associate with the new address.
        emergency_enabled:
            Whether to enable emergency calling on the new address. Can be: `true`
            or `false`.
        friendly_name:
            A descriptive string that you create to describe the new address. It can
            be up to 64 characters long.
        iso_country:
            The ISO country code of the new address.
        postal_code:
            The postal code of the new address.
        region:
            The state or region of the new address.
        street:
            The number and street address of the new address.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "auto_correct_address": auto_correct_address,
        "city": city,
        "customer_name": customer_name,
        "emergency_enabled": emergency_enabled,
        "friendly_name": friendly_name,
        "iso_country": iso_country,
        "postal_code": postal_code,
        "region": region,
        "street": street,
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
async def get_2010_04_01_accounts_account_sid_addresses_address_sid_dependent_phone_numbers_json(
    account_sid: str,
    address_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        address_sid:
            Address sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{address_sid}/DependentPhoneNumbers.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{address_sid}/DependentPhoneNumbers.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{address_sid}/DependentPhoneNumbers.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_addresses_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_addresses_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_addresses_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    auto_correct_address: bool = None,
    city: str = None,
    customer_name: str = None,
    emergency_enabled: bool = None,
    friendly_name: str = None,
    postal_code: str = None,
    region: str = None,
    street: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auto_correct_address:
            Whether we should automatically correct the address. Can be: `true` or
            `false` and the default is `true`. If empty or `true`, we
            will correct the address you provide if necessary. If
            `false`, we won't alter the address you provide.
        city:
            The city of the address.
        customer_name:
            The name to associate with the address.
        emergency_enabled:
            Whether to enable emergency calling on the address. Can be: `true` or
            `false`.
        friendly_name:
            A descriptive string that you create to describe the address. It can be
            up to 64 characters long.
        postal_code:
            The postal code of the address.
        region:
            The state or region of the address.
        street:
            The number and street address of the address.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Addresses/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "auto_correct_address": auto_correct_address,
        "city": city,
        "customer_name": customer_name,
        "emergency_enabled": emergency_enabled,
        "friendly_name": friendly_name,
        "postal_code": postal_code,
        "region": region,
        "street": street,
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
async def get_2010_04_01_accounts_account_sid_applications_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of applications representing an application within the
    requesting account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The string that identifies the Application resources to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications.json?&friendly_name=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications.json?&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_applications_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    api_version: str = None,
    friendly_name: str = None,
    message_status_callback: str = None,
    sms_fallback_method: str = None,
    sms_fallback_url: str = None,
    sms_method: str = None,
    sms_status_callback: str = None,
    sms_url: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    voice_caller_id_lookup: bool = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """
    Create a new application within your account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        api_version:
            The API version to use to start a new TwiML session. Can be:
            `2010-04-01` or `2008-08-01`. The default value is the
            account's default API version.
        friendly_name:
            A descriptive string that you create to describe the new application. It
            can be up to 64 characters long.
        message_status_callback:
            The URL we should call using a POST method to send message status
            information to your application.
        sms_fallback_method:
            The HTTP method we should use to call `sms_fallback_url`. Can be: `GET`
            or `POST`.
        sms_fallback_url:
            The URL that we should call when an error occurs while retrieving or
            executing the TwiML from `sms_url`.
        sms_method:
            The HTTP method we should use to call `sms_url`. Can be: `GET` or
            `POST`.
        sms_status_callback:
            The URL we should call using a POST method to send status information
            about SMS messages sent by the application.
        sms_url:
            The URL we should call when the phone number receives an incoming SMS
            message.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `GET`
            or `POST`.
        voice_caller_id_lookup:
            Whether we should look up the caller's caller-ID name from the CNAM
            database (additional charges apply). Can be: `true` or
            `false`.
        voice_fallback_method:
            The HTTP method we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs retrieving or executing
            the TwiML requested by `url`.
        voice_method:
            The HTTP method we should use to call `voice_url`. Can be: `GET` or
            `POST`.
        voice_url:
            The URL we should call when the phone number assigned to this
            application receives a call.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "api_version": api_version,
        "friendly_name": friendly_name,
        "message_status_callback": message_status_callback,
        "sms_fallback_method": sms_fallback_method,
        "sms_fallback_url": sms_fallback_url,
        "sms_method": sms_method,
        "sms_status_callback": sms_status_callback,
        "sms_url": sms_url,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "voice_caller_id_lookup": voice_caller_id_lookup,
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
async def delete_2010_04_01_accounts_account_sid_applications_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete the application by the specified application sid.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_applications_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the application specified by the provided sid.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_applications_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    api_version: str = None,
    friendly_name: str = None,
    message_status_callback: str = None,
    sms_fallback_method: str = None,
    sms_fallback_url: str = None,
    sms_method: str = None,
    sms_status_callback: str = None,
    sms_url: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    voice_caller_id_lookup: bool = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """
    Updates the application's properties.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        api_version:
            The API version to use to start a new TwiML session. Can be:
            `2010-04-01` or `2008-08-01`. The default value is your
            account's default API version.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        message_status_callback:
            The URL we should call using a POST method to send message status
            information to your application.
        sms_fallback_method:
            The HTTP method we should use to call `sms_fallback_url`. Can be: `GET`
            or `POST`.
        sms_fallback_url:
            The URL that we should call when an error occurs while retrieving or
            executing the TwiML from `sms_url`.
        sms_method:
            The HTTP method we should use to call `sms_url`. Can be: `GET` or
            `POST`.
        sms_status_callback:
            Same as message_status_callback: The URL we should call using a POST
            method to send status information about SMS messages sent by
            the application. Deprecated, included for backwards
            compatibility.
        sms_url:
            The URL we should call when the phone number receives an incoming SMS
            message.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `GET`
            or `POST`.
        voice_caller_id_lookup:
            Whether we should look up the caller's caller-ID name from the CNAM
            database (additional charges apply). Can be: `true` or
            `false`.
        voice_fallback_method:
            The HTTP method we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs retrieving or executing
            the TwiML requested by `url`.
        voice_method:
            The HTTP method we should use to call `voice_url`. Can be: `GET` or
            `POST`.
        voice_url:
            The URL we should call when the phone number assigned to this
            application receives a call.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Applications/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "api_version": api_version,
        "friendly_name": friendly_name,
        "message_status_callback": message_status_callback,
        "sms_fallback_method": sms_fallback_method,
        "sms_fallback_url": sms_fallback_url,
        "sms_method": sms_method,
        "sms_status_callback": sms_status_callback,
        "sms_url": sms_url,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "voice_caller_id_lookup": voice_caller_id_lookup,
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
async def get_2010_04_01_accounts_account_sid_authorized_connect_apps_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of authorized-connect-apps belonging to the account used to make
    the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AuthorizedConnectApps.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AuthorizedConnectApps.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AuthorizedConnectApps.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_authorized_connect_apps_connect_app_sid_json(
    account_sid: str,
    connect_app_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of an authorized-connect-app.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        connect_app_sid:
            Connect app sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AuthorizedConnectApps/{connect_app_sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AuthorizedConnectApps/{connect_app_sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AuthorizedConnectApps/{connect_app_sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_available_phone_numbers_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_available_phone_numbers_country_code_json(
    account_sid: str,
    country_code: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        country_code:
            Country code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_available_phone_numbers_country_code_local_json(
    account_sid: str,
    country_code: str,
    twilio_credentials: "TwilioCredentials",
    area_code: int = None,
    contains: str = None,
    sms_enabled: bool = None,
    mms_enabled: bool = None,
    voice_enabled: bool = None,
    exclude_all_address_required: bool = None,
    exclude_local_address_required: bool = None,
    exclude_foreign_address_required: bool = None,
    beta: bool = None,
    near_number: str = None,
    near_lat_long: str = None,
    distance: int = None,
    in_postal_code: str = None,
    in_region: str = None,
    in_rate_center: str = None,
    in_lata: str = None,
    in_locality: str = None,
    fax_enabled: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        country_code:
            Country code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        area_code:
            The area code of the phone numbers to read. Applies to only phone
            numbers in the US and Canada.
        contains:
            The pattern on which to match phone numbers. Valid characters are `*`,
            `0-9`, `a-z`, and `A-Z`. The `*` character matches any
            single digit. For examples, see [Example
            2](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumberlocal-resource?code-
            sample=code-find-phone-numbers-by-number-pattern) and
            [Example 3](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumberlocal-resource?code-
            sample=code-find-phone-numbers-by-character-pattern). If
            specified, this value must have at least two characters.
        sms_enabled:
            Whether the phone numbers can receive text messages. Can be: `true` or
            `false`.
        mms_enabled:
            Whether the phone numbers can receive MMS messages. Can be: `true` or
            `false`.
        voice_enabled:
            Whether the phone numbers can receive calls. Can be: `true` or `false`.
        exclude_all_address_required:
            Whether to exclude phone numbers that require an
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_local_address_required:
            Whether to exclude phone numbers that require a local
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_foreign_address_required:
            Whether to exclude phone numbers that require a foreign
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        beta:
            Whether to read phone numbers that are new to the Twilio platform. Can
            be: `true` or `false` and the default is `true`.
        near_number:
            Given a phone number, find a geographically close number within
            `distance` miles. Distance defaults to 25 miles. Applies to
            only phone numbers in the US and Canada.
        near_lat_long:
            Given a latitude/longitude pair `lat,long` find geographically close
            numbers within `distance` miles. Applies to only phone
            numbers in the US and Canada.
        distance:
            The search radius, in miles, for a `near_` query.  Can be up to `500`
            and the default is `25`. Applies to only phone numbers in
            the US and Canada.
        in_postal_code:
            Limit results to a particular postal code. Given a phone number, search
            within the same postal code as that number. Applies to only
            phone numbers in the US and Canada.
        in_region:
            Limit results to a particular region, state, or province. Given a phone
            number, search within the same region as that number.
            Applies to only phone numbers in the US and Canada.
        in_rate_center:
            Limit results to a specific rate center, or given a phone number search
            within the same rate center as that number. Requires
            `in_lata` to be set as well. Applies to only phone numbers
            in the US and Canada.
        in_lata:
            Limit results to a specific local access and transport area
            ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)).
            Given a phone number, search within the same
            [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)
            as that number. Applies to only phone numbers in the US and
            Canada.
        in_locality:
            Limit results to a particular locality or city. Given a phone number,
            search within the same Locality as that number.
        fax_enabled:
            Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Local.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Local.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Local.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "area_code": area_code,
        "contains": contains,
        "sms_enabled": sms_enabled,
        "mms_enabled": mms_enabled,
        "voice_enabled": voice_enabled,
        "exclude_all_address_required": exclude_all_address_required,
        "exclude_local_address_required": exclude_local_address_required,
        "exclude_foreign_address_required": exclude_foreign_address_required,
        "beta": beta,
        "near_number": near_number,
        "near_lat_long": near_lat_long,
        "distance": distance,
        "in_postal_code": in_postal_code,
        "in_region": in_region,
        "in_rate_center": in_rate_center,
        "in_lata": in_lata,
        "in_locality": in_locality,
        "fax_enabled": fax_enabled,
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
async def get_2010_04_01_accounts_account_sid_available_phone_numbers_country_code_machine_to_machine_json(
    account_sid: str,
    country_code: str,
    twilio_credentials: "TwilioCredentials",
    area_code: int = None,
    contains: str = None,
    sms_enabled: bool = None,
    mms_enabled: bool = None,
    voice_enabled: bool = None,
    exclude_all_address_required: bool = None,
    exclude_local_address_required: bool = None,
    exclude_foreign_address_required: bool = None,
    beta: bool = None,
    near_number: str = None,
    near_lat_long: str = None,
    distance: int = None,
    in_postal_code: str = None,
    in_region: str = None,
    in_rate_center: str = None,
    in_lata: str = None,
    in_locality: str = None,
    fax_enabled: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        country_code:
            Country code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        area_code:
            The area code of the phone numbers to read. Applies to only phone
            numbers in the US and Canada.
        contains:
            The pattern on which to match phone numbers. Valid characters are `*`,
            `0-9`, `a-z`, and `A-Z`. The `*` character matches any
            single digit. For examples, see [Example
            2](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-2) and [Example
            3](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-3). If specified, this value must
            have at least two characters.
        sms_enabled:
            Whether the phone numbers can receive text messages. Can be: `true` or
            `false`.
        mms_enabled:
            Whether the phone numbers can receive MMS messages. Can be: `true` or
            `false`.
        voice_enabled:
            Whether the phone numbers can receive calls. Can be: `true` or `false`.
        exclude_all_address_required:
            Whether to exclude phone numbers that require an
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_local_address_required:
            Whether to exclude phone numbers that require a local
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_foreign_address_required:
            Whether to exclude phone numbers that require a foreign
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        beta:
            Whether to read phone numbers that are new to the Twilio platform. Can
            be: `true` or `false` and the default is `true`.
        near_number:
            Given a phone number, find a geographically close number within
            `distance` miles. Distance defaults to 25 miles. Applies to
            only phone numbers in the US and Canada.
        near_lat_long:
            Given a latitude/longitude pair `lat,long` find geographically close
            numbers within `distance` miles. Applies to only phone
            numbers in the US and Canada.
        distance:
            The search radius, in miles, for a `near_` query.  Can be up to `500`
            and the default is `25`. Applies to only phone numbers in
            the US and Canada.
        in_postal_code:
            Limit results to a particular postal code. Given a phone number, search
            within the same postal code as that number. Applies to only
            phone numbers in the US and Canada.
        in_region:
            Limit results to a particular region, state, or province. Given a phone
            number, search within the same region as that number.
            Applies to only phone numbers in the US and Canada.
        in_rate_center:
            Limit results to a specific rate center, or given a phone number search
            within the same rate center as that number. Requires
            `in_lata` to be set as well. Applies to only phone numbers
            in the US and Canada.
        in_lata:
            Limit results to a specific local access and transport area
            ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)).
            Given a phone number, search within the same
            [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)
            as that number. Applies to only phone numbers in the US and
            Canada.
        in_locality:
            Limit results to a particular locality or city. Given a phone number,
            search within the same Locality as that number.
        fax_enabled:
            Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/MachineToMachine.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/MachineToMachine.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/MachineToMachine.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "area_code": area_code,
        "contains": contains,
        "sms_enabled": sms_enabled,
        "mms_enabled": mms_enabled,
        "voice_enabled": voice_enabled,
        "exclude_all_address_required": exclude_all_address_required,
        "exclude_local_address_required": exclude_local_address_required,
        "exclude_foreign_address_required": exclude_foreign_address_required,
        "beta": beta,
        "near_number": near_number,
        "near_lat_long": near_lat_long,
        "distance": distance,
        "in_postal_code": in_postal_code,
        "in_region": in_region,
        "in_rate_center": in_rate_center,
        "in_lata": in_lata,
        "in_locality": in_locality,
        "fax_enabled": fax_enabled,
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
async def get_2010_04_01_accounts_account_sid_available_phone_numbers_country_code_mobile_json(
    account_sid: str,
    country_code: str,
    twilio_credentials: "TwilioCredentials",
    area_code: int = None,
    contains: str = None,
    sms_enabled: bool = None,
    mms_enabled: bool = None,
    voice_enabled: bool = None,
    exclude_all_address_required: bool = None,
    exclude_local_address_required: bool = None,
    exclude_foreign_address_required: bool = None,
    beta: bool = None,
    near_number: str = None,
    near_lat_long: str = None,
    distance: int = None,
    in_postal_code: str = None,
    in_region: str = None,
    in_rate_center: str = None,
    in_lata: str = None,
    in_locality: str = None,
    fax_enabled: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        country_code:
            Country code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        area_code:
            The area code of the phone numbers to read. Applies to only phone
            numbers in the US and Canada.
        contains:
            The pattern on which to match phone numbers. Valid characters are `*`,
            `0-9`, `a-z`, and `A-Z`. The `*` character matches any
            single digit. For examples, see [Example
            2](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-2) and [Example
            3](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-3). If specified, this value must
            have at least two characters.
        sms_enabled:
            Whether the phone numbers can receive text messages. Can be: `true` or
            `false`.
        mms_enabled:
            Whether the phone numbers can receive MMS messages. Can be: `true` or
            `false`.
        voice_enabled:
            Whether the phone numbers can receive calls. Can be: `true` or `false`.
        exclude_all_address_required:
            Whether to exclude phone numbers that require an
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_local_address_required:
            Whether to exclude phone numbers that require a local
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_foreign_address_required:
            Whether to exclude phone numbers that require a foreign
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        beta:
            Whether to read phone numbers that are new to the Twilio platform. Can
            be: `true` or `false` and the default is `true`.
        near_number:
            Given a phone number, find a geographically close number within
            `distance` miles. Distance defaults to 25 miles. Applies to
            only phone numbers in the US and Canada.
        near_lat_long:
            Given a latitude/longitude pair `lat,long` find geographically close
            numbers within `distance` miles. Applies to only phone
            numbers in the US and Canada.
        distance:
            The search radius, in miles, for a `near_` query.  Can be up to `500`
            and the default is `25`. Applies to only phone numbers in
            the US and Canada.
        in_postal_code:
            Limit results to a particular postal code. Given a phone number, search
            within the same postal code as that number. Applies to only
            phone numbers in the US and Canada.
        in_region:
            Limit results to a particular region, state, or province. Given a phone
            number, search within the same region as that number.
            Applies to only phone numbers in the US and Canada.
        in_rate_center:
            Limit results to a specific rate center, or given a phone number search
            within the same rate center as that number. Requires
            `in_lata` to be set as well. Applies to only phone numbers
            in the US and Canada.
        in_lata:
            Limit results to a specific local access and transport area
            ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)).
            Given a phone number, search within the same
            [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)
            as that number. Applies to only phone numbers in the US and
            Canada.
        in_locality:
            Limit results to a particular locality or city. Given a phone number,
            search within the same Locality as that number.
        fax_enabled:
            Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Mobile.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Mobile.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Mobile.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "area_code": area_code,
        "contains": contains,
        "sms_enabled": sms_enabled,
        "mms_enabled": mms_enabled,
        "voice_enabled": voice_enabled,
        "exclude_all_address_required": exclude_all_address_required,
        "exclude_local_address_required": exclude_local_address_required,
        "exclude_foreign_address_required": exclude_foreign_address_required,
        "beta": beta,
        "near_number": near_number,
        "near_lat_long": near_lat_long,
        "distance": distance,
        "in_postal_code": in_postal_code,
        "in_region": in_region,
        "in_rate_center": in_rate_center,
        "in_lata": in_lata,
        "in_locality": in_locality,
        "fax_enabled": fax_enabled,
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
async def get_2010_04_01_accounts_account_sid_available_phone_numbers_country_code_national_json(
    account_sid: str,
    country_code: str,
    twilio_credentials: "TwilioCredentials",
    area_code: int = None,
    contains: str = None,
    sms_enabled: bool = None,
    mms_enabled: bool = None,
    voice_enabled: bool = None,
    exclude_all_address_required: bool = None,
    exclude_local_address_required: bool = None,
    exclude_foreign_address_required: bool = None,
    beta: bool = None,
    near_number: str = None,
    near_lat_long: str = None,
    distance: int = None,
    in_postal_code: str = None,
    in_region: str = None,
    in_rate_center: str = None,
    in_lata: str = None,
    in_locality: str = None,
    fax_enabled: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        country_code:
            Country code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        area_code:
            The area code of the phone numbers to read. Applies to only phone
            numbers in the US and Canada.
        contains:
            The pattern on which to match phone numbers. Valid characters are `*`,
            `0-9`, `a-z`, and `A-Z`. The `*` character matches any
            single digit. For examples, see [Example
            2](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-2) and [Example
            3](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-3). If specified, this value must
            have at least two characters.
        sms_enabled:
            Whether the phone numbers can receive text messages. Can be: `true` or
            `false`.
        mms_enabled:
            Whether the phone numbers can receive MMS messages. Can be: `true` or
            `false`.
        voice_enabled:
            Whether the phone numbers can receive calls. Can be: `true` or `false`.
        exclude_all_address_required:
            Whether to exclude phone numbers that require an
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_local_address_required:
            Whether to exclude phone numbers that require a local
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_foreign_address_required:
            Whether to exclude phone numbers that require a foreign
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        beta:
            Whether to read phone numbers that are new to the Twilio platform. Can
            be: `true` or `false` and the default is `true`.
        near_number:
            Given a phone number, find a geographically close number within
            `distance` miles. Distance defaults to 25 miles. Applies to
            only phone numbers in the US and Canada.
        near_lat_long:
            Given a latitude/longitude pair `lat,long` find geographically close
            numbers within `distance` miles. Applies to only phone
            numbers in the US and Canada.
        distance:
            The search radius, in miles, for a `near_` query.  Can be up to `500`
            and the default is `25`. Applies to only phone numbers in
            the US and Canada.
        in_postal_code:
            Limit results to a particular postal code. Given a phone number, search
            within the same postal code as that number. Applies to only
            phone numbers in the US and Canada.
        in_region:
            Limit results to a particular region, state, or province. Given a phone
            number, search within the same region as that number.
            Applies to only phone numbers in the US and Canada.
        in_rate_center:
            Limit results to a specific rate center, or given a phone number search
            within the same rate center as that number. Requires
            `in_lata` to be set as well. Applies to only phone numbers
            in the US and Canada.
        in_lata:
            Limit results to a specific local access and transport area
            ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)).
            Given a phone number, search within the same
            [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)
            as that number. Applies to only phone numbers in the US and
            Canada.
        in_locality:
            Limit results to a particular locality or city. Given a phone number,
            search within the same Locality as that number.
        fax_enabled:
            Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/National.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/National.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/National.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "area_code": area_code,
        "contains": contains,
        "sms_enabled": sms_enabled,
        "mms_enabled": mms_enabled,
        "voice_enabled": voice_enabled,
        "exclude_all_address_required": exclude_all_address_required,
        "exclude_local_address_required": exclude_local_address_required,
        "exclude_foreign_address_required": exclude_foreign_address_required,
        "beta": beta,
        "near_number": near_number,
        "near_lat_long": near_lat_long,
        "distance": distance,
        "in_postal_code": in_postal_code,
        "in_region": in_region,
        "in_rate_center": in_rate_center,
        "in_lata": in_lata,
        "in_locality": in_locality,
        "fax_enabled": fax_enabled,
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
async def get_2010_04_01_accounts_account_sid_available_phone_numbers_country_code_shared_cost_json(
    account_sid: str,
    country_code: str,
    twilio_credentials: "TwilioCredentials",
    area_code: int = None,
    contains: str = None,
    sms_enabled: bool = None,
    mms_enabled: bool = None,
    voice_enabled: bool = None,
    exclude_all_address_required: bool = None,
    exclude_local_address_required: bool = None,
    exclude_foreign_address_required: bool = None,
    beta: bool = None,
    near_number: str = None,
    near_lat_long: str = None,
    distance: int = None,
    in_postal_code: str = None,
    in_region: str = None,
    in_rate_center: str = None,
    in_lata: str = None,
    in_locality: str = None,
    fax_enabled: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        country_code:
            Country code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        area_code:
            The area code of the phone numbers to read. Applies to only phone
            numbers in the US and Canada.
        contains:
            The pattern on which to match phone numbers. Valid characters are `*`,
            `0-9`, `a-z`, and `A-Z`. The `*` character matches any
            single digit. For examples, see [Example
            2](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-2) and [Example
            3](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-3). If specified, this value must
            have at least two characters.
        sms_enabled:
            Whether the phone numbers can receive text messages. Can be: `true` or
            `false`.
        mms_enabled:
            Whether the phone numbers can receive MMS messages. Can be: `true` or
            `false`.
        voice_enabled:
            Whether the phone numbers can receive calls. Can be: `true` or `false`.
        exclude_all_address_required:
            Whether to exclude phone numbers that require an
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_local_address_required:
            Whether to exclude phone numbers that require a local
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_foreign_address_required:
            Whether to exclude phone numbers that require a foreign
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        beta:
            Whether to read phone numbers that are new to the Twilio platform. Can
            be: `true` or `false` and the default is `true`.
        near_number:
            Given a phone number, find a geographically close number within
            `distance` miles. Distance defaults to 25 miles. Applies to
            only phone numbers in the US and Canada.
        near_lat_long:
            Given a latitude/longitude pair `lat,long` find geographically close
            numbers within `distance` miles. Applies to only phone
            numbers in the US and Canada.
        distance:
            The search radius, in miles, for a `near_` query.  Can be up to `500`
            and the default is `25`. Applies to only phone numbers in
            the US and Canada.
        in_postal_code:
            Limit results to a particular postal code. Given a phone number, search
            within the same postal code as that number. Applies to only
            phone numbers in the US and Canada.
        in_region:
            Limit results to a particular region, state, or province. Given a phone
            number, search within the same region as that number.
            Applies to only phone numbers in the US and Canada.
        in_rate_center:
            Limit results to a specific rate center, or given a phone number search
            within the same rate center as that number. Requires
            `in_lata` to be set as well. Applies to only phone numbers
            in the US and Canada.
        in_lata:
            Limit results to a specific local access and transport area
            ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)).
            Given a phone number, search within the same
            [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)
            as that number. Applies to only phone numbers in the US and
            Canada.
        in_locality:
            Limit results to a particular locality or city. Given a phone number,
            search within the same Locality as that number.
        fax_enabled:
            Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/SharedCost.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/SharedCost.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/SharedCost.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "area_code": area_code,
        "contains": contains,
        "sms_enabled": sms_enabled,
        "mms_enabled": mms_enabled,
        "voice_enabled": voice_enabled,
        "exclude_all_address_required": exclude_all_address_required,
        "exclude_local_address_required": exclude_local_address_required,
        "exclude_foreign_address_required": exclude_foreign_address_required,
        "beta": beta,
        "near_number": near_number,
        "near_lat_long": near_lat_long,
        "distance": distance,
        "in_postal_code": in_postal_code,
        "in_region": in_region,
        "in_rate_center": in_rate_center,
        "in_lata": in_lata,
        "in_locality": in_locality,
        "fax_enabled": fax_enabled,
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
async def get_2010_04_01_accounts_account_sid_available_phone_numbers_country_code_toll_free_json(
    account_sid: str,
    country_code: str,
    twilio_credentials: "TwilioCredentials",
    area_code: int = None,
    contains: str = None,
    sms_enabled: bool = None,
    mms_enabled: bool = None,
    voice_enabled: bool = None,
    exclude_all_address_required: bool = None,
    exclude_local_address_required: bool = None,
    exclude_foreign_address_required: bool = None,
    beta: bool = None,
    near_number: str = None,
    near_lat_long: str = None,
    distance: int = None,
    in_postal_code: str = None,
    in_region: str = None,
    in_rate_center: str = None,
    in_lata: str = None,
    in_locality: str = None,
    fax_enabled: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        country_code:
            Country code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        area_code:
            The area code of the phone numbers to read. Applies to only phone
            numbers in the US and Canada.
        contains:
            The pattern on which to match phone numbers. Valid characters are `*`,
            `0-9`, `a-z`, and `A-Z`. The `*` character matches any
            single digit. For examples, see [Example
            2](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-2) and [Example
            3](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-3). If specified, this value must
            have at least two characters.
        sms_enabled:
            Whether the phone numbers can receive text messages. Can be: `true` or
            `false`.
        mms_enabled:
            Whether the phone numbers can receive MMS messages. Can be: `true` or
            `false`.
        voice_enabled:
            Whether the phone numbers can receive calls. Can be: `true` or `false`.
        exclude_all_address_required:
            Whether to exclude phone numbers that require an
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_local_address_required:
            Whether to exclude phone numbers that require a local
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_foreign_address_required:
            Whether to exclude phone numbers that require a foreign
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        beta:
            Whether to read phone numbers that are new to the Twilio platform. Can
            be: `true` or `false` and the default is `true`.
        near_number:
            Given a phone number, find a geographically close number within
            `distance` miles. Distance defaults to 25 miles. Applies to
            only phone numbers in the US and Canada.
        near_lat_long:
            Given a latitude/longitude pair `lat,long` find geographically close
            numbers within `distance` miles. Applies to only phone
            numbers in the US and Canada.
        distance:
            The search radius, in miles, for a `near_` query.  Can be up to `500`
            and the default is `25`. Applies to only phone numbers in
            the US and Canada.
        in_postal_code:
            Limit results to a particular postal code. Given a phone number, search
            within the same postal code as that number. Applies to only
            phone numbers in the US and Canada.
        in_region:
            Limit results to a particular region, state, or province. Given a phone
            number, search within the same region as that number.
            Applies to only phone numbers in the US and Canada.
        in_rate_center:
            Limit results to a specific rate center, or given a phone number search
            within the same rate center as that number. Requires
            `in_lata` to be set as well. Applies to only phone numbers
            in the US and Canada.
        in_lata:
            Limit results to a specific local access and transport area
            ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)).
            Given a phone number, search within the same
            [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)
            as that number. Applies to only phone numbers in the US and
            Canada.
        in_locality:
            Limit results to a particular locality or city. Given a phone number,
            search within the same Locality as that number.
        fax_enabled:
            Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/TollFree.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/TollFree.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/TollFree.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "area_code": area_code,
        "contains": contains,
        "sms_enabled": sms_enabled,
        "mms_enabled": mms_enabled,
        "voice_enabled": voice_enabled,
        "exclude_all_address_required": exclude_all_address_required,
        "exclude_local_address_required": exclude_local_address_required,
        "exclude_foreign_address_required": exclude_foreign_address_required,
        "beta": beta,
        "near_number": near_number,
        "near_lat_long": near_lat_long,
        "distance": distance,
        "in_postal_code": in_postal_code,
        "in_region": in_region,
        "in_rate_center": in_rate_center,
        "in_lata": in_lata,
        "in_locality": in_locality,
        "fax_enabled": fax_enabled,
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
async def get_2010_04_01_accounts_account_sid_available_phone_numbers_country_code_voip_json(
    account_sid: str,
    country_code: str,
    twilio_credentials: "TwilioCredentials",
    area_code: int = None,
    contains: str = None,
    sms_enabled: bool = None,
    mms_enabled: bool = None,
    voice_enabled: bool = None,
    exclude_all_address_required: bool = None,
    exclude_local_address_required: bool = None,
    exclude_foreign_address_required: bool = None,
    beta: bool = None,
    near_number: str = None,
    near_lat_long: str = None,
    distance: int = None,
    in_postal_code: str = None,
    in_region: str = None,
    in_rate_center: str = None,
    in_lata: str = None,
    in_locality: str = None,
    fax_enabled: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        country_code:
            Country code used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        area_code:
            The area code of the phone numbers to read. Applies to only phone
            numbers in the US and Canada.
        contains:
            The pattern on which to match phone numbers. Valid characters are `*`,
            `0-9`, `a-z`, and `A-Z`. The `*` character matches any
            single digit. For examples, see [Example
            2](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-2) and [Example
            3](https://www.twilio.com/docs/phone-
            numbers/api/availablephonenumber-resource
            local-get-basic-example-3). If specified, this value must
            have at least two characters.
        sms_enabled:
            Whether the phone numbers can receive text messages. Can be: `true` or
            `false`.
        mms_enabled:
            Whether the phone numbers can receive MMS messages. Can be: `true` or
            `false`.
        voice_enabled:
            Whether the phone numbers can receive calls. Can be: `true` or `false`.
        exclude_all_address_required:
            Whether to exclude phone numbers that require an
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_local_address_required:
            Whether to exclude phone numbers that require a local
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        exclude_foreign_address_required:
            Whether to exclude phone numbers that require a foreign
            [Address](https://www.twilio.com/docs/usage/api/address).
            Can be: `true` or `false` and the default is `false`.
        beta:
            Whether to read phone numbers that are new to the Twilio platform. Can
            be: `true` or `false` and the default is `true`.
        near_number:
            Given a phone number, find a geographically close number within
            `distance` miles. Distance defaults to 25 miles. Applies to
            only phone numbers in the US and Canada.
        near_lat_long:
            Given a latitude/longitude pair `lat,long` find geographically close
            numbers within `distance` miles. Applies to only phone
            numbers in the US and Canada.
        distance:
            The search radius, in miles, for a `near_` query.  Can be up to `500`
            and the default is `25`. Applies to only phone numbers in
            the US and Canada.
        in_postal_code:
            Limit results to a particular postal code. Given a phone number, search
            within the same postal code as that number. Applies to only
            phone numbers in the US and Canada.
        in_region:
            Limit results to a particular region, state, or province. Given a phone
            number, search within the same region as that number.
            Applies to only phone numbers in the US and Canada.
        in_rate_center:
            Limit results to a specific rate center, or given a phone number search
            within the same rate center as that number. Requires
            `in_lata` to be set as well. Applies to only phone numbers
            in the US and Canada.
        in_lata:
            Limit results to a specific local access and transport area
            ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)).
            Given a phone number, search within the same
            [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)
            as that number. Applies to only phone numbers in the US and
            Canada.
        in_locality:
            Limit results to a particular locality or city. Given a phone number,
            search within the same Locality as that number.
        fax_enabled:
            Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Voip.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Voip.json?&area_code=%s&contains=%s&sms_enabled=%s&mms_enabled=%s&voice_enabled=%s&exclude_all_address_required=%s&exclude_local_address_required=%s&exclude_foreign_address_required=%s&beta=%s&near_number=%s&near_lat_long=%s&distance=%s&in_postal_code=%s&in_region=%s&in_rate_center=%s&in_lata=%s&in_locality=%s&fax_enabled=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Voip.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "area_code": area_code,
        "contains": contains,
        "sms_enabled": sms_enabled,
        "mms_enabled": mms_enabled,
        "voice_enabled": voice_enabled,
        "exclude_all_address_required": exclude_all_address_required,
        "exclude_local_address_required": exclude_local_address_required,
        "exclude_foreign_address_required": exclude_foreign_address_required,
        "beta": beta,
        "near_number": near_number,
        "near_lat_long": near_lat_long,
        "distance": distance,
        "in_postal_code": in_postal_code,
        "in_region": in_region,
        "in_rate_center": in_rate_center,
        "in_lata": in_lata,
        "in_locality": in_locality,
        "fax_enabled": fax_enabled,
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
async def get_2010_04_01_accounts_account_sid_balance_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the balance for an Account based on Account Sid. Balance changes may not
    be reflected immediately. Child accounts do not contain balance information.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Balance.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Balance.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Balance.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_calls_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    to: str = None,
    from_: str = None,
    parent_call_sid: str = None,
    status: str = None,
    start_time: str = None,
    end_time: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieves a collection of calls made to and from your account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        to:
            Only show calls made to this phone number, SIP address, Client
            identifier or SIM SID.
        from_:
            Only include calls from this phone number, SIP address, Client
            identifier or SIM SID.
        parent_call_sid:
            Only include calls spawned by calls with this SID.
        status:
            The status of the calls to include. Can be: `queued`, `ringing`, `in-
            progress`, `canceled`, `completed`, `failed`, `busy`, or
            `no-answer`.
        start_time:
            Only include calls that started on this date. Specify a date as `YYYY-
            MM-DD` in GMT, for example: `2009-07-06`, to read only calls
            that started on this date. You can also specify an
            inequality, such as `StartTime<=YYYY-MM-DD`, to read calls
            that started on or before midnight of this date, and
            `StartTime>=YYYY-MM-DD` to read calls that started on or
            after midnight of this date.
        end_time:
            Only include calls that ended on this date. Specify a date as `YYYY-MM-
            DD` in GMT, for example: `2009-07-06`, to read only calls
            that ended on this date. You can also specify an inequality,
            such as `EndTime<=YYYY-MM-DD`, to read calls that ended on
            or before midnight of this date, and `EndTime>=YYYY-MM-DD`
            to read calls that ended on or after midnight of this date.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls.json?&to=%s&from_=%s&parent_call_sid=%s&status=%s&start_time=%s&start_time=%s&start_time=%s&end_time=%s&end_time=%s&end_time=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls.json?&to=%s&from_=%s&parent_call_sid=%s&status=%s&start_time=%s&start_time=%s&start_time=%s&end_time=%s&end_time=%s&end_time=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "to": to,
        "from_": from_,
        "parent_call_sid": parent_call_sid,
        "status": status,
        "start_time": start_time,
        "start_time": start_time,
        "start_time": start_time,
        "end_time": end_time,
        "end_time": end_time,
        "end_time": end_time,
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
async def post_2010_04_01_accounts_account_sid_calls_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    application_sid: str = None,
    async_amd: str = None,
    async_amd_status_callback: str = None,
    async_amd_status_callback_method: str = None,
    byoc: str = None,
    call_reason: str = None,
    call_token: str = None,
    caller_id: str = None,
    fallback_method: str = None,
    fallback_url: str = None,
    from_: str = None,
    machine_detection: str = None,
    machine_detection_silence_timeout: int = None,
    machine_detection_speech_end_threshold: int = None,
    machine_detection_speech_threshold: int = None,
    machine_detection_timeout: int = None,
    method: str = None,
    record: bool = None,
    recording_channels: str = None,
    recording_status_callback: str = None,
    recording_status_callback_event: list = None,
    recording_status_callback_method: str = None,
    recording_track: str = None,
    send_digits: str = None,
    sip_auth_password: str = None,
    sip_auth_username: str = None,
    status_callback: str = None,
    status_callback_event: list = None,
    status_callback_method: str = None,
    time_limit: int = None,
    timeout: int = None,
    to: str = None,
    trim: str = None,
    twiml: str = None,
    url: str = None,
) -> Dict[str, Any]:
    """
    Create a new outgoing call to phones, SIP-enabled endpoints or Twilio Client
    connections.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        application_sid:
            The SID of the Application resource that will handle the call, if the
            call will be handled by an application.
        async_amd:
            Select whether to perform answering machine detection in the background.
            Default, blocks the execution of the call until Answering
            Machine Detection is completed. Can be: `true` or `false`.
        async_amd_status_callback:
            The URL that we should call using the `async_amd_status_callback_method`
            to notify customer application whether the call was answered
            by human, machine or fax.
        async_amd_status_callback_method:
            The HTTP method we should use when calling the
            `async_amd_status_callback` URL. Can be: `GET` or `POST` and
            the default is `POST`.
        byoc:
            The SID of a BYOC (Bring Your Own Carrier) trunk to route this call
            with. Note that `byoc` is only meaningful when `to` is a
            phone number; it will otherwise be ignored. (Beta).
        call_reason:
            The Reason for the outgoing call. Use it to specify the purpose of the
            call that is presented on the called party's phone. (Branded
            Calls Beta).
        call_token:
            A token string needed to invoke a forwarded call. A call_token is
            generated when an incoming call is received on a Twilio
            number. Pass an incoming call's call_token value to a
            forwarded call via the call_token parameter when creating a
            new call. A forwarded call should bear the same CallerID of
            the original incoming call.
        caller_id:
            The phone number, SIP address, or Client identifier that made this call.
            Phone numbers are in [E.164
            format](https://wwnw.twilio.com/docs/glossary/what-e164)
            (e.g., +16175551212). SIP addresses are formatted as
            `name@company.com`.
        fallback_method:
            The HTTP method that we should use to request the `fallback_url`. Can
            be: `GET` or `POST` and the default is `POST`. If an
            `application_sid` parameter is present, this parameter is
            ignored.
        fallback_url:
            The URL that we call using the `fallback_method` if an error occurs when
            requesting or executing the TwiML at `url`. If an
            `application_sid` parameter is present, this parameter is
            ignored.
        from_:
            The phone number or client identifier to use as the caller id. If using
            a phone number, it must be a Twilio number or a Verified
            [outgoing caller
            id](https://www.twilio.com/docs/voice/api/outgoing-caller-
            ids) for your account. If the `to` parameter is a phone
            number, `From` must also be a phone number.
        machine_detection:
            Whether to detect if a human, answering machine, or fax has picked up
            the call. Can be: `Enable` or `DetectMessageEnd`. Use
            `Enable` if you would like us to return `AnsweredBy` as soon
            as the called party is identified. Use `DetectMessageEnd`,
            if you would like to leave a message on an answering
            machine. If `send_digits` is provided, this parameter is
            ignored. For more information, see [Answering Machine
            Detection](https://www.twilio.com/docs/voice/answering-
            machine-detection).
        machine_detection_silence_timeout:
            The number of milliseconds of initial silence after which an `unknown`
            AnsweredBy result will be returned. Possible Values:
            2000-10000. Default: 5000.
        machine_detection_speech_end_threshold:
            The number of milliseconds of silence after speech activity at which
            point the speech activity is considered complete. Possible
            Values: 500-5000. Default: 1200.
        machine_detection_speech_threshold:
            The number of milliseconds that is used as the measuring stick for the
            length of the speech activity, where durations lower than
            this value will be interpreted as a human and longer than
            this value as a machine. Possible Values: 1000-6000.
            Default: 2400.
        machine_detection_timeout:
            The number of seconds that we should attempt to detect an answering
            machine before timing out and sending a voice request with
            `AnsweredBy` of `unknown`. The default timeout is 30
            seconds.
        method:
            The HTTP method we should use when calling the `url` parameter's value.
            Can be: `GET` or `POST` and the default is `POST`. If an
            `application_sid` parameter is present, this parameter is
            ignored.
        record:
            Whether to record the call. Can be `true` to record the phone call, or
            `false` to not. The default is `false`. The `recording_url`
            is sent to the `status_callback` URL.
        recording_channels:
            The number of channels in the final recording. Can be: `mono` or `dual`.
            The default is `mono`. `mono` records both legs of the call
            in a single channel of the recording file. `dual` records
            each leg to a separate channel of the recording file. The
            first channel of a dual-channel recording contains the
            parent call and the second channel contains the child call.
        recording_status_callback:
            The URL that we call when the recording is available to be accessed.
        recording_status_callback_event:
            The recording status events that will trigger calls to the URL specified
            in `recording_status_callback`. Can be: `in-progress`,
            `completed` and `absent`. Defaults to `completed`. Separate
            multiple values with a space.
        recording_status_callback_method:
            The HTTP method we should use when calling the
            `recording_status_callback` URL. Can be: `GET` or `POST` and
            the default is `POST`.
        recording_track:
            The audio track to record for the call. Can be: `inbound`, `outbound` or
            `both`. The default is `both`. `inbound` records the audio
            that is received by Twilio. `outbound` records the audio
            that is generated from Twilio. `both` records the audio that
            is received and generated by Twilio.
        send_digits:
            A string of keys to dial after connecting to the number, maximum of 32
            digits. Valid digits in the string include: any digit
            (`0`-`9`), '`
            `', '`*`' and '`w`', to insert a half second pause. For
            example, if you connected to a company phone number and
            wanted to pause for one second, and then dial extension 1234
            followed by the pound key, the value of this parameter would
            be `ww1234
            `. Remember to URL-encode this string, since the '`
            `' character has special meaning in a URL. If both
            `SendDigits` and `MachineDetection` parameters are provided,
            then `MachineDetection` will be ignored.
        sip_auth_password:
            The password required to authenticate the user account specified in
            `sip_auth_username`.
        sip_auth_username:
            The username used to authenticate the caller making a SIP call.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application. If no
            `status_callback_event` is specified, we will send the
            `completed` status. If an `application_sid` parameter is
            present, this parameter is ignored. URLs must contain a
            valid hostname (underscores are not permitted).
        status_callback_event:
            The call progress events that we will send to the `status_callback` URL.
            Can be: `initiated`, `ringing`, `answered`, and `completed`.
            If no event is specified, we send the `completed` status. If
            you want to receive multiple events, specify each one in a
            separate `status_callback_event` parameter. See the code
            sample for [monitoring call
            progress](https://www.twilio.com/docs/voice/api/call-
            resource?code-sample=code-create-a-call-resource-and-
            specify-a-statuscallbackevent&code-sdk-version=json). If an
            `application_sid` is present, this parameter is ignored.
        status_callback_method:
            The HTTP method we should use when calling the `status_callback` URL.
            Can be: `GET` or `POST` and the default is `POST`. If an
            `application_sid` parameter is present, this parameter is
            ignored.
        time_limit:
            The maximum duration of the call in seconds. Constraints depend on
            account and configuration.
        timeout:
            The integer number of seconds that we should allow the phone to ring
            before assuming there is no answer. The default is `60`
            seconds and the maximum is `600` seconds. For some call
            flows, we will add a 5-second buffer to the timeout value
            you provide. For this reason, a timeout value of 10 seconds
            could result in an actual timeout closer to 15 seconds. You
            can set this to a short time, such as `15` seconds, to hang
            up before reaching an answering machine or voicemail.
        to:
            The phone number, SIP address, or client identifier to call.
        trim:
            Whether to trim any leading and trailing silence from the recording. Can
            be: `trim-silence` or `do-not-trim` and the default is
            `trim-silence`.
        twiml:
            TwiML instructions for the call Twilio will use without fetching Twiml
            from url parameter. If both `twiml` and `url` are provided
            then `twiml` parameter will be ignored. Max 4000 characters.
        url:
            The absolute URL that returns the TwiML instructions for the call. We
            will call this URL using the `method` when the call
            connects. For more information, see the [Url
            Parameter](https://www.twilio.com/docs/voice/make-calls
            specify-a-url-parameter) section in [Making
            Calls](https://www.twilio.com/docs/voice/make-calls).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "application_sid": application_sid,
        "async_amd": async_amd,
        "async_amd_status_callback": async_amd_status_callback,
        "async_amd_status_callback_method": async_amd_status_callback_method,
        "byoc": byoc,
        "call_reason": call_reason,
        "call_token": call_token,
        "caller_id": caller_id,
        "fallback_method": fallback_method,
        "fallback_url": fallback_url,
        "from_": from_,
        "machine_detection": machine_detection,
        "machine_detection_silence_timeout": machine_detection_silence_timeout,
        "machine_detection_speech_end_threshold": machine_detection_speech_end_threshold,  # noqa
        "machine_detection_speech_threshold": machine_detection_speech_threshold,
        "machine_detection_timeout": machine_detection_timeout,
        "method": method,
        "record": record,
        "recording_channels": recording_channels,
        "recording_status_callback": recording_status_callback,
        "recording_status_callback_event": recording_status_callback_event,
        "recording_status_callback_method": recording_status_callback_method,
        "recording_track": recording_track,
        "send_digits": send_digits,
        "sip_auth_password": sip_auth_password,
        "sip_auth_username": sip_auth_username,
        "status_callback": status_callback,
        "status_callback_event": status_callback_event,
        "status_callback_method": status_callback_method,
        "time_limit": time_limit,
        "timeout": timeout,
        "to": to,
        "trim": trim,
        "twiml": twiml,
        "url": url,
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
async def post_2010_04_01_accounts_account_sid_calls_feedback_summary_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    end_date: str = None,
    include_subaccounts: bool = None,
    start_date: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
) -> Dict[str, Any]:
    """
    Create a FeedbackSummary resource for a call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_date:
            Only include feedback given on or before this date. Format is `YYYY-MM-
            DD` and specified in UTC.
        include_subaccounts:
            Whether to also include Feedback resources from all subaccounts. `true`
            includes feedback from all subaccounts and `false`, the
            default, includes feedback from only the specified account.
        start_date:
            Only include feedback given on or after this date. Format is `YYYY-MM-
            DD` and specified in UTC.
        status_callback:
            The URL that we will request when the feedback summary is complete.
        status_callback_method:
            The HTTP method (`GET` or `POST`) we use to make the request to the
            `StatusCallback` URL.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/FeedbackSummary.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/FeedbackSummary.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/FeedbackSummary.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
        "start_date": start_date,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
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
async def delete_2010_04_01_accounts_account_sid_calls_feedback_summary_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a FeedbackSummary resource from a call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/FeedbackSummary/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/FeedbackSummary/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/FeedbackSummary/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_calls_feedback_summary_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a FeedbackSummary resource from a call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/FeedbackSummary/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/FeedbackSummary/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/FeedbackSummary/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_calls_call_sid_events_json(
    account_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all events for a call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Events.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Events.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Events.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_calls_call_sid_feedback_json(
    account_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a Feedback resource from a call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_calls_call_sid_feedback_json(
    account_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    issue: list = None,
    quality_score: int = None,
) -> Dict[str, Any]:
    """
    Update a Feedback resource for a call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        issue:
            One or more issues experienced during the call. The issues can be:
            `imperfect-audio`, `dropped-call`, `incorrect-caller-id`,
            `post-dial-delay`, `digits-not-captured`, `audio-latency`,
            `unsolicited-call`, or `one-way-audio`.
        quality_score:
            The call quality expressed as an integer from `1` to `5` where `1`
            represents very poor call quality and `5` represents a
            perfect call.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "issue": issue,
        "quality_score": quality_score,
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
async def get_2010_04_01_accounts_account_sid_calls_call_sid_notifications_json(
    account_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    log: int = None,
    message_date: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        log:
            Only read notifications of the specified log level. Can be:  `0` to read
            only ERROR notifications or `1` to read only WARNING
            notifications. By default, all notifications are read.
        message_date:
            Only show notifications for the specified date, formatted as `YYYY-MM-
            DD`. You can also specify an inequality, such as `<=YYYY-MM-
            DD` for messages logged at or before midnight on a date, or
            `>=YYYY-MM-DD` for messages logged at or after midnight on a
            date.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Notifications.json?&log=%s&message_date=%s&message_date=%s&message_date=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Notifications.json?&log=%s&message_date=%s&message_date=%s&message_date=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Notifications.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "log": log,
        "message_date": message_date,
        "message_date": message_date,
        "message_date": message_date,
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
async def get_2010_04_01_accounts_account_sid_calls_call_sid_notifications_sid_json(
    account_sid: str,
    call_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Notifications/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Notifications/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Notifications/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_calls_call_sid_payments_json(
    account_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    bank_account_type: str = None,
    charge_amount: str = None,
    currency: str = None,
    description: str = None,
    idempotency_key: str = None,
    input: str = None,
    min_postal_code_length: int = None,
    parameter: str = None,
    payment_connector: str = None,
    payment_method: str = None,
    postal_code: bool = None,
    security_code: bool = None,
    status_callback: str = None,
    timeout: int = None,
    token_type: str = None,
    valid_card_types: str = None,
) -> Dict[str, Any]:
    """
    create an instance of payments. This will start a new payments session.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        bank_account_type:
            Type of bank account if payment source is ACH. One of `consumer-
            checking`, `consumer-savings`, or `commercial-checking`. The
            default value is `consumer-checking`.
        charge_amount:
            A positive decimal value less than 1,000,000 to charge against the
            credit card or bank account. Default currency can be
            overwritten with `currency` field. Leave blank or set to 0
            to tokenize.
        currency:
            The currency of the `charge_amount`, formatted as [ISO
            4127](http://www.iso.org/iso/home/standards/currency_codes.htm)
            format. The default value is `USD` and all values allowed
            from the Pay Connector are accepted.
        description:
            The description can be used to provide more details regarding the
            transaction. This information is submitted along with the
            payment details to the Payment Connector which are then
            posted on the transactions.
        idempotency_key:
            A unique token that will be used to ensure that multiple API calls with
            the same information do not result in multiple transactions.
            This should be a unique string value per API call and can be
            a randomly generated.
        input:
            A list of inputs that should be accepted. Currently only `dtmf` is
            supported. All digits captured during a pay session are
            redacted from the logs.
        min_postal_code_length:
            A positive integer that is used to validate the length of the
            `PostalCode` inputted by the user. User must enter this many
            digits.
        parameter:
            A single-level JSON object used to pass custom parameters to payment
            processors. (Required for ACH payments). The information
            that has to be included here depends on the <Pay> Connector.
            [Read more](https://www.twilio.com/console/voice/pay-
            connectors).
        payment_connector:
            This is the unique name corresponding to the Pay Connector installed in
            the Twilio Add-ons. Learn more about [<Pay>
            Connectors](https://www.twilio.com/console/voice/pay-
            connectors). The default value is `Default`.
        payment_method:
            Type of payment being captured. One of `credit-card` or `ach-debit`. The
            default value is `credit-card`.
        postal_code:
            Indicates whether the credit card postal code (zip code) is a required
            piece of payment information that must be provided by the
            caller. The default is `true`.
        security_code:
            Indicates whether the credit card security code is a required piece of
            payment information that must be provided by the caller. The
            default is `true`.
        status_callback:
            Provide an absolute or relative URL to receive status updates regarding
            your Pay session. Read more about the [expected
            StatusCallback
            values](https://www.twilio.com/docs/voice/api/payment-
            resource
            statuscallback).
        timeout:
            The number of seconds that <Pay> should wait for the caller to press a
            digit between each subsequent digit, after the first one,
            before moving on to validate the digits captured. The
            default is `5`, maximum is `600`.
        token_type:
            Indicates whether the payment method should be tokenized as a `one-time`
            or `reusable` token. The default value is `reusable`. Do not
            enter a charge amount when tokenizing. If a charge amount is
            entered, the payment method will be charged and not
            tokenized.
        valid_card_types:
            Credit card types separated by space that Pay should accept. The default
            value is `visa mastercard amex`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Payments.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Payments.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Payments.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "bank_account_type": bank_account_type,
        "charge_amount": charge_amount,
        "currency": currency,
        "description": description,
        "idempotency_key": idempotency_key,
        "input": input,
        "min_postal_code_length": min_postal_code_length,
        "parameter": parameter,
        "payment_connector": payment_connector,
        "payment_method": payment_method,
        "postal_code": postal_code,
        "security_code": security_code,
        "status_callback": status_callback,
        "timeout": timeout,
        "token_type": token_type,
        "valid_card_types": valid_card_types,
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
async def post_2010_04_01_accounts_account_sid_calls_call_sid_payments_sid_json(
    account_sid: str,
    call_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    capture: str = None,
    idempotency_key: str = None,
    status: str = None,
    status_callback: str = None,
) -> Dict[str, Any]:
    """
    update an instance of payments with different phases of payment flows.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        capture:
            The piece of payment information that you wish the caller to enter. Must
            be one of `payment-card-number`, `expiration-date`,
            `security-code`, `postal-code`, `bank-routing-number`, or
            `bank-account-number`.
        idempotency_key:
            A unique token that will be used to ensure that multiple API calls with
            the same information do not result in multiple transactions.
            This should be a unique string value per API call and can be
            a randomly generated.
        status:
            Indicates whether the current payment session should be cancelled or
            completed. When `cancel` the payment session is cancelled.
            When `complete`, Twilio sends the payment information to the
            selected Pay Connector for processing.
        status_callback:
            Provide an absolute or relative URL to receive status updates regarding
            your Pay session. Read more about the
            [Update](https://www.twilio.com/docs/voice/api/payment-
            resource
            statuscallback-update) and
            [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-
            resource
            statuscallback-cancelcomplete) POST requests.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Payments/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Payments/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 202 | Accepted. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Payments/{sid}.json"  # noqa
    responses = {
        202: "Accepted.",  # noqa
    }

    data = {
        "capture": capture,
        "idempotency_key": idempotency_key,
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
async def get_2010_04_01_accounts_account_sid_calls_call_sid_recordings_json(
    account_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    date_created: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of recordings belonging to the call used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created:
            The `date_created` value, specified as `YYYY-MM-DD`, of the resources to
            read. You can also specify inequality: `DateCreated<=YYYY-
            MM-DD` will return recordings generated at or before
            midnight on a given date, and `DateCreated>=YYYY-MM-DD`
            returns recordings generated at or after midnight on a date.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json?&date_created=%s&date_created=%s&date_created=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json?&date_created=%s&date_created=%s&date_created=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created": date_created,
        "date_created": date_created,
        "date_created": date_created,
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
async def post_2010_04_01_accounts_account_sid_calls_call_sid_recordings_json(
    account_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    recording_channels: str = None,
    recording_status_callback: str = None,
    recording_status_callback_event: list = None,
    recording_status_callback_method: str = None,
    recording_track: str = None,
    trim: str = None,
) -> Dict[str, Any]:
    """
    Create a recording for the call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        recording_channels:
            The number of channels used in the recording. Can be: `mono` or `dual`
            and the default is `mono`. `mono` records all parties of the
            call into one channel. `dual` records each party of a
            2-party call into separate channels.
        recording_status_callback:
            The URL we should call using the `recording_status_callback_method` on
            each recording event specified in
            `recording_status_callback_event`. For more information, see
            [RecordingStatusCallback
            parameters](https://www.twilio.com/docs/voice/api/recording
            recordingstatuscallback).
        recording_status_callback_event:
            The recording status events on which we should call the
            `recording_status_callback` URL. Can be: `in-progress`,
            `completed` and `absent` and the default is `completed`.
            Separate multiple event values with a space.
        recording_status_callback_method:
            The HTTP method we should use to call `recording_status_callback`. Can
            be: `GET` or `POST` and the default is `POST`.
        recording_track:
            The audio track to record for the call. Can be: `inbound`, `outbound` or
            `both`. The default is `both`. `inbound` records the audio
            that is received by Twilio. `outbound` records the audio
            that is generated from Twilio. `both` records the audio that
            is received and generated by Twilio.
        trim:
            Whether to trim any leading and trailing silence in the recording. Can
            be: `trim-silence` or `do-not-trim` and the default is `do-
            not-trim`. `trim-silence` trims the silence from the
            beginning and end of the recording and `do-not-trim` does
            not.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "recording_channels": recording_channels,
        "recording_status_callback": recording_status_callback,
        "recording_status_callback_event": recording_status_callback_event,
        "recording_status_callback_method": recording_status_callback_method,
        "recording_track": recording_track,
        "trim": trim,
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
async def delete_2010_04_01_accounts_account_sid_calls_call_sid_recordings_sid_json(
    account_sid: str,
    call_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a recording from your account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_calls_call_sid_recordings_sid_json(
    account_sid: str,
    call_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a recording for a call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_calls_call_sid_recordings_sid_json(
    account_sid: str,
    call_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    pause_behavior: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """
    Changes the status of the recording to paused, stopped, or in-progress. Note:
    Pass `Twilio.CURRENT` instead of recording sid to reference current active
    recording.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        pause_behavior:
            Whether to record during a pause. Can be: `skip` or `silence` and the
            default is `silence`. `skip` does not record during the
            pause period, while `silence` will replace the actual audio
            of the call with silence during the pause period. This
            parameter only applies when setting `status` is set to
            `paused`.
        status:
            The new status of the recording. Can be: `stopped`, `paused`, `in-
            progress`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "pause_behavior": pause_behavior,
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
async def post_2010_04_01_accounts_account_sid_calls_call_sid_siprec_json(
    account_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    connector_name: str = None,
    name: str = None,
    parameter1_name: str = None,
    parameter1_value: str = None,
    parameter10_name: str = None,
    parameter10_value: str = None,
    parameter11_name: str = None,
    parameter11_value: str = None,
    parameter12_name: str = None,
    parameter12_value: str = None,
    parameter13_name: str = None,
    parameter13_value: str = None,
    parameter14_name: str = None,
    parameter14_value: str = None,
    parameter15_name: str = None,
    parameter15_value: str = None,
    parameter16_name: str = None,
    parameter16_value: str = None,
    parameter17_name: str = None,
    parameter17_value: str = None,
    parameter18_name: str = None,
    parameter18_value: str = None,
    parameter19_name: str = None,
    parameter19_value: str = None,
    parameter2_name: str = None,
    parameter2_value: str = None,
    parameter20_name: str = None,
    parameter20_value: str = None,
    parameter21_name: str = None,
    parameter21_value: str = None,
    parameter22_name: str = None,
    parameter22_value: str = None,
    parameter23_name: str = None,
    parameter23_value: str = None,
    parameter24_name: str = None,
    parameter24_value: str = None,
    parameter25_name: str = None,
    parameter25_value: str = None,
    parameter26_name: str = None,
    parameter26_value: str = None,
    parameter27_name: str = None,
    parameter27_value: str = None,
    parameter28_name: str = None,
    parameter28_value: str = None,
    parameter29_name: str = None,
    parameter29_value: str = None,
    parameter3_name: str = None,
    parameter3_value: str = None,
    parameter30_name: str = None,
    parameter30_value: str = None,
    parameter31_name: str = None,
    parameter31_value: str = None,
    parameter32_name: str = None,
    parameter32_value: str = None,
    parameter33_name: str = None,
    parameter33_value: str = None,
    parameter34_name: str = None,
    parameter34_value: str = None,
    parameter35_name: str = None,
    parameter35_value: str = None,
    parameter36_name: str = None,
    parameter36_value: str = None,
    parameter37_name: str = None,
    parameter37_value: str = None,
    parameter38_name: str = None,
    parameter38_value: str = None,
    parameter39_name: str = None,
    parameter39_value: str = None,
    parameter4_name: str = None,
    parameter4_value: str = None,
    parameter40_name: str = None,
    parameter40_value: str = None,
    parameter41_name: str = None,
    parameter41_value: str = None,
    parameter42_name: str = None,
    parameter42_value: str = None,
    parameter43_name: str = None,
    parameter43_value: str = None,
    parameter44_name: str = None,
    parameter44_value: str = None,
    parameter45_name: str = None,
    parameter45_value: str = None,
    parameter46_name: str = None,
    parameter46_value: str = None,
    parameter47_name: str = None,
    parameter47_value: str = None,
    parameter48_name: str = None,
    parameter48_value: str = None,
    parameter49_name: str = None,
    parameter49_value: str = None,
    parameter5_name: str = None,
    parameter5_value: str = None,
    parameter50_name: str = None,
    parameter50_value: str = None,
    parameter51_name: str = None,
    parameter51_value: str = None,
    parameter52_name: str = None,
    parameter52_value: str = None,
    parameter53_name: str = None,
    parameter53_value: str = None,
    parameter54_name: str = None,
    parameter54_value: str = None,
    parameter55_name: str = None,
    parameter55_value: str = None,
    parameter56_name: str = None,
    parameter56_value: str = None,
    parameter57_name: str = None,
    parameter57_value: str = None,
    parameter58_name: str = None,
    parameter58_value: str = None,
    parameter59_name: str = None,
    parameter59_value: str = None,
    parameter6_name: str = None,
    parameter6_value: str = None,
    parameter60_name: str = None,
    parameter60_value: str = None,
    parameter61_name: str = None,
    parameter61_value: str = None,
    parameter62_name: str = None,
    parameter62_value: str = None,
    parameter63_name: str = None,
    parameter63_value: str = None,
    parameter64_name: str = None,
    parameter64_value: str = None,
    parameter65_name: str = None,
    parameter65_value: str = None,
    parameter66_name: str = None,
    parameter66_value: str = None,
    parameter67_name: str = None,
    parameter67_value: str = None,
    parameter68_name: str = None,
    parameter68_value: str = None,
    parameter69_name: str = None,
    parameter69_value: str = None,
    parameter7_name: str = None,
    parameter7_value: str = None,
    parameter70_name: str = None,
    parameter70_value: str = None,
    parameter71_name: str = None,
    parameter71_value: str = None,
    parameter72_name: str = None,
    parameter72_value: str = None,
    parameter73_name: str = None,
    parameter73_value: str = None,
    parameter74_name: str = None,
    parameter74_value: str = None,
    parameter75_name: str = None,
    parameter75_value: str = None,
    parameter76_name: str = None,
    parameter76_value: str = None,
    parameter77_name: str = None,
    parameter77_value: str = None,
    parameter78_name: str = None,
    parameter78_value: str = None,
    parameter79_name: str = None,
    parameter79_value: str = None,
    parameter8_name: str = None,
    parameter8_value: str = None,
    parameter80_name: str = None,
    parameter80_value: str = None,
    parameter81_name: str = None,
    parameter81_value: str = None,
    parameter82_name: str = None,
    parameter82_value: str = None,
    parameter83_name: str = None,
    parameter83_value: str = None,
    parameter84_name: str = None,
    parameter84_value: str = None,
    parameter85_name: str = None,
    parameter85_value: str = None,
    parameter86_name: str = None,
    parameter86_value: str = None,
    parameter87_name: str = None,
    parameter87_value: str = None,
    parameter88_name: str = None,
    parameter88_value: str = None,
    parameter89_name: str = None,
    parameter89_value: str = None,
    parameter9_name: str = None,
    parameter9_value: str = None,
    parameter90_name: str = None,
    parameter90_value: str = None,
    parameter91_name: str = None,
    parameter91_value: str = None,
    parameter92_name: str = None,
    parameter92_value: str = None,
    parameter93_name: str = None,
    parameter93_value: str = None,
    parameter94_name: str = None,
    parameter94_value: str = None,
    parameter95_name: str = None,
    parameter95_value: str = None,
    parameter96_name: str = None,
    parameter96_value: str = None,
    parameter97_name: str = None,
    parameter97_value: str = None,
    parameter98_name: str = None,
    parameter98_value: str = None,
    parameter99_name: str = None,
    parameter99_value: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    track: str = None,
) -> Dict[str, Any]:
    """
    Create a Siprec.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        connector_name:
            Unique name used when configuring the connector via Marketplace Add-on.
        name:
            The user-specified name of this Siprec, if one was given when the Siprec
            was created. This may be used to stop the Siprec.
        parameter1_name:
            Parameter name.
        parameter1_value:
            Parameter value.
        parameter10_name:
            Parameter name.
        parameter10_value:
            Parameter value.
        parameter11_name:
            Parameter name.
        parameter11_value:
            Parameter value.
        parameter12_name:
            Parameter name.
        parameter12_value:
            Parameter value.
        parameter13_name:
            Parameter name.
        parameter13_value:
            Parameter value.
        parameter14_name:
            Parameter name.
        parameter14_value:
            Parameter value.
        parameter15_name:
            Parameter name.
        parameter15_value:
            Parameter value.
        parameter16_name:
            Parameter name.
        parameter16_value:
            Parameter value.
        parameter17_name:
            Parameter name.
        parameter17_value:
            Parameter value.
        parameter18_name:
            Parameter name.
        parameter18_value:
            Parameter value.
        parameter19_name:
            Parameter name.
        parameter19_value:
            Parameter value.
        parameter2_name:
            Parameter name.
        parameter2_value:
            Parameter value.
        parameter20_name:
            Parameter name.
        parameter20_value:
            Parameter value.
        parameter21_name:
            Parameter name.
        parameter21_value:
            Parameter value.
        parameter22_name:
            Parameter name.
        parameter22_value:
            Parameter value.
        parameter23_name:
            Parameter name.
        parameter23_value:
            Parameter value.
        parameter24_name:
            Parameter name.
        parameter24_value:
            Parameter value.
        parameter25_name:
            Parameter name.
        parameter25_value:
            Parameter value.
        parameter26_name:
            Parameter name.
        parameter26_value:
            Parameter value.
        parameter27_name:
            Parameter name.
        parameter27_value:
            Parameter value.
        parameter28_name:
            Parameter name.
        parameter28_value:
            Parameter value.
        parameter29_name:
            Parameter name.
        parameter29_value:
            Parameter value.
        parameter3_name:
            Parameter name.
        parameter3_value:
            Parameter value.
        parameter30_name:
            Parameter name.
        parameter30_value:
            Parameter value.
        parameter31_name:
            Parameter name.
        parameter31_value:
            Parameter value.
        parameter32_name:
            Parameter name.
        parameter32_value:
            Parameter value.
        parameter33_name:
            Parameter name.
        parameter33_value:
            Parameter value.
        parameter34_name:
            Parameter name.
        parameter34_value:
            Parameter value.
        parameter35_name:
            Parameter name.
        parameter35_value:
            Parameter value.
        parameter36_name:
            Parameter name.
        parameter36_value:
            Parameter value.
        parameter37_name:
            Parameter name.
        parameter37_value:
            Parameter value.
        parameter38_name:
            Parameter name.
        parameter38_value:
            Parameter value.
        parameter39_name:
            Parameter name.
        parameter39_value:
            Parameter value.
        parameter4_name:
            Parameter name.
        parameter4_value:
            Parameter value.
        parameter40_name:
            Parameter name.
        parameter40_value:
            Parameter value.
        parameter41_name:
            Parameter name.
        parameter41_value:
            Parameter value.
        parameter42_name:
            Parameter name.
        parameter42_value:
            Parameter value.
        parameter43_name:
            Parameter name.
        parameter43_value:
            Parameter value.
        parameter44_name:
            Parameter name.
        parameter44_value:
            Parameter value.
        parameter45_name:
            Parameter name.
        parameter45_value:
            Parameter value.
        parameter46_name:
            Parameter name.
        parameter46_value:
            Parameter value.
        parameter47_name:
            Parameter name.
        parameter47_value:
            Parameter value.
        parameter48_name:
            Parameter name.
        parameter48_value:
            Parameter value.
        parameter49_name:
            Parameter name.
        parameter49_value:
            Parameter value.
        parameter5_name:
            Parameter name.
        parameter5_value:
            Parameter value.
        parameter50_name:
            Parameter name.
        parameter50_value:
            Parameter value.
        parameter51_name:
            Parameter name.
        parameter51_value:
            Parameter value.
        parameter52_name:
            Parameter name.
        parameter52_value:
            Parameter value.
        parameter53_name:
            Parameter name.
        parameter53_value:
            Parameter value.
        parameter54_name:
            Parameter name.
        parameter54_value:
            Parameter value.
        parameter55_name:
            Parameter name.
        parameter55_value:
            Parameter value.
        parameter56_name:
            Parameter name.
        parameter56_value:
            Parameter value.
        parameter57_name:
            Parameter name.
        parameter57_value:
            Parameter value.
        parameter58_name:
            Parameter name.
        parameter58_value:
            Parameter value.
        parameter59_name:
            Parameter name.
        parameter59_value:
            Parameter value.
        parameter6_name:
            Parameter name.
        parameter6_value:
            Parameter value.
        parameter60_name:
            Parameter name.
        parameter60_value:
            Parameter value.
        parameter61_name:
            Parameter name.
        parameter61_value:
            Parameter value.
        parameter62_name:
            Parameter name.
        parameter62_value:
            Parameter value.
        parameter63_name:
            Parameter name.
        parameter63_value:
            Parameter value.
        parameter64_name:
            Parameter name.
        parameter64_value:
            Parameter value.
        parameter65_name:
            Parameter name.
        parameter65_value:
            Parameter value.
        parameter66_name:
            Parameter name.
        parameter66_value:
            Parameter value.
        parameter67_name:
            Parameter name.
        parameter67_value:
            Parameter value.
        parameter68_name:
            Parameter name.
        parameter68_value:
            Parameter value.
        parameter69_name:
            Parameter name.
        parameter69_value:
            Parameter value.
        parameter7_name:
            Parameter name.
        parameter7_value:
            Parameter value.
        parameter70_name:
            Parameter name.
        parameter70_value:
            Parameter value.
        parameter71_name:
            Parameter name.
        parameter71_value:
            Parameter value.
        parameter72_name:
            Parameter name.
        parameter72_value:
            Parameter value.
        parameter73_name:
            Parameter name.
        parameter73_value:
            Parameter value.
        parameter74_name:
            Parameter name.
        parameter74_value:
            Parameter value.
        parameter75_name:
            Parameter name.
        parameter75_value:
            Parameter value.
        parameter76_name:
            Parameter name.
        parameter76_value:
            Parameter value.
        parameter77_name:
            Parameter name.
        parameter77_value:
            Parameter value.
        parameter78_name:
            Parameter name.
        parameter78_value:
            Parameter value.
        parameter79_name:
            Parameter name.
        parameter79_value:
            Parameter value.
        parameter8_name:
            Parameter name.
        parameter8_value:
            Parameter value.
        parameter80_name:
            Parameter name.
        parameter80_value:
            Parameter value.
        parameter81_name:
            Parameter name.
        parameter81_value:
            Parameter value.
        parameter82_name:
            Parameter name.
        parameter82_value:
            Parameter value.
        parameter83_name:
            Parameter name.
        parameter83_value:
            Parameter value.
        parameter84_name:
            Parameter name.
        parameter84_value:
            Parameter value.
        parameter85_name:
            Parameter name.
        parameter85_value:
            Parameter value.
        parameter86_name:
            Parameter name.
        parameter86_value:
            Parameter value.
        parameter87_name:
            Parameter name.
        parameter87_value:
            Parameter value.
        parameter88_name:
            Parameter name.
        parameter88_value:
            Parameter value.
        parameter89_name:
            Parameter name.
        parameter89_value:
            Parameter value.
        parameter9_name:
            Parameter name.
        parameter9_value:
            Parameter value.
        parameter90_name:
            Parameter name.
        parameter90_value:
            Parameter value.
        parameter91_name:
            Parameter name.
        parameter91_value:
            Parameter value.
        parameter92_name:
            Parameter name.
        parameter92_value:
            Parameter value.
        parameter93_name:
            Parameter name.
        parameter93_value:
            Parameter value.
        parameter94_name:
            Parameter name.
        parameter94_value:
            Parameter value.
        parameter95_name:
            Parameter name.
        parameter95_value:
            Parameter value.
        parameter96_name:
            Parameter name.
        parameter96_value:
            Parameter value.
        parameter97_name:
            Parameter name.
        parameter97_value:
            Parameter value.
        parameter98_name:
            Parameter name.
        parameter98_value:
            Parameter value.
        parameter99_name:
            Parameter name.
        parameter99_value:
            Parameter value.
        status_callback:
            Absolute URL of the status callback.
        status_callback_method:
            The http method for the status_callback (one of GET, POST).
        track:
            One of `inbound_track`, `outbound_track`, `both_tracks`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Siprec.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Siprec.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Siprec.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "connector_name": connector_name,
        "name": name,
        "parameter1_name": parameter1_name,
        "parameter1_value": parameter1_value,
        "parameter10_name": parameter10_name,
        "parameter10_value": parameter10_value,
        "parameter11_name": parameter11_name,
        "parameter11_value": parameter11_value,
        "parameter12_name": parameter12_name,
        "parameter12_value": parameter12_value,
        "parameter13_name": parameter13_name,
        "parameter13_value": parameter13_value,
        "parameter14_name": parameter14_name,
        "parameter14_value": parameter14_value,
        "parameter15_name": parameter15_name,
        "parameter15_value": parameter15_value,
        "parameter16_name": parameter16_name,
        "parameter16_value": parameter16_value,
        "parameter17_name": parameter17_name,
        "parameter17_value": parameter17_value,
        "parameter18_name": parameter18_name,
        "parameter18_value": parameter18_value,
        "parameter19_name": parameter19_name,
        "parameter19_value": parameter19_value,
        "parameter2_name": parameter2_name,
        "parameter2_value": parameter2_value,
        "parameter20_name": parameter20_name,
        "parameter20_value": parameter20_value,
        "parameter21_name": parameter21_name,
        "parameter21_value": parameter21_value,
        "parameter22_name": parameter22_name,
        "parameter22_value": parameter22_value,
        "parameter23_name": parameter23_name,
        "parameter23_value": parameter23_value,
        "parameter24_name": parameter24_name,
        "parameter24_value": parameter24_value,
        "parameter25_name": parameter25_name,
        "parameter25_value": parameter25_value,
        "parameter26_name": parameter26_name,
        "parameter26_value": parameter26_value,
        "parameter27_name": parameter27_name,
        "parameter27_value": parameter27_value,
        "parameter28_name": parameter28_name,
        "parameter28_value": parameter28_value,
        "parameter29_name": parameter29_name,
        "parameter29_value": parameter29_value,
        "parameter3_name": parameter3_name,
        "parameter3_value": parameter3_value,
        "parameter30_name": parameter30_name,
        "parameter30_value": parameter30_value,
        "parameter31_name": parameter31_name,
        "parameter31_value": parameter31_value,
        "parameter32_name": parameter32_name,
        "parameter32_value": parameter32_value,
        "parameter33_name": parameter33_name,
        "parameter33_value": parameter33_value,
        "parameter34_name": parameter34_name,
        "parameter34_value": parameter34_value,
        "parameter35_name": parameter35_name,
        "parameter35_value": parameter35_value,
        "parameter36_name": parameter36_name,
        "parameter36_value": parameter36_value,
        "parameter37_name": parameter37_name,
        "parameter37_value": parameter37_value,
        "parameter38_name": parameter38_name,
        "parameter38_value": parameter38_value,
        "parameter39_name": parameter39_name,
        "parameter39_value": parameter39_value,
        "parameter4_name": parameter4_name,
        "parameter4_value": parameter4_value,
        "parameter40_name": parameter40_name,
        "parameter40_value": parameter40_value,
        "parameter41_name": parameter41_name,
        "parameter41_value": parameter41_value,
        "parameter42_name": parameter42_name,
        "parameter42_value": parameter42_value,
        "parameter43_name": parameter43_name,
        "parameter43_value": parameter43_value,
        "parameter44_name": parameter44_name,
        "parameter44_value": parameter44_value,
        "parameter45_name": parameter45_name,
        "parameter45_value": parameter45_value,
        "parameter46_name": parameter46_name,
        "parameter46_value": parameter46_value,
        "parameter47_name": parameter47_name,
        "parameter47_value": parameter47_value,
        "parameter48_name": parameter48_name,
        "parameter48_value": parameter48_value,
        "parameter49_name": parameter49_name,
        "parameter49_value": parameter49_value,
        "parameter5_name": parameter5_name,
        "parameter5_value": parameter5_value,
        "parameter50_name": parameter50_name,
        "parameter50_value": parameter50_value,
        "parameter51_name": parameter51_name,
        "parameter51_value": parameter51_value,
        "parameter52_name": parameter52_name,
        "parameter52_value": parameter52_value,
        "parameter53_name": parameter53_name,
        "parameter53_value": parameter53_value,
        "parameter54_name": parameter54_name,
        "parameter54_value": parameter54_value,
        "parameter55_name": parameter55_name,
        "parameter55_value": parameter55_value,
        "parameter56_name": parameter56_name,
        "parameter56_value": parameter56_value,
        "parameter57_name": parameter57_name,
        "parameter57_value": parameter57_value,
        "parameter58_name": parameter58_name,
        "parameter58_value": parameter58_value,
        "parameter59_name": parameter59_name,
        "parameter59_value": parameter59_value,
        "parameter6_name": parameter6_name,
        "parameter6_value": parameter6_value,
        "parameter60_name": parameter60_name,
        "parameter60_value": parameter60_value,
        "parameter61_name": parameter61_name,
        "parameter61_value": parameter61_value,
        "parameter62_name": parameter62_name,
        "parameter62_value": parameter62_value,
        "parameter63_name": parameter63_name,
        "parameter63_value": parameter63_value,
        "parameter64_name": parameter64_name,
        "parameter64_value": parameter64_value,
        "parameter65_name": parameter65_name,
        "parameter65_value": parameter65_value,
        "parameter66_name": parameter66_name,
        "parameter66_value": parameter66_value,
        "parameter67_name": parameter67_name,
        "parameter67_value": parameter67_value,
        "parameter68_name": parameter68_name,
        "parameter68_value": parameter68_value,
        "parameter69_name": parameter69_name,
        "parameter69_value": parameter69_value,
        "parameter7_name": parameter7_name,
        "parameter7_value": parameter7_value,
        "parameter70_name": parameter70_name,
        "parameter70_value": parameter70_value,
        "parameter71_name": parameter71_name,
        "parameter71_value": parameter71_value,
        "parameter72_name": parameter72_name,
        "parameter72_value": parameter72_value,
        "parameter73_name": parameter73_name,
        "parameter73_value": parameter73_value,
        "parameter74_name": parameter74_name,
        "parameter74_value": parameter74_value,
        "parameter75_name": parameter75_name,
        "parameter75_value": parameter75_value,
        "parameter76_name": parameter76_name,
        "parameter76_value": parameter76_value,
        "parameter77_name": parameter77_name,
        "parameter77_value": parameter77_value,
        "parameter78_name": parameter78_name,
        "parameter78_value": parameter78_value,
        "parameter79_name": parameter79_name,
        "parameter79_value": parameter79_value,
        "parameter8_name": parameter8_name,
        "parameter8_value": parameter8_value,
        "parameter80_name": parameter80_name,
        "parameter80_value": parameter80_value,
        "parameter81_name": parameter81_name,
        "parameter81_value": parameter81_value,
        "parameter82_name": parameter82_name,
        "parameter82_value": parameter82_value,
        "parameter83_name": parameter83_name,
        "parameter83_value": parameter83_value,
        "parameter84_name": parameter84_name,
        "parameter84_value": parameter84_value,
        "parameter85_name": parameter85_name,
        "parameter85_value": parameter85_value,
        "parameter86_name": parameter86_name,
        "parameter86_value": parameter86_value,
        "parameter87_name": parameter87_name,
        "parameter87_value": parameter87_value,
        "parameter88_name": parameter88_name,
        "parameter88_value": parameter88_value,
        "parameter89_name": parameter89_name,
        "parameter89_value": parameter89_value,
        "parameter9_name": parameter9_name,
        "parameter9_value": parameter9_value,
        "parameter90_name": parameter90_name,
        "parameter90_value": parameter90_value,
        "parameter91_name": parameter91_name,
        "parameter91_value": parameter91_value,
        "parameter92_name": parameter92_name,
        "parameter92_value": parameter92_value,
        "parameter93_name": parameter93_name,
        "parameter93_value": parameter93_value,
        "parameter94_name": parameter94_name,
        "parameter94_value": parameter94_value,
        "parameter95_name": parameter95_name,
        "parameter95_value": parameter95_value,
        "parameter96_name": parameter96_name,
        "parameter96_value": parameter96_value,
        "parameter97_name": parameter97_name,
        "parameter97_value": parameter97_value,
        "parameter98_name": parameter98_name,
        "parameter98_value": parameter98_value,
        "parameter99_name": parameter99_name,
        "parameter99_value": parameter99_value,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "track": track,
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
async def post_2010_04_01_accounts_account_sid_calls_call_sid_siprec_sid_json(
    account_sid: str,
    call_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Stop a Siprec using either the SID of the Siprec resource or the `name` used
    when creating the resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The status. Must have the value `stopped`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Siprec/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Siprec/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Siprec/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_calls_call_sid_streams_json(
    account_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    name: str = None,
    parameter1_name: str = None,
    parameter1_value: str = None,
    parameter10_name: str = None,
    parameter10_value: str = None,
    parameter11_name: str = None,
    parameter11_value: str = None,
    parameter12_name: str = None,
    parameter12_value: str = None,
    parameter13_name: str = None,
    parameter13_value: str = None,
    parameter14_name: str = None,
    parameter14_value: str = None,
    parameter15_name: str = None,
    parameter15_value: str = None,
    parameter16_name: str = None,
    parameter16_value: str = None,
    parameter17_name: str = None,
    parameter17_value: str = None,
    parameter18_name: str = None,
    parameter18_value: str = None,
    parameter19_name: str = None,
    parameter19_value: str = None,
    parameter2_name: str = None,
    parameter2_value: str = None,
    parameter20_name: str = None,
    parameter20_value: str = None,
    parameter21_name: str = None,
    parameter21_value: str = None,
    parameter22_name: str = None,
    parameter22_value: str = None,
    parameter23_name: str = None,
    parameter23_value: str = None,
    parameter24_name: str = None,
    parameter24_value: str = None,
    parameter25_name: str = None,
    parameter25_value: str = None,
    parameter26_name: str = None,
    parameter26_value: str = None,
    parameter27_name: str = None,
    parameter27_value: str = None,
    parameter28_name: str = None,
    parameter28_value: str = None,
    parameter29_name: str = None,
    parameter29_value: str = None,
    parameter3_name: str = None,
    parameter3_value: str = None,
    parameter30_name: str = None,
    parameter30_value: str = None,
    parameter31_name: str = None,
    parameter31_value: str = None,
    parameter32_name: str = None,
    parameter32_value: str = None,
    parameter33_name: str = None,
    parameter33_value: str = None,
    parameter34_name: str = None,
    parameter34_value: str = None,
    parameter35_name: str = None,
    parameter35_value: str = None,
    parameter36_name: str = None,
    parameter36_value: str = None,
    parameter37_name: str = None,
    parameter37_value: str = None,
    parameter38_name: str = None,
    parameter38_value: str = None,
    parameter39_name: str = None,
    parameter39_value: str = None,
    parameter4_name: str = None,
    parameter4_value: str = None,
    parameter40_name: str = None,
    parameter40_value: str = None,
    parameter41_name: str = None,
    parameter41_value: str = None,
    parameter42_name: str = None,
    parameter42_value: str = None,
    parameter43_name: str = None,
    parameter43_value: str = None,
    parameter44_name: str = None,
    parameter44_value: str = None,
    parameter45_name: str = None,
    parameter45_value: str = None,
    parameter46_name: str = None,
    parameter46_value: str = None,
    parameter47_name: str = None,
    parameter47_value: str = None,
    parameter48_name: str = None,
    parameter48_value: str = None,
    parameter49_name: str = None,
    parameter49_value: str = None,
    parameter5_name: str = None,
    parameter5_value: str = None,
    parameter50_name: str = None,
    parameter50_value: str = None,
    parameter51_name: str = None,
    parameter51_value: str = None,
    parameter52_name: str = None,
    parameter52_value: str = None,
    parameter53_name: str = None,
    parameter53_value: str = None,
    parameter54_name: str = None,
    parameter54_value: str = None,
    parameter55_name: str = None,
    parameter55_value: str = None,
    parameter56_name: str = None,
    parameter56_value: str = None,
    parameter57_name: str = None,
    parameter57_value: str = None,
    parameter58_name: str = None,
    parameter58_value: str = None,
    parameter59_name: str = None,
    parameter59_value: str = None,
    parameter6_name: str = None,
    parameter6_value: str = None,
    parameter60_name: str = None,
    parameter60_value: str = None,
    parameter61_name: str = None,
    parameter61_value: str = None,
    parameter62_name: str = None,
    parameter62_value: str = None,
    parameter63_name: str = None,
    parameter63_value: str = None,
    parameter64_name: str = None,
    parameter64_value: str = None,
    parameter65_name: str = None,
    parameter65_value: str = None,
    parameter66_name: str = None,
    parameter66_value: str = None,
    parameter67_name: str = None,
    parameter67_value: str = None,
    parameter68_name: str = None,
    parameter68_value: str = None,
    parameter69_name: str = None,
    parameter69_value: str = None,
    parameter7_name: str = None,
    parameter7_value: str = None,
    parameter70_name: str = None,
    parameter70_value: str = None,
    parameter71_name: str = None,
    parameter71_value: str = None,
    parameter72_name: str = None,
    parameter72_value: str = None,
    parameter73_name: str = None,
    parameter73_value: str = None,
    parameter74_name: str = None,
    parameter74_value: str = None,
    parameter75_name: str = None,
    parameter75_value: str = None,
    parameter76_name: str = None,
    parameter76_value: str = None,
    parameter77_name: str = None,
    parameter77_value: str = None,
    parameter78_name: str = None,
    parameter78_value: str = None,
    parameter79_name: str = None,
    parameter79_value: str = None,
    parameter8_name: str = None,
    parameter8_value: str = None,
    parameter80_name: str = None,
    parameter80_value: str = None,
    parameter81_name: str = None,
    parameter81_value: str = None,
    parameter82_name: str = None,
    parameter82_value: str = None,
    parameter83_name: str = None,
    parameter83_value: str = None,
    parameter84_name: str = None,
    parameter84_value: str = None,
    parameter85_name: str = None,
    parameter85_value: str = None,
    parameter86_name: str = None,
    parameter86_value: str = None,
    parameter87_name: str = None,
    parameter87_value: str = None,
    parameter88_name: str = None,
    parameter88_value: str = None,
    parameter89_name: str = None,
    parameter89_value: str = None,
    parameter9_name: str = None,
    parameter9_value: str = None,
    parameter90_name: str = None,
    parameter90_value: str = None,
    parameter91_name: str = None,
    parameter91_value: str = None,
    parameter92_name: str = None,
    parameter92_value: str = None,
    parameter93_name: str = None,
    parameter93_value: str = None,
    parameter94_name: str = None,
    parameter94_value: str = None,
    parameter95_name: str = None,
    parameter95_value: str = None,
    parameter96_name: str = None,
    parameter96_value: str = None,
    parameter97_name: str = None,
    parameter97_value: str = None,
    parameter98_name: str = None,
    parameter98_value: str = None,
    parameter99_name: str = None,
    parameter99_value: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    track: str = None,
    url: str = None,
) -> Dict[str, Any]:
    """
    Create a Stream.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        name:
            The user-specified name of this Stream, if one was given when the Stream
            was created. This may be used to stop the Stream.
        parameter1_name:
            Parameter name.
        parameter1_value:
            Parameter value.
        parameter10_name:
            Parameter name.
        parameter10_value:
            Parameter value.
        parameter11_name:
            Parameter name.
        parameter11_value:
            Parameter value.
        parameter12_name:
            Parameter name.
        parameter12_value:
            Parameter value.
        parameter13_name:
            Parameter name.
        parameter13_value:
            Parameter value.
        parameter14_name:
            Parameter name.
        parameter14_value:
            Parameter value.
        parameter15_name:
            Parameter name.
        parameter15_value:
            Parameter value.
        parameter16_name:
            Parameter name.
        parameter16_value:
            Parameter value.
        parameter17_name:
            Parameter name.
        parameter17_value:
            Parameter value.
        parameter18_name:
            Parameter name.
        parameter18_value:
            Parameter value.
        parameter19_name:
            Parameter name.
        parameter19_value:
            Parameter value.
        parameter2_name:
            Parameter name.
        parameter2_value:
            Parameter value.
        parameter20_name:
            Parameter name.
        parameter20_value:
            Parameter value.
        parameter21_name:
            Parameter name.
        parameter21_value:
            Parameter value.
        parameter22_name:
            Parameter name.
        parameter22_value:
            Parameter value.
        parameter23_name:
            Parameter name.
        parameter23_value:
            Parameter value.
        parameter24_name:
            Parameter name.
        parameter24_value:
            Parameter value.
        parameter25_name:
            Parameter name.
        parameter25_value:
            Parameter value.
        parameter26_name:
            Parameter name.
        parameter26_value:
            Parameter value.
        parameter27_name:
            Parameter name.
        parameter27_value:
            Parameter value.
        parameter28_name:
            Parameter name.
        parameter28_value:
            Parameter value.
        parameter29_name:
            Parameter name.
        parameter29_value:
            Parameter value.
        parameter3_name:
            Parameter name.
        parameter3_value:
            Parameter value.
        parameter30_name:
            Parameter name.
        parameter30_value:
            Parameter value.
        parameter31_name:
            Parameter name.
        parameter31_value:
            Parameter value.
        parameter32_name:
            Parameter name.
        parameter32_value:
            Parameter value.
        parameter33_name:
            Parameter name.
        parameter33_value:
            Parameter value.
        parameter34_name:
            Parameter name.
        parameter34_value:
            Parameter value.
        parameter35_name:
            Parameter name.
        parameter35_value:
            Parameter value.
        parameter36_name:
            Parameter name.
        parameter36_value:
            Parameter value.
        parameter37_name:
            Parameter name.
        parameter37_value:
            Parameter value.
        parameter38_name:
            Parameter name.
        parameter38_value:
            Parameter value.
        parameter39_name:
            Parameter name.
        parameter39_value:
            Parameter value.
        parameter4_name:
            Parameter name.
        parameter4_value:
            Parameter value.
        parameter40_name:
            Parameter name.
        parameter40_value:
            Parameter value.
        parameter41_name:
            Parameter name.
        parameter41_value:
            Parameter value.
        parameter42_name:
            Parameter name.
        parameter42_value:
            Parameter value.
        parameter43_name:
            Parameter name.
        parameter43_value:
            Parameter value.
        parameter44_name:
            Parameter name.
        parameter44_value:
            Parameter value.
        parameter45_name:
            Parameter name.
        parameter45_value:
            Parameter value.
        parameter46_name:
            Parameter name.
        parameter46_value:
            Parameter value.
        parameter47_name:
            Parameter name.
        parameter47_value:
            Parameter value.
        parameter48_name:
            Parameter name.
        parameter48_value:
            Parameter value.
        parameter49_name:
            Parameter name.
        parameter49_value:
            Parameter value.
        parameter5_name:
            Parameter name.
        parameter5_value:
            Parameter value.
        parameter50_name:
            Parameter name.
        parameter50_value:
            Parameter value.
        parameter51_name:
            Parameter name.
        parameter51_value:
            Parameter value.
        parameter52_name:
            Parameter name.
        parameter52_value:
            Parameter value.
        parameter53_name:
            Parameter name.
        parameter53_value:
            Parameter value.
        parameter54_name:
            Parameter name.
        parameter54_value:
            Parameter value.
        parameter55_name:
            Parameter name.
        parameter55_value:
            Parameter value.
        parameter56_name:
            Parameter name.
        parameter56_value:
            Parameter value.
        parameter57_name:
            Parameter name.
        parameter57_value:
            Parameter value.
        parameter58_name:
            Parameter name.
        parameter58_value:
            Parameter value.
        parameter59_name:
            Parameter name.
        parameter59_value:
            Parameter value.
        parameter6_name:
            Parameter name.
        parameter6_value:
            Parameter value.
        parameter60_name:
            Parameter name.
        parameter60_value:
            Parameter value.
        parameter61_name:
            Parameter name.
        parameter61_value:
            Parameter value.
        parameter62_name:
            Parameter name.
        parameter62_value:
            Parameter value.
        parameter63_name:
            Parameter name.
        parameter63_value:
            Parameter value.
        parameter64_name:
            Parameter name.
        parameter64_value:
            Parameter value.
        parameter65_name:
            Parameter name.
        parameter65_value:
            Parameter value.
        parameter66_name:
            Parameter name.
        parameter66_value:
            Parameter value.
        parameter67_name:
            Parameter name.
        parameter67_value:
            Parameter value.
        parameter68_name:
            Parameter name.
        parameter68_value:
            Parameter value.
        parameter69_name:
            Parameter name.
        parameter69_value:
            Parameter value.
        parameter7_name:
            Parameter name.
        parameter7_value:
            Parameter value.
        parameter70_name:
            Parameter name.
        parameter70_value:
            Parameter value.
        parameter71_name:
            Parameter name.
        parameter71_value:
            Parameter value.
        parameter72_name:
            Parameter name.
        parameter72_value:
            Parameter value.
        parameter73_name:
            Parameter name.
        parameter73_value:
            Parameter value.
        parameter74_name:
            Parameter name.
        parameter74_value:
            Parameter value.
        parameter75_name:
            Parameter name.
        parameter75_value:
            Parameter value.
        parameter76_name:
            Parameter name.
        parameter76_value:
            Parameter value.
        parameter77_name:
            Parameter name.
        parameter77_value:
            Parameter value.
        parameter78_name:
            Parameter name.
        parameter78_value:
            Parameter value.
        parameter79_name:
            Parameter name.
        parameter79_value:
            Parameter value.
        parameter8_name:
            Parameter name.
        parameter8_value:
            Parameter value.
        parameter80_name:
            Parameter name.
        parameter80_value:
            Parameter value.
        parameter81_name:
            Parameter name.
        parameter81_value:
            Parameter value.
        parameter82_name:
            Parameter name.
        parameter82_value:
            Parameter value.
        parameter83_name:
            Parameter name.
        parameter83_value:
            Parameter value.
        parameter84_name:
            Parameter name.
        parameter84_value:
            Parameter value.
        parameter85_name:
            Parameter name.
        parameter85_value:
            Parameter value.
        parameter86_name:
            Parameter name.
        parameter86_value:
            Parameter value.
        parameter87_name:
            Parameter name.
        parameter87_value:
            Parameter value.
        parameter88_name:
            Parameter name.
        parameter88_value:
            Parameter value.
        parameter89_name:
            Parameter name.
        parameter89_value:
            Parameter value.
        parameter9_name:
            Parameter name.
        parameter9_value:
            Parameter value.
        parameter90_name:
            Parameter name.
        parameter90_value:
            Parameter value.
        parameter91_name:
            Parameter name.
        parameter91_value:
            Parameter value.
        parameter92_name:
            Parameter name.
        parameter92_value:
            Parameter value.
        parameter93_name:
            Parameter name.
        parameter93_value:
            Parameter value.
        parameter94_name:
            Parameter name.
        parameter94_value:
            Parameter value.
        parameter95_name:
            Parameter name.
        parameter95_value:
            Parameter value.
        parameter96_name:
            Parameter name.
        parameter96_value:
            Parameter value.
        parameter97_name:
            Parameter name.
        parameter97_value:
            Parameter value.
        parameter98_name:
            Parameter name.
        parameter98_value:
            Parameter value.
        parameter99_name:
            Parameter name.
        parameter99_value:
            Parameter value.
        status_callback:
            Absolute URL of the status callback.
        status_callback_method:
            The http method for the status_callback (one of GET, POST).
        track:
            One of `inbound_track`, `outbound_track`, `both_tracks`.
        url:
            Relative or absolute url where WebSocket connection will be established.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Streams.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Streams.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Streams.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "name": name,
        "parameter1_name": parameter1_name,
        "parameter1_value": parameter1_value,
        "parameter10_name": parameter10_name,
        "parameter10_value": parameter10_value,
        "parameter11_name": parameter11_name,
        "parameter11_value": parameter11_value,
        "parameter12_name": parameter12_name,
        "parameter12_value": parameter12_value,
        "parameter13_name": parameter13_name,
        "parameter13_value": parameter13_value,
        "parameter14_name": parameter14_name,
        "parameter14_value": parameter14_value,
        "parameter15_name": parameter15_name,
        "parameter15_value": parameter15_value,
        "parameter16_name": parameter16_name,
        "parameter16_value": parameter16_value,
        "parameter17_name": parameter17_name,
        "parameter17_value": parameter17_value,
        "parameter18_name": parameter18_name,
        "parameter18_value": parameter18_value,
        "parameter19_name": parameter19_name,
        "parameter19_value": parameter19_value,
        "parameter2_name": parameter2_name,
        "parameter2_value": parameter2_value,
        "parameter20_name": parameter20_name,
        "parameter20_value": parameter20_value,
        "parameter21_name": parameter21_name,
        "parameter21_value": parameter21_value,
        "parameter22_name": parameter22_name,
        "parameter22_value": parameter22_value,
        "parameter23_name": parameter23_name,
        "parameter23_value": parameter23_value,
        "parameter24_name": parameter24_name,
        "parameter24_value": parameter24_value,
        "parameter25_name": parameter25_name,
        "parameter25_value": parameter25_value,
        "parameter26_name": parameter26_name,
        "parameter26_value": parameter26_value,
        "parameter27_name": parameter27_name,
        "parameter27_value": parameter27_value,
        "parameter28_name": parameter28_name,
        "parameter28_value": parameter28_value,
        "parameter29_name": parameter29_name,
        "parameter29_value": parameter29_value,
        "parameter3_name": parameter3_name,
        "parameter3_value": parameter3_value,
        "parameter30_name": parameter30_name,
        "parameter30_value": parameter30_value,
        "parameter31_name": parameter31_name,
        "parameter31_value": parameter31_value,
        "parameter32_name": parameter32_name,
        "parameter32_value": parameter32_value,
        "parameter33_name": parameter33_name,
        "parameter33_value": parameter33_value,
        "parameter34_name": parameter34_name,
        "parameter34_value": parameter34_value,
        "parameter35_name": parameter35_name,
        "parameter35_value": parameter35_value,
        "parameter36_name": parameter36_name,
        "parameter36_value": parameter36_value,
        "parameter37_name": parameter37_name,
        "parameter37_value": parameter37_value,
        "parameter38_name": parameter38_name,
        "parameter38_value": parameter38_value,
        "parameter39_name": parameter39_name,
        "parameter39_value": parameter39_value,
        "parameter4_name": parameter4_name,
        "parameter4_value": parameter4_value,
        "parameter40_name": parameter40_name,
        "parameter40_value": parameter40_value,
        "parameter41_name": parameter41_name,
        "parameter41_value": parameter41_value,
        "parameter42_name": parameter42_name,
        "parameter42_value": parameter42_value,
        "parameter43_name": parameter43_name,
        "parameter43_value": parameter43_value,
        "parameter44_name": parameter44_name,
        "parameter44_value": parameter44_value,
        "parameter45_name": parameter45_name,
        "parameter45_value": parameter45_value,
        "parameter46_name": parameter46_name,
        "parameter46_value": parameter46_value,
        "parameter47_name": parameter47_name,
        "parameter47_value": parameter47_value,
        "parameter48_name": parameter48_name,
        "parameter48_value": parameter48_value,
        "parameter49_name": parameter49_name,
        "parameter49_value": parameter49_value,
        "parameter5_name": parameter5_name,
        "parameter5_value": parameter5_value,
        "parameter50_name": parameter50_name,
        "parameter50_value": parameter50_value,
        "parameter51_name": parameter51_name,
        "parameter51_value": parameter51_value,
        "parameter52_name": parameter52_name,
        "parameter52_value": parameter52_value,
        "parameter53_name": parameter53_name,
        "parameter53_value": parameter53_value,
        "parameter54_name": parameter54_name,
        "parameter54_value": parameter54_value,
        "parameter55_name": parameter55_name,
        "parameter55_value": parameter55_value,
        "parameter56_name": parameter56_name,
        "parameter56_value": parameter56_value,
        "parameter57_name": parameter57_name,
        "parameter57_value": parameter57_value,
        "parameter58_name": parameter58_name,
        "parameter58_value": parameter58_value,
        "parameter59_name": parameter59_name,
        "parameter59_value": parameter59_value,
        "parameter6_name": parameter6_name,
        "parameter6_value": parameter6_value,
        "parameter60_name": parameter60_name,
        "parameter60_value": parameter60_value,
        "parameter61_name": parameter61_name,
        "parameter61_value": parameter61_value,
        "parameter62_name": parameter62_name,
        "parameter62_value": parameter62_value,
        "parameter63_name": parameter63_name,
        "parameter63_value": parameter63_value,
        "parameter64_name": parameter64_name,
        "parameter64_value": parameter64_value,
        "parameter65_name": parameter65_name,
        "parameter65_value": parameter65_value,
        "parameter66_name": parameter66_name,
        "parameter66_value": parameter66_value,
        "parameter67_name": parameter67_name,
        "parameter67_value": parameter67_value,
        "parameter68_name": parameter68_name,
        "parameter68_value": parameter68_value,
        "parameter69_name": parameter69_name,
        "parameter69_value": parameter69_value,
        "parameter7_name": parameter7_name,
        "parameter7_value": parameter7_value,
        "parameter70_name": parameter70_name,
        "parameter70_value": parameter70_value,
        "parameter71_name": parameter71_name,
        "parameter71_value": parameter71_value,
        "parameter72_name": parameter72_name,
        "parameter72_value": parameter72_value,
        "parameter73_name": parameter73_name,
        "parameter73_value": parameter73_value,
        "parameter74_name": parameter74_name,
        "parameter74_value": parameter74_value,
        "parameter75_name": parameter75_name,
        "parameter75_value": parameter75_value,
        "parameter76_name": parameter76_name,
        "parameter76_value": parameter76_value,
        "parameter77_name": parameter77_name,
        "parameter77_value": parameter77_value,
        "parameter78_name": parameter78_name,
        "parameter78_value": parameter78_value,
        "parameter79_name": parameter79_name,
        "parameter79_value": parameter79_value,
        "parameter8_name": parameter8_name,
        "parameter8_value": parameter8_value,
        "parameter80_name": parameter80_name,
        "parameter80_value": parameter80_value,
        "parameter81_name": parameter81_name,
        "parameter81_value": parameter81_value,
        "parameter82_name": parameter82_name,
        "parameter82_value": parameter82_value,
        "parameter83_name": parameter83_name,
        "parameter83_value": parameter83_value,
        "parameter84_name": parameter84_name,
        "parameter84_value": parameter84_value,
        "parameter85_name": parameter85_name,
        "parameter85_value": parameter85_value,
        "parameter86_name": parameter86_name,
        "parameter86_value": parameter86_value,
        "parameter87_name": parameter87_name,
        "parameter87_value": parameter87_value,
        "parameter88_name": parameter88_name,
        "parameter88_value": parameter88_value,
        "parameter89_name": parameter89_name,
        "parameter89_value": parameter89_value,
        "parameter9_name": parameter9_name,
        "parameter9_value": parameter9_value,
        "parameter90_name": parameter90_name,
        "parameter90_value": parameter90_value,
        "parameter91_name": parameter91_name,
        "parameter91_value": parameter91_value,
        "parameter92_name": parameter92_name,
        "parameter92_value": parameter92_value,
        "parameter93_name": parameter93_name,
        "parameter93_value": parameter93_value,
        "parameter94_name": parameter94_name,
        "parameter94_value": parameter94_value,
        "parameter95_name": parameter95_name,
        "parameter95_value": parameter95_value,
        "parameter96_name": parameter96_name,
        "parameter96_value": parameter96_value,
        "parameter97_name": parameter97_name,
        "parameter97_value": parameter97_value,
        "parameter98_name": parameter98_name,
        "parameter98_value": parameter98_value,
        "parameter99_name": parameter99_name,
        "parameter99_value": parameter99_value,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "track": track,
        "url": url,
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
async def post_2010_04_01_accounts_account_sid_calls_call_sid_streams_sid_json(
    account_sid: str,
    call_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Stop a Stream using either the SID of the Stream resource or the `name` used
    when creating the resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The status. Must have the value `stopped`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Streams/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Streams/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Streams/{sid}.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_calls_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Call record from your account. Once the record is deleted, it will no
    longer appear in the API and Account Portal logs.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_calls_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the call specified by the provided Call SID.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_calls_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    fallback_method: str = None,
    fallback_url: str = None,
    method: str = None,
    status: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    time_limit: int = None,
    twiml: str = None,
    url: str = None,
) -> Dict[str, Any]:
    """
    Initiates a call redirect or terminates a call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        fallback_method:
            The HTTP method that we should use to request the `fallback_url`. Can
            be: `GET` or `POST` and the default is `POST`. If an
            `application_sid` parameter is present, this parameter is
            ignored.
        fallback_url:
            The URL that we call using the `fallback_method` if an error occurs when
            requesting or executing the TwiML at `url`. If an
            `application_sid` parameter is present, this parameter is
            ignored.
        method:
            The HTTP method we should use when calling the `url`. Can be: `GET` or
            `POST` and the default is `POST`. If an `application_sid`
            parameter is present, this parameter is ignored.
        status:
            The new status of the resource. Can be: `canceled` or `completed`.
            Specifying `canceled` will attempt to hang up calls that are
            queued or ringing; however, it will not affect calls already
            in progress. Specifying `completed` will attempt to hang up
            a call even if it's already in progress.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application. If no
            `status_callback_event` is specified, we will send the
            `completed` status. If an `application_sid` parameter is
            present, this parameter is ignored. URLs must contain a
            valid hostname (underscores are not permitted).
        status_callback_method:
            The HTTP method we should use when requesting the `status_callback` URL.
            Can be: `GET` or `POST` and the default is `POST`. If an
            `application_sid` parameter is present, this parameter is
            ignored.
        time_limit:
            The maximum duration of the call in seconds. Constraints depend on
            account and configuration.
        twiml:
            TwiML instructions for the call Twilio will use without fetching Twiml
            from url. Twiml and url parameters are mutually exclusive.
        url:
            The absolute URL that returns the TwiML instructions for the call. We
            will call this URL using the `method` when the call
            connects. For more information, see the [Url
            Parameter](https://www.twilio.com/docs/voice/make-calls
            specify-a-url-parameter) section in [Making
            Calls](https://www.twilio.com/docs/voice/make-calls).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "fallback_method": fallback_method,
        "fallback_url": fallback_url,
        "method": method,
        "status": status,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "time_limit": time_limit,
        "twiml": twiml,
        "url": url,
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
async def get_2010_04_01_accounts_account_sid_conferences_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    date_created: str = None,
    date_updated: str = None,
    friendly_name: str = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of conferences belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created:
            The `date_created` value, specified as `YYYY-MM-DD`, of the resources to
            read. To read conferences that started on or before midnight
            on a date, use `<=YYYY-MM-DD`, and to specify  conferences
            that started on or after midnight on a date, use `>=YYYY-MM-
            DD`.
        date_updated:
            The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to
            read. To read conferences that were last updated on or
            before midnight on a date, use `<=YYYY-MM-DD`, and to
            specify conferences that were last updated on or after
            midnight on a given date, use  `>=YYYY-MM-DD`.
        friendly_name:
            The string that identifies the Conference resources to read.
        status:
            The status of the resources to read. Can be: `init`, `in-progress`, or
            `completed`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences.json?&date_created=%s&date_created=%s&date_created=%s&date_updated=%s&date_updated=%s&date_updated=%s&friendly_name=%s&status=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences.json?&date_created=%s&date_created=%s&date_created=%s&date_updated=%s&date_updated=%s&date_updated=%s&friendly_name=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created": date_created,
        "date_created": date_created,
        "date_created": date_created,
        "date_updated": date_updated,
        "date_updated": date_updated,
        "date_updated": date_updated,
        "friendly_name": friendly_name,
        "status": status,
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
async def get_2010_04_01_accounts_account_sid_conferences_conference_sid_participants_json(
    account_sid: str,
    conference_sid: str,
    twilio_credentials: "TwilioCredentials",
    muted: bool = None,
    hold: bool = None,
    coaching: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of participants belonging to the account used to make the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        muted:
            Whether to return only participants that are muted. Can be: `true` or
            `false`.
        hold:
            Whether to return only participants that are on hold. Can be: `true` or
            `false`.
        coaching:
            Whether to return only participants who are coaching another call. Can
            be: `true` or `false`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json?&muted=%s&hold=%s&coaching=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json?&muted=%s&hold=%s&coaching=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "muted": muted,
        "hold": hold,
        "coaching": coaching,
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
async def post_2010_04_01_accounts_account_sid_conferences_conference_sid_participants_json(
    account_sid: str,
    conference_sid: str,
    twilio_credentials: "TwilioCredentials",
    beep: str = None,
    byoc: str = None,
    call_reason: str = None,
    call_sid_to_coach: str = None,
    caller_id: str = None,
    coaching: bool = None,
    conference_record: str = None,
    conference_recording_status_callback: str = None,
    conference_recording_status_callback_event: list = None,
    conference_recording_status_callback_method: str = None,
    conference_status_callback: str = None,
    conference_status_callback_event: list = None,
    conference_status_callback_method: str = None,
    conference_trim: str = None,
    early_media: bool = None,
    end_conference_on_exit: bool = None,
    from_: str = None,
    jitter_buffer_size: str = None,
    label: str = None,
    max_participants: int = None,
    muted: bool = None,
    record: bool = None,
    recording_channels: str = None,
    recording_status_callback: str = None,
    recording_status_callback_event: list = None,
    recording_status_callback_method: str = None,
    recording_track: str = None,
    region: str = None,
    sip_auth_password: str = None,
    sip_auth_username: str = None,
    start_conference_on_enter: bool = None,
    status_callback: str = None,
    status_callback_event: list = None,
    status_callback_method: str = None,
    time_limit: int = None,
    timeout: int = None,
    to: str = None,
    wait_method: str = None,
    wait_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        beep:
            Whether to play a notification beep to the conference when the
            participant joins. Can be: `true`, `false`, `onEnter`, or
            `onExit`. The default value is `true`.
        byoc:
            The SID of a BYOC (Bring Your Own Carrier) trunk to route this call
            with. Note that `byoc` is only meaningful when `to` is a
            phone number; it will otherwise be ignored. (Beta).
        call_reason:
            The Reason for the outgoing call. Use it to specify the purpose of the
            call that is presented on the called party's phone. (Branded
            Calls Beta).
        call_sid_to_coach:
            The SID of the participant who is being `coached`. The participant being
            coached is the only participant who can hear the participant
            who is `coaching`.
        caller_id:
            The phone number, Client identifier, or username portion of SIP address
            that made this call. Phone numbers are in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format (e.g., +16175551212). Client identifiers are
            formatted `client:name`. If using a phone number, it must be
            a Twilio number or a Verified [outgoing caller
            id](https://www.twilio.com/docs/voice/api/outgoing-caller-
            ids) for your account. If the `to` parameter is a phone
            number, `callerId` must also be a phone number. If `to` is
            sip address, this value of `callerId` should be a username
            portion to be used to populate the From header that is
            passed to the SIP endpoint.
        coaching:
            Whether the participant is coaching another call. Can be: `true` or
            `false`. If not present, defaults to `false` unless
            `call_sid_to_coach` is defined. If `true`,
            `call_sid_to_coach` must be defined.
        conference_record:
            Whether to record the conference the participant is joining. Can be:
            `true`, `false`, `record-from-start`, and `do-not-record`.
            The default value is `false`.
        conference_recording_status_callback:
            The URL we should call using the
            `conference_recording_status_callback_method` when the
            conference recording is available.
        conference_recording_status_callback_event:
            The conference recording state changes that generate a call to
            `conference_recording_status_callback`. Can be: `in-
            progress`, `completed`, `failed`, and `absent`. Separate
            multiple values with a space, ex: `'in-progress completed
            failed'`.
        conference_recording_status_callback_method:
            The HTTP method we should use to call
            `conference_recording_status_callback`. Can be: `GET` or
            `POST` and defaults to `POST`.
        conference_status_callback:
            The URL we should call using the `conference_status_callback_method`
            when the conference events in
            `conference_status_callback_event` occur. Only the value set
            by the first participant to join the conference is used.
            Subsequent `conference_status_callback` values are ignored.
        conference_status_callback_event:
            The conference state changes that should generate a call to
            `conference_status_callback`. Can be: `start`, `end`,
            `join`, `leave`, `mute`, `hold`, `modify`, `speaker`, and
            `announcement`. Separate multiple values with a space.
            Defaults to `start end`.
        conference_status_callback_method:
            The HTTP method we should use to call `conference_status_callback`. Can
            be: `GET` or `POST` and defaults to `POST`.
        conference_trim:
            Whether to trim leading and trailing silence from your recorded
            conference audio files. Can be: `trim-silence` or `do-not-
            trim` and defaults to `trim-silence`.
        early_media:
            Whether to allow an agent to hear the state of the outbound call,
            including ringing or disconnect messages. Can be: `true` or
            `false` and defaults to `true`.
        end_conference_on_exit:
            Whether to end the conference when the participant leaves. Can be:
            `true` or `false` and defaults to `false`.
        from_:
            The phone number, Client identifier, or username portion of SIP address
            that made this call. Phone numbers are in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format (e.g., +16175551212). Client identifiers are
            formatted `client:name`. If using a phone number, it must be
            a Twilio number or a Verified [outgoing caller
            id](https://www.twilio.com/docs/voice/api/outgoing-caller-
            ids) for your account. If the `to` parameter is a phone
            number, `from` must also be a phone number. If `to` is sip
            address, this value of `from` should be a username portion
            to be used to populate the P-Asserted-Identity header that
            is passed to the SIP endpoint.
        jitter_buffer_size:
            Jitter buffer size for the connecting participant. Twilio will use this
            setting to apply Jitter Buffer before participant's audio is
            mixed into the conference. Can be: `off`, `small`, `medium`,
            and `large`. Default to `large`.
        label:
            A label for this participant. If one is supplied, it may subsequently be
            used to fetch, update or delete the participant.
        max_participants:
            The maximum number of participants in the conference. Can be a positive
            integer from `2` to `250`. The default value is `250`.
        muted:
            Whether the agent is muted in the conference. Can be `true` or `false`
            and the default is `false`.
        record:
            Whether to record the participant and their conferences, including the
            time between conferences. Can be `true` or `false` and the
            default is `false`.
        recording_channels:
            The recording channels for the final recording. Can be: `mono` or `dual`
            and the default is `mono`.
        recording_status_callback:
            The URL that we should call using the `recording_status_callback_method`
            when the recording status changes.
        recording_status_callback_event:
            The recording state changes that should generate a call to
            `recording_status_callback`. Can be: `started`, `in-
            progress`, `paused`, `resumed`, `stopped`, `completed`,
            `failed`, and `absent`. Separate multiple values with a
            space, ex: `'in-progress completed failed'`.
        recording_status_callback_method:
            The HTTP method we should use when we call `recording_status_callback`.
            Can be: `GET` or `POST` and defaults to `POST`.
        recording_track:
            The audio track to record for the call. Can be: `inbound`, `outbound` or
            `both`. The default is `both`. `inbound` records the audio
            that is received by Twilio. `outbound` records the audio
            that is sent from Twilio. `both` records the audio that is
            received and sent by Twilio.
        region:
            The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-
            global-low-latency-routing-and-region-selection-work-for-
            conferences-and-Client-calls) where we should mix the
            recorded audio. Can be:`us1`, `ie1`, `de1`, `sg1`, `br1`,
            `au1`, or `jp1`.
        sip_auth_password:
            The SIP password for authentication.
        sip_auth_username:
            The SIP username used for authentication.
        start_conference_on_enter:
            Whether to start the conference when the participant joins, if it has
            not already started. Can be: `true` or `false` and the
            default is `true`. If `false` and the conference has not
            started, the participant is muted and hears background music
            until another participant starts the conference.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_event:
            The conference state changes that should generate a call to
            `status_callback`. Can be: `initiated`, `ringing`,
            `answered`, and `completed`. Separate multiple values with a
            space. The default value is `completed`.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `GET`
            and `POST` and defaults to `POST`.
        time_limit:
            The maximum duration of the call in seconds. Constraints depend on
            account and configuration.
        timeout:
            The number of seconds that we should allow the phone to ring before
            assuming there is no answer. Can be an integer between `5`
            and `600`, inclusive. The default value is `60`. We always
            add a 5-second timeout buffer to outgoing calls, so  value
            of 10 would result in an actual timeout that was closer to
            15 seconds.
        to:
            The phone number, SIP address, or Client identifier that received this
            call. Phone numbers are in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format (e.g., +16175551212). SIP addresses are formatted as
            `sip:name@company.com`. Client identifiers are formatted
            `client:name`. [Custom
            parameters](https://www.twilio.com/docs/voice/api/conference-
            participant-resource
            custom-parameters) may also be specified.
        wait_method:
            The HTTP method we should use to call `wait_url`. Can be `GET` or `POST`
            and the default is `POST`. When using a static audio file,
            this should be `GET` so that we can cache the file.
        wait_url:
            The URL we should call using the `wait_method` for the music to play
            while participants are waiting for the conference to start.
            The default value is the URL of our standard hold music.
            [Learn more about hold
            music](https://www.twilio.com/labs/twimlets/holdmusic).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "beep": beep,
        "byoc": byoc,
        "call_reason": call_reason,
        "call_sid_to_coach": call_sid_to_coach,
        "caller_id": caller_id,
        "coaching": coaching,
        "conference_record": conference_record,
        "conference_recording_status_callback": conference_recording_status_callback,  # noqa
        "conference_recording_status_callback_event": conference_recording_status_callback_event,  # noqa
        "conference_recording_status_callback_method": conference_recording_status_callback_method,  # noqa
        "conference_status_callback": conference_status_callback,
        "conference_status_callback_event": conference_status_callback_event,
        "conference_status_callback_method": conference_status_callback_method,
        "conference_trim": conference_trim,
        "early_media": early_media,
        "end_conference_on_exit": end_conference_on_exit,
        "from_": from_,
        "jitter_buffer_size": jitter_buffer_size,
        "label": label,
        "max_participants": max_participants,
        "muted": muted,
        "record": record,
        "recording_channels": recording_channels,
        "recording_status_callback": recording_status_callback,
        "recording_status_callback_event": recording_status_callback_event,
        "recording_status_callback_method": recording_status_callback_method,
        "recording_track": recording_track,
        "region": region,
        "sip_auth_password": sip_auth_password,
        "sip_auth_username": sip_auth_username,
        "start_conference_on_enter": start_conference_on_enter,
        "status_callback": status_callback,
        "status_callback_event": status_callback_event,
        "status_callback_method": status_callback_method,
        "time_limit": time_limit,
        "timeout": timeout,
        "to": to,
        "wait_method": wait_method,
        "wait_url": wait_url,
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
async def delete_2010_04_01_accounts_account_sid_conferences_conference_sid_participants_call_sid_json(
    account_sid: str,
    conference_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Kick a participant from a given conference.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_conferences_conference_sid_participants_call_sid_json(
    account_sid: str,
    conference_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a participant.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_conferences_conference_sid_participants_call_sid_json(
    account_sid: str,
    conference_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    announce_method: str = None,
    announce_url: str = None,
    beep_on_exit: bool = None,
    call_sid_to_coach: str = None,
    coaching: bool = None,
    end_conference_on_exit: bool = None,
    hold: bool = None,
    hold_method: str = None,
    hold_url: str = None,
    muted: bool = None,
    wait_method: str = None,
    wait_url: str = None,
) -> Dict[str, Any]:
    """
    Update the properties of the participant.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        announce_method:
            The HTTP method we should use to call `announce_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        announce_url:
            The URL we call using the `announce_method` for an announcement to the
            participant. The URL must return an MP3 file, a WAV file, or
            a TwiML document that contains `<Play>` or `<Say>` commands.
        beep_on_exit:
            Whether to play a notification beep to the conference when the
            participant exits. Can be: `true` or `false`.
        call_sid_to_coach:
            The SID of the participant who is being `coached`. The participant being
            coached is the only participant who can hear the participant
            who is `coaching`.
        coaching:
            Whether the participant is coaching another call. Can be: `true` or
            `false`. If not present, defaults to `false` unless
            `call_sid_to_coach` is defined. If `true`,
            `call_sid_to_coach` must be defined.
        end_conference_on_exit:
            Whether to end the conference when the participant leaves. Can be:
            `true` or `false` and defaults to `false`.
        hold:
            Whether the participant should be on hold. Can be: `true` or `false`.
            `true` puts the participant on hold, and `false` lets them
            rejoin the conference.
        hold_method:
            The HTTP method we should use to call `hold_url`. Can be: `GET` or
            `POST` and the default is `GET`.
        hold_url:
            The URL we call using the `hold_method` for  music that plays when the
            participant is on hold. The URL may return an MP3 file, a
            WAV file, or a TwiML document that contains the `<Play>`,
            `<Say>` or `<Redirect>` commands.
        muted:
            Whether the participant should be muted. Can be `true` or `false`.
            `true` will mute the participant, and `false` will un-mute
            them. Anything value other than `true` or `false` is
            interpreted as `false`.
        wait_method:
            The HTTP method we should use to call `wait_url`. Can be `GET` or `POST`
            and the default is `POST`. When using a static audio file,
            this should be `GET` so that we can cache the file.
        wait_url:
            The URL we should call using the `wait_method` for the music to play
            while participants are waiting for the conference to start.
            The default value is the URL of our standard hold music.
            [Learn more about hold
            music](https://www.twilio.com/labs/twimlets/holdmusic).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "announce_method": announce_method,
        "announce_url": announce_url,
        "beep_on_exit": beep_on_exit,
        "call_sid_to_coach": call_sid_to_coach,
        "coaching": coaching,
        "end_conference_on_exit": end_conference_on_exit,
        "hold": hold,
        "hold_method": hold_method,
        "hold_url": hold_url,
        "muted": muted,
        "wait_method": wait_method,
        "wait_url": wait_url,
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
async def get_2010_04_01_accounts_account_sid_conferences_conference_sid_recordings_json(
    account_sid: str,
    conference_sid: str,
    twilio_credentials: "TwilioCredentials",
    date_created: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of recordings belonging to the call used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created:
            The `date_created` value, specified as `YYYY-MM-DD`, of the resources to
            read. You can also specify inequality: `DateCreated<=YYYY-
            MM-DD` will return recordings generated at or before
            midnight on a given date, and `DateCreated>=YYYY-MM-DD`
            returns recordings generated at or after midnight on a date.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json?&date_created=%s&date_created=%s&date_created=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json?&date_created=%s&date_created=%s&date_created=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created": date_created,
        "date_created": date_created,
        "date_created": date_created,
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
async def delete_2010_04_01_accounts_account_sid_conferences_conference_sid_recordings_sid_json(
    account_sid: str,
    conference_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a recording from your account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_conferences_conference_sid_recordings_sid_json(
    account_sid: str,
    conference_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a recording for a call.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_conferences_conference_sid_recordings_sid_json(
    account_sid: str,
    conference_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    pause_behavior: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """
    Changes the status of the recording to paused, stopped, or in-progress. Note: To
    use `Twilio.CURRENT`, pass it as recording sid.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        conference_sid:
            Conference sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        pause_behavior:
            Whether to record during a pause. Can be: `skip` or `silence` and the
            default is `silence`. `skip` does not record during the
            pause period, while `silence` will replace the actual audio
            of the call with silence during the pause period. This
            parameter only applies when setting `status` is set to
            `paused`.
        status:
            The new status of the recording. Can be: `stopped`, `paused`, `in-
            progress`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "pause_behavior": pause_behavior,
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
async def get_2010_04_01_accounts_account_sid_conferences_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a conference.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_conferences_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    announce_method: str = None,
    announce_url: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        announce_method:
            The HTTP method used to call `announce_url`. Can be: `GET` or `POST` and
            the default is `POST`.
        announce_url:
            The URL we should call to announce something into the conference. The
            URL can return an MP3, a WAV, or a TwiML document with
            `<Play>` or `<Say>`.
        status:
            The new status of the resource. Can be:  Can be: `init`, `in-progress`,
            or `completed`. Specifying `completed` will end the
            conference and hang up all participants.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Conferences/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "announce_method": announce_method,
        "announce_url": announce_url,
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
async def get_2010_04_01_accounts_account_sid_connect_apps_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of connect-apps belonging to the account used to make the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_connect_apps_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete an instance of a connect-app.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_connect_apps_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a connect-app.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_connect_apps_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    authorize_redirect_url: str = None,
    company_name: str = None,
    deauthorize_callback_method: str = None,
    deauthorize_callback_url: str = None,
    description: str = None,
    friendly_name: str = None,
    homepage_url: str = None,
    permissions: list = None,
) -> Dict[str, Any]:
    """
    Update a connect-app with the specified parameters.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        authorize_redirect_url:
            The URL to redirect the user to after we authenticate the user and
            obtain authorization to access the Connect App.
        company_name:
            The company name to set for the Connect App.
        deauthorize_callback_method:
            The HTTP method to use when calling `deauthorize_callback_url`.
        deauthorize_callback_url:
            The URL to call using the `deauthorize_callback_method` to de-authorize
            the Connect App.
        description:
            A description of the Connect App.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        homepage_url:
            A public URL where users can obtain more information about this Connect
            App.
        permissions:
            A comma-separated list of the permissions you will request from the
            users of this ConnectApp.  Can include: `get-all` and `post-
            all`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "authorize_redirect_url": authorize_redirect_url,
        "company_name": company_name,
        "deauthorize_callback_method": deauthorize_callback_method,
        "deauthorize_callback_url": deauthorize_callback_url,
        "description": description,
        "friendly_name": friendly_name,
        "homepage_url": homepage_url,
        "permissions": permissions,
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
async def get_2010_04_01_accounts_account_sid_incoming_phone_numbers_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    beta: bool = None,
    friendly_name: str = None,
    phone_number: str = None,
    origin: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of incoming-phone-numbers belonging to the account used to make
    the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        beta:
            Whether to include phone numbers new to the Twilio platform. Can be:
            `true` or `false` and the default is `true`.
        friendly_name:
            A string that identifies the IncomingPhoneNumber resources to read.
        phone_number:
            The phone numbers of the IncomingPhoneNumber resources to read. You can
            specify partial numbers and use '*' as a wildcard for any
            digit.
        origin:
            Whether to include phone numbers based on their origin. Can be: `twilio`
            or `hosted`. By default, phone numbers of all origin are
            included.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers.json?&beta=%s&friendly_name=%s&phone_number=%s&origin=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers.json?&beta=%s&friendly_name=%s&phone_number=%s&origin=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "beta": beta,
        "friendly_name": friendly_name,
        "phone_number": phone_number,
        "origin": origin,
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
async def post_2010_04_01_accounts_account_sid_incoming_phone_numbers_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    address_sid: str = None,
    api_version: str = None,
    area_code: str = None,
    bundle_sid: str = None,
    emergency_address_sid: str = None,
    emergency_status: str = None,
    friendly_name: str = None,
    identity_sid: str = None,
    phone_number: str = None,
    sms_application_sid: str = None,
    sms_fallback_method: str = None,
    sms_fallback_url: str = None,
    sms_method: str = None,
    sms_url: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    trunk_sid: str = None,
    voice_application_sid: str = None,
    voice_caller_id_lookup: bool = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_receive_mode: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """
    Purchase a phone-number for the account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        address_sid:
            The SID of the Address resource we should associate with the new phone
            number. Some regions require addresses to meet local
            regulations.
        api_version:
            The API version to use for incoming calls made to the new phone number.
            The default is `2010-04-01`.
        area_code:
            The desired area code for your new incoming phone number. Can be any
            three-digit, US or Canada area code. We will provision an
            available phone number within this area code for you. **You
            must provide an `area_code` or a `phone_number`.** (US and
            Canada only).
        bundle_sid:
            The SID of the Bundle resource that you associate with the phone number.
            Some regions require a Bundle to meet local Regulations.
        emergency_address_sid:
            The SID of the emergency address configuration to use for emergency
            calling from the new phone number.
        emergency_status:
            The parameter displays if emergency calling is enabled for this number.
            Active numbers may place emergency calls by dialing valid
            emergency numbers for the country.
        friendly_name:
            A descriptive string that you created to describe the new phone number.
            It can be up to 64 characters long. By default, this is a
            formatted version of the new phone number.
        identity_sid:
            The SID of the Identity resource that we should associate with the new
            phone number. Some regions require an identity to meet local
            regulations.
        phone_number:
            The phone number to purchase specified in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format.  E.164 phone numbers consist of a + followed by the
            country code and subscriber number without punctuation
            characters. For example, +14155551234.
        sms_application_sid:
            The SID of the application that should handle SMS messages sent to the
            new phone number. If an `sms_application_sid` is present, we
            ignore all of the `sms_*_url` urls and use those set on the
            application.
        sms_fallback_method:
            The HTTP method that we should use to call `sms_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        sms_fallback_url:
            The URL that we should call when an error occurs while requesting or
            executing the TwiML defined by `sms_url`.
        sms_method:
            The HTTP method that we should use to call `sms_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        sms_url:
            The URL we should call when the new phone number receives an incoming
            SMS message.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `GET`
            or `POST` and defaults to `POST`.
        trunk_sid:
            The SID of the Trunk we should use to handle calls to the new phone
            number. If a `trunk_sid` is present, we ignore all of the
            voice urls and voice applications and use only those set on
            the Trunk. Setting a `trunk_sid` will automatically delete
            your `voice_application_sid` and vice versa.
        voice_application_sid:
            The SID of the application we should use to handle calls to the new
            phone number. If a `voice_application_sid` is present, we
            ignore all of the voice urls and use only those set on the
            application. Setting a `voice_application_sid` will
            automatically delete your `trunk_sid` and vice versa.
        voice_caller_id_lookup:
            Whether to lookup the caller's name from the CNAM database and post it
            to your app. Can be: `true` or `false` and defaults to
            `false`.
        voice_fallback_method:
            The HTTP method that we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs retrieving or executing
            the TwiML requested by `url`.
        voice_method:
            The HTTP method that we should use to call `voice_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        voice_receive_mode:
            The configuration parameter for the new phone number to receive incoming
            voice calls or faxes. Can be: `fax` or `voice` and defaults
            to `voice`.
        voice_url:
            The URL that we should call to answer a call to the new phone number.
            The `voice_url` will not be called if a
            `voice_application_sid` or a `trunk_sid` is set.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "address_sid": address_sid,
        "api_version": api_version,
        "area_code": area_code,
        "bundle_sid": bundle_sid,
        "emergency_address_sid": emergency_address_sid,
        "emergency_status": emergency_status,
        "friendly_name": friendly_name,
        "identity_sid": identity_sid,
        "phone_number": phone_number,
        "sms_application_sid": sms_application_sid,
        "sms_fallback_method": sms_fallback_method,
        "sms_fallback_url": sms_fallback_url,
        "sms_method": sms_method,
        "sms_url": sms_url,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "trunk_sid": trunk_sid,
        "voice_application_sid": voice_application_sid,
        "voice_caller_id_lookup": voice_caller_id_lookup,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_receive_mode": voice_receive_mode,
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
async def get_2010_04_01_accounts_account_sid_incoming_phone_numbers_local_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    beta: bool = None,
    friendly_name: str = None,
    phone_number: str = None,
    origin: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        beta:
            Whether to include phone numbers new to the Twilio platform. Can be:
            `true` or `false` and the default is `true`.
        friendly_name:
            A string that identifies the resources to read.
        phone_number:
            The phone numbers of the IncomingPhoneNumber resources to read. You can
            specify partial numbers and use '*' as a wildcard for any
            digit.
        origin:
            Whether to include phone numbers based on their origin. Can be: `twilio`
            or `hosted`. By default, phone numbers of all origin are
            included.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Local.json?&beta=%s&friendly_name=%s&phone_number=%s&origin=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Local.json?&beta=%s&friendly_name=%s&phone_number=%s&origin=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Local.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "beta": beta,
        "friendly_name": friendly_name,
        "phone_number": phone_number,
        "origin": origin,
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
async def post_2010_04_01_accounts_account_sid_incoming_phone_numbers_local_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    address_sid: str = None,
    api_version: str = None,
    bundle_sid: str = None,
    emergency_address_sid: str = None,
    emergency_status: str = None,
    friendly_name: str = None,
    identity_sid: str = None,
    phone_number: str = None,
    sms_application_sid: str = None,
    sms_fallback_method: str = None,
    sms_fallback_url: str = None,
    sms_method: str = None,
    sms_url: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    trunk_sid: str = None,
    voice_application_sid: str = None,
    voice_caller_id_lookup: bool = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_receive_mode: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        address_sid:
            The SID of the Address resource we should associate with the new phone
            number. Some regions require addresses to meet local
            regulations.
        api_version:
            The API version to use for incoming calls made to the new phone number.
            The default is `2010-04-01`.
        bundle_sid:
            The SID of the Bundle resource that you associate with the phone number.
            Some regions require a Bundle to meet local Regulations.
        emergency_address_sid:
            The SID of the emergency address configuration to use for emergency
            calling from the new phone number.
        emergency_status:
            The parameter displays if emergency calling is enabled for this number.
            Active numbers may place emergency calls by dialing valid
            emergency numbers for the country.
        friendly_name:
            A descriptive string that you created to describe the new phone number.
            It can be up to 64 characters long. By default, this is a
            formatted version of the phone number.
        identity_sid:
            The SID of the Identity resource that we should associate with the new
            phone number. Some regions require an identity to meet local
            regulations.
        phone_number:
            The phone number to purchase specified in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format.  E.164 phone numbers consist of a + followed by the
            country code and subscriber number without punctuation
            characters. For example, +14155551234.
        sms_application_sid:
            The SID of the application that should handle SMS messages sent to the
            new phone number. If an `sms_application_sid` is present, we
            ignore all of the `sms_*_url` urls and use those set on the
            application.
        sms_fallback_method:
            The HTTP method that we should use to call `sms_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        sms_fallback_url:
            The URL that we should call when an error occurs while requesting or
            executing the TwiML defined by `sms_url`.
        sms_method:
            The HTTP method that we should use to call `sms_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        sms_url:
            The URL we should call when the new phone number receives an incoming
            SMS message.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `GET`
            or `POST` and defaults to `POST`.
        trunk_sid:
            The SID of the Trunk we should use to handle calls to the new phone
            number. If a `trunk_sid` is present, we ignore all of the
            voice urls and voice applications and use only those set on
            the Trunk. Setting a `trunk_sid` will automatically delete
            your `voice_application_sid` and vice versa.
        voice_application_sid:
            The SID of the application we should use to handle calls to the new
            phone number. If a `voice_application_sid` is present, we
            ignore all of the voice urls and use only those set on the
            application. Setting a `voice_application_sid` will
            automatically delete your `trunk_sid` and vice versa.
        voice_caller_id_lookup:
            Whether to lookup the caller's name from the CNAM database and post it
            to your app. Can be: `true` or `false` and defaults to
            `false`.
        voice_fallback_method:
            The HTTP method that we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs retrieving or executing
            the TwiML requested by `url`.
        voice_method:
            The HTTP method that we should use to call `voice_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        voice_receive_mode:
            The configuration parameter for the new phone number to receive incoming
            voice calls or faxes. Can be: `fax` or `voice` and defaults
            to `voice`.
        voice_url:
            The URL that we should call to answer a call to the new phone number.
            The `voice_url` will not be called if a
            `voice_application_sid` or a `trunk_sid` is set.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Local.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Local.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Local.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "address_sid": address_sid,
        "api_version": api_version,
        "bundle_sid": bundle_sid,
        "emergency_address_sid": emergency_address_sid,
        "emergency_status": emergency_status,
        "friendly_name": friendly_name,
        "identity_sid": identity_sid,
        "phone_number": phone_number,
        "sms_application_sid": sms_application_sid,
        "sms_fallback_method": sms_fallback_method,
        "sms_fallback_url": sms_fallback_url,
        "sms_method": sms_method,
        "sms_url": sms_url,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "trunk_sid": trunk_sid,
        "voice_application_sid": voice_application_sid,
        "voice_caller_id_lookup": voice_caller_id_lookup,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_receive_mode": voice_receive_mode,
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
async def get_2010_04_01_accounts_account_sid_incoming_phone_numbers_mobile_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    beta: bool = None,
    friendly_name: str = None,
    phone_number: str = None,
    origin: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        beta:
            Whether to include phone numbers new to the Twilio platform. Can be:
            `true` or `false` and the default is `true`.
        friendly_name:
            A string that identifies the resources to read.
        phone_number:
            The phone numbers of the IncomingPhoneNumber resources to read. You can
            specify partial numbers and use '*' as a wildcard for any
            digit.
        origin:
            Whether to include phone numbers based on their origin. Can be: `twilio`
            or `hosted`. By default, phone numbers of all origin are
            included.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Mobile.json?&beta=%s&friendly_name=%s&phone_number=%s&origin=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Mobile.json?&beta=%s&friendly_name=%s&phone_number=%s&origin=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Mobile.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "beta": beta,
        "friendly_name": friendly_name,
        "phone_number": phone_number,
        "origin": origin,
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
async def post_2010_04_01_accounts_account_sid_incoming_phone_numbers_mobile_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    address_sid: str = None,
    api_version: str = None,
    bundle_sid: str = None,
    emergency_address_sid: str = None,
    emergency_status: str = None,
    friendly_name: str = None,
    identity_sid: str = None,
    phone_number: str = None,
    sms_application_sid: str = None,
    sms_fallback_method: str = None,
    sms_fallback_url: str = None,
    sms_method: str = None,
    sms_url: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    trunk_sid: str = None,
    voice_application_sid: str = None,
    voice_caller_id_lookup: bool = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_receive_mode: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        address_sid:
            The SID of the Address resource we should associate with the new phone
            number. Some regions require addresses to meet local
            regulations.
        api_version:
            The API version to use for incoming calls made to the new phone number.
            The default is `2010-04-01`.
        bundle_sid:
            The SID of the Bundle resource that you associate with the phone number.
            Some regions require a Bundle to meet local Regulations.
        emergency_address_sid:
            The SID of the emergency address configuration to use for emergency
            calling from the new phone number.
        emergency_status:
            The parameter displays if emergency calling is enabled for this number.
            Active numbers may place emergency calls by dialing valid
            emergency numbers for the country.
        friendly_name:
            A descriptive string that you created to describe the new phone number.
            It can be up to 64 characters long. By default, the is a
            formatted version of the phone number.
        identity_sid:
            The SID of the Identity resource that we should associate with the new
            phone number. Some regions require an identity to meet local
            regulations.
        phone_number:
            The phone number to purchase specified in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format.  E.164 phone numbers consist of a + followed by the
            country code and subscriber number without punctuation
            characters. For example, +14155551234.
        sms_application_sid:
            The SID of the application that should handle SMS messages sent to the
            new phone number. If an `sms_application_sid` is present, we
            ignore all of the `sms_*_url` urls and use those of the
            application.
        sms_fallback_method:
            The HTTP method that we should use to call `sms_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        sms_fallback_url:
            The URL that we should call when an error occurs while requesting or
            executing the TwiML defined by `sms_url`.
        sms_method:
            The HTTP method that we should use to call `sms_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        sms_url:
            The URL we should call when the new phone number receives an incoming
            SMS message.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `GET`
            or `POST` and defaults to `POST`.
        trunk_sid:
            The SID of the Trunk we should use to handle calls to the new phone
            number. If a `trunk_sid` is present, we ignore all of the
            voice urls and voice applications and use only those set on
            the Trunk. Setting a `trunk_sid` will automatically delete
            your `voice_application_sid` and vice versa.
        voice_application_sid:
            The SID of the application we should use to handle calls to the new
            phone number. If a `voice_application_sid` is present, we
            ignore all of the voice urls and use only those set on the
            application. Setting a `voice_application_sid` will
            automatically delete your `trunk_sid` and vice versa.
        voice_caller_id_lookup:
            Whether to lookup the caller's name from the CNAM database and post it
            to your app. Can be: `true` or `false` and defaults to
            `false`.
        voice_fallback_method:
            The HTTP method that we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs retrieving or executing
            the TwiML requested by `url`.
        voice_method:
            The HTTP method that we should use to call `voice_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        voice_receive_mode:
            The configuration parameter for the new phone number to receive incoming
            voice calls or faxes. Can be: `fax` or `voice` and defaults
            to `voice`.
        voice_url:
            The URL that we should call to answer a call to the new phone number.
            The `voice_url` will not be called if a
            `voice_application_sid` or a `trunk_sid` is set.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Mobile.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Mobile.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Mobile.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "address_sid": address_sid,
        "api_version": api_version,
        "bundle_sid": bundle_sid,
        "emergency_address_sid": emergency_address_sid,
        "emergency_status": emergency_status,
        "friendly_name": friendly_name,
        "identity_sid": identity_sid,
        "phone_number": phone_number,
        "sms_application_sid": sms_application_sid,
        "sms_fallback_method": sms_fallback_method,
        "sms_fallback_url": sms_fallback_url,
        "sms_method": sms_method,
        "sms_url": sms_url,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "trunk_sid": trunk_sid,
        "voice_application_sid": voice_application_sid,
        "voice_caller_id_lookup": voice_caller_id_lookup,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_receive_mode": voice_receive_mode,
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
async def get_2010_04_01_accounts_account_sid_incoming_phone_numbers_toll_free_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    beta: bool = None,
    friendly_name: str = None,
    phone_number: str = None,
    origin: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        beta:
            Whether to include phone numbers new to the Twilio platform. Can be:
            `true` or `false` and the default is `true`.
        friendly_name:
            A string that identifies the resources to read.
        phone_number:
            The phone numbers of the IncomingPhoneNumber resources to read. You can
            specify partial numbers and use '*' as a wildcard for any
            digit.
        origin:
            Whether to include phone numbers based on their origin. Can be: `twilio`
            or `hosted`. By default, phone numbers of all origin are
            included.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/TollFree.json?&beta=%s&friendly_name=%s&phone_number=%s&origin=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/TollFree.json?&beta=%s&friendly_name=%s&phone_number=%s&origin=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/TollFree.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "beta": beta,
        "friendly_name": friendly_name,
        "phone_number": phone_number,
        "origin": origin,
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
async def post_2010_04_01_accounts_account_sid_incoming_phone_numbers_toll_free_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    address_sid: str = None,
    api_version: str = None,
    bundle_sid: str = None,
    emergency_address_sid: str = None,
    emergency_status: str = None,
    friendly_name: str = None,
    identity_sid: str = None,
    phone_number: str = None,
    sms_application_sid: str = None,
    sms_fallback_method: str = None,
    sms_fallback_url: str = None,
    sms_method: str = None,
    sms_url: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    trunk_sid: str = None,
    voice_application_sid: str = None,
    voice_caller_id_lookup: bool = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_receive_mode: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        address_sid:
            The SID of the Address resource we should associate with the new phone
            number. Some regions require addresses to meet local
            regulations.
        api_version:
            The API version to use for incoming calls made to the new phone number.
            The default is `2010-04-01`.
        bundle_sid:
            The SID of the Bundle resource that you associate with the phone number.
            Some regions require a Bundle to meet local Regulations.
        emergency_address_sid:
            The SID of the emergency address configuration to use for emergency
            calling from the new phone number.
        emergency_status:
            The parameter displays if emergency calling is enabled for this number.
            Active numbers may place emergency calls by dialing valid
            emergency numbers for the country.
        friendly_name:
            A descriptive string that you created to describe the new phone number.
            It can be up to 64 characters long. By default, this is a
            formatted version of the phone number.
        identity_sid:
            The SID of the Identity resource that we should associate with the new
            phone number. Some regions require an Identity to meet local
            regulations.
        phone_number:
            The phone number to purchase specified in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format.  E.164 phone numbers consist of a + followed by the
            country code and subscriber number without punctuation
            characters. For example, +14155551234.
        sms_application_sid:
            The SID of the application that should handle SMS messages sent to the
            new phone number. If an `sms_application_sid` is present, we
            ignore all `sms_*_url` values and use those of the
            application.
        sms_fallback_method:
            The HTTP method that we should use to call `sms_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        sms_fallback_url:
            The URL that we should call when an error occurs while requesting or
            executing the TwiML defined by `sms_url`.
        sms_method:
            The HTTP method that we should use to call `sms_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        sms_url:
            The URL we should call when the new phone number receives an incoming
            SMS message.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `GET`
            or `POST` and defaults to `POST`.
        trunk_sid:
            The SID of the Trunk we should use to handle calls to the new phone
            number. If a `trunk_sid` is present, we ignore all of the
            voice urls and voice applications and use only those set on
            the Trunk. Setting a `trunk_sid` will automatically delete
            your `voice_application_sid` and vice versa.
        voice_application_sid:
            The SID of the application we should use to handle calls to the new
            phone number. If a `voice_application_sid` is present, we
            ignore all of the voice urls and use those set on the
            application. Setting a `voice_application_sid` will
            automatically delete your `trunk_sid` and vice versa.
        voice_caller_id_lookup:
            Whether to lookup the caller's name from the CNAM database and post it
            to your app. Can be: `true` or `false` and defaults to
            `false`.
        voice_fallback_method:
            The HTTP method that we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs retrieving or executing
            the TwiML requested by `url`.
        voice_method:
            The HTTP method that we should use to call `voice_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        voice_receive_mode:
            The configuration parameter for the new phone number to receive incoming
            voice calls or faxes. Can be: `fax` or `voice` and defaults
            to `voice`.
        voice_url:
            The URL that we should call to answer a call to the new phone number.
            The `voice_url` will not be called if a
            `voice_application_sid` or a `trunk_sid` is set.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/TollFree.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/TollFree.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/TollFree.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "address_sid": address_sid,
        "api_version": api_version,
        "bundle_sid": bundle_sid,
        "emergency_address_sid": emergency_address_sid,
        "emergency_status": emergency_status,
        "friendly_name": friendly_name,
        "identity_sid": identity_sid,
        "phone_number": phone_number,
        "sms_application_sid": sms_application_sid,
        "sms_fallback_method": sms_fallback_method,
        "sms_fallback_url": sms_fallback_url,
        "sms_method": sms_method,
        "sms_url": sms_url,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "trunk_sid": trunk_sid,
        "voice_application_sid": voice_application_sid,
        "voice_caller_id_lookup": voice_caller_id_lookup,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_receive_mode": voice_receive_mode,
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
async def get_2010_04_01_accounts_account_sid_incoming_phone_numbers_resource_sid_assigned_add_ons_json(
    account_sid: str,
    resource_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Add-on installations currently assigned to this Number.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        resource_sid:
            Resource sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_incoming_phone_numbers_resource_sid_assigned_add_ons_json(
    account_sid: str,
    resource_sid: str,
    twilio_credentials: "TwilioCredentials",
    installed_add_on_sid: str = None,
) -> Dict[str, Any]:
    """
    Assign an Add-on installation to the Number specified.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        resource_sid:
            Resource sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        installed_add_on_sid:
            The SID that identifies the Add-on installation.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "installed_add_on_sid": installed_add_on_sid,
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
async def get_2010_04_01_accounts_account_sid_incoming_phone_numbers_resource_sid_assigned_add_ons_assigned_add_on_sid_extensions_json(
    account_sid: str,
    resource_sid: str,
    assigned_add_on_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Extensions for the Assigned Add-on.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        resource_sid:
            Resource sid used in formatting the endpoint URL.
        assigned_add_on_sid:
            Assigned add on sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_incoming_phone_numbers_resource_sid_assigned_add_ons_assigned_add_on_sid_extensions_sid_json(
    account_sid: str,
    resource_sid: str,
    assigned_add_on_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of an Extension for the Assigned Add-on.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        resource_sid:
            Resource sid used in formatting the endpoint URL.
        assigned_add_on_sid:
            Assigned add on sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions/{sid}.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_incoming_phone_numbers_resource_sid_assigned_add_ons_sid_json(
    account_sid: str,
    resource_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove the assignment of an Add-on installation from the Number specified.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        resource_sid:
            Resource sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_incoming_phone_numbers_resource_sid_assigned_add_ons_sid_json(
    account_sid: str,
    resource_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of an Add-on installation currently assigned to this Number.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        resource_sid:
            Resource sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid}.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_incoming_phone_numbers_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a phone-numbers belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_incoming_phone_numbers_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an incoming-phone-number belonging to the account used to make the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_incoming_phone_numbers_sid_json(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    account_sid: str = None,
    address_sid: str = None,
    api_version: str = None,
    bundle_sid: str = None,
    emergency_address_sid: str = None,
    emergency_status: str = None,
    friendly_name: str = None,
    identity_sid: str = None,
    sms_application_sid: str = None,
    sms_fallback_method: str = None,
    sms_fallback_url: str = None,
    sms_method: str = None,
    sms_url: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    trunk_sid: str = None,
    voice_application_sid: str = None,
    voice_caller_id_lookup: bool = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_receive_mode: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """
    Update an incoming-phone-number instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        account_sid:
            The SID of the [Account](https://www.twilio.com/docs/iam/api/account)
            that created the IncomingPhoneNumber resource to update.
            For more information, see [Exchanging Numbers Between
            Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts
            exchanging-numbers).
        address_sid:
            The SID of the Address resource we should associate with the phone
            number. Some regions require addresses to meet local
            regulations.
        api_version:
            The API version to use for incoming calls made to the phone number. The
            default is `2010-04-01`.
        bundle_sid:
            The SID of the Bundle resource that you associate with the phone number.
            Some regions require a Bundle to meet local Regulations.
        emergency_address_sid:
            The SID of the emergency address configuration to use for emergency
            calling from this phone number.
        emergency_status:
            The parameter displays if emergency calling is enabled for this number.
            Active numbers may place emergency calls by dialing valid
            emergency numbers for the country.
        friendly_name:
            A descriptive string that you created to describe this phone number. It
            can be up to 64 characters long. By default, this is a
            formatted version of the phone number.
        identity_sid:
            The SID of the Identity resource that we should associate with the phone
            number. Some regions require an identity to meet local
            regulations.
        sms_application_sid:
            The SID of the application that should handle SMS messages sent to the
            number. If an `sms_application_sid` is present, we ignore
            all of the `sms_*_url` urls and use those set on the
            application.
        sms_fallback_method:
            The HTTP method that we should use to call `sms_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        sms_fallback_url:
            The URL that we should call when an error occurs while requesting or
            executing the TwiML defined by `sms_url`.
        sms_method:
            The HTTP method that we should use to call `sms_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        sms_url:
            The URL we should call when the phone number receives an incoming SMS
            message.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `GET`
            or `POST` and defaults to `POST`.
        trunk_sid:
            The SID of the Trunk we should use to handle phone calls to the phone
            number. If a `trunk_sid` is present, we ignore all of the
            voice urls and voice applications and use only those set on
            the Trunk. Setting a `trunk_sid` will automatically delete
            your `voice_application_sid` and vice versa.
        voice_application_sid:
            The SID of the application we should use to handle phone calls to the
            phone number. If a `voice_application_sid` is present, we
            ignore all of the voice urls and use only those set on the
            application. Setting a `voice_application_sid` will
            automatically delete your `trunk_sid` and vice versa.
        voice_caller_id_lookup:
            Whether to lookup the caller's name from the CNAM database and post it
            to your app. Can be: `true` or `false` and defaults to
            `false`.
        voice_fallback_method:
            The HTTP method that we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST` and defaults to `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs retrieving or executing
            the TwiML requested by `url`.
        voice_method:
            The HTTP method that we should use to call `voice_url`. Can be: `GET` or
            `POST` and defaults to `POST`.
        voice_receive_mode:
            The configuration parameter for the phone number to receive incoming
            voice calls or faxes. Can be: `fax` or `voice` and defaults
            to `voice`.
        voice_url:
            The URL that we should call to answer a call to the phone number. The
            `voice_url` will not be called if a `voice_application_sid`
            or a `trunk_sid` is set.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "account_sid": account_sid,
        "address_sid": address_sid,
        "api_version": api_version,
        "bundle_sid": bundle_sid,
        "emergency_address_sid": emergency_address_sid,
        "emergency_status": emergency_status,
        "friendly_name": friendly_name,
        "identity_sid": identity_sid,
        "sms_application_sid": sms_application_sid,
        "sms_fallback_method": sms_fallback_method,
        "sms_fallback_url": sms_fallback_url,
        "sms_method": sms_method,
        "sms_url": sms_url,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "trunk_sid": trunk_sid,
        "voice_application_sid": voice_application_sid,
        "voice_caller_id_lookup": voice_caller_id_lookup,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_receive_mode": voice_receive_mode,
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
async def get_2010_04_01_accounts_account_sid_keys_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_keys_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_keys_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_keys_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_keys_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Keys/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_messages_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    to: str = None,
    from_: str = None,
    date_sent: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of messages belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        to:
            Read messages sent to only this phone number.
        from_:
            Read messages sent from only this phone number or alphanumeric sender
            ID.
        date_sent:
            The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT
            to read only messages sent on this date. For example:
            `2009-07-06`. You can also specify an inequality, such as
            `DateSent<=YYYY-MM-DD`, to read messages sent on or before
            midnight on a date, and `DateSent>=YYYY-MM-DD` to read
            messages sent on or after midnight on a date.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json?&to=%s&from_=%s&date_sent=%s&date_sent=%s&date_sent=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json?&to=%s&from_=%s&date_sent=%s&date_sent=%s&date_sent=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "to": to,
        "from_": from_,
        "date_sent": date_sent,
        "date_sent": date_sent,
        "date_sent": date_sent,
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
async def post_2010_04_01_accounts_account_sid_messages_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    address_retention: str = None,
    application_sid: str = None,
    attempt: int = None,
    body: str = None,
    content_retention: str = None,
    force_delivery: bool = None,
    from_: str = None,
    max_price: str = None,
    media_url: list = None,
    messaging_service_sid: str = None,
    persistent_action: list = None,
    provide_feedback: bool = None,
    schedule_type: str = None,
    send_as_mms: bool = None,
    send_at: str = None,
    smart_encoded: bool = None,
    status_callback: str = None,
    to: str = None,
    validity_period: int = None,
) -> Dict[str, Any]:
    """
    Send a message from the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        address_retention:
            Determines if the address can be stored or obfuscated based on privacy
            settings.
        application_sid:
            The SID of the application that should receive message status. We POST a
            `message_sid` parameter and a `message_status` parameter
            with a value of `sent` or `failed` to the
            [application](https://www.twilio.com/docs/usage/api/applications)'s
            `message_status_callback`. If a `status_callback` parameter
            is also passed, it will be ignored and the application's
            `message_status_callback` parameter will be used.
        attempt:
            Total number of attempts made ( including this ) to send out the message
            regardless of the provider used.
        body:
            The text of the message you want to send. Can be up to 1,600 characters
            in length.
        content_retention:
            Determines if the message content can be stored or redacted based on
            privacy settings.
        force_delivery:
            Reserved.
        from_:
            A Twilio phone number in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format, an [alphanumeric sender
            ID](https://www.twilio.com/docs/sms/send-messages
            use-an-alphanumeric-sender-id), or a [Channel Endpoint
            address](https://www.twilio.com/docs/sms/channels
            channel-addresses) that is enabled for the type of message
            you want to send. Phone numbers or [short
            codes](https://www.twilio.com/docs/sms/api/short-code)
            purchased from Twilio also work here. You cannot, for
            example, spoof messages from a private cell phone number. If
            you are using `messaging_service_sid`, this parameter must
            be empty.
        max_price:
            The maximum total price in US dollars that you will pay for the message
            to be delivered. Can be a decimal value that has up to 4
            decimal places. All messages are queued for delivery and the
            message cost is checked before the message is sent. If the
            cost exceeds `max_price`, the message will fail and a status
            of `Failed` is sent to the status callback. If `MaxPrice` is
            not set, the message cost is not checked.
        media_url:
            The URL of the media to send with the message. The media can be of type
            `gif`, `png`, and `jpeg` and will be formatted correctly on
            the recipient's device. The media size limit is 5MB for
            supported file types (JPEG, PNG, GIF) and 500KB for [other
            types](https://www.twilio.com/docs/sms/accepted-mime-types)
            of accepted media. To send more than one image in the
            message body, provide multiple `media_url` parameters in the
            POST request. You can include up to 10 `media_url`
            parameters per message. You can send images in an SMS
            message in only the US and Canada.
        messaging_service_sid:
            The SID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services
            send-a-message-with-copilot) you want to associate with the
            Message. Set this parameter to use the [Messaging Service
            Settings and Copilot
            Features](https://www.twilio.com/console/sms/services) you
            have configured and leave the `from` parameter empty. When
            only this parameter is set, Twilio will use your enabled
            Copilot Features to select the `from` phone number for
            delivery.
        persistent_action:
            Rich actions for Channels Messages.
        provide_feedback:
            Whether to confirm delivery of the message. Set this value to `true` if
            you are sending messages that have a trackable user action
            and you intend to confirm delivery of the message using the
            [Message Feedback
            API](https://www.twilio.com/docs/sms/api/message-feedback-
            resource). This parameter is `false` by default.
        schedule_type:
            Indicates your intent to schedule a message. Pass the value `fixed` to
            schedule a message at a fixed time.
        send_as_mms:
            If set to True, Twilio will deliver the message as a single MMS message,
            regardless of the presence of media.
        send_at:
            The time that Twilio will send the message. Must be in ISO 8601 format.
        smart_encoded:
            Whether to detect Unicode characters that have a similar GSM-7 character
            and replace them. Can be: `true` or `false`.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application. If specified, we POST these
            message status changes to the URL: `queued`, `failed`,
            `sent`, `delivered`, or `undelivered`. Twilio will POST its
            [standard request
            parameters](https://www.twilio.com/docs/sms/twiml
            request-parameters) as well as some additional parameters
            including `MessageSid`, `MessageStatus`, and `ErrorCode`. If
            you include this parameter with the `messaging_service_sid`,
            we use this URL instead of the Status Callback URL of the
            [Messaging
            Service](https://www.twilio.com/docs/sms/services/api). URLs
            must contain a valid hostname and underscores are not
            allowed.
        to:
            The destination phone number in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format for SMS/MMS or [Channel user
            address](https://www.twilio.com/docs/sms/channels
            channel-addresses) for other 3rd-party channels.
        validity_period:
            How long in seconds the message can remain in our outgoing message
            queue. After this period elapses, the message fails and we
            call your status callback. Can be between 1 and the default
            value of 14,400 seconds. After a message has been accepted
            by a carrier, however, we cannot guarantee that the message
            will not be queued after this period. We recommend that this
            value be at least 5 seconds.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "address_retention": address_retention,
        "application_sid": application_sid,
        "attempt": attempt,
        "body": body,
        "content_retention": content_retention,
        "force_delivery": force_delivery,
        "from_": from_,
        "max_price": max_price,
        "media_url": media_url,
        "messaging_service_sid": messaging_service_sid,
        "persistent_action": persistent_action,
        "provide_feedback": provide_feedback,
        "schedule_type": schedule_type,
        "send_as_mms": send_as_mms,
        "send_at": send_at,
        "smart_encoded": smart_encoded,
        "status_callback": status_callback,
        "to": to,
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
async def post_2010_04_01_accounts_account_sid_messages_message_sid_feedback_json(
    account_sid: str,
    message_sid: str,
    twilio_credentials: "TwilioCredentials",
    outcome: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        message_sid:
            Message sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        outcome:
            Whether the feedback has arrived. Can be: `unconfirmed` or `confirmed`.
            If `provide_feedback`=`true` in [the initial HTTP
            POST](https://www.twilio.com/docs/sms/api/message-resource
            create-a-message-resource), the initial value of this
            property is `unconfirmed`. After the message arrives, update
            the value to `confirmed`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Feedback.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Feedback.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Feedback.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "outcome": outcome,
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
async def get_2010_04_01_accounts_account_sid_messages_message_sid_media_json(
    account_sid: str,
    message_sid: str,
    twilio_credentials: "TwilioCredentials",
    date_created: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of Media resources belonging to the account used to make the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        message_sid:
            Message sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created:
            Only include media that was created on this date. Specify a date as
            `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read
            media that was created on this date. You can also specify an
            inequality, such as `StartTime<=YYYY-MM-DD`, to read media
            that was created on or before midnight of this date, and
            `StartTime>=YYYY-MM-DD` to read media that was created on or
            after midnight of this date.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media.json?&date_created=%s&date_created=%s&date_created=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media.json?&date_created=%s&date_created=%s&date_created=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created": date_created,
        "date_created": date_created,
        "date_created": date_created,
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
async def delete_2010_04_01_accounts_account_sid_messages_message_sid_media_sid_json(
    account_sid: str,
    message_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete media from your account. Once delete, you will no longer be billed.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
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
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_messages_message_sid_media_sid_json(
    account_sid: str,
    message_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a single media instance belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
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
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_messages_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Deletes a message record from your account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_messages_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a message belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_messages_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    body: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """
    To redact a message-body from a post-flight message record, post to the message
    instance resource with an empty body.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        body:
            The text of the message you want to send. Can be up to 1,600 characters
            long.
        status:
            When set as `canceled`, allows a message cancelation request if a
            message has not yet been sent.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "body": body,
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
async def get_2010_04_01_accounts_account_sid_notifications_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    log: int = None,
    message_date: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of notifications belonging to the account used to make the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        log:
            Only read notifications of the specified log level. Can be:  `0` to read
            only ERROR notifications or `1` to read only WARNING
            notifications. By default, all notifications are read.
        message_date:
            Only show notifications for the specified date, formatted as `YYYY-MM-
            DD`. You can also specify an inequality, such as `<=YYYY-MM-
            DD` for messages logged at or before midnight on a date, or
            `>=YYYY-MM-DD` for messages logged at or after midnight on a
            date.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Notifications.json?&log=%s&message_date=%s&message_date=%s&message_date=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Notifications.json?&log=%s&message_date=%s&message_date=%s&message_date=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Notifications.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "log": log,
        "message_date": message_date,
        "message_date": message_date,
        "message_date": message_date,
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
async def get_2010_04_01_accounts_account_sid_notifications_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a notification belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Notifications/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Notifications/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Notifications/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_outgoing_caller_ids_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    phone_number: str = None,
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of outgoing-caller-ids belonging to the account used to make the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        phone_number:
            The phone number of the OutgoingCallerId resources to read.
        friendly_name:
            The string that identifies the OutgoingCallerId resources to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds.json?&phone_number=%s&friendly_name=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds.json?&phone_number=%s&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "phone_number": phone_number,
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
async def post_2010_04_01_accounts_account_sid_outgoing_caller_ids_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    call_delay: int = None,
    extension: str = None,
    friendly_name: str = None,
    phone_number: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        call_delay:
            The number of seconds to delay before initiating the verification call.
            Can be an integer between `0` and `60`, inclusive. The
            default is `0`.
        extension:
            The digits to dial after connecting the verification call.
        friendly_name:
            A descriptive string that you create to describe the new caller ID
            resource. It can be up to 64 characters long. The default
            value is a formatted version of the phone number.
        phone_number:
            The phone number to verify in
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            format, which consists of a + followed by the country code
            and subscriber number.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information about the verification process to your
            application.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `GET`
            or `POST`, and the default is `POST`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "call_delay": call_delay,
        "extension": extension,
        "friendly_name": friendly_name,
        "phone_number": phone_number,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
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
async def delete_2010_04_01_accounts_account_sid_outgoing_caller_ids_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete the caller-id specified from the account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_outgoing_caller_ids_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an outgoing-caller-id belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_outgoing_caller_ids_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Updates the caller-id.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_queues_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of queues belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_queues_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    max_size: int = None,
) -> Dict[str, Any]:
    """
    Create a queue.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you created to describe this resource. It can
            be up to 64 characters long.
        max_size:
            The maximum number of calls allowed to be in the queue. The default is
            100. The maximum is 5000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues.json"  # noqa
    )
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "max_size": max_size,
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
async def get_2010_04_01_accounts_account_sid_queues_queue_sid_members_json(
    account_sid: str,
    queue_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve the members of the queue.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        queue_sid:
            Queue sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_queues_queue_sid_members_call_sid_json(
    account_sid: str,
    queue_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific member from the queue.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        queue_sid:
            Queue sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_queues_queue_sid_members_call_sid_json(
    account_sid: str,
    queue_sid: str,
    call_sid: str,
    twilio_credentials: "TwilioCredentials",
    method: str = None,
    url: str = None,
) -> Dict[str, Any]:
    """
    Dequeue a member from a queue and have the member's call begin executing the
    TwiML document at that URL.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        queue_sid:
            Queue sid used in formatting the endpoint URL.
        call_sid:
            Call sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        method:
            How to pass the update request data. Can be `GET` or `POST` and the
            default is `POST`. `POST` sends the data as encoded form
            data and `GET` sends the data as query parameters.
        url:
            The absolute URL of the Queue resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "method": method,
        "url": url,
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
async def delete_2010_04_01_accounts_account_sid_queues_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Remove an empty queue.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_queues_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a queue identified by the QueueSid.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_queues_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    max_size: int = None,
) -> Dict[str, Any]:
    """
    Update the queue with the new parameters.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you created to describe this resource. It can
            be up to 64 characters long.
        max_size:
            The maximum number of calls allowed to be in the queue. The default is
            100. The maximum is 5000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Queues/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
        "max_size": max_size,
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
async def get_2010_04_01_accounts_account_sid_recordings_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    date_created: str = None,
    call_sid: str = None,
    conference_sid: str = None,
    include_soft_deleted: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of recordings belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created:
            Only include recordings that were created on this date. Specify a date
            as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read
            recordings that were created on this date. You can also
            specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to
            read recordings that were created on or before midnight of
            this date, and `DateCreated>=YYYY-MM-DD` to read recordings
            that were created on or after midnight of this date.
        call_sid:
            The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of
            the resources to read.
        conference_sid:
            The Conference SID that identifies the conference associated with the
            recording to read.
        include_soft_deleted:
            A boolean parameter indicating whether to retrieve soft deleted
            recordings or not. Recordings metadata are kept after
            deletion for a retention period of 40 days.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings.json?&date_created=%s&date_created=%s&date_created=%s&call_sid=%s&conference_sid=%s&include_soft_deleted=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings.json?&date_created=%s&date_created=%s&date_created=%s&call_sid=%s&conference_sid=%s&include_soft_deleted=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created": date_created,
        "date_created": date_created,
        "date_created": date_created,
        "call_sid": call_sid,
        "conference_sid": conference_sid,
        "include_soft_deleted": include_soft_deleted,
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
async def get_2010_04_01_accounts_account_sid_recordings_recording_sid_transcriptions_json(
    account_sid: str,
    recording_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        recording_sid:
            Recording sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_recordings_recording_sid_transcriptions_sid_json(
    account_sid: str,
    recording_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        recording_sid:
            Recording sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_recordings_recording_sid_transcriptions_sid_json(
    account_sid: str,
    recording_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        recording_sid:
            Recording sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_recordings_reference_sid_add_on_results_json(
    account_sid: str,
    reference_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of results belonging to the recording.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        reference_sid:
            Reference sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_recordings_reference_sid_add_on_results_add_on_result_sid_payloads_json(
    account_sid: str,
    reference_sid: str,
    add_on_result_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of payloads belonging to the AddOnResult.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        reference_sid:
            Reference sid used in formatting the endpoint URL.
        add_on_result_sid:
            Add on result sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_recordings_reference_sid_add_on_results_add_on_result_sid_payloads_sid_json(
    account_sid: str,
    reference_sid: str,
    add_on_result_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a payload from the result along with all associated Data.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        reference_sid:
            Reference sid used in formatting the endpoint URL.
        add_on_result_sid:
            Add on result sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_recordings_reference_sid_add_on_results_add_on_result_sid_payloads_sid_json(
    account_sid: str,
    reference_sid: str,
    add_on_result_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a result payload.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        reference_sid:
            Reference sid used in formatting the endpoint URL.
        add_on_result_sid:
            Add on result sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid}.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_recordings_reference_sid_add_on_results_sid_json(
    account_sid: str,
    reference_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a result and purge all associated Payloads.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        reference_sid:
            Reference sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_recordings_reference_sid_add_on_results_sid_json(
    account_sid: str,
    reference_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of an AddOnResult.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        reference_sid:
            Reference sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{sid}.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_recordings_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a recording from your account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_recordings_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    include_soft_deleted: bool = None,
) -> Dict[str, Any]:
    """
    Fetch an instance of a recording.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        include_soft_deleted:
            A boolean parameter indicating whether to retrieve soft deleted
            recordings or not. Recordings metadata are kept after
            deletion for a retention period of 40 days.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{sid}.json?&include_soft_deleted=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{sid}.json?&include_soft_deleted=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "include_soft_deleted": include_soft_deleted,
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
async def get_2010_04_01_accounts_account_sid_sip_credential_lists_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Get All Credential Lists.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_credential_lists_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Create a Credential List.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A human readable descriptive text that describes the CredentialList, up
            to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_credential_lists_credential_list_sid_credentials_json(
    account_sid: str,
    credential_list_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of credentials.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        credential_list_sid:
            Credential list sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_credential_lists_credential_list_sid_credentials_json(
    account_sid: str,
    credential_list_sid: str,
    twilio_credentials: "TwilioCredentials",
    password: str = None,
    username: str = None,
) -> Dict[str, Any]:
    """
    Create a new credential resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        credential_list_sid:
            Credential list sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        password:
            The password that the username will use when authenticating SIP
            requests. The password must be a minimum of 12 characters,
            contain at least 1 digit, and have mixed case. (eg
            `IWasAtSignal2018`).
        username:
            The username that will be passed when authenticating SIP requests. The
            username should be sent in response to Twilio's challenge of
            the initial INVITE. It can be up to 32 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "password": password,
        "username": username,
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
async def delete_2010_04_01_accounts_account_sid_sip_credential_lists_credential_list_sid_credentials_sid_json(
    account_sid: str,
    credential_list_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a credential resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        credential_list_sid:
            Credential list sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_credential_lists_credential_list_sid_credentials_sid_json(
    account_sid: str,
    credential_list_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a single credential.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        credential_list_sid:
            Credential list sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_credential_lists_credential_list_sid_credentials_sid_json(
    account_sid: str,
    credential_list_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    password: str = None,
) -> Dict[str, Any]:
    """
    Update a credential resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        credential_list_sid:
            Credential list sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        password:
            The password that the username will use when authenticating SIP
            requests. The password must be a minimum of 12 characters,
            contain at least 1 digit, and have mixed case. (eg
            `IWasAtSignal2018`).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "password": password,
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
async def delete_2010_04_01_accounts_account_sid_sip_credential_lists_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Credential List.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_credential_lists_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Get a Credential List.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_credential_lists_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update a Credential List.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A human readable descriptive text for a CredentialList, up to 64
            characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of domains belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_domains_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    byoc_trunk_sid: str = None,
    domain_name: str = None,
    emergency_caller_sid: str = None,
    emergency_calling_enabled: bool = None,
    friendly_name: str = None,
    secure: bool = None,
    sip_registration: bool = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_status_callback_method: str = None,
    voice_status_callback_url: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """
    Create a new Domain.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        byoc_trunk_sid:
            The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip
            Domain will be associated with.
        domain_name:
            The unique address you reserve on Twilio to which you route your SIP
            traffic. Domain names can contain letters, digits, and "-"
            and must end with `sip.twilio.com`.
        emergency_caller_sid:
            Whether an emergency caller sid is configured for the domain. If
            present, this phone number will be used as the callback for
            the emergency call.
        emergency_calling_enabled:
            Whether emergency calling is enabled for the domain. If enabled, allows
            emergency calls on the domain from phone numbers with
            validated addresses.
        friendly_name:
            A descriptive string that you created to describe the resource. It can
            be up to 64 characters long.
        secure:
            Whether secure SIP is enabled for the domain. If enabled, TLS will be
            enforced and SRTP will be negotiated on all incoming calls
            to this sip domain.
        sip_registration:
            Whether to allow SIP Endpoints to register with the domain to receive
            calls. Can be `true` or `false`. `true` allows SIP Endpoints
            to register with the domain to receive calls, `false` does
            not.
        voice_fallback_method:
            The HTTP method we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs while retrieving or
            executing the TwiML from `voice_url`.
        voice_method:
            The HTTP method we should use to call `voice_url`. Can be: `GET` or
            `POST`.
        voice_status_callback_method:
            The HTTP method we should use to call `voice_status_callback_url`. Can
            be: `GET` or `POST`.
        voice_status_callback_url:
            The URL that we should call to pass status parameters (such as call
            ended) to your application.
        voice_url:
            The URL we should when the domain receives a call.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "byoc_trunk_sid": byoc_trunk_sid,
        "domain_name": domain_name,
        "emergency_caller_sid": emergency_caller_sid,
        "emergency_calling_enabled": emergency_calling_enabled,
        "friendly_name": friendly_name,
        "secure": secure,
        "sip_registration": sip_registration,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_status_callback_method": voice_status_callback_method,
        "voice_status_callback_url": voice_status_callback_url,
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_calls_credential_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of credential list mappings belonging to the domain used in the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_calls_credential_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    credential_list_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new credential list mapping resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        credential_list_sid:
            The SID of the CredentialList resource to map to the SIP domain.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "credential_list_sid": credential_list_sid,
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
async def delete_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_calls_credential_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a credential list mapping from the requested domain.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_calls_credential_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific instance of a credential list mapping.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_calls_ip_access_control_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of IP Access Control List mappings belonging to the domain used
    in the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_calls_ip_access_control_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    ip_access_control_list_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new IP Access Control List mapping.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ip_access_control_list_sid:
            The SID of the IpAccessControlList resource to map to the SIP domain.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "ip_access_control_list_sid": ip_access_control_list_sid,
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
async def delete_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_calls_ip_access_control_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete an IP Access Control List mapping from the requested domain.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_calls_ip_access_control_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific instance of an IP Access Control List mapping.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/IpAccessControlListMappings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_registrations_credential_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of credential list mappings belonging to the domain used in the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_registrations_credential_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    credential_list_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new credential list mapping resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        credential_list_sid:
            The SID of the CredentialList resource to map to the SIP domain.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "credential_list_sid": credential_list_sid,
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
async def delete_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_registrations_credential_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a credential list mapping from the requested domain.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_auth_registrations_credential_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific instance of a credential list mapping.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_credential_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Read multiple CredentialListMapping resources from an account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_domains_domain_sid_credential_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    credential_list_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a CredentialListMapping resource for an account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        credential_list_sid:
            A 34 character string that uniquely identifies the CredentialList
            resource to map to the SIP domain.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "credential_list_sid": credential_list_sid,
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
async def delete_2010_04_01_accounts_account_sid_sip_domains_domain_sid_credential_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a CredentialListMapping resource from an account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_credential_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a single CredentialListMapping resource from an account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_ip_access_control_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of IpAccessControlListMapping resources.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_domains_domain_sid_ip_access_control_list_mappings_json(
    account_sid: str,
    domain_sid: str,
    twilio_credentials: "TwilioCredentials",
    ip_access_control_list_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new IpAccessControlListMapping resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ip_access_control_list_sid:
            The unique id of the IP access control list to map to the SIP domain.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "ip_access_control_list_sid": ip_access_control_list_sid,
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
async def delete_2010_04_01_accounts_account_sid_sip_domains_domain_sid_ip_access_control_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete an IpAccessControlListMapping resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_domain_sid_ip_access_control_list_mappings_sid_json(
    account_sid: str,
    domain_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an IpAccessControlListMapping resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        domain_sid:
            Domain sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings/{sid}.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_sip_domains_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete an instance of a Domain.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_domains_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a Domain.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_domains_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    byoc_trunk_sid: str = None,
    domain_name: str = None,
    emergency_caller_sid: str = None,
    emergency_calling_enabled: bool = None,
    friendly_name: str = None,
    secure: bool = None,
    sip_registration: bool = None,
    voice_fallback_method: str = None,
    voice_fallback_url: str = None,
    voice_method: str = None,
    voice_status_callback_method: str = None,
    voice_status_callback_url: str = None,
    voice_url: str = None,
) -> Dict[str, Any]:
    """
    Update the attributes of a domain.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        byoc_trunk_sid:
            The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip
            Domain will be associated with.
        domain_name:
            The unique address you reserve on Twilio to which you route your SIP
            traffic. Domain names can contain letters, digits, and "-"
            and must end with `sip.twilio.com`.
        emergency_caller_sid:
            Whether an emergency caller sid is configured for the domain. If
            present, this phone number will be used as the callback for
            the emergency call.
        emergency_calling_enabled:
            Whether emergency calling is enabled for the domain. If enabled, allows
            emergency calls on the domain from phone numbers with
            validated addresses.
        friendly_name:
            A descriptive string that you created to describe the resource. It can
            be up to 64 characters long.
        secure:
            Whether secure SIP is enabled for the domain. If enabled, TLS will be
            enforced and SRTP will be negotiated on all incoming calls
            to this sip domain.
        sip_registration:
            Whether to allow SIP Endpoints to register with the domain to receive
            calls. Can be `true` or `false`. `true` allows SIP Endpoints
            to register with the domain to receive calls, `false` does
            not.
        voice_fallback_method:
            The HTTP method we should use to call `voice_fallback_url`. Can be:
            `GET` or `POST`.
        voice_fallback_url:
            The URL that we should call when an error occurs while retrieving or
            executing the TwiML requested by `voice_url`.
        voice_method:
            The HTTP method we should use to call `voice_url`.
        voice_status_callback_method:
            The HTTP method we should use to call `voice_status_callback_url`. Can
            be: `GET` or `POST`.
        voice_status_callback_url:
            The URL that we should call to pass status parameters (such as call
            ended) to your application.
        voice_url:
            The URL we should call when the domain receives a call.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "byoc_trunk_sid": byoc_trunk_sid,
        "domain_name": domain_name,
        "emergency_caller_sid": emergency_caller_sid,
        "emergency_calling_enabled": emergency_calling_enabled,
        "friendly_name": friendly_name,
        "secure": secure,
        "sip_registration": sip_registration,
        "voice_fallback_method": voice_fallback_method,
        "voice_fallback_url": voice_fallback_url,
        "voice_method": voice_method,
        "voice_status_callback_method": voice_status_callback_method,
        "voice_status_callback_url": voice_status_callback_url,
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
async def get_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of IpAccessControlLists that belong to the account used to make
    the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new IpAccessControlList resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A human readable descriptive text that describes the
            IpAccessControlList, up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_ip_access_control_list_sid_ip_addresses_json(
    account_sid: str,
    ip_access_control_list_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Read multiple IpAddress resources.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        ip_access_control_list_sid:
            Ip access control list sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_ip_access_control_list_sid_ip_addresses_json(
    account_sid: str,
    ip_access_control_list_sid: str,
    twilio_credentials: "TwilioCredentials",
    cidr_prefix_length: int = None,
    friendly_name: str = None,
    ip_address: str = None,
) -> Dict[str, Any]:
    """
    Create a new IpAddress resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        ip_access_control_list_sid:
            Ip access control list sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        cidr_prefix_length:
            An integer representing the length of the CIDR prefix to use with this
            IP address when accepting traffic. By default the entire IP
            address is used.
        friendly_name:
            A human readable descriptive text for this resource, up to 64 characters
            long.
        ip_address:
            An IP address in dotted decimal notation from which you want to accept
            traffic. Any SIP requests from this IP address will be
            allowed by Twilio. IPv4 only supported today.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "cidr_prefix_length": cidr_prefix_length,
        "friendly_name": friendly_name,
        "ip_address": ip_address,
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
async def delete_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_ip_access_control_list_sid_ip_addresses_sid_json(
    account_sid: str,
    ip_access_control_list_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete an IpAddress resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        ip_access_control_list_sid:
            Ip access control list sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_ip_access_control_list_sid_ip_addresses_sid_json(
    account_sid: str,
    ip_access_control_list_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Read one IpAddress resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        ip_access_control_list_sid:
            Ip access control list sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_ip_access_control_list_sid_ip_addresses_sid_json(
    account_sid: str,
    ip_access_control_list_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    cidr_prefix_length: int = None,
    friendly_name: str = None,
    ip_address: str = None,
) -> Dict[str, Any]:
    """
    Update an IpAddress resource.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        ip_access_control_list_sid:
            Ip access control list sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        cidr_prefix_length:
            An integer representing the length of the CIDR prefix to use with this
            IP address when accepting traffic. By default the entire IP
            address is used.
        friendly_name:
            A human readable descriptive text for this resource, up to 64 characters
            long.
        ip_address:
            An IP address in dotted decimal notation from which you want to accept
            traffic. Any SIP requests from this IP address will be
            allowed by Twilio. IPv4 only supported today.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "cidr_prefix_length": cidr_prefix_length,
        "friendly_name": friendly_name,
        "ip_address": ip_address,
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
async def delete_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete an IpAccessControlList from the requested account.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific instance of an IpAccessControlList.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sip_ip_access_control_lists_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Rename an IpAccessControlList.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A human readable descriptive text, up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_sms_short_codes_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    short_code: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of short-codes belonging to the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The string that identifies the ShortCode resources to read.
        short_code:
            Only show the ShortCode resources that match this pattern. You can
            specify partial numbers and use '*' as a wildcard for any
            digit.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SMS/ShortCodes.json?&friendly_name=%s&short_code=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SMS/ShortCodes.json?&friendly_name=%s&short_code=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SMS/ShortCodes.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "friendly_name": friendly_name,
        "short_code": short_code,
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
async def get_2010_04_01_accounts_account_sid_sms_short_codes_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a short code.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SMS/ShortCodes/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SMS/ShortCodes/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SMS/ShortCodes/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_sms_short_codes_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    api_version: str = None,
    friendly_name: str = None,
    sms_fallback_method: str = None,
    sms_fallback_url: str = None,
    sms_method: str = None,
    sms_url: str = None,
) -> Dict[str, Any]:
    """
    Update a short code with the following parameters.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        api_version:
            The API version to use to start a new TwiML session. Can be:
            `2010-04-01` or `2008-08-01`.
        friendly_name:
            A descriptive string that you created to describe this resource. It can
            be up to 64 characters long. By default, the `FriendlyName`
            is the short code.
        sms_fallback_method:
            The HTTP method that we should use to call the `sms_fallback_url`. Can
            be: `GET` or `POST`.
        sms_fallback_url:
            The URL that we should call if an error occurs while retrieving or
            executing the TwiML from `sms_url`.
        sms_method:
            The HTTP method we should use when calling the `sms_url`. Can be: `GET`
            or `POST`.
        sms_url:
            The URL we should call when receiving an incoming SMS message to this
            short code.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SMS/ShortCodes/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SMS/ShortCodes/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SMS/ShortCodes/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "api_version": api_version,
        "friendly_name": friendly_name,
        "sms_fallback_method": sms_fallback_method,
        "sms_fallback_url": sms_fallback_url,
        "sms_method": sms_method,
        "sms_url": sms_url,
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
async def get_2010_04_01_accounts_account_sid_signing_keys_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_signing_keys_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Signing Key for the account making the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_signing_keys_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_signing_keys_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_signing_keys_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/SigningKeys/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_tokens_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    ttl: int = None,
) -> Dict[str, Any]:
    """
    Create a new token for ICE servers.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ttl:
            The duration in seconds for which the generated credentials are valid.
            The default value is 86400 (24 hours).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Tokens.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Tokens.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Tokens.json"  # noqa
    )
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
async def get_2010_04_01_accounts_account_sid_transcriptions_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of transcriptions belonging to the account used to make the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Transcriptions.json?&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Transcriptions.json?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Transcriptions.json"  # noqa
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
async def delete_2010_04_01_accounts_account_sid_transcriptions_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a transcription from the account used to make the request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Transcriptions/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Transcriptions/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Transcriptions/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_transcriptions_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an instance of a Transcription.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Transcriptions/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Transcriptions/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Transcriptions/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_usage_records_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    category: str = None,
    start_date: str = None,
    end_date: str = None,
    include_subaccounts: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of usage-records belonging to the account used to make the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        category:
            The [usage category](https://www.twilio.com/docs/usage/api/usage-record
            usage-categories) of the UsageRecord resources to read. Only
            UsageRecord resources in the specified category are
            retrieved.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`. You can also specify
            offsets from the current date, such as: `-30days`, which
            will set the start date to be 30 days before the current
            date.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.  You can also
            specify offsets from the current date, such as: `+30days`,
            which will set the end date to 30 days from the current
            date.
        include_subaccounts:
            Whether to include usage from the master account and all its
            subaccounts. Can be: `true` (the default) to include usage
            from the master account and all subaccounts or `false` to
            retrieve usage from only the specified account.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "category": category,
        "start_date": start_date,
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
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
async def get_2010_04_01_accounts_account_sid_usage_records_all_time_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    category: str = None,
    start_date: str = None,
    end_date: str = None,
    include_subaccounts: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        category:
            The [usage category](https://www.twilio.com/docs/usage/api/usage-record
            usage-categories) of the UsageRecord resources to read. Only
            UsageRecord resources in the specified category are
            retrieved.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`. You can also specify
            offsets from the current date, such as: `-30days`, which
            will set the start date to be 30 days before the current
            date.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.  You can also
            specify offsets from the current date, such as: `+30days`,
            which will set the end date to 30 days from the current
            date.
        include_subaccounts:
            Whether to include usage from the master account and all its
            subaccounts. Can be: `true` (the default) to include usage
            from the master account and all subaccounts or `false` to
            retrieve usage from only the specified account.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/AllTime.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/AllTime.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/AllTime.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "category": category,
        "start_date": start_date,
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
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
async def get_2010_04_01_accounts_account_sid_usage_records_daily_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    category: str = None,
    start_date: str = None,
    end_date: str = None,
    include_subaccounts: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        category:
            The [usage category](https://www.twilio.com/docs/usage/api/usage-record
            usage-categories) of the UsageRecord resources to read. Only
            UsageRecord resources in the specified category are
            retrieved.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`. You can also specify
            offsets from the current date, such as: `-30days`, which
            will set the start date to be 30 days before the current
            date.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.  You can also
            specify offsets from the current date, such as: `+30days`,
            which will set the end date to 30 days from the current
            date.
        include_subaccounts:
            Whether to include usage from the master account and all its
            subaccounts. Can be: `true` (the default) to include usage
            from the master account and all subaccounts or `false` to
            retrieve usage from only the specified account.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Daily.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Daily.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Daily.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "category": category,
        "start_date": start_date,
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
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
async def get_2010_04_01_accounts_account_sid_usage_records_last_month_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    category: str = None,
    start_date: str = None,
    end_date: str = None,
    include_subaccounts: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        category:
            The [usage category](https://www.twilio.com/docs/usage/api/usage-record
            usage-categories) of the UsageRecord resources to read. Only
            UsageRecord resources in the specified category are
            retrieved.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`. You can also specify
            offsets from the current date, such as: `-30days`, which
            will set the start date to be 30 days before the current
            date.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.  You can also
            specify offsets from the current date, such as: `+30days`,
            which will set the end date to 30 days from the current
            date.
        include_subaccounts:
            Whether to include usage from the master account and all its
            subaccounts. Can be: `true` (the default) to include usage
            from the master account and all subaccounts or `false` to
            retrieve usage from only the specified account.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/LastMonth.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/LastMonth.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/LastMonth.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "category": category,
        "start_date": start_date,
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
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
async def get_2010_04_01_accounts_account_sid_usage_records_monthly_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    category: str = None,
    start_date: str = None,
    end_date: str = None,
    include_subaccounts: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        category:
            The [usage category](https://www.twilio.com/docs/usage/api/usage-record
            usage-categories) of the UsageRecord resources to read. Only
            UsageRecord resources in the specified category are
            retrieved.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`. You can also specify
            offsets from the current date, such as: `-30days`, which
            will set the start date to be 30 days before the current
            date.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.  You can also
            specify offsets from the current date, such as: `+30days`,
            which will set the end date to 30 days from the current
            date.
        include_subaccounts:
            Whether to include usage from the master account and all its
            subaccounts. Can be: `true` (the default) to include usage
            from the master account and all subaccounts or `false` to
            retrieve usage from only the specified account.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Monthly.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Monthly.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Monthly.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "category": category,
        "start_date": start_date,
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
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
async def get_2010_04_01_accounts_account_sid_usage_records_this_month_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    category: str = None,
    start_date: str = None,
    end_date: str = None,
    include_subaccounts: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        category:
            The [usage category](https://www.twilio.com/docs/usage/api/usage-record
            usage-categories) of the UsageRecord resources to read. Only
            UsageRecord resources in the specified category are
            retrieved.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`. You can also specify
            offsets from the current date, such as: `-30days`, which
            will set the start date to be 30 days before the current
            date.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.  You can also
            specify offsets from the current date, such as: `+30days`,
            which will set the end date to 30 days from the current
            date.
        include_subaccounts:
            Whether to include usage from the master account and all its
            subaccounts. Can be: `true` (the default) to include usage
            from the master account and all subaccounts or `false` to
            retrieve usage from only the specified account.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/ThisMonth.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/ThisMonth.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/ThisMonth.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "category": category,
        "start_date": start_date,
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
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
async def get_2010_04_01_accounts_account_sid_usage_records_today_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    category: str = None,
    start_date: str = None,
    end_date: str = None,
    include_subaccounts: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        category:
            The [usage category](https://www.twilio.com/docs/usage/api/usage-record
            usage-categories) of the UsageRecord resources to read. Only
            UsageRecord resources in the specified category are
            retrieved.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`. You can also specify
            offsets from the current date, such as: `-30days`, which
            will set the start date to be 30 days before the current
            date.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.  You can also
            specify offsets from the current date, such as: `+30days`,
            which will set the end date to 30 days from the current
            date.
        include_subaccounts:
            Whether to include usage from the master account and all its
            subaccounts. Can be: `true` (the default) to include usage
            from the master account and all subaccounts or `false` to
            retrieve usage from only the specified account.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Today.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Today.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Today.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "category": category,
        "start_date": start_date,
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
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
async def get_2010_04_01_accounts_account_sid_usage_records_yearly_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    category: str = None,
    start_date: str = None,
    end_date: str = None,
    include_subaccounts: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        category:
            The [usage category](https://www.twilio.com/docs/usage/api/usage-record
            usage-categories) of the UsageRecord resources to read. Only
            UsageRecord resources in the specified category are
            retrieved.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`. You can also specify
            offsets from the current date, such as: `-30days`, which
            will set the start date to be 30 days before the current
            date.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.  You can also
            specify offsets from the current date, such as: `+30days`,
            which will set the end date to 30 days from the current
            date.
        include_subaccounts:
            Whether to include usage from the master account and all its
            subaccounts. Can be: `true` (the default) to include usage
            from the master account and all subaccounts or `false` to
            retrieve usage from only the specified account.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Yearly.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Yearly.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Yearly.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "category": category,
        "start_date": start_date,
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
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
async def get_2010_04_01_accounts_account_sid_usage_records_yesterday_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    category: str = None,
    start_date: str = None,
    end_date: str = None,
    include_subaccounts: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        category:
            The [usage category](https://www.twilio.com/docs/usage/api/usage-record
            usage-categories) of the UsageRecord resources to read. Only
            UsageRecord resources in the specified category are
            retrieved.
        start_date:
            Only include usage that has occurred on or after this date. Specify the
            date in GMT and format as `YYYY-MM-DD`. You can also specify
            offsets from the current date, such as: `-30days`, which
            will set the start date to be 30 days before the current
            date.
        end_date:
            Only include usage that occurred on or before this date. Specify the
            date in GMT and format as `YYYY-MM-DD`.  You can also
            specify offsets from the current date, such as: `+30days`,
            which will set the end date to 30 days from the current
            date.
        include_subaccounts:
            Whether to include usage from the master account and all its
            subaccounts. Can be: `true` (the default) to include usage
            from the master account and all subaccounts or `false` to
            retrieve usage from only the specified account.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Yesterday.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Yesterday.json?&category=%s&start_date=%s&end_date=%s&include_subaccounts=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Records/Yesterday.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "category": category,
        "start_date": start_date,
        "end_date": end_date,
        "include_subaccounts": include_subaccounts,
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
async def get_2010_04_01_accounts_account_sid_usage_triggers_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    recurring: str = None,
    trigger_by: str = None,
    usage_category: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of usage-triggers belonging to the account used to make the
    request.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        recurring:
            The frequency of recurring UsageTriggers to read. Can be: `daily`,
            `monthly`, or `yearly` to read recurring UsageTriggers. An
            empty value or a value of `alltime` reads non-recurring
            UsageTriggers.
        trigger_by:
            The trigger field of the UsageTriggers to read.  Can be: `count`,
            `usage`, or `price` as described in the [UsageRecords
            documentation](https://www.twilio.com/docs/usage/api/usage-
            record
            usage-count-price).
        usage_category:
            The usage category of the UsageTriggers to read. Must be a supported
            [usage
            categories](https://www.twilio.com/docs/usage/api/usage-
            record
            usage-categories).
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers.json?&recurring=%s&trigger_by=%s&usage_category=%s&page_size=%s](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers.json?&recurring=%s&trigger_by=%s&usage_category=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "recurring": recurring,
        "trigger_by": trigger_by,
        "usage_category": usage_category,
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
async def post_2010_04_01_accounts_account_sid_usage_triggers_json(
    account_sid: str,
    twilio_credentials: "TwilioCredentials",
    callback_method: str = None,
    callback_url: str = None,
    friendly_name: str = None,
    recurring: str = None,
    trigger_by: str = None,
    trigger_value: str = None,
    usage_category: str = None,
) -> Dict[str, Any]:
    """
    Create a new UsageTrigger.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_method:
            The HTTP method we should use to call `callback_url`. Can be: `GET` or
            `POST` and the default is `POST`.
        callback_url:
            The URL we should call using `callback_method` when the trigger fires.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        recurring:
            The frequency of a recurring UsageTrigger.  Can be: `daily`, `monthly`,
            or `yearly` for recurring triggers or empty for non-
            recurring triggers. A trigger will only fire once during
            each period. Recurring times are in GMT.
        trigger_by:
            The field in the
            [UsageRecord](https://www.twilio.com/docs/usage/api/usage-
            record) resource that should fire the trigger.  Can be:
            `count`, `usage`, or `price` as described in the
            [UsageRecords
            documentation](https://www.twilio.com/docs/usage/api/usage-
            record
            usage-count-price).  The default is `usage`.
        trigger_value:
            The usage value at which the trigger should fire.  For convenience, you
            can use an offset value such as `+30` to specify a
            trigger_value that is 30 units more than the current usage
            value. Be sure to urlencode a `+` as `%2B`.
        usage_category:
            The usage category that the trigger should watch.  Use one of the
            supported [usage
            categories](https://www.twilio.com/docs/usage/api/usage-
            record
            usage-categories) for this value.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers.json"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "callback_method": callback_method,
        "callback_url": callback_url,
        "friendly_name": friendly_name,
        "recurring": recurring,
        "trigger_by": trigger_by,
        "trigger_value": trigger_value,
        "usage_category": usage_category,
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
async def delete_2010_04_01_accounts_account_sid_usage_triggers_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid}.json"  # noqa
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
async def get_2010_04_01_accounts_account_sid_usage_triggers_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch and instance of a usage-trigger.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_account_sid_usage_triggers_sid_json(
    account_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    callback_method: str = None,
    callback_url: str = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update an instance of a usage trigger.

    Args:
        account_sid:
            Account sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_method:
            The HTTP method we should use to call `callback_url`. Can be: `GET` or
            `POST` and the default is `POST`.
        callback_url:
            The URL we should call using `callback_method` when the trigger fires.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "callback_method": callback_method,
        "callback_url": callback_url,
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
async def get_2010_04_01_accounts_sid_json(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the account specified by the provided Account Sid.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}.json"  # noqa
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
async def post_2010_04_01_accounts_sid_json(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """
    Modify the properties of a given Account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            Update the human-readable description of this Account.
        status:
            Alter the status of this account: use `closed` to irreversibly close
            this account, `suspended` to temporarily suspend it, or
            `active` to reactivate it.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://api.twilio.com/2010-04-01/Accounts/{sid}.json?](
    https://api.twilio.com/2010-04-01/Accounts/{sid}.json?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}.json"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
