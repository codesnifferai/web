from rest_framework.views import APIView
from rest_framework.response import Response

from home.api import serializers
from rest_framework import status
from home.models import CodeSnippet, Scores
from IACode.sniffer import Sniffer
class HomeAPIVew(APIView):

    def get(selfself, request):
        codes = CodeSnippet.objects.all()
        serializer = serializers.CodeSnippetSerializer(codes, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = serializers.CodeSnippetSerializer(data=request.data)
        if serializer.is_valid():

            cs = serializer.save()
            cs.source = "api"
            cs.save()
            #Chama a IA para gerar os smells
            ia_scores = Sniffer.CodeAnalysis(request.data['code'])
            for d in ia_scores:
                scores = Scores()
                scores.name = d
                scores.code = cs
                scores.value = ia_scores[d]
                scores.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



