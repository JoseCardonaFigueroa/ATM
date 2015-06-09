from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth
from retiro.models import Cuenta

# Create your views here.

@login_required
def hola(request):
    cuenta = Cuenta.objects.get(user=request.user)
    print cuenta.cantidad_total
    return render_to_response('retiro/index.html',
                                context_instance=RequestContext(request,
                                {'cantidad_total': cuenta.cantidad_total})
                            )
@login_required
def retiro(request):
    cuenta = Cuenta.objects.get(user=request.user)
    return render_to_response('retiro/retiro.html',
                                context_instance=RequestContext(request,
                                {'cantidad_total': cuenta.cantidad_total}))
@login_required
def confirmar(request):

    if request.POST.get ('monto', ''):
        cuenta = Cuenta.objects.get(user=request.user)
        monto = float(request.POST.get('monto', ''))
        if cuenta.cantidad_total >= monto:
            cuenta.cantidad_total = cuenta.cantidad_total - monto
            cuenta.save()

            return render_to_response('retiro/confirmar.html',
                                        context_instance=RequestContext(request,
                                        {'cantidad_total': cuenta.cantidad_total,
                                        'monto': monto
                                        }))
        else:
            return HttpResponse('No se pudo realizar el retiro \
             El monto a retirar es mayor al dinero disponible \
             Monto: %s \
             Cantidad disponible: %s' % (monto,cuenta.cantidad_total))

    else:
        return redirect('/retiro/')

def logout(request):
    auth.logout(request)
    return redirect('/')
