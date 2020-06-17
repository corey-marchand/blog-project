from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


#1 create the view
#2 add a url
#3 create a html page