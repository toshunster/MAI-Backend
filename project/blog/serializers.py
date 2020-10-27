from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
