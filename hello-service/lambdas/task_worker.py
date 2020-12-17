def run_query_task(event, context):
    """
    Will be invoked whenever an SQS event is dequeued.

    :param event:
    :param context:
    :return:
    """
    print("Received query event: {}".format(event))
    return "SUCCESS"
