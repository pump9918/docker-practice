# chatbot/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer
from .api import get_chatgpt_response

class ChatBotView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['user_message']
            response = get_chatgpt_response(user_message)
            return Response({'bot_response': response})
        return Response(serializer.errors)
