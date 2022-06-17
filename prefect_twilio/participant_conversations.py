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
async def get_v1_participant_conversations(
    twilio_credentials: "TwilioCredentials",
    identity: str = None,
    address: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Retrieve a list of all Conversations that this Participant belongs to by
    identity or by address. Only one parameter should be specified.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        identity:
            A unique string identifier for the conversation participant as
            [Conversation
            User](https://www.twilio.com/docs/conversations/api/user-
            resource). This parameter is non-null if (and only if) the
            participant is using the Conversations SDK to communicate.
            Limited to 256 characters.
        address:
            A unique string identifier for the conversation participant who's not a
            Conversation User. This parameter could be found in
            messaging_binding.address field of Participant resource. It
            should be url-encoded.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://conversations.twilio.com/v1/ParticipantConversations?&identity=%s&address=%s&page_size=%s](
    https://conversations.twilio.com/v1/ParticipantConversations?&identity=%s&address=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://conversations.twilio.com/v1/ParticipantConversations"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "identity": identity,
        "address": address,
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
