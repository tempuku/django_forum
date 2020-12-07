from app.celery import app
from django.utils.crypto import get_random_string
from forum.models import Forum


@app.task
def randomly_forums(user_id, total):
    for i in range(total):
        random_title = get_random_string(50)
        Forum.objects.create(user=user_id, title=random_title)
    return f'{total} topics were created'
