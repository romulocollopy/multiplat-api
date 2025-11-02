from django.http import JsonResponse
from django.views.generic import View
from graphene_django.views import GraphQLView
from django.middleware.csrf import get_token


class HomeView(GraphQLView): ...


class CSRFView(View):
    def get(self, request):
        return JsonResponse(dict(csrf_token=get_token(request)))
