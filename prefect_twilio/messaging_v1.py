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
async def get_v1_deactivations(
    twilio_credentials: "TwilioCredentials",
    date: str = None,
) -> Dict[str, Any]:
    """
    Fetch a list of all United States numbers that have been deactivated on a
    specific date.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date:
            The request will return a list of all United States Phone Numbers that
            were deactivated on the day specified by this parameter.
            This date should be specified in YYYY-MM-DD format.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://messaging.twilio.com/v1/Deactivations?&date=%s](
    https://messaging.twilio.com/v1/Deactivations?&date=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 307 | Temporary Redirect. |
    """  # noqa
    url = "https://messaging.twilio.com/v1/Deactivations"  # noqa

    responses = {
        307: "Temporary Redirect.",  # noqa
    }

    params = {
        "date": date,
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
async def get_v1_services_messaging_service_sid_compliance_usa2p_usecases(  # noqa
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
async def delete_v1_services_messaging_service_sid_compliance_usa2p_sid(  # noqa
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
async def get_v1_services_messaging_service_sid_compliance_usa2p_sid(  # noqa
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
async def get_v1_a2p_brand_registrations_brand_sid_vettings_brand_vetting_sid(  # noqa
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
