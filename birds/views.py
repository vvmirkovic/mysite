from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse

from birds.models import BirdPhoto
from birds.forms import BirdCaptchaForm

import logging

class BirdMain(View):
    def get(self, request):
        return render(request, 'birds/bird_main.html', {})



class BirdPhotoView(View):
    def get(self, request):
        bp = BirdPhoto.objects.all()

        ctx = {'bird_photos': bp}
        return render(request, 'birds/birdphoto_list.html', ctx)


class BirdPhotoSubmit(CreateView):
    model = BirdPhoto
    fields = '__all__'
    succes_url = reverse_lazy('birds:bird_photos')
    
    def get(self, request, **kwargs):
        form = BirdCaptchaForm()
        ctx = {'form': form}
        return render(request, 'birds/birdphoto_form.html', ctx)

    def post(self, request, **kwargs):
        form = BirdCaptchaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
            return HttpResponse(form.errors.__str__)

        return redirect(reverse_lazy('birds:bird_photos'))




class BirdPhotoDelete(CreateView):
    model = BirdPhoto
    fields = '__all__'
