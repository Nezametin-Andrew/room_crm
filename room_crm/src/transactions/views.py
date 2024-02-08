from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import View


class MainView(View):

    def get(self, request):
        return HttpResponse(loader.get_template('operations.html').render(request=request, context={}))
