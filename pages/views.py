from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/homepage.html"



def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'pages/homepage.html')
    return render(request, 'pages/testpage.html')