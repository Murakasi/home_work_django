from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def review_list(request):
    review = ['Book1', 'Book2', 'Book3', 'Book4']
    return Response(review)