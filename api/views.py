from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import AppUser, FinancialRecord
from .serializers import UserSerializer, FinancialRecordSerializer
from .permissions import RolePermission, IsAdminUserCustom

class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create' and not AppUser.objects.exists():
            return []
        if self.action == 'create':
            return [IsAuthenticated(), IsAdminUserCustom()]

        return [IsAuthenticated()]

class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated, RolePermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            queryset = FinancialRecord.objects.all()
        else:
            queryset = FinancialRecord.objects.filter(user=user)

        record_type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        date = self.request.query_params.get('date')

        if record_type:
            queryset = queryset.filter(type=record_type)

        if category:
            queryset = queryset.filter(category__icontains=category)

        if date:
            queryset = queryset.filter(date=date)

        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        if user.role == 'admin':
            serializer.save()
        else:
            serializer.save(user=user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_summary(request):
    user = request.user
    if user.role == 'admin':
        records = FinancialRecord.objects.all()
    else:
        records = FinancialRecord.objects.filter(user=user)

    total_income = sum(r.amount for r in records if r.type == 'income')
    total_expense = sum(r.amount for r in records if r.type == 'expense')

    return Response({
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    })