from rest_framework import serializers
from .models import Student

#serializer-
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     #for update-
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance
#     # def validate_roll(self, value):
#     #     if value >= 100:
#     #         raise serializers.ValidationError('Seat Full')
#     #     return value
#     def validate(self,data):
#         nm = data.get('name')
#         if nm != "jay":
#             raise serializers.ValidationError("YOu are not jay")
#         return data

#model Serializerss-
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']