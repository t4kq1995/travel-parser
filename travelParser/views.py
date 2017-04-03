from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.http import JsonResponse


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def parse(request):
    return JsonResponse({'status': 'test'})
