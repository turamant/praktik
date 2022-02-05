from rest_framework import serializers

from web_admin.models import New


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'
