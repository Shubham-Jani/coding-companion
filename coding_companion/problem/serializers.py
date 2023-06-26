from rest_framework import serializers
from .models import Problem, TopicTag


class TopicTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicTag
        fields = ('tag',)


class ProblemSerializer(serializers.ModelSerializer):
    tag = TopicTagSerializer(many=True)  # Updated field name

    class Meta:
        model = Problem
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tag')  # Updated field name

        problem = Problem.objects.create(**validated_data)

        for tag_data in tags_data:
            tag, _ = TopicTag.objects.get_or_create(tag=tag_data['tag'])
            problem.tag.add(tag)  # Updated field name

        return problem
