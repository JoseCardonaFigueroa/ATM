from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth

# Create your views here.

@login_required
def hola(request):
    return render_to_response('retiro/index.html',
                                context_instance=RequestContext(request, {}))
@login_required
def retiro(request):
    return render_to_response('retiro/retiro.html',
                                context_instance=RequestContext(request, {}))
@login_required
def confirmar(request):
    return render_to_response('retiro/confirmar.html',
                                context_instance=RequestContext(request, {}))

def logout(request):
    auth.logout(request)
    return render(request, 'accounts/logout.html')
