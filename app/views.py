from django.shortcuts import render,redirect
from .models import blog
from .forms import blogform

# Create your views here.

def Home(request):
    return render(request,'app/home.html')

def Post(request):
    if request.method=='POST':
        form=blogform(request.POST or None,request.FILES or None)    
        if form.is_valid():
            form.save()
            return redirect(Read)

    else:
        form=blogform(request.FILES)
    return render(request,'app/post.html',{'form':form})  

def Read(request):
    read=blog.objects.all()
    return render(request,'app/read.html',{'read':read})


def Update(request,id):
   upd=blog.objects.get(id=id)
   update=blogform(request.POST or None,request.FILES or None,instance=upd)
   if update.is_valid():
       update.save()
       return redirect(Read)
   return render(request,'app.update.html',{'update':update})


def Delete(request,id):
    del_t=blog.objects.get(id=id)
    del_t.Delete()
    return redirect(Read)


