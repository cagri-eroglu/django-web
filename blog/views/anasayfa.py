from django.shortcuts import render
from django.http import HttpResponse
def anasayfa(request):
    context={
        'isim':'Cagri Eroglu'
    }

    return render(request, 'pages/anasayfa.html',context=context)