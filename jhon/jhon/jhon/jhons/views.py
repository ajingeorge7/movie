from django.shortcuts import render
from.models import Movie
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import MovieForm
def index(request):
    movie=Movie.objects.all()
    context={'movie_list':movie}
    return render(request,'index.html',context)
def detail(request,movie_id):
   movie=Movie.objects.get(id=movie_id)
   return render(request,"detail.html",{'movie':movie})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        year = request.POST.get('year', '')

        if not name or not desc or not year:
            return render(request, "add.html", {'error_message': "Please fill in all the required fields."})

        try:
            img = request.FILES['img']
            movie = Movie(name=name, desc=desc, year=year, img=img)
            movie.save()

            # Now 'movie' has the ID assigned by the database
            movie_id = movie.id

            return redirect('/')
        except Exception as e:
            return redirect('/')

    return render(request, "add.html")
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')