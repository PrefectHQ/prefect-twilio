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


@task
async def get_v1_compositions(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    room_sid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List of all Recording compositions.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Read only Composition resources with this status. Can be: `enqueued`,
            `processing`, `completed`, `deleted`, or `failed`.
        date_created_after:
            Read only Composition resources created on or after this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with
            time zone.
        date_created_before:
            Read only Composition resources created before this ISO 8601 date-time
            with time zone.
        room_sid:
            Read only Composition resources with this Room SID.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Compositions?&status=%s&date_created_after=%s&date_created_before=%s&room_sid=%s&page_size=%s](
    https://video.twilio.com/v1/Compositions?&status=%s&date_created_after=%s&date_created_before=%s&room_sid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://video.twilio.com/v1/Compositions"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "room_sid": room_sid,
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
async def post_v1_compositions(
    twilio_credentials: "TwilioCredentials",
    audio_sources: list = None,
    audio_sources_excluded: list = None,
    format: str = None,
    resolution: str = None,
    room_sid: str = None,
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
            An array of track names from the same group room to merge into the new
            composition. Can include zero or more track names. The new
            composition includes all audio sources specified in
            `audio_sources` except for those specified in
            `audio_sources_excluded`. The track names in this parameter
            can include an asterisk as a wild card character, which will
            match zero or more characters in a track name. For example,
            `student*` includes `student` as well as `studentTeam`.
            Please, be aware that either video_layout or audio_sources
            have to be provided to get a valid creation request.
        audio_sources_excluded:
            An array of track names to exclude. The new composition includes all
            audio sources specified in `audio_sources` except for those
            specified in `audio_sources_excluded`. The track names in
            this parameter can include an asterisk as a wild card
            character, which will match zero or more characters in a
            track name. For example, `student*` excludes `student` as
            well as `studentTeam`. This parameter can also be empty.
        format:
            The container format of the composition's media files. Can be: `mp4` or
            `webm` and the default is `webm`. If you specify `mp4` or
            `webm`, you must also specify one or more `audio_sources`
            and/or a `video_layout` element that contains a valid
            `video_sources` list, otherwise an error occurs.
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
        room_sid:
            The SID of the Group Room with the media tracks to be used as
            composition sources.
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
            composition. The default is `true`. Compositions with `trim`
            enabled are shorter when the Room is created and no
            Participant joins for a while as well as if all the
            Participants leave the room and join later, because those
            gaps will be removed. See [Specifying Video
            Layouts](https://www.twilio.com/docs/video/api/compositions-
            resource
            specifying-video-layouts) for more info.
        video_layout:
            An object that describes the video layout of the composition in terms of
            regions. See [Specifying Video
            Layouts](https://www.twilio.com/docs/video/api/compositions-
            resource
            specifying-video-layouts) for more info. Please, be aware
            that either video_layout or audio_sources have to be
            provided to get a valid creation request.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Compositions?](
    https://video.twilio.com/v1/Compositions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://video.twilio.com/v1/Compositions"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "audio_sources": audio_sources,
        "audio_sources_excluded": audio_sources_excluded,
        "format": format,
        "resolution": resolution,
        "room_sid": room_sid,
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
async def delete_v1_compositions_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Recording Composition resource identified by a Composition SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Compositions/{sid}?](
    https://video.twilio.com/v1/Compositions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Compositions/{sid}"  # noqa
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
async def get_v1_compositions_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single Composition resource identified by a Composition SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Compositions/{sid}?](
    https://video.twilio.com/v1/Compositions/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Compositions/{sid}"  # noqa
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
async def get_v1_recording_settings_default(
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
    [https://video.twilio.com/v1/RecordingSettings/Default?](
    https://video.twilio.com/v1/RecordingSettings/Default?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://video.twilio.com/v1/RecordingSettings/Default"  # noqa

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
async def post_v1_recording_settings_default(
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
            The URL of the AWS S3 bucket where the recordings should be stored. We
            only support DNS-compliant URLs like `https://documentation-
            example-twilio-bucket/recordings`, where `recordings` is the
            path in which you want the recordings to be stored. This URL
            accepts only URI-valid characters, as described in the <a
            href='https://tools.ietf.org/html/rfc3986
            section-2'>RFC 3986</a>.
        aws_storage_enabled:
            Whether all recordings should be written to the `aws_s3_url`. When
            `false`, all recordings are stored in our cloud.
        encryption_enabled:
            Whether all recordings should be stored in an encrypted form. The
            default is `false`.
        encryption_key_sid:
            The SID of the Public Key resource to use for encryption.
        friendly_name:
            A descriptive string that you create to describe the resource and be
            shown to users in the console.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/RecordingSettings/Default?](
    https://video.twilio.com/v1/RecordingSettings/Default?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://video.twilio.com/v1/RecordingSettings/Default"  # noqa

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


@task
async def get_v1_recordings(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    source_sid: str = None,
    grouping_sid: list = None,
    date_created_after: str = None,
    date_created_before: str = None,
    media_type: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """
    List of all Track recordings.

    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Read only the recordings that have this status. Can be: `processing`,
            `completed`, or `deleted`.
        source_sid:
            Read only the recordings that have this `source_sid`.
        grouping_sid:
            Read only recordings with this `grouping_sid`, which may include a
            `participant_sid` and/or a `room_sid`.
        date_created_after:
            Read only recordings that started on or after this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with
            time zone.
        date_created_before:
            Read only recordings that started before this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with
            time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-
            MM-DDThh:mm:ssZ`.
        media_type:
            Read only recordings that have this media type. Can be either `audio` or
            `video`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Recordings?&status=%s&source_sid=%s&grouping_sid=%s&date_created_after=%s&date_created_before=%s&media_type=%s&page_size=%s](
    https://video.twilio.com/v1/Recordings?&status=%s&source_sid=%s&grouping_sid=%s&date_created_after=%s&date_created_before=%s&media_type=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://video.twilio.com/v1/Recordings"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "source_sid": source_sid,
        "grouping_sid": grouping_sid,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
        "media_type": media_type,
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
async def delete_v1_recordings_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Delete a Recording resource identified by a Recording SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Recordings/{sid}?](
    https://video.twilio.com/v1/Recordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Recordings/{sid}"  # noqa
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
async def get_v1_recordings_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single Recording resource identified by a Recording SID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Recordings/{sid}?](
    https://video.twilio.com/v1/Recordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Recordings/{sid}"  # noqa
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
async def get_v1_rooms(
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    unique_name: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Read only the rooms with this status. Can be: `in-progress` (default) or
            `completed`.
        unique_name:
            Read only rooms with the this `unique_name`.
        date_created_after:
            Read only rooms that started on or after this date, given as `YYYY-MM-
            DD`.
        date_created_before:
            Read only rooms that started before this date, given as `YYYY-MM-DD`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms?&status=%s&unique_name=%s&date_created_after=%s&date_created_before=%s&page_size=%s](
    https://video.twilio.com/v1/Rooms?&status=%s&unique_name=%s&date_created_after=%s&date_created_before=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://video.twilio.com/v1/Rooms"  # noqa

    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "unique_name": unique_name,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
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
async def post_v1_rooms(
    twilio_credentials: "TwilioCredentials",
    audio_only: bool = None,
    empty_room_timeout: int = None,
    enable_turn: bool = None,
    large_room: bool = None,
    max_participant_duration: int = None,
    max_participants: int = None,
    media_region: str = None,
    record_participants_on_connect: bool = None,
    recording_rules: str = None,
    status_callback: str = None,
    status_callback_method: str = None,
    type: str = None,
    unique_name: str = None,
    unused_room_timeout: int = None,
    video_codecs: list = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        audio_only:
            When set to true, indicates that the participants in the room will only
            publish audio. No video tracks will be allowed. Group rooms
            only.
        empty_room_timeout:
            Configures how long (in minutes) a room will remain active after last
            participant leaves. Valid values range from 1 to 60 minutes
            (no fractions).
        enable_turn:
            Deprecated, now always considered to be true.
        large_room:
            When set to true, indicated that this is the large room.
        max_participant_duration:
            The maximum number of seconds a Participant can be connected to the
            room. The maximum possible value is 86400 seconds (24
            hours). The default is 14400 seconds (4 hours).
        max_participants:
            The maximum number of concurrent Participants allowed in the room. Peer-
            to-peer rooms can have up to 10 Participants. Small Group
            rooms can have up to 4 Participants. Group rooms can have up
            to 50 Participants.
        media_region:
            The region for the media server in Group Rooms.  Can be: one of the
            [available Media
            Regions](https://www.twilio.com/docs/video/ip-address-
            whitelisting
            group-rooms-media-servers). ***This feature is not available
            in `peer-to-peer` rooms.***.
        record_participants_on_connect:
            Whether to start recording when Participants connect. ***This feature is
            not available in `peer-to-peer` rooms.***.
        recording_rules:
            A collection of Recording Rules that describe how to include or exclude
            matching tracks for recording.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application on every room event. See
            [Status
            Callbacks](https://www.twilio.com/docs/video/api/status-
            callbacks) for more info.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be `POST`
            or `GET`.
        type:
            The type of room. Can be: `go`, `peer-to-peer`, `group-small`, or
            `group`. The default value is `group`.
        unique_name:
            An application-defined string that uniquely identifies the resource. It
            can be used as a `room_sid` in place of the resource's `sid`
            in the URL to address the resource, assuming it does not
            contain any [reserved
            characters](https://tools.ietf.org/html/rfc3986
            section-2.2) that would need to be URL encoded. This value
            is unique for `in-progress` rooms. SDK clients can use this
            name to connect to the room. REST API clients can use this
            name in place of the Room SID to interact with the room as
            long as the room is `in-progress`.
        unused_room_timeout:
            Configures how long (in minutes) a room will remain active if no one
            joins. Valid values range from 1 to 60 minutes (no
            fractions).
        video_codecs:
            An array of the video codecs that are supported when publishing a track
            in the room.  Can be: `VP8` and `H264`.  ***This feature is
            not available in `peer-to-peer` rooms***.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms?](
    https://video.twilio.com/v1/Rooms?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://video.twilio.com/v1/Rooms"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "audio_only": audio_only,
        "empty_room_timeout": empty_room_timeout,
        "enable_turn": enable_turn,
        "large_room": large_room,
        "max_participant_duration": max_participant_duration,
        "max_participants": max_participants,
        "media_region": media_region,
        "record_participants_on_connect": record_participants_on_connect,
        "recording_rules": recording_rules,
        "status_callback": status_callback,
        "status_callback_method": status_callback_method,
        "type": type,
        "unique_name": unique_name,
        "unused_room_timeout": unused_room_timeout,
        "video_codecs": video_codecs,
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
async def get_v1_rooms_room_sid_participants(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    identity: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Read only the participants with this status. Can be: `connected` or
            `disconnected`. For `in-progress` Rooms the default Status
            is `connected`, for `completed` Rooms only `disconnected`
            Participants are returned.
        identity:
            Read only the Participants with this
            [User](https://www.twilio.com/docs/chat/rest/user-resource)
            `identity` value.
        date_created_after:
            Read only Participants that started after this date in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601
            UTC) format.
        date_created_before:
            Read only Participants that started before this date in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601
            UTC) format.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants?&status=%s&identity=%s&date_created_after=%s&date_created_before=%s&page_size=%s](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants?&status=%s&identity=%s&date_created_after=%s&date_created_before=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "identity": identity,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
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
async def get_v1_rooms_room_sid_participants_participant_sid_published_tracks(  # noqa
    room_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Returns a list of tracks associated with a given Participant. Only `currently`
    Published Tracks are in the list resource.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks?&page_size=%s](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks"  # noqa
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
async def get_v1_rooms_room_sid_participants_participant_sid_published_tracks_sid(  # noqa
    room_sid: str,
    participant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single Track resource represented by TrackName or SID.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/PublishedTracks/{sid}"  # noqa
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
async def get_v1_rooms_room_sid_participants_participant_sid_subscribe_rules(  # noqa
    room_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a list of Subscribe Rules for the Participant.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules"  # noqa
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
async def post_v1_rooms_room_sid_participants_participant_sid_subscribe_rules(  # noqa
    room_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
    rules: str = None,
) -> Dict[str, Any]:
    """
    Update the Subscribe Rules for the Participant.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        rules:
            A JSON-encoded array of subscribe rules. See the [Specifying Subscribe
            Rules](https://www.twilio.com/docs/video/api/track-
            subscriptions
            specifying-sr) section for further information.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 202 | Accepted. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules"  # noqa
    responses = {
        202: "Accepted.",  # noqa
    }

    data = {
        "rules": rules,
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
async def get_v1_rooms_room_sid_participants_participant_sid_subscribed_tracks(  # noqa
    room_sid: str,
    participant_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """
    Returns a list of tracks that are subscribed for the participant.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks?&page_size=%s](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks"  # noqa
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
async def get_v1_rooms_room_sid_participants_participant_sid_subscribed_tracks_sid(  # noqa
    room_sid: str,
    participant_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a single Track resource represented by `track_sid`.  Note: This is one
    resource with the Video API that requires a SID, be Track Name on the
    subscriber side is not guaranteed to be unique.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        participant_sid:
            Participant sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks/{sid}"  # noqa
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
async def get_v1_rooms_room_sid_participants_sid(
    room_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}"  # noqa
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
async def post_v1_rooms_room_sid_participants_sid(
    room_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The new status of the resource. Can be: `connected` or `disconnected`.
            For `in-progress` Rooms the default Status is `connected`,
            for `completed` Rooms only `disconnected` Participants are
            returned.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Participants/{sid}"  # noqa
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
async def get_v1_rooms_room_sid_recording_rules(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """
    Returns a list of Recording Rules for the Room.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules?](
    https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules"  # noqa
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
async def post_v1_rooms_room_sid_recording_rules(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
    rules: str = None,
) -> Dict[str, Any]:
    """
    Update the Recording Rules for the Room.

    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        rules:
            A JSON-encoded array of recording rules.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules?](
    https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 202 | Accepted. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/RecordingRules"  # noqa
    responses = {
        202: "Accepted.",  # noqa
    }

    data = {
        "rules": rules,
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
async def get_v1_rooms_room_sid_recordings(
    room_sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
    source_sid: str = None,
    date_created_after: str = None,
    date_created_before: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            Read only the recordings with this status. Can be: `processing`,
            `completed`, or `deleted`.
        source_sid:
            Read only the recordings that have this `source_sid`.
        date_created_after:
            Read only recordings that started on or after this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with
            time zone.
        date_created_before:
            Read only Recordings that started before this [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with
            time zone.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Recordings?&status=%s&source_sid=%s&date_created_after=%s&date_created_before=%s&page_size=%s](
    https://video.twilio.com/v1/Rooms/{room_sid}/Recordings?&status=%s&source_sid=%s&date_created_after=%s&date_created_before=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Recordings"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "status": status,
        "source_sid": source_sid,
        "date_created_after": date_created_after,
        "date_created_before": date_created_before,
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
async def delete_v1_rooms_room_sid_recordings_sid(
    room_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}"  # noqa
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
async def get_v1_rooms_room_sid_recordings_sid(
    room_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        room_sid:
            Room sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}?](
    https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{room_sid}/Recordings/{sid}"  # noqa
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
async def get_v1_rooms_sid(
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
    [https://video.twilio.com/v1/Rooms/{sid}?](
    https://video.twilio.com/v1/Rooms/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{sid}"  # noqa
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
async def post_v1_rooms_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    status: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        status:
            The new status of the resource. Set to `completed` to end the room.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://video.twilio.com/v1/Rooms/{sid}?](
    https://video.twilio.com/v1/Rooms/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://video.twilio.com/v1/Rooms/{sid}"  # noqa
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
