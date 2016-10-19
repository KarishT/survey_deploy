from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "survey/index.html")




def show(request):
    if 'count' not in request.session:
        request.session['count']=1
    else:
        request.session['count']+=1;

    if request.method == "POST":
        request.session['name']= request.POST['name']
        request.session['loc']= request.POST['selection']
        request.session['lang']= request.POST['selection1']
        request.session['comment']= request.POST['comment']
    return redirect('/page')

def page(request):
    return render(request, "survey/result.html")
