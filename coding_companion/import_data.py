import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coding_companion.settings')
django.setup()

from problem.models import Problem, TopicTag
import json

with open("leetcode.json", "r") as file:
    data = json.loads(file.read())
    for item in data:
        # Split tags and remove whitespace
        tags = [tag.strip() for tag in item['topic_tags'].split(',') if tag.strip()]

        # Create TopicTag instances and add them to a list
        topic_tags = []
        for tag in tags:
            topic_tag, _ = TopicTag.objects.get_or_create(tag=tag)
            topic_tags.append(topic_tag)

        # Create Problem instance
        problem = Problem.objects.create(
            title=item['title'],
            likes=item['likes'],
            category=item['category'],
            difficulty=item['difficulty'],
            has_solution=item['has_solution'],
        )
        problem.tag.set(topic_tags)
