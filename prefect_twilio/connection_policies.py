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
async def get_v1_connection_policies(
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
    [https://voice.twilio.com/v1/ConnectionPolicies?&page_size=%s](
    https://voice.twilio.com/v1/ConnectionPolicies?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://voice.twilio.com/v1/ConnectionPolicies"  # noqa

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
async def post_v1_connection_policies(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies?](
    https://voice.twilio.com/v1/ConnectionPolicies?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://voice.twilio.com/v1/ConnectionPolicies"  # noqa

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
async def get_v1_connection_policies_connection_policy_sid_targets(
    connection_policy_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets?&page_size=%s](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets"  # noqa
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
async def post_v1_connection_policies_connection_policy_sid_targets(
    connection_policy_sid: str,
    twilio_credentials: "TwilioCredentials",
    enabled: bool = None,
    friendly_name: str = None,
    priority: int = None,
    target: str = None,
    weight: int = None,
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        enabled:
            Whether the Target is enabled. The default is `true`.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        priority:
            The relative importance of the target. Can be an integer from 0 to
            65535, inclusive, and the default is 10. The lowest number
            represents the most important target.
        target:
            The SIP address you want Twilio to route your calls to. This must be a
            `sip:` schema. `sips` is NOT supported.
        weight:
            The value that determines the relative share of the load the Target
            should receive compared to other Targets with the same
            priority. Can be an integer from 1 to 65535, inclusive, and
            the default is 10. Targets with higher values receive more
            load than those with lower ones with the same priority.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets?](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "enabled": enabled,
        "friendly_name": friendly_name,
        "priority": priority,
        "target": target,
        "weight": weight,
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
async def delete_v1_connection_policies_connection_policy_sid_targets_sid(
    connection_policy_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}"  # noqa
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
async def get_v1_connection_policies_connection_policy_sid_targets_sid(
    connection_policy_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}"  # noqa
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
async def post_v1_connection_policies_connection_policy_sid_targets_sid(
    connection_policy_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    enabled: bool = None,
    friendly_name: str = None,
    priority: int = None,
    target: str = None,
    weight: int = None,
) -> Dict[str, Any]:
    """


    Args:
        connection_policy_sid:
            Connection policy sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        enabled:
            Whether the Target is enabled.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        priority:
            The relative importance of the target. Can be an integer from 0 to
            65535, inclusive. The lowest number represents the most
            important target.
        target:
            The SIP address you want Twilio to route your calls to. This must be a
            `sip:` schema. `sips` is NOT supported.
        weight:
            The value that determines the relative share of the load the Target
            should receive compared to other Targets with the same
            priority. Can be an integer from 1 to 65535, inclusive.
            Targets with higher values receive more load than those with
            lower ones with the same priority.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "enabled": enabled,
        "friendly_name": friendly_name,
        "priority": priority,
        "target": target,
        "weight": weight,
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
async def delete_v1_connection_policies_sid(
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
    [https://voice.twilio.com/v1/ConnectionPolicies/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{sid}"  # noqa
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
async def get_v1_connection_policies_sid(
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
    [https://voice.twilio.com/v1/ConnectionPolicies/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{sid}"  # noqa
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
async def post_v1_connection_policies_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://voice.twilio.com/v1/ConnectionPolicies/{sid}?](
    https://voice.twilio.com/v1/ConnectionPolicies/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://voice.twilio.com/v1/ConnectionPolicies/{sid}"  # noqa
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
