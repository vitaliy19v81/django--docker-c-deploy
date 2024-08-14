from django.views import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/home.html', context={})
