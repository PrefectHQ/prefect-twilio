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
async def get_v1_e_sim_profiles(
    twilio_credentials: "TwilioCredentials",
    eid: str = None,
    sim_sid: str = None,
    status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of eSIM Profiles.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        eid:
            List the eSIM Profiles that have been associated with an EId.
        sim_sid:
            Find the eSIM Profile resource related to a
            [Sim](https://www.twilio.com/docs/wireless/api/sim-resource)
            resource by providing the SIM SID. Will always return an
            array with either 1 or 0 records.
        status:
            List the eSIM Profiles that are in a given status.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/ESimProfiles?&eid=%s&sim_sid=%s&status=%s&page_size=%s](
    https://supersim.twilio.com/v1/ESimProfiles?&eid=%s&sim_sid=%s&status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/ESimProfiles"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "eid": eid,
        "sim_sid": sim_sid,
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
async def post_v1_e_sim_profiles(
    twilio_credentials: "TwilioCredentials",
    callback_method: str = None,
    callback_url: str = None,
    eid: str = None,
) -> Dict[str, Any]:
    """
    Order an eSIM Profile.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        callback_method:
            The HTTP method we should use to call `callback_url`. Can be: `GET` or
            `POST` and the default is POST.
        callback_url:
            The URL we should call using the `callback_method` when the status of
            the eSIM Profile changes. At this stage of the eSIM Profile
            pilot, the a request to the URL will only be called when the
            ESimProfile resource changes from `reserving` to
            `available`.
        eid:
            Identifier of the eUICC that will claim the eSIM Profile.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/ESimProfiles?](
    https://supersim.twilio.com/v1/ESimProfiles?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://supersim.twilio.com/v1/ESimProfiles"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "callback_method": callback_method,
        "callback_url": callback_url,
        "eid": eid,
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
async def get_v1_e_sim_profiles_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Fetch an eSIM Profile.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://supersim.twilio.com/v1/ESimProfiles/{sid}?](
    https://supersim.twilio.com/v1/ESimProfiles/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://supersim.twilio.com/v1/ESimProfiles/{sid}"  # noqa
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
