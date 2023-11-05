from django.urls import path

from users.views import ChatView


urlpatterns = [
    path("<int:company_id>", ChatView.as_view(), name="chats"),
]
