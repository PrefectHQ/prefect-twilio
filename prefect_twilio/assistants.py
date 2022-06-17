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
async def get_v1_assistants(
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
    [https://autopilot.twilio.com/v1/Assistants?&page_size=%s](
    https://autopilot.twilio.com/v1/Assistants?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://autopilot.twilio.com/v1/Assistants"  # noqa

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
async def post_v1_assistants(
    twilio_credentials: "TwilioCredentials",
    callback_events: str = None,
    callback_url: str = None,
    defaults: str = None,
    friendly_name: str = None,
    log_queries: bool = None,
    style_sheet: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_events:
            Reserved.
        callback_url:
            Reserved.
        defaults:
            A JSON object that defines the Assistant's [default
            tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults)
            for various scenarios, including initiation actions and
            fallback tasks.
        friendly_name:
            A descriptive string that you create to describe the new resource. It is
            not unique and can be up to 255 characters long.
        log_queries:
            Whether queries should be logged and kept after training. Can be: `true`
            or `false` and defaults to `true`. If `true`, queries are
            stored for 30 days, and then deleted. If `false`, no queries
            are stored.
        style_sheet:
            The JSON string that defines the Assistant's [style
            sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet).
        unique_name:
            An application-defined string that uniquely identifies the new resource.
            It can be used as an alternative to the `sid` in the URL
            path to address the resource. The first 64 characters must
            be unique.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants?](
    https://autopilot.twilio.com/v1/Assistants?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://autopilot.twilio.com/v1/Assistants"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "callback_events": callback_events,
        "callback_url": callback_url,
        "defaults": defaults,
        "friendly_name": friendly_name,
        "log_queries": log_queries,
        "style_sheet": style_sheet,
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
async def post_v1_assistants_restore(
    twilio_credentials: "TwilioCredentials",
    assistant: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        assistant:
            The Twilio-provided string that uniquely identifies the Assistant
            resource to restore.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/Restore?](
    https://autopilot.twilio.com/v1/Assistants/Restore?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://autopilot.twilio.com/v1/Assistants/Restore"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "assistant": assistant,
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
async def get_v1_assistants_assistant_sid_defaults(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Defaults?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Defaults?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Defaults"  # noqa
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
async def post_v1_assistants_assistant_sid_defaults(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    defaults: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        defaults:
            A JSON string that describes the default task links for the
            `assistant_initiation`, `collect`, and `fallback`
            situations.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Defaults?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Defaults?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Defaults"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "defaults": defaults,
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
async def get_v1_assistants_assistant_sid_dialogues_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Dialogues/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Dialogues/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Dialogues/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_field_types(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes?&page_size=%s](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes"  # noqa
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
async def post_v1_assistants_assistant_sid_field_types(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the new resource. It is
            not unique and can be up to 255 characters long.
        unique_name:
            An application-defined string that uniquely identifies the new resource.
            It can be used as an alternative to the `sid` in the URL
            path to address the resource. The first 64 characters must
            be unique.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes"  # noqa
    )
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v1_assistants_assistant_sid_field_types_field_type_sid_field_values(
    assistant_sid: str,
    field_type_sid: str,
    twilio_credentials: "TwilioCredentials",
    language: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        field_type_sid:
            Field type sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        language:
            The [ISO language-
            country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html)
            tag that specifies the language of the value. Currently
            supported tags: `en-US`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues?&language=%s&page_size=%s](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues?&language=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "language": language,
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
async def post_v1_assistants_assistant_sid_field_types_field_type_sid_field_values(
    assistant_sid: str,
    field_type_sid: str,
    twilio_credentials: "TwilioCredentials",
    language: str = None,
    synonym_of: str = None,
    value: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        field_type_sid:
            Field type sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        language:
            The [ISO language-
            country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html)
            tag that specifies the language of the value. Currently
            supported tags: `en-US`.
        synonym_of:
            The string value that indicates which word the field value is a synonym
            of.
        value:
            The Field Value data.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "language": language,
        "synonym_of": synonym_of,
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
async def delete_v1_assistants_assistant_sid_field_types_field_type_sid_field_values_sid(
    assistant_sid: str,
    field_type_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        field_type_sid:
            Field type sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_field_types_field_type_sid_field_values_sid(
    assistant_sid: str,
    field_type_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        field_type_sid:
            Field type sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues/{sid}"  # noqa
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
async def delete_v1_assistants_assistant_sid_field_types_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_field_types_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{sid}"  # noqa
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
async def post_v1_assistants_assistant_sid_field_types_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used as an alternative to the `sid` in the URL path
            to address the resource. The first 64 characters must be
            unique.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/FieldTypes/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "friendly_name": friendly_name,
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
async def get_v1_assistants_assistant_sid_model_builds(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds?&page_size=%s](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds"  # noqa
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
async def post_v1_assistants_assistant_sid_model_builds(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    status_callback: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status_callback:
            The URL we should call using a POST method to send status information to
            your application.
        unique_name:
            An application-defined string that uniquely identifies the new resource.
            This value must be a unique string of no more than 64
            characters. It can be used as an alternative to the `sid` in
            the URL path to address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "status_callback": status_callback,
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
async def delete_v1_assistants_assistant_sid_model_builds_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_model_builds_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds/{sid}"  # noqa
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
async def post_v1_assistants_assistant_sid_model_builds_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        unique_name:
            An application-defined string that uniquely identifies the resource.
            This value must be a unique string of no more than 64
            characters. It can be used as an alternative to the `sid` in
            the URL path to address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/ModelBuilds/{sid}"  # noqa
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


@task
async def get_v1_assistants_assistant_sid_queries(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    language: str = None,
    model_build: str = None,
    status: str = None,
    dialogue_sid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        language:
            The [ISO language-
            country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html)
            string that specifies the language used by the Query
            resources to read. For example: `en-US`.
        model_build:
            The SID or unique name of the [Model
            Build](https://www.twilio.com/docs/autopilot/api/model-
            build) to be queried.
        status:
            The status of the resources to read. Can be: `pending-review`,
            `reviewed`, or `discarded`.
        dialogue_sid:
            The SID of the
            [Dialogue](https://www.twilio.com/docs/autopilot/api/dialogue).
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries?&language=%s&model_build=%s&status=%s&dialogue_sid=%s&page_size=%s](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries?&language=%s&model_build=%s&status=%s&dialogue_sid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "language": language,
        "model_build": model_build,
        "status": status,
        "dialogue_sid": dialogue_sid,
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
async def post_v1_assistants_assistant_sid_queries(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    language: str = None,
    model_build: str = None,
    query: str = None,
    tasks: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        language:
            The [ISO language-
            country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html)
            string that specifies the language used for the new query.
            For example: `en-US`.
        model_build:
            The SID or unique name of the [Model
            Build](https://www.twilio.com/docs/autopilot/api/model-
            build) to be queried.
        query:
            The end-user's natural language input. It can be up to 2048 characters
            long.
        tasks:
            The list of tasks to limit the new query to. Tasks are expressed as a
            comma-separated list of task `unique_name` values. For
            example, `task-unique_name-1, task-unique_name-2`. Listing
            specific tasks is useful to constrain the paths that a user
            can take.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "language": language,
        "model_build": model_build,
        "query": query,
        "tasks": tasks,
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
async def delete_v1_assistants_assistant_sid_queries_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_queries_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries/{sid}"  # noqa
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
async def post_v1_assistants_assistant_sid_queries_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    sample_sid: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        sample_sid:
            The SID of an optional reference to the
            [Sample](https://www.twilio.com/docs/autopilot/api/task-
            sample) created from the query.
        status:
            The new status of the resource. Can be: `pending-review`, `reviewed`, or
            `discarded`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Queries/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "sample_sid": sample_sid,
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
async def get_v1_assistants_assistant_sid_style_sheet(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns Style sheet JSON object for the Assistant.

    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/StyleSheet?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/StyleSheet?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/StyleSheet"  # noqa
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
async def post_v1_assistants_assistant_sid_style_sheet(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    style_sheet: str = None,
) -> Dict[str, Any]:
    """
    Updates the style sheet for an Assistant identified by `assistant_sid`.

    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        style_sheet:
            The JSON string that describes the style sheet object.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/StyleSheet?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/StyleSheet?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/StyleSheet"  # noqa
    )
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "style_sheet": style_sheet,
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
async def get_v1_assistants_assistant_sid_tasks(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks?&page_size=%s](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks"  # noqa
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
async def post_v1_assistants_assistant_sid_tasks(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    actions: str = None,
    actions_url: str = None,
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        actions:
            The JSON string that specifies the
            [actions](https://www.twilio.com/docs/autopilot/actions)
            that instruct the Assistant on how to perform the task. It
            is optional and not unique.
        actions_url:
            The URL from which the Assistant can fetch actions.
        friendly_name:
            A descriptive string that you create to describe the new resource. It is
            not unique and can be up to 255 characters long.
        unique_name:
            An application-defined string that uniquely identifies the new resource.
            It can be used as an alternative to the `sid` in the URL
            path to address the resource. This value must be unique and
            64 characters or less in length.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "actions": actions,
        "actions_url": actions_url,
        "friendly_name": friendly_name,
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
async def delete_v1_assistants_assistant_sid_tasks_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_tasks_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{sid}"  # noqa
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
async def post_v1_assistants_assistant_sid_tasks_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    actions: str = None,
    actions_url: str = None,
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        actions:
            The JSON string that specifies the
            [actions](https://www.twilio.com/docs/autopilot/actions)
            that instruct the Assistant on how to perform the task.
        actions_url:
            The URL from which the Assistant can fetch actions.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        unique_name:
            An application-defined string that uniquely identifies the resource.
            This value must be 64 characters or less in length and be
            unique. It can be used as an alternative to the `sid` in the
            URL path to address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "actions": actions,
        "actions_url": actions_url,
        "friendly_name": friendly_name,
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
async def get_v1_assistants_assistant_sid_tasks_task_sid_actions(
    assistant_sid: str,
    task_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns JSON actions for the Task.

    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Actions?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Actions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Actions"  # noqa
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
async def post_v1_assistants_assistant_sid_tasks_task_sid_actions(
    assistant_sid: str,
    task_sid: str,
    twilio_credentials: "TwilioCredentials",
    actions: str = None,
) -> Dict[str, Any]:
    """
    Updates the actions of an Task identified by {TaskSid} or {TaskUniqueName}.

    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        actions:
            The JSON string that specifies the
            [actions](https://www.twilio.com/docs/autopilot/actions)
            that instruct the Assistant on how to perform the task.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Actions?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Actions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Actions"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "actions": actions,
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
async def get_v1_assistants_assistant_sid_tasks_task_sid_fields(
    assistant_sid: str,
    task_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields?&page_size=%s](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields"  # noqa
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
async def post_v1_assistants_assistant_sid_tasks_task_sid_fields(
    assistant_sid: str,
    task_sid: str,
    twilio_credentials: "TwilioCredentials",
    field_type: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        field_type:
            The Field Type of the new field. Can be: a [Built-in Field
            Type](https://www.twilio.com/docs/autopilot/built-in-field-
            types), the `unique_name`, or the `sid` of a custom Field
            Type.
        unique_name:
            An application-defined string that uniquely identifies the new resource.
            This value must be a unique string of no more than 64
            characters. It can be used as an alternative to the `sid` in
            the URL path to address the resource.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "field_type": field_type,
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
async def delete_v1_assistants_assistant_sid_tasks_task_sid_fields_sid(
    assistant_sid: str,
    task_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_tasks_task_sid_fields_sid(
    assistant_sid: str,
    task_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_tasks_task_sid_samples(
    assistant_sid: str,
    task_sid: str,
    twilio_credentials: "TwilioCredentials",
    language: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        language:
            The [ISO language-
            country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html)
            string that specifies the language used for the sample. For
            example: `en-US`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples?&language=%s&page_size=%s](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples?&language=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "language": language,
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
async def post_v1_assistants_assistant_sid_tasks_task_sid_samples(
    assistant_sid: str,
    task_sid: str,
    twilio_credentials: "TwilioCredentials",
    language: str = None,
    source_channel: str = None,
    tagged_text: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        language:
            The [ISO language-
            country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html)
            string that specifies the language used for the new sample.
            For example: `en-US`.
        source_channel:
            The communication channel from which the new sample was captured. Can
            be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`,
            `slack`, or null if not included.
        tagged_text:
            The text example of how end users might express the task. The sample can
            contain [Field tag
            blocks](https://www.twilio.com/docs/autopilot/api/task-
            sample
            field-tagging).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "language": language,
        "source_channel": source_channel,
        "tagged_text": tagged_text,
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
async def delete_v1_assistants_assistant_sid_tasks_task_sid_samples_sid(
    assistant_sid: str,
    task_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_tasks_task_sid_samples_sid(
    assistant_sid: str,
    task_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}"  # noqa
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
async def post_v1_assistants_assistant_sid_tasks_task_sid_samples_sid(
    assistant_sid: str,
    task_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    language: str = None,
    source_channel: str = None,
    tagged_text: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        language:
            The [ISO language-
            country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html)
            string that specifies the language used for the sample. For
            example: `en-US`.
        source_channel:
            The communication channel from which the sample was captured. Can be:
            `voice`, `sms`, `chat`, `alexa`, `google-assistant`,
            `slack`, or null if not included.
        tagged_text:
            The text example of how end users might express the task. The sample can
            contain [Field tag
            blocks](https://www.twilio.com/docs/autopilot/api/task-
            sample
            field-tagging).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "language": language,
        "source_channel": source_channel,
        "tagged_text": tagged_text,
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
async def get_v1_assistants_assistant_sid_tasks_task_sid_statistics(
    assistant_sid: str,
    task_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Statistics?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Statistics?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Statistics"  # noqa
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
async def get_v1_assistants_assistant_sid_webhooks(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks?&page_size=%s](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks"  # noqa
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
async def post_v1_assistants_assistant_sid_webhooks(
    assistant_sid: str,
    twilio_credentials: "TwilioCredentials",
    events: str = None,
    unique_name: str = None,
    webhook_method: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        events:
            The list of space-separated events that this Webhook will subscribe to.
        unique_name:
            An application-defined string that uniquely identifies the new resource.
            It can be used as an alternative to the `sid` in the URL
            path to address the resource. This value must be unique and
            64 characters or less in length.
        webhook_method:
            The method to be used when calling the webhook's URL.
        webhook_url:
            The URL associated with this Webhook.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "events": events,
        "unique_name": unique_name,
        "webhook_method": webhook_method,
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
async def delete_v1_assistants_assistant_sid_webhooks_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks/{sid}"  # noqa
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
async def get_v1_assistants_assistant_sid_webhooks_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks/{sid}"  # noqa
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
async def post_v1_assistants_assistant_sid_webhooks_sid(
    assistant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    events: str = None,
    unique_name: str = None,
    webhook_method: str = None,
    webhook_url: str = None,
) -> Dict[str, Any]:
    """


    Args:
        assistant_sid:
            Assistant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        events:
            The list of space-separated events that this Webhook will subscribe to.
        unique_name:
            An application-defined string that uniquely identifies the new resource.
            It can be used as an alternative to the `sid` in the URL
            path to address the resource. This value must be unique and
            64 characters or less in length.
        webhook_method:
            The method to be used when calling the webhook's URL.
        webhook_url:
            The URL associated with this Webhook.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{assistant_sid}/Webhooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "events": events,
        "unique_name": unique_name,
        "webhook_method": webhook_method,
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
async def delete_v1_assistants_sid(
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
    [https://autopilot.twilio.com/v1/Assistants/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{sid}"  # noqa
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
async def get_v1_assistants_sid(
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
    [https://autopilot.twilio.com/v1/Assistants/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{sid}"  # noqa
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
async def post_v1_assistants_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    callback_events: str = None,
    callback_url: str = None,
    defaults: str = None,
    development_stage: str = None,
    friendly_name: str = None,
    log_queries: bool = None,
    style_sheet: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_events:
            Reserved.
        callback_url:
            Reserved.
        defaults:
            A JSON object that defines the Assistant's [default
            tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults)
            for various scenarios, including initiation actions and
            fallback tasks.
        development_stage:
            A string describing the state of the assistant.
        friendly_name:
            A descriptive string that you create to describe the resource. It is not
            unique and can be up to 255 characters long.
        log_queries:
            Whether queries should be logged and kept after training. Can be: `true`
            or `false` and defaults to `true`. If `true`, queries are
            stored for 30 days, and then deleted. If `false`, no queries
            are stored.
        style_sheet:
            The JSON string that defines the Assistant's [style
            sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet).
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used as an alternative to the `sid` in the URL path
            to address the resource. The first 64 characters must be
            unique.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://autopilot.twilio.com/v1/Assistants/{sid}?](
    https://autopilot.twilio.com/v1/Assistants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://autopilot.twilio.com/v1/Assistants/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "callback_events": callback_events,
        "callback_url": callback_url,
        "defaults": defaults,
        "development_stage": development_stage,
        "friendly_name": friendly_name,
        "log_queries": log_queries,
        "style_sheet": style_sheet,
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
