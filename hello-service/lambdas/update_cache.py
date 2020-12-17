def update_cache(event, context):
    """
    Will be inovked when S3 object is created
    :param event:
    :param context:
    :return:
    """
    print("Received event: {}".format(event))
    return "SUCCESS"
