"""Credential classes used to perform authenticated interactions with Twilio"""

from dataclasses import dataclass

from httpx import AsyncClient


@dataclass
class TwilioCredentials:
    """
    Dataclass used to manage Twilio authentication.

    Args:
        token: the token to authenticate into Twilio.
    """

    token: str = None

    def get_client(self) -> AsyncClient:
        """
        Gets an authenticated Twilio REST AsyncClient.

        Returns:
            An authenticated Twilio REST AsyncClient

        Example:
            Gets an authenticated Twilio REST AsyncClient.
            ```python
            from prefect import flow
            from prefect_twilio import TwilioCredentials

            @flow
            def example_get_client_flow():
                token = "consumer_key"
                twilio_credentials = TwilioCredentials(token)
                endpoint = twilio_credentials.get_client()
                return endpoint

            example_get_client_flow()
            ```
        """
        if self.token is not None:
            headers = {"Authorization": f"Bearer {self.token}"}
        else:
            headers = None
        client = AsyncClient(headers=headers)
        return client
