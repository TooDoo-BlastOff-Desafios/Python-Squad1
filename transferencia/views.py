from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from transferencia.models import Transferencia
from transferencia.api import serializers

class TransferenciaAPIView(APIView):
    """
    API de transferĂȘncias do banco
    """
    def get(self, request):
        transferencia = Transferencia.objects.all()
        infos = serializers.TransferenciaSerializer(transferencia, many=True)
        return Response(infos.data)

    def post(self, request):
        infos = serializers.TransferenciaSerializer(data=request.data)
        infos.is_valid(raise_exception=True)
        infos.save()
        return Response(infos.data, status=status.HTTP_201_CREATED)