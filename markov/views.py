from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic


# # Create your views here.

# def index(request):
#     template = loader.get_template('home/index.html')
#     return HttpResponse(template.render())


from django.shortcuts import render_to_response, RequestContext

def questionnaire(request):
    template = loader.get_template('markov/questionnaire.html')
    return render_to_response('markov/questionnaire.html', locals(), context_instance = RequestContext(request))

