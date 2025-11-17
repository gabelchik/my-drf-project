from rest_framework.response import Response

from women.models import *
from women.serializers import WomenSerializer
from rest_framework import viewsets
from rest_framework.decorators import action


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cat = Category.objects.get(pk=pk)
        return Response({'cats': cat.name})


    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if pk is None:
            return Women.objects.all()[:3]
        else:
            return Women.objects.filter(pk=pk)