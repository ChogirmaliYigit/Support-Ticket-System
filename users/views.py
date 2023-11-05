from django.views import View
from django.shortcuts import render

from chat.models import Chat, Message


class ChatView(View):
    template_name = 'chats.html'

    def get(self, request, company_id, *args, **kwargs):
        all_chats = {}
        chats = Chat.objects.filter(company_id=company_id, user=request.user).order_by("updated_at")
        for chat in chats:
            messages = Message.objects.filter(chat=chat, user=request.user).order_by("updated_at")
            all_chats[chat.subject] = {"last_message": messages.last(), "messages": messages}
        return render(request, self.template_name, {"chats": all_chats})
