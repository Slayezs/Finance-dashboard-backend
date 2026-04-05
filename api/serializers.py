from rest_framework import serializers
from .models import AppUser, FinancialRecord

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return AppUser.objects.create_user(**validated_data)


class FinancialRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialRecord
        fields = '__all__'
        
        def validate(self, data):
            request = self.context.get('request')
            user = request.user
            if user.role != 'admin':
                data['user'] = user

            return data