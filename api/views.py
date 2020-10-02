from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from news.models import Content
from .serializers import ContentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ContentListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ContentDetailView(RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

