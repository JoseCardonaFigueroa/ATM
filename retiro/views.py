from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.
@login_required
def hola(request):

    return render_to_response('retiro/index.html',
                                context_instance=RequestContext(request, {}))
