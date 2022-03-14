from django.shortcuts import render,redirect
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    return render(request,'duf/index.html',{})

def uploadFile(request):
    if request.method == 'POST':
        _file = request.FILES.get('_file',None)
        if not _file:
            return HttpResponse('no files for upload!')
        # print(_file)
        _dir = os.path.dirname(os.getcwd())
        print('dir: ',_dir)
        _dest = open( os.path.join(_dir,_file.name),'wb+')
        for chunk in _file.chunks():
            _dest.write(chunk)
            print(_dest,'...')
        _dest.close()

    return redirect('/')
