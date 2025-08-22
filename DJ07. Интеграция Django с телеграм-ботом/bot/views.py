from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TelegramUser
from .serializers import TelegramUserSerializer

@api_view(['POST'])
def register_user(request):
    data = request.data
    user, created = TelegramUser.objects.get_or_create(
        user_id=data['user_id'],
        defaults={'user_name': data.get('user_name', '')}
    )
    print(created)
    serializer = TelegramUserSerializer(user)
    if created:
        return Response(serializer.data, status=201)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_info(request, user_id):
    try:
        user = TelegramUser.objects.get(user_id=user_id)
        serializer = TelegramUserSerializer(user)
        return Response(serializer.data)
    except TelegramUser.DoesNotExist:
        return Response({'message': "User not found"}, status=404)
