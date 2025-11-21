from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from women.permissions import *
from women.models import *
from women.serializers import WomenSerializer
from rest_framework import generics

# Кастомный viewset, работающий с моделью Women.
# Кастомный маршрут category для роутера.
# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cat = Category.objects.get(pk=pk)
#         return Response({'cats': cat.name})
#
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if pk is None:
#             return Women.objects.all()[:3]
#         else:
#             return Women.objects.filter(pk=pk)


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)
