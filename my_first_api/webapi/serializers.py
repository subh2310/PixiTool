from rest_framework import serializers

# Create your serializers here.
class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    email = serializers.EmailField(max_length=50)
    city = serializers.CharField(max_length=50)