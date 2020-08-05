from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def status(request):
    """
    This is the "lookaside" auth from nginx ingress.
    TODO: gate from internal call 
    """
    for (key, value) in request.META.items():
        print(key, ' => ', value)
    return Response()