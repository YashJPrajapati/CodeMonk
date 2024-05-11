from rest_framework import serializers
from .models import Paragraph

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'
