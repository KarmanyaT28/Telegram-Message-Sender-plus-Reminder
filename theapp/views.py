from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm, EditForm 
from django.urls import reverse_lazy
import requests

# def home(request):
#     return render(request,'home.html', {})

class HomeView(ListView):
    model = Post
    template_name='first.html'


class PostView(DetailView):
    model = Post
    template_name = 'details.html'
    # success_url = reverse_lazy('home')


class ManagePostView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_time']




def sendmess(request):
    return render(request,'message.html')



def postmess(request):
    if request.method == "POST":
        fiel = request.POST['n2']
        p = request.FILES['image']
        from .models import User
        c=User(image = p)
        c.save()
        
    files= {'photo':open('C:/Users/Karmanya/Pictures/Camera Roll/beautiful_natural_scenery_04_hd_pictures_166229.jpg','rb')}
    
    resp = requests.post('https://api.telegram.org/bot1409753121:AAFpkrG3Ty_PK3lfdPhe1Druktimrz2uHyU/sendPhoto?chat_id=-325846964',files=files)
    print(resp.status_code)
    fields12 = fiel
    base_url = 'https://api.telegram.org/bot1519165001:AAEb-g0ioCNOpDvTBNDaevDyEc3hc5f2Wkc/sendMessage?chat_id=-325846964&text="{}"'.format(fields12)
    a = requests.get(base_url)
    return render(request,'details.html',{'a':a,'getvalue':files})

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    # fields = '_all_'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'
    # fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
