from leads.models import LeadModel
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset

# models.py의 LeadModel 데이터의 모든 objects를 가져와 queryset으로 정의
# permission_classes의 permissions.AllowAny를 사용하여 인증여부에 상광없이 뷰 호출 허용 (default 값)
# serializers.py에서 LeadSerializer클래스를 가져와 serializer_class로 정의


class LeadViewSet(viewsets.ModelViewSet):
    queryset = LeadModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
