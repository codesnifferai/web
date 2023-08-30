from rest_framework import viewsets, response

from home.api import  serializers
from home.models import CodeSnippet
from IACode.sniffer import Sniffer

class HomeViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CodeSnippetSerializer
    queryset = CodeSnippet.objects.only("id", "code",)



