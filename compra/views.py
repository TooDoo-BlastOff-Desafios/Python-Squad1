from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from compra.models import Compra
from compra.api import serializers

class CompraAPIView(APIView):
    """
    API de compras 
    """
    def get(self, request):
        compra = Compra.objects.all()
        infos = serializers.CompraSerializer(compra, many=True)
        return Response(infos.data)

    def post(self, request):
        infos = serializers.CompraSerializer(data=request.data)
        infos.is_valid(raise_exception=True)
        infos.save()
        return Response(infos.data, status=status.HTTP_201_CREATED)