from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatLog
from .ai_utils import get_ai_rely

# Create your views here.
def chat_page(request):
    return render(request, "chatbot/chat.html")


def chat_api(request):
    user_message = request.GET.get("message", "").lower()

    if "fees" in user_message:
        reply = "School fees are N150,000 per session."
    elif "resumption" in user_message:
        reply = "School resumes on September 18."
    else:
        # AI fallback
        reply = get_ai_rely(user_message)


        ChatLog.objects.create(
            user_message=user_message,
            bot_reply = reply
        )
        
    return JsonResponse({"reply": reply})