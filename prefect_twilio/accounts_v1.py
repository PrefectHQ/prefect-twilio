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
async def post_v1_auth_tokens_promote(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Promote the secondary Auth Token to primary. After promoting the new token, all
    requests to Twilio using your old primary Auth Token will result in an
    error.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/AuthTokens/Promote?](
    https://accounts.twilio.com/v1/AuthTokens/Promote?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/AuthTokens/Promote"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def delete_v1_auth_tokens_secondary(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete the secondary Auth Token from your account.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/AuthTokens/Secondary?](
    https://accounts.twilio.com/v1/AuthTokens/Secondary?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/AuthTokens/Secondary"  # noqa

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
async def post_v1_auth_tokens_secondary(
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Create a new secondary Auth Token.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/AuthTokens/Secondary?](
    https://accounts.twilio.com/v1/AuthTokens/Secondary?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/AuthTokens/Secondary"  # noqa

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
async def get_v1_credentials_aws(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieves a collection of AWS Credentials belonging to the account used to make
    the request.

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
    [https://accounts.twilio.com/v1/Credentials/AWS?&page_size=%s](
    https://accounts.twilio.com/v1/Credentials/AWS?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/Credentials/AWS"  # noqa

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
async def post_v1_credentials_aws(
    twilio_credentials: "TwilioCredentials",
    account_sid: str = None,
    credentials: str = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Create a new AWS Credential.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        account_sid:
            The SID of the Subaccount that this Credential should be associated
            with. Must be a valid Subaccount of the account issuing the
            request.
        credentials:
            A string that contains the AWS access credentials in the format
            `<AWS_ACCESS_KEY_ID>:<AWS_SECRET_ACCESS_KEY>`. For example,
            `AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/Credentials/AWS?](
    https://accounts.twilio.com/v1/Credentials/AWS?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/Credentials/AWS"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "account_sid": account_sid,
        "credentials": credentials,
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
async def delete_v1_credentials_aws_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Credential from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/Credentials/AWS/{sid}?](
    https://accounts.twilio.com/v1/Credentials/AWS/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://accounts.twilio.com/v1/Credentials/AWS/{sid}"  # noqa
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
async def get_v1_credentials_aws_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the AWS credentials specified by the provided Credential Sid.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/Credentials/AWS/{sid}?](
    https://accounts.twilio.com/v1/Credentials/AWS/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://accounts.twilio.com/v1/Credentials/AWS/{sid}"  # noqa
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
async def post_v1_credentials_aws_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Modify the properties of a given Account.

    Args:
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
    [https://accounts.twilio.com/v1/Credentials/AWS/{sid}?](
    https://accounts.twilio.com/v1/Credentials/AWS/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://accounts.twilio.com/v1/Credentials/AWS/{sid}"  # noqa
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
async def get_v1_credentials_public_keys(
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieves a collection of Public Key Credentials belonging to the account used
    to make the request.

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
    [https://accounts.twilio.com/v1/Credentials/PublicKeys?&page_size=%s](
    https://accounts.twilio.com/v1/Credentials/PublicKeys?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/Credentials/PublicKeys"  # noqa

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
async def post_v1_credentials_public_keys(
    twilio_credentials: "TwilioCredentials",
    account_sid: str = None,
    friendly_name: str = None,
    public_key: str = None,
) -> Dict[str, Any]:
    """
    Create a new Public Key Credential.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        account_sid:
            The SID of the Subaccount that this Credential should be associated
            with. Must be a valid Subaccount of the account issuing the
            request.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to 64 characters long.
        public_key:
            A URL encoded representation of the public key. For example, `-----BEGIN
            PUBLIC KEY-----MIIBIjANB.pa9xQIDAQAB-----END PUBLIC
            KEY-----`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/Credentials/PublicKeys?](
    https://accounts.twilio.com/v1/Credentials/PublicKeys?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://accounts.twilio.com/v1/Credentials/PublicKeys"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "account_sid": account_sid,
        "friendly_name": friendly_name,
        "public_key": public_key,
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
async def delete_v1_credentials_public_keys_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Credential from your account.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/Credentials/PublicKeys/{sid}?](
    https://accounts.twilio.com/v1/Credentials/PublicKeys/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://accounts.twilio.com/v1/Credentials/PublicKeys/{sid}"  # noqa
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
async def get_v1_credentials_public_keys_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch the public key specified by the provided Credential Sid.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.twilio.com/v1/Credentials/PublicKeys/{sid}?](
    https://accounts.twilio.com/v1/Credentials/PublicKeys/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://accounts.twilio.com/v1/Credentials/PublicKeys/{sid}"  # noqa
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
async def post_v1_credentials_public_keys_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """
    Modify the properties of a given Account.

    Args:
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
    [https://accounts.twilio.com/v1/Credentials/PublicKeys/{sid}?](
    https://accounts.twilio.com/v1/Credentials/PublicKeys/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://accounts.twilio.com/v1/Credentials/PublicKeys/{sid}"  # noqa
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
