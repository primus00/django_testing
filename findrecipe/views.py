from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Recipe
from .serializer import RecipeSerializer, RecipeDetailSerializer

from itertools import chain

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
