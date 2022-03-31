from django.shortcuts import render

# Create your views here.
def bootstrap(request):
    return render(request,'bootstrap.html')

def bootstrap_cnd(request):
    return render(request,'bootstrap_cnd.html')
