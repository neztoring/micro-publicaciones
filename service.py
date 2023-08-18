from datetime import datetime


def create_post(request):

    current_date = datetime.now()
    return { "id": "1", "userId":"1", "createdAt": current_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')},201