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
async def get_v1_composition_settings_default(
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
    [https://video.twilio.com/v1/CompositionSettings/Default?](
    https://video.twilio.com/v1/CompositionSettings/Default?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://video.twilio.com/v1/CompositionSettings/Default"  # noqa

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
async def post_v1_composition_settings_default(
    twilio_credentials: "TwilioCredentials",
    aws_credentials_sid: str = None,
    aws_s3_url: str = None,
    aws_storage_enabled: bool = None,
    encryption_enabled: bool = None,
    encryption_key_sid: str = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        aws_credentials_sid:
            The SID of the stored Credential resource.
        aws_s3_url:
            The URL of the AWS S3 bucket where the compositions should be stored. We
            only support DNS-compliant URLs like `https://documentation-
            example-twilio-bucket/compositions`, where `compositions` is
            the path in which you want the compositions to be stored.
            This URL accepts only URI-valid characters, as described in
            the <a href='https://tools.ietf.org/html/rfc3986
            section-2'>RFC 3986</a>.
        aws_storage_enabled:
            Whether all compositions should be written to the `aws_s3_url`. When
            `false`, all compositions are stored in our cloud.
        encryption_enabled:
            Whether all compositions should be stored in an encrypted form. The
            default is `false`.
        encryption_key_sid:
            The SID of the Public Key resource to use for encryption.
        friendly_name:
            A descriptive string that you create to describe the resource and show
            to the user in the console.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/CompositionSettings/Default?](
    https://video.twilio.com/v1/CompositionSettings/Default?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://video.twilio.com/v1/CompositionSettings/Default"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "aws_credentials_sid": aws_credentials_sid,
        "aws_s3_url": aws_s3_url,
        "aws_storage_enabled": aws_storage_enabled,
        "encryption_enabled": encryption_enabled,
        "encryption_key_sid": encryption_key_sid,
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
