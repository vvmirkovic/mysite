from django.shortcuts import render
from django.views import View

class MainView(View):
    template_name = 'home/main.html'
    def get(self, request):
        return render(request, self.template_name, {})

