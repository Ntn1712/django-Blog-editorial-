from django.shortcuts import render
from .models import articles,posts,delhi,mumbai,bangalore,chennai,ques
from .forms import articlesForm,delhiForm,mumbaiForm,chennaiForm,bangaloreForm,quesForm
from django.http import *

from django.urls import reverse_lazy
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    template=loader.get_template('lean/index.html')
    context={}
    return HttpResponse(template.render(context,request))

def blog_display(request):
        disp = articles.objects.all()
        context = {'disp' : disp }
        return render(request, 'lean/blog_display.html', context)
        

def article_add(request):
    if request.method == 'POST':
        form = articlesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/')
    else:
        form =  articlesForm()
        context = {'form': form }
        return render(request, 'lean/article_add.html', context)


def post_display(request):
    data = posts.objects.all()
    context = {'data': data}
    return render(request, 'lean/post_display.html', context)


def location_disp(request):
        template = loader.get_template('lean/listing.html')
        context = {}
        return HttpResponse(template.render(context,request)) 

def delhi_add(request):
      if request.method == 'POST':
        form1 = delhiForm(request.POST)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('/listing/')
      else:
        form1 =  delhiForm()
        context = {'form1': form1 }
        return render(request, 'lean/delhi_add.html', context)

def chennai_add(request):
      if request.method == 'POST':
        form2 = chennaiForm(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect('/listing/')
      else:
        form2 =  chennaiForm()
        context = {'form2': form2 }
        return render(request, 'lean/chennai_add.html', context)

def mumbai_add(request):
      if request.method == 'POST':
        form3 = mumbaiForm(request.POST)
        if form3.is_valid():
            form3.save()
            return HttpResponseRedirect('/listing/')
      else:
        form3 =  mumbaiForm()
        context = {'form3': form3 }
        return render(request, 'lean/mumbai_add.html', context)

def bangalore_add(request):
      if request.method == 'POST':
        form4 = bangaloreForm(request.POST)
        if form4.is_valid():
            form4.save()
            return HttpResponseRedirect('/listing/')
      else:
        form4 =  bangaloreForm()
        context = {'form4': form4 }
        return render(request, 'lean/bangalore_add.html', context)


def delhi_disp(request):
    disp1 = delhi.objects.all()
    context = {'disp1': disp1}
    return render(request, 'lean/listing.html', context)

def bangalore_disp(request):
    disp2 = bangalore.objects.all()
    context = {'disp2': disp2}
    return render(request, 'lean/listing.html', context)

def mumbai_disp(request):
    disp3 = mumbai.objects.all()
    context = {'disp3': disp3}
    return render(request, 'lean/listing.html', context)

def chennai_disp(request):
    disp4 = chennai.objects.all()
    context = {'disp4': disp4 }
    return render(request, 'lean/listing.html', context)


def ques_add(request):
    if request.method == 'POST':
        form5 = quesForm(request.POST)
        if form5.is_valid():
            form5.save()
            return HttpResponseRedirect('/questions/')
    else:
        form5 =  quesForm()
        context = {'form5': form5 }
        return render(request, 'lean/ques_add.html', context)
        

def ques_disp(request):
        disp5 = ques.objects.all()
        context = {'disp5' : disp5 }
        return render(request, 'lean/ques_disp.html', context)

def home_disp(request):
        template = loader.get_template('lean/home.html')
        context = {}
        return HttpResponse(template.render(context,request))
