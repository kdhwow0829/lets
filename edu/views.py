from django.shortcuts import render, get_object_or_404
from django.views.generic import view

# Create your views here.
class Index(view):
    temlate_name = 'index.html'

    def get(self, request):
        return render(request, self.temlate_name)