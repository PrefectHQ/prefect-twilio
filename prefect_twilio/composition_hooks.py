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
async def get_v1_composition_hooks(
    twilio_credentials: "TwilioCredentials",
    enabled: bool = None,
    date_created_after: str = None,
    date_created_before: str = None,
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List of all Recording CompositionHook resources.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        enabled:
            Read only CompositionHook resources with an `enabled` value that matches
            this parameter.
        date_created_after:
            Read only CompositionHook resources created on or after this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with
            time zone.
        date_created_before:
            Read only CompositionHook resources created before this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with
            time zone.
        friendly_name:
            Read only CompositionHook resources with friendly names that match this
            string. The match is not case sensitive and can include
            asterisk `*` characters as wildcard match.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/CompositionHooks?&enabled=%s&date_created_after=%s&date_created_before=%s&friendly_name=%s&page_size=%s](
    https://video.twilio.com/v1/CompositionHooks?&enabled=%s&date_created_after=%s&date_created_before=%s&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://video.twilio.com/v1/CompositionHooks"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "enabled": enabled,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
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
async def post_v1_composition_hooks(
    twilio_credentials: "TwilioCredentials",
    audio_sources: list = None,
    audio_sources_excluded: list = None,
    enabled: bool = None,
    format: str = None,
    friendly_name: str = None,
    resolution: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    trim: bool = None,
    video_layout: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        audio_sources:
            An array of track names from the same group room to merge into the
            compositions created by the composition hook. Can include
            zero or more track names. A composition triggered by the
            composition hook includes all audio sources specified in
            `audio_sources` except those specified in
            `audio_sources_excluded`. The track names in this parameter
            can include an asterisk as a wild card character, which
            matches zero or more characters in a track name. For
            example, `student*` includes tracks named `student` as well
            as `studentTeam`.
        audio_sources_excluded:
            An array of track names to exclude. A composition triggered by the
            composition hook includes all audio sources specified in
            `audio_sources` except for those specified in
            `audio_sources_excluded`. The track names in this parameter
            can include an asterisk as a wild card character, which
            matches zero or more characters in a track name. For
            example, `student*` excludes `student` as well as
            `studentTeam`. This parameter can also be empty.
        enabled:
            Whether the composition hook is active. When `true`, the composition
            hook will be triggered for every completed Group Room in the
            account. When `false`, the composition hook will never be
            triggered.
        format:
            The container format of the media files used by the compositions created
            by the composition hook. Can be: `mp4` or `webm` and the
            default is `webm`. If `mp4` or `webm`, `audio_sources` must
            have one or more tracks and/or a `video_layout` element must
            contain a valid `video_sources` list, otherwise an error
            occurs.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to  100 characters long and it must be unique within the
            account.
        resolution:
            A string that describes the columns (width) and rows (height) of the
            generated composed video in pixels. Defaults to `640x480`.
            The string's format is `{width}x{height}` where:
            * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 *
            `{width}` * `{height}` <= 921,600  Typical values are:
            * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF
            = `320x240`  Note that the `resolution` imposes an aspect
            ratio to the resulting composition. When the original video
            tracks are constrained by the aspect ratio, they are scaled
            to fit. See [Specifying Video
            Layouts](https://www.twilio.com/docs/video/api/compositions-
            resource
            specifying-video-layouts) for more info.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application on every composition event.
            If not provided, status callback events will not be
            dispatched.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `POST`
            or `GET` and the default is `POST`.
        trim:
            Whether to clip the intervals where there is no active media in the
            Compositions triggered by the composition hook. The default
            is `true`. Compositions with `trim` enabled are shorter when
            the Room is created and no Participant joins for a while as
            well as if all the Participants leave the room and join
            later, because those gaps will be removed. See [Specifying
            Video
            Layouts](https://www.twilio.com/docs/video/api/compositions-
            resource
            specifying-video-layouts) for more info.
        video_layout:
            An object that describes the video layout of the composition hook in
            terms of regions. See [Specifying Video
            Layouts](https://www.twilio.com/docs/video/api/compositions-
            resource
            specifying-video-layouts) for more info.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/CompositionHooks?](
    https://video.twilio.com/v1/CompositionHooks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://video.twilio.com/v1/CompositionHooks"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "audio_sources": audio_sources,
        "audio_sources_excluded": audio_sources_excluded,
        "enabled": enabled,
        "format": format,
        "friendly_name": friendly_name,
        "resolution": resolution,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "trim": trim,
        "video_layout": video_layout,
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
async def delete_v1_composition_hooks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Recording CompositionHook resource identified by a `CompositionHook
    SID`.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/CompositionHooks/{sid}?](
    https://video.twilio.com/v1/CompositionHooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://video.twilio.com/v1/CompositionHooks/{sid}"  # noqa
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
async def get_v1_composition_hooks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single CompositionHook resource identified by a CompositionHook SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/CompositionHooks/{sid}?](
    https://video.twilio.com/v1/CompositionHooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/CompositionHooks/{sid}"  # noqa
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
async def post_v1_composition_hooks_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    audio_sources: list = None,
    audio_sources_excluded: list = None,
    enabled: bool = None,
    format: str = None,
    friendly_name: str = None,
    resolution: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    trim: bool = None,
    video_layout: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        audio_sources:
            An array of track names from the same group room to merge into the
            compositions created by the composition hook. Can include
            zero or more track names. A composition triggered by the
            composition hook includes all audio sources specified in
            `audio_sources` except those specified in
            `audio_sources_excluded`. The track names in this parameter
            can include an asterisk as a wild card character, which
            matches zero or more characters in a track name. For
            example, `student*` includes tracks named `student` as well
            as `studentTeam`.
        audio_sources_excluded:
            An array of track names to exclude. A composition triggered by the
            composition hook includes all audio sources specified in
            `audio_sources` except for those specified in
            `audio_sources_excluded`. The track names in this parameter
            can include an asterisk as a wild card character, which
            matches zero or more characters in a track name. For
            example, `student*` excludes `student` as well as
            `studentTeam`. This parameter can also be empty.
        enabled:
            Whether the composition hook is active. When `true`, the composition
            hook will be triggered for every completed Group Room in the
            account. When `false`, the composition hook never triggers.
        format:
            The container format of the media files used by the compositions created
            by the composition hook. Can be: `mp4` or `webm` and the
            default is `webm`. If `mp4` or `webm`, `audio_sources` must
            have one or more tracks and/or a `video_layout` element must
            contain a valid `video_sources` list, otherwise an error
            occurs.
        friendly_name:
            A descriptive string that you create to describe the resource. It can be
            up to  100 characters long and it must be unique within the
            account.
        resolution:
            A string that describes the columns (width) and rows (height) of the
            generated composed video in pixels. Defaults to `640x480`.
            The string's format is `{width}x{height}` where:
            * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 *
            `{width}` * `{height}` <= 921,600  Typical values are:
            * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF
            = `320x240`  Note that the `resolution` imposes an aspect
            ratio to the resulting composition. When the original video
            tracks are constrained by the aspect ratio, they are scaled
            to fit. See [Specifying Video
            Layouts](https://www.twilio.com/docs/video/api/compositions-
            resource
            specifying-video-layouts) for more info.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application on every composition event.
            If not provided, status callback events will not be
            dispatched.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `POST`
            or `GET` and the default is `POST`.
        trim:
            Whether to clip the intervals where there is no active media in the
            compositions triggered by the composition hook. The default
            is `true`. Compositions with `trim` enabled are shorter when
            the Room is created and no Participant joins for a while as
            well as if all the Participants leave the room and join
            later, because those gaps will be removed. See [Specifying
            Video
            Layouts](https://www.twilio.com/docs/video/api/compositions-
            resource
            specifying-video-layouts) for more info.
        video_layout:
            A JSON object that describes the video layout of the composition hook in
            terms of regions. See [Specifying Video
            Layouts](https://www.twilio.com/docs/video/api/compositions-
            resource
            specifying-video-layouts) for more info.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/CompositionHooks/{sid}?](
    https://video.twilio.com/v1/CompositionHooks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/CompositionHooks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "audio_sources": audio_sources,
        "audio_sources_excluded": audio_sources_excluded,
        "enabled": enabled,
        "format": format,
        "friendly_name": friendly_name,
        "resolution": resolution,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "trim": trim,
        "video_layout": video_layout,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
