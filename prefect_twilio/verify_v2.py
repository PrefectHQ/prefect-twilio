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
async def get_v2_attempts(
    twilio_credentials: "TwilioCredentials",
    date_created_after: str = None,
    date_created_before: str = None,
    channel_data_to: str = None,
    country: str = None,
    channel: str = None,
    verify_service_sid: str = None,
    verification_sid: str = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all the verification attempts for a given Account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        date_created_after:
            Datetime filter used to query Verification Attempts created after this
            datetime. Given as GMT in RFC 2822 format.
        date_created_before:
            Datetime filter used to query Verification Attempts created before this
            datetime. Given as GMT in RFC 2822 format.
        channel_data_to:
            Destination of a verification. It is phone number in E.164 format.
        country:
            Filter used to query Verification Attempts sent to the specified
            destination country.
        channel:
            Filter used to query Verification Attempts by communication channel.
            Valid values are `SMS` and `CALL`.
        verify_service_sid:
            Filter used to query Verification Attempts by verify service. Only
            attempts of the provided SID will be returned.
        verification_sid:
            Filter used to return all the Verification Attempts of a single
            verification. Only attempts of the provided verification SID
            will be returned.
        status:
            Filter used to query Verification Attempts by conversion status. Valid
            values are `UNCONVERTED`, for attempts that were not
            converted, and `CONVERTED`, for attempts that were
            confirmed.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Attempts?&date_created_after=%s&date_created_before=%s&channel_data_to=%s&country=%s&channel=%s&verify_service_sid=%s&verification_sid=%s&status=%s&page_size=%s](
    https://verify.twilio.com/v2/Attempts?&date_created_after=%s&date_created_before=%s&channel_data_to=%s&country=%s&channel=%s&verify_service_sid=%s&verification_sid=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Attempts"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "channel_data_to": channel_data_to,
        "country": country,
        "channel": channel,
        "verify_service_sid": verify_service_sid,
        "verification_sid": verification_sid,
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
async def get_v2_attempts_summary(
    twilio_credentials: "TwilioCredentials",
    verify_service_sid: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    country: str = None,
    channel: str = None,
    destination_prefix: str = None,
) -> Dict[str, Any]:
    """
    Get a summary of how many attempts were made and how many were converted.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        verify_service_sid:
            Filter used to consider only Verification Attempts of the given verify
            service on the summary aggregation.
        date_created_after:
            Datetime filter used to consider only Verification Attempts created
            after this datetime on the summary aggregation. Given as GMT
            in RFC 2822 format.
        date_created_before:
            Datetime filter used to consider only Verification Attempts created
            before this datetime on the summary aggregation. Given as
            GMT in RFC 2822 format.
        country:
            Filter used to consider only Verification Attempts sent to the specified
            destination country on the summary aggregation.
        channel:
            Filter Verification Attempts considered on the summary aggregation by
            communication channel. Valid values are `SMS` and `CALL`.
        destination_prefix:
            Filter the Verification Attempts considered on the summary aggregation
            by Destination prefix. It is the prefix of a phone number in
            E.164 format.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Attempts/Summary?&verify_service_sid=%s&date_created_after=%s&date_created_before=%s&country=%s&channel=%s&destination_prefix=%s](
    https://verify.twilio.com/v2/Attempts/Summary?&verify_service_sid=%s&date_created_after=%s&date_created_before=%s&country=%s&channel=%s&destination_prefix=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Attempts/Summary"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "verify_service_sid": verify_service_sid,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "country": country,
        "channel": channel,
        "destination_prefix": destination_prefix,
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
async def get_v2_attempts_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific verification attempt.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Attempts/{sid}?](
    https://verify.twilio.com/v2/Attempts/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Attempts/{sid}"  # noqa
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
async def get_v2_forms_form_type(
    form_type: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the forms for a specific Form Type.

    Args:
        form_type:
            Form type used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Forms/{form_type}?](
    https://verify.twilio.com/v2/Forms/{form_type}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Forms/{form_type}"  # noqa
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
async def get_v2_services(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Verification Services for an account.

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
    [https://verify.twilio.com/v2/Services?&page_size=%s](
    https://verify.twilio.com/v2/Services?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Services"  # noqa

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
async def post_v2_services(
    twilio_credentials: "TwilioCredentials",
    code_length: int = None,
    custom_code_enabled: bool = None,
    default_template_sid: str = None,
    do_not_share_warning_enabled: bool = None,
    dtmf_input_required: bool = None,
    friendly_name: str = None,
    lookup_enabled: bool = None,
    psd2_enabled: bool = None,
    push_apn_credential_sid: str = None,
    push_fcm_credential_sid: str = None,
    push_include_date: bool = None,
    skip_sms_to_landlines: bool = None,
    totp_code_length: int = None,
    totp_issuer: str = None,
    totp_skew: int = None,
    totp_time_step: int = None,
    tts_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Verification Service.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        code_length:
            The length of the verification code to generate. Must be an integer
            value between 4 and 10, inclusive.
        custom_code_enabled:
            Whether to allow sending verifications with a custom code instead of a
            randomly generated one. Not available for all customers.
        default_template_sid:
            The default message
            [template](https://www.twilio.com/docs/verify/api/templates).
            Will be used for all SMS verifications unless explicitly
            overriden. SMS channel only.
        do_not_share_warning_enabled:
            Whether to add a security warning at the end of an SMS verification
            body. Disabled by default and applies only to SMS. Example
            SMS body: `Your AppName verification code is: 1234. Don’t
            share this code with anyone; our employees will never ask
            for the code`.
        dtmf_input_required:
            Whether to ask the user to press a number before delivering the verify
            code in a phone call.
        friendly_name:
            A descriptive string that you create to describe the verification
            service. It can be up to 30 characters long. **This value
            should not contain PII.**.
        lookup_enabled:
            Whether to perform a lookup with each verification started and return
            info about the phone number.
        psd2_enabled:
            Whether to pass PSD2 transaction parameters when starting a
            verification.
        push_apn_credential_sid:
            Optional configuration for the Push factors. Set the APN Credential for
            this service. This will allow to send push notifications to
            iOS devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_fcm_credential_sid:
            Optional configuration for the Push factors. Set the FCM Credential for
            this service. This will allow to send push notifications to
            Android devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_include_date:
            Optional configuration for the Push factors. If true, include the date
            in the Challenge's response. Otherwise, the date is omitted
            from the response. See
            [Challenge](https://www.twilio.com/docs/verify/api/challenge)
            resource’s details parameter for more info. Default: false.
            **Deprecated** do not use this parameter. This timestamp
            value is the same one as the one found in `date_created`,
            please use that one instead.
        skip_sms_to_landlines:
            Whether to skip sending SMS verifications to landlines. Requires
            `lookup_enabled`.
        totp_code_length:
            Optional configuration for the TOTP factors. Number of digits for
            generated TOTP codes. Must be between 3 and 8, inclusive.
            Defaults to 6.
        totp_issuer:
            Optional configuration for the TOTP factors. Set TOTP Issuer for this
            service. This will allow to configure the issuer of the TOTP
            URI. Defaults to the service friendly name if not provided.
        totp_skew:
            Optional configuration for the TOTP factors. The number of time-steps,
            past and future, that are valid for validation of TOTP
            codes. Must be between 0 and 2, inclusive. Defaults to 1.
        totp_time_step:
            Optional configuration for the TOTP factors. Defines how often, in
            seconds, are TOTP codes generated. i.e, a new TOTP code is
            generated every time_step seconds. Must be between 20 and 60
            seconds, inclusive. Defaults to 30 seconds.
        tts_name:
            The name of an alternative text-to-speech service to use in phone calls.
            Applies only to TTS languages.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services?](
    https://verify.twilio.com/v2/Services?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Services"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "code_length": code_length,
        "custom_code_enabled": custom_code_enabled,
        "default_template_sid": default_template_sid,
        "do_not_share_warning_enabled": do_not_share_warning_enabled,
        "dtmf_input_required": dtmf_input_required,
        "friendly_name": friendly_name,
        "lookup_enabled": lookup_enabled,
        "psd2_enabled": psd2_enabled,
        "push_apn_credential_sid": push_apn_credential_sid,
        "push_fcm_credential_sid": push_fcm_credential_sid,
        "push_include_date": push_include_date,
        "skip_sms_to_landlines": skip_sms_to_landlines,
        "totp_code_length": totp_code_length,
        "totp_issuer": totp_issuer,
        "totp_skew": totp_skew,
        "totp_time_step": totp_time_step,
        "tts_name": tts_name,
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
async def post_v2_services_service_sid_access_tokens(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    factor_friendly_name: str = None,
    factor_type: str = None,
    identity: str = None,
    ttl: int = None,
) -> Dict[str, Any]:
    """
    Create a new enrollment Access Token for the Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        factor_friendly_name:
            The friendly name of the factor that is going to be created with this
            access token.
        factor_type:
            The Type of this Factor. Eg. `push`.
        identity:
            The unique external identifier for the Entity of the Service. This
            identifier should be immutable, not PII, and generated by
            your external system, such as your user's UUID, GUID, or
            SID.
        ttl:
            How long, in seconds, the access token is valid. Can be an integer
            between 60 and 300. Default is 60.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens?](
    https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "factor_friendly_name": factor_friendly_name,
        "factor_type": factor_type,
        "identity": identity,
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
async def get_v2_services_service_sid_access_tokens_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an Access Token for the Entity.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/AccessTokens/{sid}"  # noqa
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
async def get_v2_services_service_sid_entities(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Entities for a Service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities"  # noqa
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
async def post_v2_services_service_sid_entities(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
) -> Dict[str, Any]:
    """
    Create a new Entity for the Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            The unique external identifier for the Entity of the Service. This
            identifier should be immutable, not PII, length between 8
            and 64 characters, and generated by your external system,
            such as your user's UUID, GUID, or SID. It can only contain
            dash (-) separated alphanumeric characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "identity": identity,
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
async def delete_v2_services_service_sid_entities_identity(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}"  # noqa
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
async def get_v2_services_service_sid_entities_identity(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}"  # noqa
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
async def get_v2_services_service_sid_entities_identity_challenges(  # noqa
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    factor_sid: str = None,
    status: str = None,
    order: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Challenges for a Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        factor_sid:
            The unique SID identifier of the Factor.
        status:
            The Status of the Challenges to fetch. One of `pending`, `expired`,
            `approved` or `denied`.
        order:
            The desired sort order of the Challenges list. One of `asc` or `desc`
            for ascending and descending respectively. Defaults to
            `asc`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?&factor_sid=%s&status=%s&order=%s&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?&factor_sid=%s&status=%s&order=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "factor_sid": factor_sid,
        "status": status,
        "order": order,
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
async def post_v2_services_service_sid_entities_identity_challenges(  # noqa
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    auth_payload: str = None,
    details_fields: list = None,
    details_message: str = None,
    expiration_date: str = None,
    factor_sid: str = None,
    hidden_details: str = None,
) -> Dict[str, Any]:
    """
    Create a new Challenge for the Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auth_payload:
            Optional payload used to verify the Challenge upon creation. Only used
            with a Factor of type `totp` to carry the TOTP code that
            needs to be verified. For `TOTP` this value must be between
            3 and 8 characters long.
        details_fields:
            A list of objects that describe the Fields included in the Challenge.
            Each object contains the label and value of the field, the
            label can be up to 36 characters in length and the value can
            be up to 128 characters in length. Used when `factor_type`
            is `push`. There can be up to 20 details fields.
        details_message:
            Shown to the user when the push notification arrives. Required when
            `factor_type` is `push`. Can be up to 256 characters in
            length.
        expiration_date:
            The date-time when this Challenge expires, given in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format. The
            default value is five (5) minutes after Challenge creation.
            The max value is sixty (60) minutes after creation.
        factor_sid:
            The unique SID identifier of the Factor.
        hidden_details:
            Details provided to give context about the Challenge. Not shown to the
            end user. It must be a stringified JSON with only strings
            values eg. `{"ip": "172.168.1.234"}`. Can be up to 1024
            characters in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "auth_payload": auth_payload,
        "details_fields": details_fields,
        "details_message": details_message,
        "expiration_date": expiration_date,
        "factor_sid": factor_sid,
        "hidden_details": hidden_details,
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
async def post_v2_services_service_sid_entities_identity_challenges_challenge_sid_notifications(  # noqa
    service_sid: str,
    identity: str,
    challenge_sid: str,
    twilio_credentials: "TwilioCredentials",
    ttl: int = None,
) -> Dict[str, Any]:
    """
    Create a new Notification for the corresponding Challenge.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        challenge_sid:
            Challenge sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        ttl:
            How long, in seconds, the notification is valid. Can be an integer
            between 0 and 300. Default is 300. Delivery is attempted
            until the TTL elapses, even if the device is offline. 0
            means that the notification delivery is attempted
            immediately, only once, and is not stored for future
            delivery.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications"  # noqa
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
async def get_v2_services_service_sid_entities_identity_challenges_sid(  # noqa
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Challenge.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}"  # noqa
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
async def post_v2_services_service_sid_entities_identity_challenges_sid(  # noqa
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    auth_payload: str = None,
    metadata: str = None,
) -> Dict[str, Any]:
    """
    Verify a specific Challenge.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auth_payload:
            The optional payload needed to verify the Challenge. E.g., a TOTP would
            use the numeric code. For `TOTP` this value must be between
            3 and 8 characters long. For `Push` this value can be up to
            5456 characters in length.
        metadata:
            Custom metadata associated with the challenge. This is added by the
            Device/SDK directly to allow for the inclusion of device
            information. It must be a stringified JSON with only strings
            values eg. `{"os": "Android"}`. Can be up to 1024 characters
            in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Challenges/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "auth_payload": auth_payload,
        "metadata": metadata,
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
async def get_v2_services_service_sid_entities_identity_factors(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Factors for an Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors"  # noqa
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
async def post_v2_services_service_sid_entities_identity_factors(
    service_sid: str,
    identity: str,
    twilio_credentials: "TwilioCredentials",
    binding_alg: str = None,
    binding_public_key: str = None,
    binding_secret: str = None,
    config_alg: str = None,
    config_app_id: str = None,
    config_code_length: int = None,
    config_notification_platform: str = None,
    config_notification_token: str = None,
    config_sdk_version: str = None,
    config_skew: int = None,
    config_time_step: int = None,
    factor_type: str = None,
    friendly_name: str = None,
    metadata: str = None,
) -> Dict[str, Any]:
    """
    Create a new Factor for the Entity.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        binding_alg:
            The algorithm used when `factor_type` is `push`. Algorithm supported:
            `ES256`.
        binding_public_key:
            The Ecdsa public key in PKIX, ASN.1 DER format encoded in Base64.
            Required when `factor_type` is `push`.
        binding_secret:
            The shared secret for TOTP factors encoded in Base32. This can be
            provided when creating the Factor, otherwise it will be
            generated.  Used when `factor_type` is `totp`.
        config_alg:
            The algorithm used to derive the TOTP codes. Can be `sha1`, `sha256` or
            `sha512`. Defaults to `sha1`.  Used when `factor_type` is
            `totp`.
        config_app_id:
            The ID that uniquely identifies your app in the Google or Apple store,
            such as `com.example.myapp`. It can be up to 100 characters
            long.  Required when `factor_type` is `push`.
        config_code_length:
            Number of digits for generated TOTP codes. Must be between 3 and 8,
            inclusive. The default value is defined at the service level
            in the property `totp.code_length`. If not configured
            defaults to 6.  Used when `factor_type` is `totp`.
        config_notification_platform:
            The transport technology used to generate the Notification Token. Can be
            `apn`, `fcm` or `none`.  Required when `factor_type` is
            `push`.
        config_notification_token:
            For APN, the device token. For FCM, the registration token. It is used
            to send the push notifications. Must be between 32 and 255
            characters long.  Required when `factor_type` is `push`.
        config_sdk_version:
            The Verify Push SDK version used to configure the factor  Required when
            `factor_type` is `push`.
        config_skew:
            The number of time-steps, past and future, that are valid for validation
            of TOTP codes. Must be between 0 and 2, inclusive. The
            default value is defined at the service level in the
            property `totp.skew`. If not configured defaults to 1.  Used
            when `factor_type` is `totp`.
        config_time_step:
            Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP
            code is generated every time_step seconds. Must be between
            20 and 60 seconds, inclusive. The default value is defined
            at the service level in the property `totp.time_step`.
            Defaults to 30 seconds if not configured.  Used when
            `factor_type` is `totp`.
        factor_type:
            The Type of this Factor. Currently `push` and `totp` are supported.
        friendly_name:
            The friendly name of this Factor. This can be any string up to 64
            characters, meant for humans to distinguish between Factors.
            For `factor_type` `push`, this could be a device name. For
            `factor_type` `totp`, this value is used as the “account
            name” in constructing the `binding.uri` property. At the
            same time, we recommend avoiding providing PII.
        metadata:
            Custom metadata associated with the factor. This is added by the
            Device/SDK directly to allow for the inclusion of device
            information. It must be a stringified JSON with only strings
            values eg. `{"os": "Android"}`. Can be up to 1024 characters
            in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "binding_alg": binding_alg,
        "binding_public_key": binding_public_key,
        "binding_secret": binding_secret,
        "config_alg": config_alg,
        "config_app_id": config_app_id,
        "config_code_length": config_code_length,
        "config_notification_platform": config_notification_platform,
        "config_notification_token": config_notification_token,
        "config_sdk_version": config_sdk_version,
        "config_skew": config_skew,
        "config_time_step": config_time_step,
        "factor_type": factor_type,
        "friendly_name": friendly_name,
        "metadata": metadata,
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
async def delete_v2_services_service_sid_entities_identity_factors_sid(  # noqa
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}"  # noqa
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
async def get_v2_services_service_sid_entities_identity_factors_sid(  # noqa
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Factor.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}"  # noqa
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
async def post_v2_services_service_sid_entities_identity_factors_sid(  # noqa
    service_sid: str,
    identity: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    auth_payload: str = None,
    config_alg: str = None,
    config_code_length: int = None,
    config_notification_platform: str = None,
    config_notification_token: str = None,
    config_sdk_version: str = None,
    config_skew: int = None,
    config_time_step: int = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Factor. This endpoint can be used to Verify a Factor if passed
    an `AuthPayload` param.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        identity:
            Identity used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        auth_payload:
            The optional payload needed to verify the Factor for the first time.
            E.g. for a TOTP, the numeric code.
        config_alg:
            The algorithm used to derive the TOTP codes. Can be `sha1`, `sha256` or
            `sha512`.
        config_code_length:
            Number of digits for generated TOTP codes. Must be between 3 and 8,
            inclusive.
        config_notification_platform:
            The transport technology used to generate the Notification Token. Can be
            `apn`, `fcm` or `none`.  Required when `factor_type` is
            `push`.
        config_notification_token:
            For APN, the device token. For FCM, the registration token. It is used
            to send the push notifications. Required when `factor_type`
            is `push`. If specified, this value must be between 32 and
            255 characters long.
        config_sdk_version:
            The Verify Push SDK version used to configure the factor.
        config_skew:
            The number of time-steps, past and future, that are valid for validation
            of TOTP codes. Must be between 0 and 2, inclusive.
        config_time_step:
            Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP
            code is generated every time_step seconds. Must be between
            20 and 60 seconds, inclusive.
        friendly_name:
            The new friendly name of this Factor. It can be up to 64 characters.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Entities/{identity}/Factors/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "auth_payload": auth_payload,
        "config_alg": config_alg,
        "config_code_length": config_code_length,
        "config_notification_platform": config_notification_platform,
        "config_notification_token": config_notification_token,
        "config_sdk_version": config_sdk_version,
        "config_skew": config_skew,
        "config_time_step": config_time_step,
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
async def get_v2_services_service_sid_messaging_configurations(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Messaging Configurations for a Service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations"  # noqa
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
async def post_v2_services_service_sid_messaging_configurations(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    country: str = None,
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """
    Create a new MessagingConfiguration for a service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        country:
            The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
            country code of the country this configuration will be
            applied to. If this is a global configuration, Country will
            take the value `all`.
        messaging_service_sid:
            The SID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) to be
            used to send SMS to the country of this configuration.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "country": country,
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
async def delete_v2_services_service_sid_messaging_configurations_country(  # noqa
    service_sid: str,
    country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific MessagingConfiguration.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        country:
            Country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}"  # noqa
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
async def get_v2_services_service_sid_messaging_configurations_country(  # noqa
    service_sid: str,
    country: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific MessagingConfiguration.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        country:
            Country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}"  # noqa
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
async def post_v2_services_service_sid_messaging_configurations_country(  # noqa
    service_sid: str,
    country: str,
    twilio_credentials: "TwilioCredentials",
    messaging_service_sid: str = None,
) -> Dict[str, Any]:
    """
    Update a specific MessagingConfiguration.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        country:
            Country used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        messaging_service_sid:
            The SID of the [Messaging
            Service](https://www.twilio.com/docs/sms/services/api) to be
            used to send SMS to the country of this configuration.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?](
    https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/MessagingConfigurations/{country}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
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
async def get_v2_services_service_sid_rate_limits(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Rate Limits for a service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits"  # noqa
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
async def post_v2_services_service_sid_rate_limits(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    description: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new Rate Limit for a Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            Description of this Rate Limit.
        unique_name:
            Provides a unique and addressable name to be assigned to this Rate
            Limit, assigned by the developer, to be optionally used in
            addition to SID. **This value should not contain PII.**.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "description": description,
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
async def get_v2_services_service_sid_rate_limits_rate_limit_sid_buckets(  # noqa
    service_sid: str,
    rate_limit_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Buckets for a Rate Limit.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets"  # noqa
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
async def post_v2_services_service_sid_rate_limits_rate_limit_sid_buckets(  # noqa
    service_sid: str,
    rate_limit_sid: str,
    twilio_credentials: "TwilioCredentials",
    interval: int = None,
    max: int = None,
) -> Dict[str, Any]:
    """
    Create a new Bucket for a Rate Limit.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        interval:
            Number of seconds that the rate limit will be enforced over.
        max:
            Maximum number of requests permitted in during the interval.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "interval": interval,
        "max": max,
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
async def delete_v2_services_service_sid_rate_limits_rate_limit_sid_buckets_sid(  # noqa
    service_sid: str,
    rate_limit_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Bucket.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}"  # noqa
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
async def get_v2_services_service_sid_rate_limits_rate_limit_sid_buckets_sid(  # noqa
    service_sid: str,
    rate_limit_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Bucket.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}"  # noqa
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
async def post_v2_services_service_sid_rate_limits_rate_limit_sid_buckets_sid(  # noqa
    service_sid: str,
    rate_limit_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    interval: int = None,
    max: int = None,
) -> Dict[str, Any]:
    """
    Update a specific Bucket.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        rate_limit_sid:
            Rate limit sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        interval:
            Number of seconds that the rate limit will be enforced over.
        max:
            Maximum number of requests permitted in during the interval.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "interval": interval,
        "max": max,
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
async def delete_v2_services_service_sid_rate_limits_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Rate Limit.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}"  # noqa
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
async def get_v2_services_service_sid_rate_limits_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Rate Limit.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}"  # noqa
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
async def post_v2_services_service_sid_rate_limits_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    description: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Rate Limit.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        description:
            Description of this Rate Limit.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/RateLimits/{sid}"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "description": description,
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
async def post_v2_services_service_sid_verification_check(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    amount: str = None,
    code: str = None,
    payee: str = None,
    to: str = None,
    verification_sid: str = None,
) -> Dict[str, Any]:
    """
    challenge a specific Verification Check.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        amount:
            The amount of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        code:
            The 4-10 character string being verified.
        payee:
            The payee of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        to:
            The phone number or [email](https://www.twilio.com/docs/verify/email) to
            verify. Either this parameter or the `verification_sid` must
            be specified. Phone numbers must be in [E.164
            format](https://www.twilio.com/docs/glossary/what-e164).
        verification_sid:
            A SID that uniquely identifies the Verification Check. Either this
            parameter or the `to` phone
            number/[email](https://www.twilio.com/docs/verify/email)
            must be specified.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/VerificationCheck?](
    https://verify.twilio.com/v2/Services/{service_sid}/VerificationCheck?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://verify.twilio.com/v2/Services/{service_sid}/VerificationCheck"  # noqa
    )
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "amount": amount,
        "code": code,
        "payee": payee,
        "to": to,
        "verification_sid": verification_sid,
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
async def post_v2_services_service_sid_verifications(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    amount: str = None,
    app_hash: str = None,
    channel: str = None,
    channel_configuration: str = None,
    custom_code: str = None,
    custom_friendly_name: str = None,
    custom_message: str = None,
    locale: str = None,
    payee: str = None,
    rate_limits: str = None,
    send_digits: str = None,
    template_custom_substitutions: str = None,
    template_sid: str = None,
    to: str = None,
) -> Dict[str, Any]:
    """
    Create a new Verification using a Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        amount:
            The amount of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        app_hash:
            Your [App Hash](https://developers.google.com/identity/sms-
            retriever/verify
            computing_your_apps_hash_string) to be appended at the end
            of your verification SMS body. Applies only to SMS. Example
            SMS body: `<
            > Your AppName verification code is: 1234 He42w354ol9`.
        channel:
            The verification method to use. Can be:
            [`email`](https://www.twilio.com/docs/verify/email), `sms`,
            `whatsapp` or `call`.
        channel_configuration:
            [`email`](https://www.twilio.com/docs/verify/email) channel
            configuration in json format. The fields 'from' and
            'from_name' are optional but if included the 'from' field
            must have a valid email address.
        custom_code:
            A pre-generated code to use for verification. The code can be between 4
            and 10 characters, inclusive.
        custom_friendly_name:
            A custom user defined friendly name that overwrites the existing one in
            the verification message.
        custom_message:
            The text of a custom message to use for the verification.
        locale:
            The locale to use for the verification SMS, WhatsApp or call. Can be:
            `af`, `ar`, `ca`, `cs`, `da`, `de`, `el`, `en`, `en-GB`,
            `es`, `fi`, `fr`, `he`, `hi`, `hr`, `hu`, `id`, `it`, `ja`,
            `ko`, `ms`, `nb`, `nl`, `pl`, `pt`, `pr-BR`, `ro`, `ru`,
            `sv`, `th`, `tl`, `tr`, `vi`, `zh`, `zh-CN`, or `zh-HK.`.
        payee:
            The payee of the associated PSD2 compliant transaction. Requires the
            PSD2 Service flag enabled.
        rate_limits:
            The custom key-value pairs of Programmable Rate Limits. Keys correspond
            to `unique_name` fields defined when [creating your Rate
            Limit](https://www.twilio.com/docs/verify/api/service-rate-
            limits). Associated value pairs represent values in the
            request that you are rate limiting on. You may include
            multiple Rate Limit values in each request.
        send_digits:
            The digits to send after a phone call is answered, for example, to dial
            an extension. For more information, see the Programmable
            Voice documentation of
            [sendDigits](https://www.twilio.com/docs/voice/twiml/number
            attributes-sendDigits).
        template_custom_substitutions:
            A stringified JSON object in which the keys are the template's special
            variables and the values are the variables substitutions.
        template_sid:
            The message
            [template](https://www.twilio.com/docs/verify/api/templates).
            If provided, will override the default template for the
            Service. SMS channel only.
        to:
            The phone number or [email](https://www.twilio.com/docs/verify/email) to
            verify. Phone numbers must be in [E.164
            format](https://www.twilio.com/docs/glossary/what-e164).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Verifications?](
    https://verify.twilio.com/v2/Services/{service_sid}/Verifications?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "amount": amount,
        "app_hash": app_hash,
        "channel": channel,
        "channel_configuration": channel_configuration,
        "custom_code": custom_code,
        "custom_friendly_name": custom_friendly_name,
        "custom_message": custom_message,
        "locale": locale,
        "payee": payee,
        "rate_limits": rate_limits,
        "send_digits": send_digits,
        "template_custom_substitutions": template_custom_substitutions,
        "template_sid": template_sid,
        "to": to,
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
async def get_v2_services_service_sid_verifications_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Verification.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}"  # noqa
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
async def post_v2_services_service_sid_verifications_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """
    Update a Verification status.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The new status of the resource. Can be: `canceled` or `approved`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Verifications/{sid}"  # noqa
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
async def get_v2_services_service_sid_webhooks(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Webhooks for a Service.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?&page_size=%s](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks"  # noqa
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
async def post_v2_services_service_sid_webhooks(
    service_sid: str,
    twilio_credentials: "TwilioCredentials",
    event_types: list = None,
    friendly_name: str = None,
    status: str = None,
    version: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """
    Create a new Webhook for the Service.

    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        event_types:
            The array of events that this Webhook is subscribed to. Possible event
            types: `*, factor.deleted, factor.created, factor.verified,
            challenge.approved, challenge.denied`.
        friendly_name:
            The string that you assigned to describe the webhook. **This value
            should not contain PII.**.
        status:
            The webhook status. Default value is `enabled`. One of: `enabled` or
            `disabled`.
        version:
            The webhook version. Default value is `v2` which includes all the latest
            fields. Version `v1` is legacy and may be removed in the
            future.
        webhook_url:
            The URL associated with this Webhook.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "event_types": event_types,
        "friendly_name": friendly_name,
        "status": status,
        "version": version,
        "webhook_url": webhook_url,
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
async def delete_v2_services_service_sid_webhooks_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Webhook.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}"  # noqa
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
async def get_v2_services_service_sid_webhooks_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch a specific Webhook.

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
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}"  # noqa
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
async def post_v2_services_service_sid_webhooks_sid(
    service_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    event_types: list = None,
    friendly_name: str = None,
    status: str = None,
    version: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        service_sid:
            Service sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        event_types:
            The array of events that this Webhook is subscribed to. Possible event
            types: `*, factor.deleted, factor.created, factor.verified,
            challenge.approved, challenge.denied`.
        friendly_name:
            The string that you assigned to describe the webhook. **This value
            should not contain PII.**.
        status:
            The webhook status. Default value is `enabled`. One of: `enabled` or
            `disabled`.
        version:
            The webhook version. Default value is `v2` which includes all the latest
            fields. Version `v1` is legacy and may be removed in the
            future.
        webhook_url:
            The URL associated with this Webhook.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?](
    https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{service_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "event_types": event_types,
        "friendly_name": friendly_name,
        "status": status,
        "version": version,
        "webhook_url": webhook_url,
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
async def delete_v2_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a specific Verification Service Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{sid}?](
    https://verify.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{sid}"  # noqa
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
async def get_v2_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch specific Verification Service Instance.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{sid}?](
    https://verify.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{sid}"  # noqa
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
async def post_v2_services_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    code_length: int = None,
    custom_code_enabled: bool = None,
    default_template_sid: str = None,
    do_not_share_warning_enabled: bool = None,
    dtmf_input_required: bool = None,
    friendly_name: str = None,
    lookup_enabled: bool = None,
    psd2_enabled: bool = None,
    push_apn_credential_sid: str = None,
    push_fcm_credential_sid: str = None,
    push_include_date: bool = None,
    skip_sms_to_landlines: bool = None,
    totp_code_length: int = None,
    totp_issuer: str = None,
    totp_skew: int = None,
    totp_time_step: int = None,
    tts_name: str = None,
) -> Dict[str, Any]:
    """
    Update a specific Verification Service.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        code_length:
            The length of the verification code to generate. Must be an integer
            value between 4 and 10, inclusive.
        custom_code_enabled:
            Whether to allow sending verifications with a custom code instead of a
            randomly generated one. Not available for all customers.
        default_template_sid:
            The default message
            [template](https://www.twilio.com/docs/verify/api/templates).
            Will be used for all SMS verifications unless explicitly
            overriden. SMS channel only.
        do_not_share_warning_enabled:
            Whether to add a privacy warning at the end of an SMS. **Disabled by
            default and applies only for SMS.**.
        dtmf_input_required:
            Whether to ask the user to press a number before delivering the verify
            code in a phone call.
        friendly_name:
            A descriptive string that you create to describe the verification
            service. It can be up to 30 characters long. **This value
            should not contain PII.**.
        lookup_enabled:
            Whether to perform a lookup with each verification started and return
            info about the phone number.
        psd2_enabled:
            Whether to pass PSD2 transaction parameters when starting a
            verification.
        push_apn_credential_sid:
            Optional configuration for the Push factors. Set the APN Credential for
            this service. This will allow to send push notifications to
            iOS devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_fcm_credential_sid:
            Optional configuration for the Push factors. Set the FCM Credential for
            this service. This will allow to send push notifications to
            Android devices. See [Credential
            Resource](https://www.twilio.com/docs/notify/api/credential-
            resource).
        push_include_date:
            Optional configuration for the Push factors. If true, include the date
            in the Challenge's response. Otherwise, the date is omitted
            from the response. See
            [Challenge](https://www.twilio.com/docs/verify/api/challenge)
            resource’s details parameter for more info. Default: false.
            **Deprecated** do not use this parameter.
        skip_sms_to_landlines:
            Whether to skip sending SMS verifications to landlines. Requires
            `lookup_enabled`.
        totp_code_length:
            Optional configuration for the TOTP factors. Number of digits for
            generated TOTP codes. Must be between 3 and 8, inclusive.
            Defaults to 6.
        totp_issuer:
            Optional configuration for the TOTP factors. Set TOTP Issuer for this
            service. This will allow to configure the issuer of the TOTP
            URI.
        totp_skew:
            Optional configuration for the TOTP factors. The number of time-steps,
            past and future, that are valid for validation of TOTP
            codes. Must be between 0 and 2, inclusive. Defaults to 1.
        totp_time_step:
            Optional configuration for the TOTP factors. Defines how often, in
            seconds, are TOTP codes generated. i.e, a new TOTP code is
            generated every time_step seconds. Must be between 20 and 60
            seconds, inclusive. Defaults to 30 seconds.
        tts_name:
            The name of an alternative text-to-speech service to use in phone calls.
            Applies only to TTS languages.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Services/{sid}?](
    https://verify.twilio.com/v2/Services/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://verify.twilio.com/v2/Services/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "code_length": code_length,
        "custom_code_enabled": custom_code_enabled,
        "default_template_sid": default_template_sid,
        "do_not_share_warning_enabled": do_not_share_warning_enabled,
        "dtmf_input_required": dtmf_input_required,
        "friendly_name": friendly_name,
        "lookup_enabled": lookup_enabled,
        "psd2_enabled": psd2_enabled,
        "push_apn_credential_sid": push_apn_credential_sid,
        "push_fcm_credential_sid": push_fcm_credential_sid,
        "push_include_date": push_include_date,
        "skip_sms_to_landlines": skip_sms_to_landlines,
        "totp_code_length": totp_code_length,
        "totp_issuer": totp_issuer,
        "totp_skew": totp_skew,
        "totp_time_step": totp_time_step,
        "tts_name": tts_name,
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
async def get_v2_templates(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List all the available templates for a given Account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            String filter used to query templates with a given friendly name.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://verify.twilio.com/v2/Templates?&friendly_name=%s&page_size=%s](
    https://verify.twilio.com/v2/Templates?&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://verify.twilio.com/v2/Templates"  # noqa

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
