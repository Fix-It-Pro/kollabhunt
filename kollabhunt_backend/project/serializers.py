from kollabhunt.models.projects import Project
from kollabhunt.models.users import User
from rest_framework import serializers, exceptions

class ProjectSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=600)
    description = serializers.CharField()
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    def validate_owner(self, value):
        try:
            if value:
                return value
            else:
                raise serializers.ValidationError()
        except Exception as e:
            raise exceptions.APIException("Failed to validate object." + str(e))

    def validate_creator(self, value):
        try:
            if value:
                return value
            else:
                raise serializers.ValidationError()
        except Exception as e:
            raise exceptions.APIException("Failed to validate object." + str(e))

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for item in validated_data:
            setattr(instance, item.key, item.value)
        instance.save()
        return instance



