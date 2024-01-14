from rest_framework.serializers import ModelSerializer
from customer_support.models.messages import Message

class MessageCreateSerializer(ModelSerializer):
    class Meta:
        model=Message
        fields='__all__'
        extra_kwargs={'messageID': {'required': False}}