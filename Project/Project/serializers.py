from rest_framework import serializers
from .models import Fact


# Converts Fact model data to JSON (for APIs) and validates input
class CatFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact  # Links to the Fact model
        fields = '__all__'  # Includes all model fields in the API
