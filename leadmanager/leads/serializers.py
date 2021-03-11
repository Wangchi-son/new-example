from rest_framework import serializers
from leads.models import LeadModel

# Lead Serializer

# leads의 models.py에 LeadModels 클래스를 가져와 사용
# model = (클래스 이름)
# fields = 가져올 모델 범위


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadModel
        fields = '__all__'
