from  django.urls import path
from .views import ContentListView, ContentDetailView

urlpatterns = [
  path('',ContentListView.as_view()),
  path('<pk>/',ContentDetailView.as_view()),
]