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
async def get_v1_workspaces(
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The `friendly_name` of the Workspace resources to read. For example
            `Customer Support` or `2014 Election Campaign`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces?&friendly_name=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces?&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = "https://taskrouter.twilio.com/v1/Workspaces"  # noqa

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


@task
async def post_v1_workspaces(
    twilio_credentials: "TwilioCredentials",
    event_callback_url: str = None,
    events_filter: str = None,
    friendly_name: str = None,
    multi_task_enabled: bool = None,
    prioritize_queue_order: str = None,
    template: str = None,
) -> Dict[str, Any]:
    """


    Args:
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        event_callback_url:
            The URL we should call when an event occurs. If provided, the Workspace
            will publish events to this URL, for example, to collect
            data for reporting. See [Workspace
            Events](https://www.twilio.com/docs/taskrouter/api/event)
            for more information. This parameter supports Twilio's
            [Webhooks (HTTP callbacks) Connection
            Overrides](https://www.twilio.com/docs/usage/webhooks/webhooks-
            connection-overrides).
        events_filter:
            The list of Workspace events for which to call event_callback_url. For
            example, if `EventsFilter=task.created, task.canceled,
            worker.activity.update`, then TaskRouter will call
            event_callback_url only when a task is created, canceled, or
            a Worker activity is updated.
        friendly_name:
            A descriptive string that you create to describe the Workspace resource.
            It can be up to 64 characters long. For example: `Customer
            Support` or `2014 Election Campaign`.
        multi_task_enabled:
            Whether to enable multi-tasking. Can be: `true` to enable multi-tasking,
            or `false` to disable it. However, all workspaces should be
            created as multi-tasking. The default is `true`. Multi-
            tasking allows Workers to handle multiple Tasks
            simultaneously. When enabled (`true`), each Worker can
            receive parallel reservations up to the per-channel maximums
            defined in the Workers section. In single-tasking mode
            (legacy mode), each Worker will only receive a new
            reservation when the previous task is completed. Learn more
            at
            [Multitasking](https://www.twilio.com/docs/taskrouter/multitasking).
        prioritize_queue_order:
            The type of TaskQueue to prioritize when Workers are receiving Tasks
            from both types of TaskQueues. Can be: `LIFO` or `FIFO` and
            the default is `FIFO`. For more information, see [Queue
            Ordering](https://www.twilio.com/docs/taskrouter/queue-
            ordering-last-first-out-lifo).
        template:
            An available template name. Can be: `NONE` or `FIFO` and the default is
            `NONE`. Pre-configures the Workspace with the Workflow and
            Activities specified in the template. `NONE` will create a
            Workspace with only a set of default activities. `FIFO` will
            configure TaskRouter with a set of default activities and a
            single TaskQueue for first-in, first-out distribution, which
            can be useful when you are getting started with TaskRouter.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces?](
    https://taskrouter.twilio.com/v1/Workspaces?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = "https://taskrouter.twilio.com/v1/Workspaces"  # noqa

    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "event_callback_url": event_callback_url,
        "events_filter": events_filter,
        "friendly_name": friendly_name,
        "multi_task_enabled": multi_task_enabled,
        "prioritize_queue_order": prioritize_queue_order,
        "template": template,
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
async def delete_v1_workspaces_sid(
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
    [https://taskrouter.twilio.com/v1/Workspaces/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{sid}"  # noqa
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
async def get_v1_workspaces_sid(
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
    [https://taskrouter.twilio.com/v1/Workspaces/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{sid}"  # noqa
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
async def post_v1_workspaces_sid(
    sid: str,
    twilio_credentials: "TwilioCredentials",
    default_activity_sid: str = None,
    event_callback_url: str = None,
    events_filter: str = None,
    friendly_name: str = None,
    multi_task_enabled: bool = None,
    prioritize_queue_order: str = None,
    timeout_activity_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        default_activity_sid:
            The SID of the Activity that will be used when new Workers are created
            in the Workspace.
        event_callback_url:
            The URL we should call when an event occurs. See [Workspace
            Events](https://www.twilio.com/docs/taskrouter/api/event)
            for more information. This parameter supports Twilio's
            [Webhooks (HTTP callbacks) Connection
            Overrides](https://www.twilio.com/docs/usage/webhooks/webhooks-
            connection-overrides).
        events_filter:
            The list of Workspace events for which to call event_callback_url. For
            example if
            `EventsFilter=task.created,task.canceled,worker.activity.update`,
            then TaskRouter will call event_callback_url only when a
            task is created, canceled, or a Worker activity is updated.
        friendly_name:
            A descriptive string that you create to describe the Workspace resource.
            For example: `Sales Call Center` or `Customer Support Team`.
        multi_task_enabled:
            Whether to enable multi-tasking. Can be: `true` to enable multi-tasking,
            or `false` to disable it. However, all workspaces should be
            maintained as multi-tasking. There is no default when
            omitting this parameter. A multi-tasking Workspace can't be
            updated to single-tasking unless it is not a Flex Project
            and another (legacy) single-tasking Workspace exists. Multi-
            tasking allows Workers to handle multiple Tasks
            simultaneously. In multi-tasking mode, each Worker can
            receive parallel reservations up to the per-channel maximums
            defined in the Workers section. In single-tasking mode
            (legacy mode), each Worker will only receive a new
            reservation when the previous task is completed. Learn more
            at
            [Multitasking](https://www.twilio.com/docs/taskrouter/multitasking).
        prioritize_queue_order:
            The type of TaskQueue to prioritize when Workers are receiving Tasks
            from both types of TaskQueues. Can be: `LIFO` or `FIFO`. For
            more information, see [Queue
            Ordering](https://www.twilio.com/docs/taskrouter/queue-
            ordering-last-first-out-lifo).
        timeout_activity_sid:
            The SID of the Activity that will be assigned to a Worker when a Task
            reservation times out without a response.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "default_activity_sid": default_activity_sid,
        "event_callback_url": event_callback_url,
        "events_filter": events_filter,
        "friendly_name": friendly_name,
        "multi_task_enabled": multi_task_enabled,
        "prioritize_queue_order": prioritize_queue_order,
        "timeout_activity_sid": timeout_activity_sid,
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
async def get_v1_workspaces_workspace_sid_activities(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    available: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The `friendly_name` of the Activity resources to read.
        available:
            Whether return only Activity resources that are available or
            unavailable. A value of `true` returns only available
            activities. Values of '1' or `yes` also indicate `true`. All
            other values represent `false` and return activities that
            are unavailable.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities?&friendly_name=%s&available=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities?&friendly_name=%s&available=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "friendly_name": friendly_name,
        "available": available,
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
async def post_v1_workspaces_workspace_sid_activities(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    available: bool = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        available:
            Whether the Worker should be eligible to receive a Task when it occupies
            the Activity. A value of `true`, `1`, or `yes` specifies the
            Activity is available. All other values specify that it is
            not. The value cannot be changed after the Activity is
            created.
        friendly_name:
            A descriptive string that you create to describe the Activity resource.
            It can be up to 64 characters long. These names are used to
            calculate and expose statistics about Workers, and provide
            visibility into the state of each Worker. Examples of
            friendly names include: `on-call`, `break`, and `email`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "available": available,
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
async def delete_v1_workspaces_workspace_sid_activities_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities/{sid}"  # noqa
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
async def get_v1_workspaces_workspace_sid_activities_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities/{sid}"  # noqa
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
async def post_v1_workspaces_workspace_sid_activities_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            A descriptive string that you create to describe the Activity resource.
            It can be up to 64 characters long. These names are used to
            calculate and expose statistics about Workers, and provide
            visibility into the state of each Worker. Examples of
            friendly names include: `on-call`, `break`, and `email`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Activities/{sid}"  # noqa
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
async def get_v1_workspaces_workspace_sid_cumulative_statistics(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    end_date: str = None,
    minutes: int = None,
    start_date: str = None,
    task_channel: str = None,
    split_by_wait_time: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_date:
            Only include usage that occurred on or before this date, specified in
            GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            date-time.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default 15 minutes. This is helpful for displaying
            statistics for the last 15 minutes, 240 minutes (4 hours),
            and 480 minutes (8 hours) to see trends.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        task_channel:
            Only calculate cumulative statistics on this TaskChannel. Can be the
            TaskChannel's SID or its `unique_name`, such as `voice`,
            `sms`, or `default`.
        split_by_wait_time:
            A comma separated list of values that describes the thresholds, in
            seconds, to calculate statistics on. For each threshold
            specified, the number of Tasks canceled and reservations
            accepted above and below the specified thresholds in seconds
            are computed. For example, `5,30` would show splits of Tasks
            that were canceled or accepted before and after 5 seconds
            and before and after 30 seconds. This can be used to show
            short abandoned Tasks or Tasks that failed to meet an SLA.
            TaskRouter will calculate statistics on up to 10,000 Tasks
            for any given threshold.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/CumulativeStatistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/CumulativeStatistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/CumulativeStatistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end_date": end_date,
        "minutes": minutes,
        "start_date": start_date,
        "task_channel": task_channel,
        "split_by_wait_time": split_by_wait_time,
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
async def get_v1_workspaces_workspace_sid_events(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    end_date: str = None,
    event_type: str = None,
    minutes: int = None,
    reservation_sid: str = None,
    start_date: str = None,
    task_queue_sid: str = None,
    task_sid: str = None,
    worker_sid: str = None,
    workflow_sid: str = None,
    task_channel: str = None,
    sid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_date:
            Only include Events that occurred on or before this date, specified in
            GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            date-time.
        event_type:
            The type of Events to read. Returns only Events of the type specified.
        minutes:
            The period of events to read in minutes. Returns only Events that
            occurred since this many minutes in the past. The default is
            `15` minutes. Task Attributes for Events occuring more
            43,200 minutes ago will be redacted.
        reservation_sid:
            The SID of the Reservation with the Events to read. Returns only Events
            that pertain to the specified Reservation.
        start_date:
            Only include Events from on or after this date and time, specified in
            [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
            Task Attributes for Events older than 30 days will be
            redacted.
        task_queue_sid:
            The SID of the TaskQueue with the Events to read. Returns only the
            Events that pertain to the specified TaskQueue.
        task_sid:
            The SID of the Task with the Events to read. Returns only the Events
            that pertain to the specified Task.
        worker_sid:
            The SID of the Worker with the Events to read. Returns only the Events
            that pertain to the specified Worker.
        workflow_sid:
            The SID of the Workflow with the Events to read. Returns only the Events
            that pertain to the specified Workflow.
        task_channel:
            The TaskChannel with the Events to read. Returns only the Events that
            pertain to the specified TaskChannel.
        sid:
            The SID of the Event resource to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Events?&end_date=%s&event_type=%s&minutes=%s&reservation_sid=%s&start_date=%s&task_queue_sid=%s&task_sid=%s&worker_sid=%s&workflow_sid=%s&task_channel=%s&sid=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Events?&end_date=%s&event_type=%s&minutes=%s&reservation_sid=%s&start_date=%s&task_queue_sid=%s&task_sid=%s&worker_sid=%s&workflow_sid=%s&task_channel=%s&sid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Events"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end_date": end_date,
        "event_type": event_type,
        "minutes": minutes,
        "reservation_sid": reservation_sid,
        "start_date": start_date,
        "task_queue_sid": task_queue_sid,
        "task_sid": task_sid,
        "worker_sid": worker_sid,
        "workflow_sid": workflow_sid,
        "task_channel": task_channel,
        "sid": sid,
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
async def get_v1_workspaces_workspace_sid_events_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Events/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Events/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Events/{sid}"  # noqa
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
async def get_v1_workspaces_workspace_sid_real_time_statistics(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    task_channel: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        task_channel:
            Only calculate real-time statistics on this TaskChannel. Can be the
            TaskChannel's SID or its `unique_name`, such as `voice`,
            `sms`, or `default`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/RealTimeStatistics?&task_channel=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/RealTimeStatistics?&task_channel=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/RealTimeStatistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "task_channel": task_channel,
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
async def get_v1_workspaces_workspace_sid_statistics(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    minutes: int = None,
    start_date: str = None,
    end_date: str = None,
    task_channel: str = None,
    split_by_wait_time: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default 15 minutes. This is helpful for displaying
            statistics for the last 15 minutes, 240 minutes (4 hours),
            and 480 minutes (8 hours) to see trends.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        end_date:
            Only calculate statistics from this date and time and earlier, specified
            in GMT as an [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        task_channel:
            Only calculate statistics on this TaskChannel. Can be the TaskChannel's
            SID or its `unique_name`, such as `voice`, `sms`, or
            `default`.
        split_by_wait_time:
            A comma separated list of values that describes the thresholds, in
            seconds, to calculate statistics on. For each threshold
            specified, the number of Tasks canceled and reservations
            accepted above and below the specified thresholds in seconds
            are computed. For example, `5,30` would show splits of Tasks
            that were canceled or accepted before and after 5 seconds
            and before and after 30 seconds. This can be used to show
            short abandoned Tasks or Tasks that failed to meet an SLA.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Statistics?&minutes=%s&start_date=%s&end_date=%s&task_channel=%s&split_by_wait_time=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Statistics?&minutes=%s&start_date=%s&end_date=%s&task_channel=%s&split_by_wait_time=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Statistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "minutes": minutes,
        "start_date": start_date,
        "end_date": end_date,
        "task_channel": task_channel,
        "split_by_wait_time": split_by_wait_time,
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
async def get_v1_workspaces_workspace_sid_task_channels(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels?&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels"  # noqa
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
async def post_v1_workspaces_workspace_sid_task_channels(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    channel_optimized_routing: bool = None,
    friendly_name: str = None,
    unique_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        channel_optimized_routing:
            Whether the Task Channel should prioritize Workers that have been idle.
            If `true`, Workers that have been idle the longest are
            prioritized.
        friendly_name:
            A descriptive string that you create to describe the Task Channel. It
            can be up to 64 characters long.
        unique_name:
            An application-defined string that uniquely identifies the Task Channel,
            such as `voice` or `sms`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "channel_optimized_routing": channel_optimized_routing,
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
async def delete_v1_workspaces_workspace_sid_task_channels_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels/{sid}"  # noqa
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
async def get_v1_workspaces_workspace_sid_task_channels_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels/{sid}"  # noqa
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
async def post_v1_workspaces_workspace_sid_task_channels_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    channel_optimized_routing: bool = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        channel_optimized_routing:
            Whether the TaskChannel should prioritize Workers that have been idle.
            If `true`, Workers that have been idle the longest are
            prioritized.
        friendly_name:
            A descriptive string that you create to describe the Task Channel. It
            can be up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskChannels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "channel_optimized_routing": channel_optimized_routing,
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
async def get_v1_workspaces_workspace_sid_task_queues(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    evaluate_worker_attributes: str = None,
    worker_sid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The `friendly_name` of the TaskQueue resources to read.
        evaluate_worker_attributes:
            The attributes of the Workers to read. Returns the TaskQueues with
            Workers that match the attributes specified in this
            parameter.
        worker_sid:
            The SID of the Worker with the TaskQueue resources to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues?&friendly_name=%s&evaluate_worker_attributes=%s&worker_sid=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues?&friendly_name=%s&evaluate_worker_attributes=%s&worker_sid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "friendly_name": friendly_name,
        "evaluate_worker_attributes": evaluate_worker_attributes,
        "worker_sid": worker_sid,
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
async def post_v1_workspaces_workspace_sid_task_queues(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    assignment_activity_sid: str = None,
    friendly_name: str = None,
    max_reserved_workers: int = None,
    reservation_activity_sid: str = None,
    target_workers: str = None,
    task_order: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        assignment_activity_sid:
            The SID of the Activity to assign Workers when a task is assigned to
            them.
        friendly_name:
            A descriptive string that you create to describe the TaskQueue. For
            example `Support-Tier 1`, `Sales`, or `Escalation`.
        max_reserved_workers:
            The maximum number of Workers to reserve for the assignment of a Task in
            the queue. Can be an integer between 1 and 50, inclusive and
            defaults to 1.
        reservation_activity_sid:
            The SID of the Activity to assign Workers when a task is reserved for
            them.
        target_workers:
            A string that describes the Worker selection criteria for any Tasks that
            enter the TaskQueue. For example, `'"language" ==
            "spanish"'`. The default value is `1==1`. If this value is
            empty, Tasks will wait in the TaskQueue until they are
            deleted or moved to another TaskQueue. For more information
            about Worker selection, see [Describing Worker selection
            criteria](https://www.twilio.com/docs/taskrouter/api/taskqueues
            target-workers).
        task_order:
            How Tasks will be assigned to Workers. Set this parameter to `LIFO` to
            assign most recently created Task first or FIFO to assign
            the oldest Task first. Default is `FIFO`. [Click
            here](https://www.twilio.com/docs/taskrouter/queue-ordering-
            last-first-out-lifo) to learn more.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "assignment_activity_sid": assignment_activity_sid,
        "friendly_name": friendly_name,
        "max_reserved_workers": max_reserved_workers,
        "reservation_activity_sid": reservation_activity_sid,
        "target_workers": target_workers,
        "task_order": task_order,
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
async def get_v1_workspaces_workspace_sid_task_queues_statistics(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    end_date: str = None,
    friendly_name: str = None,
    minutes: int = None,
    start_date: str = None,
    task_channel: str = None,
    split_by_wait_time: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_date:
            Only calculate statistics from this date and time and earlier, specified
            in GMT as an [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        friendly_name:
            The `friendly_name` of the TaskQueue statistics to read.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default is 15 minutes.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        task_channel:
            Only calculate statistics on this TaskChannel. Can be the TaskChannel's
            SID or its `unique_name`, such as `voice`, `sms`, or
            `default`.
        split_by_wait_time:
            A comma separated list of values that describes the thresholds, in
            seconds, to calculate statistics on. For each threshold
            specified, the number of Tasks canceled and reservations
            accepted above and below the specified thresholds in seconds
            are computed.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/Statistics?&end_date=%s&friendly_name=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/Statistics?&end_date=%s&friendly_name=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/Statistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end_date": end_date,
        "friendly_name": friendly_name,
        "minutes": minutes,
        "start_date": start_date,
        "task_channel": task_channel,
        "split_by_wait_time": split_by_wait_time,
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
async def delete_v1_workspaces_workspace_sid_task_queues_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}"  # noqa
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
async def get_v1_workspaces_workspace_sid_task_queues_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}"  # noqa
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
async def post_v1_workspaces_workspace_sid_task_queues_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    assignment_activity_sid: str = None,
    friendly_name: str = None,
    max_reserved_workers: int = None,
    reservation_activity_sid: str = None,
    target_workers: str = None,
    task_order: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        assignment_activity_sid:
            The SID of the Activity to assign Workers when a task is assigned for
            them.
        friendly_name:
            A descriptive string that you create to describe the TaskQueue. For
            example `Support-Tier 1`, `Sales`, or `Escalation`.
        max_reserved_workers:
            The maximum number of Workers to create reservations for the assignment
            of a task while in the queue. Maximum of 50.
        reservation_activity_sid:
            The SID of the Activity to assign Workers when a task is reserved for
            them.
        target_workers:
            A string describing the Worker selection criteria for any Tasks that
            enter the TaskQueue. For example '"language" == "spanish"'
            If no TargetWorkers parameter is provided, Tasks will wait
            in the queue until they are either deleted or moved to
            another queue. Additional examples on how to describing
            Worker selection criteria below.
        task_order:
            How Tasks will be assigned to Workers. Can be: `FIFO` or `LIFO` and the
            default is `FIFO`. Use `FIFO` to assign the oldest task
            first and `LIFO` to assign the most recent task first. For
            more information, see [Queue
            Ordering](https://www.twilio.com/docs/taskrouter/queue-
            ordering-last-first-out-lifo).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "assignment_activity_sid": assignment_activity_sid,
        "friendly_name": friendly_name,
        "max_reserved_workers": max_reserved_workers,
        "reservation_activity_sid": reservation_activity_sid,
        "target_workers": target_workers,
        "task_order": task_order,
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
async def get_v1_workspaces_workspace_sid_task_queues_task_queue_sid_cumulative_statistics(
    workspace_sid: str,
    task_queue_sid: str,
    twilio_credentials: "TwilioCredentials",
    end_date: str = None,
    minutes: int = None,
    start_date: str = None,
    task_channel: str = None,
    split_by_wait_time: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        task_queue_sid:
            Task queue sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_date:
            Only calculate statistics from this date and time and earlier, specified
            in GMT as an [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default is 15 minutes.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        task_channel:
            Only calculate cumulative statistics on this TaskChannel. Can be the
            TaskChannel's SID or its `unique_name`, such as `voice`,
            `sms`, or `default`.
        split_by_wait_time:
            A comma separated list of values that describes the thresholds, in
            seconds, to calculate statistics on. For each threshold
            specified, the number of Tasks canceled and reservations
            accepted above and below the specified thresholds in seconds
            are computed. TaskRouter will calculate statistics on up to
            10,000 Tasks/Reservations for any given threshold.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/CumulativeStatistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/CumulativeStatistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/CumulativeStatistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end_date": end_date,
        "minutes": minutes,
        "start_date": start_date,
        "task_channel": task_channel,
        "split_by_wait_time": split_by_wait_time,
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
async def get_v1_workspaces_workspace_sid_task_queues_task_queue_sid_real_time_statistics(
    workspace_sid: str,
    task_queue_sid: str,
    twilio_credentials: "TwilioCredentials",
    task_channel: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        task_queue_sid:
            Task queue sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        task_channel:
            The TaskChannel for which to fetch statistics. Can be the TaskChannel's
            SID or its `unique_name`, such as `voice`, `sms`, or
            `default`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/RealTimeStatistics?&task_channel=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/RealTimeStatistics?&task_channel=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/RealTimeStatistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "task_channel": task_channel,
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
async def get_v1_workspaces_workspace_sid_task_queues_task_queue_sid_statistics(
    workspace_sid: str,
    task_queue_sid: str,
    twilio_credentials: "TwilioCredentials",
    end_date: str = None,
    minutes: int = None,
    start_date: str = None,
    task_channel: str = None,
    split_by_wait_time: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        task_queue_sid:
            Task queue sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_date:
            Only calculate statistics from this date and time and earlier, specified
            in GMT as an [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default is 15 minutes.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        task_channel:
            Only calculate real-time and cumulative statistics for the specified
            TaskChannel. Can be the TaskChannel's SID or its
            `unique_name`, such as `voice`, `sms`, or `default`.
        split_by_wait_time:
            A comma separated list of values that describes the thresholds, in
            seconds, to calculate statistics on. For each threshold
            specified, the number of Tasks canceled and reservations
            accepted above and below the specified thresholds in seconds
            are computed.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/Statistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/Statistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/Statistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end_date": end_date,
        "minutes": minutes,
        "start_date": start_date,
        "task_channel": task_channel,
        "split_by_wait_time": split_by_wait_time,
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
async def get_v1_workspaces_workspace_sid_tasks(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    priority: int = None,
    assignment_status: list = None,
    workflow_sid: str = None,
    workflow_name: str = None,
    task_queue_sid: str = None,
    task_queue_name: str = None,
    evaluate_task_attributes: str = None,
    ordering: str = None,
    has_addons: bool = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        priority:
            The priority value of the Tasks to read. Returns the list of all Tasks
            in the Workspace with the specified priority.
        assignment_status:
            The `assignment_status` of the Tasks you want to read. Can be:
            `pending`, `reserved`, `assigned`, `canceled`, `wrapping`,
            or `completed`. Returns all Tasks in the Workspace with the
            specified `assignment_status`.
        workflow_sid:
            The SID of the Workflow with the Tasks to read. Returns the Tasks
            controlled by the Workflow identified by this SID.
        workflow_name:
            The friendly name of the Workflow with the Tasks to read. Returns the
            Tasks controlled by the Workflow identified by this friendly
            name.
        task_queue_sid:
            The SID of the TaskQueue with the Tasks to read. Returns the Tasks
            waiting in the TaskQueue identified by this SID.
        task_queue_name:
            The `friendly_name` of the TaskQueue with the Tasks to read. Returns the
            Tasks waiting in the TaskQueue identified by this friendly
            name.
        evaluate_task_attributes:
            The attributes of the Tasks to read. Returns the Tasks that match the
            attributes specified in this parameter.
        ordering:
            How to order the returned Task resources. y default, Tasks are sorted by
            ascending DateCreated. This value is specified as:
            `Attribute:Order`, where `Attribute` can be either
            `Priority` or `DateCreated` and `Order` can be either `asc`
            or `desc`. For example, `Priority:desc` returns Tasks
            ordered in descending order of their Priority. Multiple sort
            orders can be specified in a comma-separated list such as
            `Priority:desc,DateCreated:asc`, which returns the Tasks in
            descending Priority order and ascending DateCreated Order.
        has_addons:
            Whether to read Tasks with addons. If `true`, returns only Tasks with
            addons. If `false`, returns only Tasks without addons.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks?&priority=%s&assignment_status=%s&workflow_sid=%s&workflow_name=%s&task_queue_sid=%s&task_queue_name=%s&evaluate_task_attributes=%s&ordering=%s&has_addons=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks?&priority=%s&assignment_status=%s&workflow_sid=%s&workflow_name=%s&task_queue_sid=%s&task_queue_name=%s&evaluate_task_attributes=%s&ordering=%s&has_addons=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "priority": priority,
        "assignment_status": assignment_status,
        "workflow_sid": workflow_sid,
        "workflow_name": workflow_name,
        "task_queue_sid": task_queue_sid,
        "task_queue_name": task_queue_name,
        "evaluate_task_attributes": evaluate_task_attributes,
        "ordering": ordering,
        "has_addons": has_addons,
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
async def post_v1_workspaces_workspace_sid_tasks(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    attributes: str = None,
    priority: int = None,
    task_channel: str = None,
    timeout: int = None,
    workflow_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        attributes:
            A URL-encoded JSON string with the attributes of the new task. This
            value is passed to the Workflow's `assignment_callback_url`
            when the Task is assigned to a Worker. For example: `{
            "task_type": "call", "twilio_call_sid": "CAxxx",
            "customer_ticket_number": "12345" }`.
        priority:
            The priority to assign the new task and override the default. When
            supplied, the new Task will have this priority unless it
            matches a Workflow Target with a Priority set. When not
            supplied, the new Task will have the priority of the
            matching Workflow Target. Value can be 0 to 2^31^
            (2,147,483,647).
        task_channel:
            When MultiTasking is enabled, specify the TaskChannel by passing either
            its `unique_name` or `sid`. Default value is `default`.
        timeout:
            The amount of time in seconds the new task can live before being
            assigned. Can be up to a maximum of 2 weeks (1,209,600
            seconds). The default value is 24 hours (86,400 seconds). On
            timeout, the `task.canceled` event will fire with
            description `Task TTL Exceeded`.
        workflow_sid:
            The SID of the Workflow that you would like to handle routing for the
            new Task. If there is only one Workflow defined for the
            Workspace that you are posting the new task to, this
            parameter is optional.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "attributes": attributes,
        "priority": priority,
        "task_channel": task_channel,
        "timeout": timeout,
        "workflow_sid": workflow_sid,
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
async def delete_v1_workspaces_workspace_sid_tasks_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            If provided, deletes this Task if (and only if) the
            [ETag](https://developer.mozilla.org/en-
            US/docs/Web/HTTP/Headers/ETag) header of the Task matches
            the provided value. This matches the semantics of (and is
            implemented with) the HTTP [If-Match
            header](https://developer.mozilla.org/en-
            US/docs/Web/HTTP/Headers/If-Match).

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{sid}?&if_match=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{sid}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v1_workspaces_workspace_sid_tasks_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{sid}"  # noqa
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
async def post_v1_workspaces_workspace_sid_tasks_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
    assignment_status: str = None,
    attributes: str = None,
    priority: int = None,
    reason: str = None,
    task_channel: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            If provided, applies this mutation if (and only if) the
            [ETag](https://developer.mozilla.org/en-
            US/docs/Web/HTTP/Headers/ETag) header of the Task matches
            the provided value. This matches the semantics of (and is
            implemented with) the HTTP [If-Match
            header](https://developer.mozilla.org/en-
            US/docs/Web/HTTP/Headers/If-Match).
        assignment_status:
            The new status of the task. Can be: `canceled`, to cancel a Task that is
            currently `pending` or `reserved`; `wrapping`, to move the
            Task to wrapup state; or `completed`, to move a Task to the
            completed state.
        attributes:
            The JSON string that describes the custom attributes of the task.
        priority:
            The Task's new priority value. When supplied, the Task takes on the
            specified priority unless it matches a Workflow Target with
            a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
        reason:
            The reason that the Task was canceled or completed. This parameter is
            required only if the Task is canceled or completed. Setting
            this value queues the task for deletion and logs the reason.
        task_channel:
            When MultiTasking is enabled, specify the TaskChannel with the task to
            update. Can be the TaskChannel's SID or its `unique_name`,
            such as `voice`, `sms`, or `default`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{sid}?&if_match=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{sid}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    data = {
        "assignment_status": assignment_status,
        "attributes": attributes,
        "priority": priority,
        "reason": reason,
        "task_channel": task_channel,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_workspaces_workspace_sid_tasks_task_sid_reservations(
    workspace_sid: str,
    task_sid: str,
    twilio_credentials: "TwilioCredentials",
    reservation_status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        reservation_status:
            Returns the list of reservations for a task with a specified
            ReservationStatus.  Can be: `pending`, `accepted`,
            `rejected`, or `timeout`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations?&reservation_status=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations?&reservation_status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "reservation_status": reservation_status,
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
async def get_v1_workspaces_workspace_sid_tasks_task_sid_reservations_sid(
    workspace_sid: str,
    task_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
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
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}"  # noqa
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
async def post_v1_workspaces_workspace_sid_tasks_task_sid_reservations_sid(
    workspace_sid: str,
    task_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
    beep: str = None,
    beep_on_customer_entrance: bool = None,
    call_accept: bool = None,
    call_from: str = None,
    call_record: str = None,
    call_status_callback_url: str = None,
    call_timeout: int = None,
    call_to: str = None,
    call_url: str = None,
    conference_record: str = None,
    conference_recording_status_callback: str = None,
    conference_recording_status_callback_method: str = None,
    conference_status_callback: str = None,
    conference_status_callback_event: list = None,
    conference_status_callback_method: str = None,
    conference_trim: str = None,
    dequeue_from: str = None,
    dequeue_post_work_activity_sid: str = None,
    dequeue_record: str = None,
    dequeue_status_callback_event: list = None,
    dequeue_status_callback_url: str = None,
    dequeue_timeout: int = None,
    dequeue_to: str = None,
    early_media: bool = None,
    end_conference_on_customer_exit: bool = None,
    end_conference_on_exit: bool = None,
    from_: str = None,
    instruction: str = None,
    max_participants: int = None,
    muted: bool = None,
    post_work_activity_sid: str = None,
    record: bool = None,
    recording_channels: str = None,
    recording_status_callback: str = None,
    recording_status_callback_method: str = None,
    redirect_accept: bool = None,
    redirect_call_sid: str = None,
    redirect_url: str = None,
    region: str = None,
    reservation_status: str = None,
    sip_auth_password: str = None,
    sip_auth_username: str = None,
    start_conference_on_enter: bool = None,
    status_callback: str = None,
    status_callback_event: list = None,
    status_callback_method: str = None,
    supervisor: str = None,
    supervisor_mode: str = None,
    timeout: int = None,
    to: str = None,
    wait_method: str = None,
    wait_url: str = None,
    worker_activity_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        task_sid:
            Task sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            The If-Match HTTP request header.
        beep:
            Whether to play a notification beep when the participant joins or when
            to play a beep. Can be: `true`, `false`, `onEnter`, or
            `onExit`. The default value is `true`.
        beep_on_customer_entrance:
            Whether to play a notification beep when the customer joins.
        call_accept:
            Whether to accept a reservation when executing a Call instruction.
        call_from:
            The Caller ID of the outbound call when executing a Call instruction.
        call_record:
            Whether to record both legs of a call when executing a Call instruction
            or which leg to record.
        call_status_callback_url:
            The URL to call  for the completed call event when executing a Call
            instruction.
        call_timeout:
            Timeout for call when executing a Call instruction.
        call_to:
            The Contact URI of the worker when executing a Call instruction.  Can be
            the URI of the Twilio Client, the SIP URI for Programmable
            SIP, or the
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            formatted phone number, depending on the destination.
        call_url:
            TwiML URI executed on answering the worker's leg as a result of the Call
            instruction.
        conference_record:
            Whether to record the conference the participant is joining or when to
            record the conference. Can be: `true`, `false`, `record-
            from-start`, and `do-not-record`. The default value is
            `false`.
        conference_recording_status_callback:
            The URL we should call using the
            `conference_recording_status_callback_method` when the
            conference recording is available.
        conference_recording_status_callback_method:
            The HTTP method we should use to call
            `conference_recording_status_callback`. Can be: `GET` or
            `POST` and defaults to `POST`.
        conference_status_callback:
            The URL we should call using the `conference_status_callback_method`
            when the conference events in
            `conference_status_callback_event` occur. Only the value set
            by the first participant to join the conference is used.
            Subsequent `conference_status_callback` values are ignored.
        conference_status_callback_event:
            The conference status events that we will send to
            `conference_status_callback`. Can be: `start`, `end`,
            `join`, `leave`, `mute`, `hold`, `speaker`.
        conference_status_callback_method:
            The HTTP method we should use to call `conference_status_callback`. Can
            be: `GET` or `POST` and defaults to `POST`.
        conference_trim:
            How to trim the leading and trailing silence from your recorded
            conference audio files. Can be: `trim-silence` or `do-not-
            trim` and defaults to `trim-silence`.
        dequeue_from:
            The Caller ID of the call to the worker when executing a Dequeue
            instruction.
        dequeue_post_work_activity_sid:
            The SID of the Activity resource to start after executing a Dequeue
            instruction.
        dequeue_record:
            Whether to record both legs of a call when executing a Dequeue
            instruction or which leg to record.
        dequeue_status_callback_event:
            The Call progress events sent via webhooks as a result of a Dequeue
            instruction.
        dequeue_status_callback_url:
            The Callback URL for completed call event when executing a Dequeue
            instruction.
        dequeue_timeout:
            Timeout for call when executing a Dequeue instruction.
        dequeue_to:
            The Contact URI of the worker when executing a Dequeue instruction. Can
            be the URI of the Twilio Client, the SIP URI for
            Programmable SIP, or the
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            formatted phone number, depending on the destination.
        early_media:
            Whether to allow an agent to hear the state of the outbound call,
            including ringing or disconnect messages. The default is
            `true`.
        end_conference_on_customer_exit:
            Whether to end the conference when the customer leaves.
        end_conference_on_exit:
            Whether to end the conference when the agent leaves.
        from_:
            The Caller ID of the call to the worker when executing a Conference
            instruction.
        instruction:
            The assignment instruction for reservation.
        max_participants:
            The maximum number of participants in the conference. Can be a positive
            integer from `2` to `250`. The default value is `250`.
        muted:
            Whether the agent is muted in the conference. The default is `false`.
        post_work_activity_sid:
            The new worker activity SID after executing a Conference instruction.
        record:
            Whether to record the participant and their conferences, including the
            time between conferences. The default is `false`.
        recording_channels:
            The recording channels for the final recording. Can be: `mono` or `dual`
            and the default is `mono`.
        recording_status_callback:
            The URL that we should call using the `recording_status_callback_method`
            when the recording status changes.
        recording_status_callback_method:
            The HTTP method we should use when we call `recording_status_callback`.
            Can be: `GET` or `POST` and defaults to `POST`.
        redirect_accept:
            Whether the reservation should be accepted when executing a Redirect
            instruction.
        redirect_call_sid:
            The Call SID of the call parked in the queue when executing a Redirect
            instruction.
        redirect_url:
            TwiML URI to redirect the call to when executing the Redirect
            instruction.
        region:
            The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-
            global-low-latency-routing-and-region-selection-work-for-
            conferences-and-Client-calls) where we should mix the
            recorded audio. Can be:`us1`, `ie1`, `de1`, `sg1`, `br1`,
            `au1`, or `jp1`.
        reservation_status:
            The new status of the reservation. Can be: `pending`, `accepted`,
            `rejected`, or `timeout`.
        sip_auth_password:
            The SIP password for authentication.
        sip_auth_username:
            The SIP username used for authentication.
        start_conference_on_enter:
            Whether to start the conference when the participant joins, if it has
            not already started. The default is `true`. If `false` and
            the conference has not started, the participant is muted and
            hears background music until another participant starts the
            conference.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_event:
            The call progress events that we will send to `status_callback`. Can be:
            `initiated`, `ringing`, `answered`, or `completed`.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `POST`
            or `GET` and the default is `POST`.
        supervisor:
            The Supervisor SID/URI when executing the Supervise instruction.
        supervisor_mode:
            The Supervisor mode when executing the Supervise instruction.
        timeout:
            Timeout for call when executing a Conference instruction.
        to:
            The Contact URI of the worker when executing a Conference instruction.
            Can be the URI of the Twilio Client, the SIP URI for
            Programmable SIP, or the
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            formatted phone number, depending on the destination.
        wait_method:
            The HTTP method we should use to call `wait_url`. Can be `GET` or `POST`
            and the default is `POST`. When using a static audio file,
            this should be `GET` so that we can cache the file.
        wait_url:
            The URL we should call using the `wait_method` for the music to play
            while participants are waiting for the conference to start.
            The default value is the URL of our standard hold music.
            [Learn more about hold
            music](https://www.twilio.com/labs/twimlets/holdmusic).
        worker_activity_sid:
            The new worker activity SID if rejecting a reservation.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}?&if_match=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    data = {
        "beep": beep,
        "beep_on_customer_entrance": beep_on_customer_entrance,
        "call_accept": call_accept,
        "call_from": call_from,
        "call_record": call_record,
        "call_status_callback_url": call_status_callback_url,
        "call_timeout": call_timeout,
        "call_to": call_to,
        "call_url": call_url,
        "conference_record": conference_record,
        "conference_recording_status_callback": conference_recording_status_callback,  # noqa
        "conference_recording_status_callback_method": conference_recording_status_callback_method,  # noqa
        "conference_status_callback": conference_status_callback,
        "conference_status_callback_event": conference_status_callback_event,
        "conference_status_callback_method": conference_status_callback_method,
        "conference_trim": conference_trim,
        "dequeue_from": dequeue_from,
        "dequeue_post_work_activity_sid": dequeue_post_work_activity_sid,
        "dequeue_record": dequeue_record,
        "dequeue_status_callback_event": dequeue_status_callback_event,
        "dequeue_status_callback_url": dequeue_status_callback_url,
        "dequeue_timeout": dequeue_timeout,
        "dequeue_to": dequeue_to,
        "early_media": early_media,
        "end_conference_on_customer_exit": end_conference_on_customer_exit,
        "end_conference_on_exit": end_conference_on_exit,
        "from_": from_,
        "instruction": instruction,
        "max_participants": max_participants,
        "muted": muted,
        "post_work_activity_sid": post_work_activity_sid,
        "record": record,
        "recording_channels": recording_channels,
        "recording_status_callback": recording_status_callback,
        "recording_status_callback_method": recording_status_callback_method,
        "redirect_accept": redirect_accept,
        "redirect_call_sid": redirect_call_sid,
        "redirect_url": redirect_url,
        "region": region,
        "reservation_status": reservation_status,
        "sip_auth_password": sip_auth_password,
        "sip_auth_username": sip_auth_username,
        "start_conference_on_enter": start_conference_on_enter,
        "status_callback": status_callback,
        "status_callback_event": status_callback_event,
        "status_callback_method": status_callback_method,
        "supervisor": supervisor,
        "supervisor_mode": supervisor_mode,
        "timeout": timeout,
        "to": to,
        "wait_method": wait_method,
        "wait_url": wait_url,
        "worker_activity_sid": worker_activity_sid,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_workspaces_workspace_sid_workers(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    activity_name: str = None,
    activity_sid: str = None,
    available: str = None,
    friendly_name: str = None,
    target_workers_expression: str = None,
    task_queue_name: str = None,
    task_queue_sid: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        activity_name:
            The `activity_name` of the Worker resources to read.
        activity_sid:
            The `activity_sid` of the Worker resources to read.
        available:
            Whether to return only Worker resources that are available or
            unavailable. Can be `true`, `1`, or `yes` to return Worker
            resources that are available, and `false`, or any value
            returns the Worker resources that are not available.
        friendly_name:
            The `friendly_name` of the Worker resources to read.
        target_workers_expression:
            Filter by Workers that would match an expression on a TaskQueue. This is
            helpful for debugging which Workers would match a potential
            queue.
        task_queue_name:
            The `friendly_name` of the TaskQueue that the Workers to read are
            eligible for.
        task_queue_sid:
            The SID of the TaskQueue that the Workers to read are eligible for.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers?&activity_name=%s&activity_sid=%s&available=%s&friendly_name=%s&target_workers_expression=%s&task_queue_name=%s&task_queue_sid=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers?&activity_name=%s&activity_sid=%s&available=%s&friendly_name=%s&target_workers_expression=%s&task_queue_name=%s&task_queue_sid=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "activity_name": activity_name,
        "activity_sid": activity_sid,
        "available": available,
        "friendly_name": friendly_name,
        "target_workers_expression": target_workers_expression,
        "task_queue_name": task_queue_name,
        "task_queue_sid": task_queue_sid,
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
async def post_v1_workspaces_workspace_sid_workers(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    activity_sid: str = None,
    attributes: str = None,
    friendly_name: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        activity_sid:
            The SID of a valid Activity that will describe the new Worker's initial
            state. See
            [Activities](https://www.twilio.com/docs/taskrouter/api/activity)
            for more information. If not provided, the new Worker's
            initial state is the `default_activity_sid` configured on
            the Workspace.
        attributes:
            A valid JSON string that describes the new Worker. For example: `{
            "email": "Bob@example.com", "phone": "+5095551234" }`. This
            data is passed to the `assignment_callback_url` when
            TaskRouter assigns a Task to the Worker. Defaults to {}.
        friendly_name:
            A descriptive string that you create to describe the new Worker. It can
            be up to 64 characters long.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers"  # noqa
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "activity_sid": activity_sid,
        "attributes": attributes,
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
async def get_v1_workspaces_workspace_sid_workers_cumulative_statistics(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    end_date: str = None,
    minutes: int = None,
    start_date: str = None,
    task_channel: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_date:
            Only calculate statistics from this date and time and earlier, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default 15 minutes. This is helpful for displaying
            statistics for the last 15 minutes, 240 minutes (4 hours),
            and 480 minutes (8 hours) to see trends.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        task_channel:
            Only calculate cumulative statistics on this TaskChannel. Can be the
            TaskChannel's SID or its `unique_name`, such as `voice`,
            `sms`, or `default`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/CumulativeStatistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/CumulativeStatistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/CumulativeStatistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end_date": end_date,
        "minutes": minutes,
        "start_date": start_date,
        "task_channel": task_channel,
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
async def get_v1_workspaces_workspace_sid_workers_real_time_statistics(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    task_channel: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        task_channel:
            Only calculate real-time statistics on this TaskChannel. Can be the
            TaskChannel's SID or its `unique_name`, such as `voice`,
            `sms`, or `default`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/RealTimeStatistics?&task_channel=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/RealTimeStatistics?&task_channel=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/RealTimeStatistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "task_channel": task_channel,
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
async def get_v1_workspaces_workspace_sid_workers_statistics(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    minutes: int = None,
    start_date: str = None,
    end_date: str = None,
    task_queue_sid: str = None,
    task_queue_name: str = None,
    friendly_name: str = None,
    task_channel: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default 15 minutes. This is helpful for displaying
            statistics for the last 15 minutes, 240 minutes (4 hours),
            and 480 minutes (8 hours) to see trends.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        end_date:
            Only calculate statistics from this date and time and earlier, specified
            in GMT as an [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        task_queue_sid:
            The SID of the TaskQueue for which to fetch Worker statistics.
        task_queue_name:
            The `friendly_name` of the TaskQueue for which to fetch Worker
            statistics.
        friendly_name:
            Only include Workers with `friendly_name` values that match this
            parameter.
        task_channel:
            Only calculate statistics on this TaskChannel. Can be the TaskChannel's
            SID or its `unique_name`, such as `voice`, `sms`, or
            `default`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/Statistics?&minutes=%s&start_date=%s&end_date=%s&task_queue_sid=%s&task_queue_name=%s&friendly_name=%s&task_channel=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/Statistics?&minutes=%s&start_date=%s&end_date=%s&task_queue_sid=%s&task_queue_name=%s&friendly_name=%s&task_channel=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/Statistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "minutes": minutes,
        "start_date": start_date,
        "end_date": end_date,
        "task_queue_sid": task_queue_sid,
        "task_queue_name": task_queue_name,
        "friendly_name": friendly_name,
        "task_channel": task_channel,
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
async def delete_v1_workspaces_workspace_sid_workers_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            The If-Match HTTP request header.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{sid}?&if_match=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{sid}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{sid}"  # noqa
    responses = {
        204: "The resource was deleted successfully.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_v1_workspaces_workspace_sid_workers_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{sid}"  # noqa
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
async def post_v1_workspaces_workspace_sid_workers_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
    activity_sid: str = None,
    attributes: str = None,
    friendly_name: str = None,
    reject_pending_reservations: bool = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            The If-Match HTTP request header.
        activity_sid:
            The SID of a valid Activity that will describe the Worker's initial
            state. See
            [Activities](https://www.twilio.com/docs/taskrouter/api/activity)
            for more information.
        attributes:
            The JSON string that describes the Worker. For example: `{ "email":
            "Bob@example.com", "phone": "+5095551234" }`. This data is
            passed to the `assignment_callback_url` when TaskRouter
            assigns a Task to the Worker. Defaults to {}.
        friendly_name:
            A descriptive string that you create to describe the Worker. It can be
            up to 64 characters long.
        reject_pending_reservations:
            Whether to reject the Worker's pending reservations. This option is only
            valid if the Worker's new
            [Activity](https://www.twilio.com/docs/taskrouter/api/activity)
            resource has its `availability` property set to `False`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{sid}?&if_match=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{sid}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    data = {
        "activity_sid": activity_sid,
        "attributes": attributes,
        "friendly_name": friendly_name,
        "reject_pending_reservations": reject_pending_reservations,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_workspaces_workspace_sid_workers_worker_sid_channels(
    workspace_sid: str,
    worker_sid: str,
    twilio_credentials: "TwilioCredentials",
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        worker_sid:
            Worker sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels?&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels?&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels"  # noqa
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
async def get_v1_workspaces_workspace_sid_workers_worker_sid_channels_sid(
    workspace_sid: str,
    worker_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        worker_sid:
            Worker sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels/{sid}"  # noqa
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
async def post_v1_workspaces_workspace_sid_workers_worker_sid_channels_sid(
    workspace_sid: str,
    worker_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    available: bool = None,
    capacity: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        worker_sid:
            Worker sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        available:
            Whether the WorkerChannel is available. Set to `false` to prevent the
            Worker from receiving any new Tasks of this TaskChannel
            type.
        capacity:
            The total number of Tasks that the Worker should handle for the
            TaskChannel type. TaskRouter creates reservations for Tasks
            of this TaskChannel type up to the specified capacity. If
            the capacity is 0, no new reservations will be created.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "available": available,
        "capacity": capacity,
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
async def get_v1_workspaces_workspace_sid_workers_worker_sid_reservations(
    workspace_sid: str,
    worker_sid: str,
    twilio_credentials: "TwilioCredentials",
    reservation_status: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        worker_sid:
            Worker sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        reservation_status:
            Returns the list of reservations for a worker with a specified
            ReservationStatus. Can be: `pending`, `accepted`,
            `rejected`, `timeout`, `canceled`, or `rescinded`.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations?&reservation_status=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations?&reservation_status=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "reservation_status": reservation_status,
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
async def get_v1_workspaces_workspace_sid_workers_worker_sid_reservations_sid(
    workspace_sid: str,
    worker_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        worker_sid:
            Worker sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations/{sid}"  # noqa
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
async def post_v1_workspaces_workspace_sid_workers_worker_sid_reservations_sid(
    workspace_sid: str,
    worker_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    if_match: str = None,
    beep: str = None,
    beep_on_customer_entrance: bool = None,
    call_accept: bool = None,
    call_from: str = None,
    call_record: str = None,
    call_status_callback_url: str = None,
    call_timeout: int = None,
    call_to: str = None,
    call_url: str = None,
    conference_record: str = None,
    conference_recording_status_callback: str = None,
    conference_recording_status_callback_method: str = None,
    conference_status_callback: str = None,
    conference_status_callback_event: list = None,
    conference_status_callback_method: str = None,
    conference_trim: str = None,
    dequeue_from: str = None,
    dequeue_post_work_activity_sid: str = None,
    dequeue_record: str = None,
    dequeue_status_callback_event: list = None,
    dequeue_status_callback_url: str = None,
    dequeue_timeout: int = None,
    dequeue_to: str = None,
    early_media: bool = None,
    end_conference_on_customer_exit: bool = None,
    end_conference_on_exit: bool = None,
    from_: str = None,
    instruction: str = None,
    max_participants: int = None,
    muted: bool = None,
    post_work_activity_sid: str = None,
    record: bool = None,
    recording_channels: str = None,
    recording_status_callback: str = None,
    recording_status_callback_method: str = None,
    redirect_accept: bool = None,
    redirect_call_sid: str = None,
    redirect_url: str = None,
    region: str = None,
    reservation_status: str = None,
    sip_auth_password: str = None,
    sip_auth_username: str = None,
    start_conference_on_enter: bool = None,
    status_callback: str = None,
    status_callback_event: list = None,
    status_callback_method: str = None,
    timeout: int = None,
    to: str = None,
    wait_method: str = None,
    wait_url: str = None,
    worker_activity_sid: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        worker_sid:
            Worker sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        if_match:
            The If-Match HTTP request header.
        beep:
            Whether to play a notification beep when the participant joins or when
            to play a beep. Can be: `true`, `false`, `onEnter`, or
            `onExit`. The default value is `true`.
        beep_on_customer_entrance:
            Whether to play a notification beep when the customer joins.
        call_accept:
            Whether to accept a reservation when executing a Call instruction.
        call_from:
            The Caller ID of the outbound call when executing a Call instruction.
        call_record:
            Whether to record both legs of a call when executing a Call instruction.
        call_status_callback_url:
            The URL to call for the completed call event when executing a Call
            instruction.
        call_timeout:
            The timeout for a call when executing a Call instruction.
        call_to:
            The contact URI of the worker when executing a Call instruction. Can be
            the URI of the Twilio Client, the SIP URI for Programmable
            SIP, or the
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            formatted phone number, depending on the destination.
        call_url:
            TwiML URI executed on answering the worker's leg as a result of the Call
            instruction.
        conference_record:
            Whether to record the conference the participant is joining or when to
            record the conference. Can be: `true`, `false`, `record-
            from-start`, and `do-not-record`. The default value is
            `false`.
        conference_recording_status_callback:
            The URL we should call using the
            `conference_recording_status_callback_method` when the
            conference recording is available.
        conference_recording_status_callback_method:
            The HTTP method we should use to call
            `conference_recording_status_callback`. Can be: `GET` or
            `POST` and defaults to `POST`.
        conference_status_callback:
            The URL we should call using the `conference_status_callback_method`
            when the conference events in
            `conference_status_callback_event` occur. Only the value set
            by the first participant to join the conference is used.
            Subsequent `conference_status_callback` values are ignored.
        conference_status_callback_event:
            The conference status events that we will send to
            `conference_status_callback`. Can be: `start`, `end`,
            `join`, `leave`, `mute`, `hold`, `speaker`.
        conference_status_callback_method:
            The HTTP method we should use to call `conference_status_callback`. Can
            be: `GET` or `POST` and defaults to `POST`.
        conference_trim:
            Whether to trim leading and trailing silence from your recorded
            conference audio files. Can be: `trim-silence` or `do-not-
            trim` and defaults to `trim-silence`.
        dequeue_from:
            The caller ID of the call to the worker when executing a Dequeue
            instruction.
        dequeue_post_work_activity_sid:
            The SID of the Activity resource to start after executing a Dequeue
            instruction.
        dequeue_record:
            Whether to record both legs of a call when executing a Dequeue
            instruction or which leg to record.
        dequeue_status_callback_event:
            The call progress events sent via webhooks as a result of a Dequeue
            instruction.
        dequeue_status_callback_url:
            The callback URL for completed call event when executing a Dequeue
            instruction.
        dequeue_timeout:
            The timeout for call when executing a Dequeue instruction.
        dequeue_to:
            The contact URI of the worker when executing a Dequeue instruction. Can
            be the URI of the Twilio Client, the SIP URI for
            Programmable SIP, or the
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            formatted phone number, depending on the destination.
        early_media:
            Whether to allow an agent to hear the state of the outbound call,
            including ringing or disconnect messages. The default is
            `true`.
        end_conference_on_customer_exit:
            Whether to end the conference when the customer leaves.
        end_conference_on_exit:
            Whether to end the conference when the agent leaves.
        from_:
            The caller ID of the call to the worker when executing a Conference
            instruction.
        instruction:
            The assignment instruction for the reservation.
        max_participants:
            The maximum number of participants allowed in the conference. Can be a
            positive integer from `2` to `250`. The default value is
            `250`.
        muted:
            Whether the agent is muted in the conference. Defaults to `false`.
        post_work_activity_sid:
            The new worker activity SID after executing a Conference instruction.
        record:
            Whether to record the participant and their conferences, including the
            time between conferences. Can be `true` or `false` and the
            default is `false`.
        recording_channels:
            The recording channels for the final recording. Can be: `mono` or `dual`
            and the default is `mono`.
        recording_status_callback:
            The URL that we should call using the `recording_status_callback_method`
            when the recording status changes.
        recording_status_callback_method:
            The HTTP method we should use when we call `recording_status_callback`.
            Can be: `GET` or `POST` and defaults to `POST`.
        redirect_accept:
            Whether the reservation should be accepted when executing a Redirect
            instruction.
        redirect_call_sid:
            The Call SID of the call parked in the queue when executing a Redirect
            instruction.
        redirect_url:
            TwiML URI to redirect the call to when executing the Redirect
            instruction.
        region:
            The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-
            global-low-latency-routing-and-region-selection-work-for-
            conferences-and-Client-calls) where we should mix the
            recorded audio. Can be:`us1`, `ie1`, `de1`, `sg1`, `br1`,
            `au1`, or `jp1`.
        reservation_status:
            The new status of the reservation. Can be: `pending`, `accepted`,
            `rejected`, `timeout`, `canceled`, or `rescinded`.
        sip_auth_password:
            The SIP password for authentication.
        sip_auth_username:
            The SIP username used for authentication.
        start_conference_on_enter:
            Whether to start the conference when the participant joins, if it has
            not already started. Can be: `true` or `false` and the
            default is `true`. If `false` and the conference has not
            started, the participant is muted and hears background music
            until another participant starts the conference.
        status_callback:
            The URL we should call using the `status_callback_method` to send status
            information to your application.
        status_callback_event:
            The call progress events that we will send to `status_callback`. Can be:
            `initiated`, `ringing`, `answered`, or `completed`.
        status_callback_method:
            The HTTP method we should use to call `status_callback`. Can be: `POST`
            or `GET` and the default is `POST`.
        timeout:
            The timeout for a call when executing a Conference instruction.
        to:
            The Contact URI of the worker when executing a Conference instruction.
            Can be the URI of the Twilio Client, the SIP URI for
            Programmable SIP, or the
            [E.164](https://www.twilio.com/docs/glossary/what-e164)
            formatted phone number, depending on the destination.
        wait_method:
            The HTTP method we should use to call `wait_url`. Can be `GET` or `POST`
            and the default is `POST`. When using a static audio file,
            this should be `GET` so that we can cache the file.
        wait_url:
            The URL we should call using the `wait_method` for the music to play
            while participants are waiting for the conference to start.
            The default value is the URL of our standard hold music.
            [Learn more about hold
            music](https://www.twilio.com/labs/twimlets/holdmusic).
        worker_activity_sid:
            The new worker activity SID if rejecting a reservation.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations/{sid}?&if_match=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations/{sid}?&if_match=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Reservations/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "if_match": if_match,
    }

    data = {
        "beep": beep,
        "beep_on_customer_entrance": beep_on_customer_entrance,
        "call_accept": call_accept,
        "call_from": call_from,
        "call_record": call_record,
        "call_status_callback_url": call_status_callback_url,
        "call_timeout": call_timeout,
        "call_to": call_to,
        "call_url": call_url,
        "conference_record": conference_record,
        "conference_recording_status_callback": conference_recording_status_callback,  # noqa
        "conference_recording_status_callback_method": conference_recording_status_callback_method,  # noqa
        "conference_status_callback": conference_status_callback,
        "conference_status_callback_event": conference_status_callback_event,
        "conference_status_callback_method": conference_status_callback_method,
        "conference_trim": conference_trim,
        "dequeue_from": dequeue_from,
        "dequeue_post_work_activity_sid": dequeue_post_work_activity_sid,
        "dequeue_record": dequeue_record,
        "dequeue_status_callback_event": dequeue_status_callback_event,
        "dequeue_status_callback_url": dequeue_status_callback_url,
        "dequeue_timeout": dequeue_timeout,
        "dequeue_to": dequeue_to,
        "early_media": early_media,
        "end_conference_on_customer_exit": end_conference_on_customer_exit,
        "end_conference_on_exit": end_conference_on_exit,
        "from_": from_,
        "instruction": instruction,
        "max_participants": max_participants,
        "muted": muted,
        "post_work_activity_sid": post_work_activity_sid,
        "record": record,
        "recording_channels": recording_channels,
        "recording_status_callback": recording_status_callback,
        "recording_status_callback_method": recording_status_callback_method,
        "redirect_accept": redirect_accept,
        "redirect_call_sid": redirect_call_sid,
        "redirect_url": redirect_url,
        "region": region,
        "reservation_status": reservation_status,
        "sip_auth_password": sip_auth_password,
        "sip_auth_username": sip_auth_username,
        "start_conference_on_enter": start_conference_on_enter,
        "status_callback": status_callback,
        "status_callback_event": status_callback_event,
        "status_callback_method": status_callback_method,
        "timeout": timeout,
        "to": to,
        "wait_method": wait_method,
        "wait_url": wait_url,
        "worker_activity_sid": worker_activity_sid,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_v1_workspaces_workspace_sid_workers_worker_sid_statistics(
    workspace_sid: str,
    worker_sid: str,
    twilio_credentials: "TwilioCredentials",
    minutes: int = None,
    start_date: str = None,
    end_date: str = None,
    task_channel: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        worker_sid:
            Worker sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default 15 minutes. This is helpful for displaying
            statistics for the last 15 minutes, 240 minutes (4 hours),
            and 480 minutes (8 hours) to see trends.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        end_date:
            Only include usage that occurred on or before this date, specified in
            GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            date-time.
        task_channel:
            Only calculate statistics on this TaskChannel. Can be the TaskChannel's
            SID or its `unique_name`, such as `voice`, `sms`, or
            `default`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Statistics?&minutes=%s&start_date=%s&end_date=%s&task_channel=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Statistics?&minutes=%s&start_date=%s&end_date=%s&task_channel=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Statistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "minutes": minutes,
        "start_date": start_date,
        "end_date": end_date,
        "task_channel": task_channel,
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
async def get_v1_workspaces_workspace_sid_workflows(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    friendly_name: str = None,
    page_size: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        friendly_name:
            The `friendly_name` of the Workflow resources to read.
        page_size:
            How many resources to return in each list page. The default is 50, and
            the maximum is 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows?&friendly_name=%s&page_size=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows?&friendly_name=%s&page_size=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = (
        f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows"  # noqa
    )
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


@task
async def post_v1_workspaces_workspace_sid_workflows(
    workspace_sid: str,
    twilio_credentials: "TwilioCredentials",
    assignment_callback_url: str = None,
    configuration: str = None,
    fallback_assignment_callback_url: str = None,
    friendly_name: str = None,
    task_reservation_timeout: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        assignment_callback_url:
            The URL from your application that will process task assignment events.
            See [Handling Task Assignment
            Callback](https://www.twilio.com/docs/taskrouter/handle-
            assignment-callbacks) for more details.
        configuration:
            A JSON string that contains the rules to apply to the Workflow. See
            [Configuring
            Workflows](https://www.twilio.com/docs/taskrouter/workflow-
            configuration) for more information.
        fallback_assignment_callback_url:
            The URL that we should call when a call to the `assignment_callback_url`
            fails.
        friendly_name:
            A descriptive string that you create to describe the Workflow resource.
            For example, `Inbound Call Workflow` or `2014 Outbound
            Campaign`.
        task_reservation_timeout:
            How long TaskRouter will wait for a confirmation response from your
            application after it assigns a Task to a Worker. Can be up
            to `86,400` (24 hours) and the default is `120`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Created. |
    """  # noqa
    url = (
        f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows"  # noqa
    )
    responses = {
        201: "Created.",  # noqa
    }

    data = {
        "assignment_callback_url": assignment_callback_url,
        "configuration": configuration,
        "fallback_assignment_callback_url": fallback_assignment_callback_url,
        "friendly_name": friendly_name,
        "task_reservation_timeout": task_reservation_timeout,
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
async def delete_v1_workspaces_workspace_sid_workflows_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The resource was deleted successfully. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{sid}"  # noqa
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
async def get_v1_workspaces_workspace_sid_workflows_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{sid}"  # noqa
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
async def post_v1_workspaces_workspace_sid_workflows_sid(
    workspace_sid: str,
    sid: str,
    twilio_credentials: "TwilioCredentials",
    assignment_callback_url: str = None,
    configuration: str = None,
    fallback_assignment_callback_url: str = None,
    friendly_name: str = None,
    re_evaluate_tasks: str = None,
    task_reservation_timeout: int = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        sid:
            Sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        assignment_callback_url:
            The URL from your application that will process task assignment events.
            See [Handling Task Assignment
            Callback](https://www.twilio.com/docs/taskrouter/handle-
            assignment-callbacks) for more details.
        configuration:
            A JSON string that contains the rules to apply to the Workflow. See
            [Configuring
            Workflows](https://www.twilio.com/docs/taskrouter/workflow-
            configuration) for more information.
        fallback_assignment_callback_url:
            The URL that we should call when a call to the `assignment_callback_url`
            fails.
        friendly_name:
            A descriptive string that you create to describe the Workflow resource.
            For example, `Inbound Call Workflow` or `2014 Outbound
            Campaign`.
        re_evaluate_tasks:
            Whether or not to re-evaluate Tasks. The default is `false`, which means
            Tasks in the Workflow will not be processed through the
            assignment loop again.
        task_reservation_timeout:
            How long TaskRouter will wait for a confirmation response from your
            application after it assigns a Task to a Worker. Can be up
            to `86,400` (24 hours) and the default is `120`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{sid}?](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{sid}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{sid}"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    data = {
        "assignment_callback_url": assignment_callback_url,
        "configuration": configuration,
        "fallback_assignment_callback_url": fallback_assignment_callback_url,
        "friendly_name": friendly_name,
        "re_evaluate_tasks": re_evaluate_tasks,
        "task_reservation_timeout": task_reservation_timeout,
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
async def get_v1_workspaces_workspace_sid_workflows_workflow_sid_cumulative_statistics(
    workspace_sid: str,
    workflow_sid: str,
    twilio_credentials: "TwilioCredentials",
    end_date: str = None,
    minutes: int = None,
    start_date: str = None,
    task_channel: str = None,
    split_by_wait_time: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        workflow_sid:
            Workflow sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        end_date:
            Only include usage that occurred on or before this date, specified in
            GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            date-time.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default 15 minutes. This is helpful for displaying
            statistics for the last 15 minutes, 240 minutes (4 hours),
            and 480 minutes (8 hours) to see trends.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        task_channel:
            Only calculate cumulative statistics on this TaskChannel. Can be the
            TaskChannel's SID or its `unique_name`, such as `voice`,
            `sms`, or `default`.
        split_by_wait_time:
            A comma separated list of values that describes the thresholds, in
            seconds, to calculate statistics on. For each threshold
            specified, the number of Tasks canceled and reservations
            accepted above and below the specified thresholds in seconds
            are computed. For example, `5,30` would show splits of Tasks
            that were canceled or accepted before and after 5 seconds
            and before and after 30 seconds. This can be used to show
            short abandoned Tasks or Tasks that failed to meet an SLA.
            TaskRouter will calculate statistics on up to 10,000 Tasks
            for any given threshold.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/CumulativeStatistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/CumulativeStatistics?&end_date=%s&minutes=%s&start_date=%s&task_channel=%s&split_by_wait_time=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/CumulativeStatistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "end_date": end_date,
        "minutes": minutes,
        "start_date": start_date,
        "task_channel": task_channel,
        "split_by_wait_time": split_by_wait_time,
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
async def get_v1_workspaces_workspace_sid_workflows_workflow_sid_real_time_statistics(
    workspace_sid: str,
    workflow_sid: str,
    twilio_credentials: "TwilioCredentials",
    task_channel: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        workflow_sid:
            Workflow sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        task_channel:
            Only calculate real-time statistics on this TaskChannel. Can be the
            TaskChannel's SID or its `unique_name`, such as `voice`,
            `sms`, or `default`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/RealTimeStatistics?&task_channel=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/RealTimeStatistics?&task_channel=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/RealTimeStatistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "task_channel": task_channel,
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
async def get_v1_workspaces_workspace_sid_workflows_workflow_sid_statistics(
    workspace_sid: str,
    workflow_sid: str,
    twilio_credentials: "TwilioCredentials",
    minutes: int = None,
    start_date: str = None,
    end_date: str = None,
    task_channel: str = None,
    split_by_wait_time: str = None,
) -> Dict[str, Any]:
    """


    Args:
        workspace_sid:
            Workspace sid used in formatting the endpoint URL.
        workflow_sid:
            Workflow sid used in formatting the endpoint URL.
        twilio_credentials:
            Credentials to use for authentication with Twilio.
        minutes:
            Only calculate statistics since this many minutes in the past. The
            default 15 minutes. This is helpful for displaying
            statistics for the last 15 minutes, 240 minutes (4 hours),
            and 480 minutes (8 hours) to see trends.
        start_date:
            Only calculate statistics from this date and time and later, specified
            in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
            format.
        end_date:
            Only calculate statistics from this date and time and earlier, specified
            in GMT as an [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        task_channel:
            Only calculate real-time statistics on this TaskChannel. Can be the
            TaskChannel's SID or its `unique_name`, such as `voice`,
            `sms`, or `default`.
        split_by_wait_time:
            A comma separated list of values that describes the thresholds, in
            seconds, to calculate statistics on. For each threshold
            specified, the number of Tasks canceled and reservations
            accepted above and below the specified thresholds in seconds
            are computed. For example, `5,30` would show splits of Tasks
            that were canceled or accepted before and after 5 seconds
            and before and after 30 seconds. This can be used to show
            short abandoned Tasks or Tasks that failed to meet an SLA.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/Statistics?&minutes=%s&start_date=%s&end_date=%s&task_channel=%s&split_by_wait_time=%s](
    https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/Statistics?&minutes=%s&start_date=%s&end_date=%s&task_channel=%s&split_by_wait_time=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    """  # noqa
    url = f"https://taskrouter.twilio.com/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/Statistics"  # noqa
    responses = {
        200: "OK.",  # noqa
    }

    params = {
        "minutes": minutes,
        "start_date": start_date,
        "end_date": end_date,
        "task_channel": task_channel,
        "split_by_wait_time": split_by_wait_time,
    }

    result = await execute_endpoint.fn(
        url,
        twilio_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
