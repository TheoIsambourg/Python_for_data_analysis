from rest_framework import serializers
from prediction.models import Activity

class ActivitySerializer(serializers.Serializer):
    ACTIVITY_ID = serializers.IntegerField(allow_null=True)
    ACC_X = serializers.JSONField()

    def create(self, validated_data):
        return Activity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #instance.ACTIVITY_ID = validated_data.get('ACTIVITY_ID', instance.ACTIVITY_ID)
        instance.ACC_X = validated_data.get('ACC_X', instance.ACC_X)
        instance.save()
        return instance
