from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.parsers import JSONParser
from .models import Recipe, Ingredient
from .serializer import RecipeSerializer, RecipeDetailSerializer
from rest_framework_swagger.views import get_swagger_view

from itertools import chain

schema_view = get_swagger_view(title='Pastebin API')

@api_view(['GET', 'POST'])
def search(request):
    if request.method == 'POST':
        search_for = request.data['search_text']
        if search_for is not None and search_for != "":
            result_ = Recipe.objects.filter(name__contains=search_for)
            result2_ = Recipe.objects.filter(ingredient__name__startswith = search_for)
            result_list = list(chain(result_, result2_))
            list2 = list(set(result_list))
            result = RecipeSerializer(list2, many=True)
            return JsonResponse(result.data, safe=False)
        else:
            final_search_result = []
            return JsonResponse(final_search_result)

@api_view(['GET', 'POST'])
def get(request):
    if request.method == 'POST':
        search_for = request.data['search_text']
        if search_for is not None and search_for != "":
            result_ = Recipe.objects.filter(name=search_for)
            result = RecipeDetailSerializer(result_, many=True)
            return JsonResponse(result.data, safe=False)
        else:
            final_search_result = []
            return JsonResponse(final_search_result)
