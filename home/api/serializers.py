from rest_framework import serializers
from home.models import CodeSnippet

class CodeSnippetSerializer(serializers.ModelSerializer):
    scores = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = CodeSnippet
        fields = ['id', 'code', 'scores']

