from django.db import models
from news.models import Content
from .serializers import ContentSerializer
from djangochannelsrestframework import permissions
from djangochannelsrestframework.observer.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (ListModelMixin, RetrieveModelMixin,)
from djangochannelsrestframework.observer import model_observer


class ContentListConsumer(ListModelMixin,GenericAsyncAPIConsumer):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # Subscribing
    @model_observer(Content)
    async def model_activity(self, message, observer=None, **kwargs):
        # send activity to your frontend
        await self.send_json(message)


class ContentDetailConsumer(RetrieveModelMixin,GenericAsyncAPIConsumer):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # Subscribing
    @model_observer(Content)
    async def model_activity(self, message, observer=None, **kwargs):
        # send activity to your frontend
        await self.send_json(message)








