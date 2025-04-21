import random
from django.shortcuts import render
from .models import Fact
from .serializers import CatFactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# API view to list all facts or create new ones
@api_view(['GET', 'POST'])
def cat_fact_list(request):
    if request.method == 'GET':
        facts = Fact.objects.all()  # Get all facts from DB
        serializer = CatFactSerializer(facts, many=True)  # Convert to JSON
        return Response(serializer.data)  # Return JSON response

    if request.method == 'POST':
        serializer = CatFactSerializer(data=request.data)  # Convert JSON to model
        if serializer.is_valid():  # Validate data
            serializer.save()  # Save to DB
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created


# API view to get/update/delete single fact
@api_view(['GET', 'PUT', 'DELETE'])
def fact_detail(request, id):
    try:
        fact = Fact.objects.get(pk=id)  # Try to find fact by ID
    except Fact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found

    if request.method == 'GET':
        serializer = CatFactSerializer(fact)  # Convert single fact to JSON
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CatFactSerializer(fact, data=request.data)  # Update fact
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

    elif request.method == 'DELETE':
        fact.delete()  # Delete fact
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return success


# Regular Django view to show random fact on webpage
def home(request):
    all_facts = Fact.objects.all()  # Get all facts
    fact_descriptions = [fact.description for fact in all_facts]  # Extract facts (descriptions)
    random_fact = random.choice(fact_descriptions) if fact_descriptions else "No facts available"
    return render(request, 'Project/fact.html', {'fact': random_fact})  # Render HTML template
