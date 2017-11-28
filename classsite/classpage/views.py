from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Announcement, File_math, File_language, File_others
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def index(request):
    news_list = News.objects.all().order_by('-time')
    paginator = Paginator(news_list, 1)

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:   
        news = paginator.page(paginator.num_pages)
    First = Announcement.objects.last()
    return render(request, 'class_home_page.html', {'news' : news, 'First' : First})

def course_view(request):
    First = Announcement.objects.last()
    return render(request, 'course.html', {'First' : First})

def Announce_view(request):
    Announce_list = Announcement.objects.all().order_by('-time')

    First = Announcement.objects.last()

    return render(request, 'Announce.html', {'announce_list' : Announce_list, 'First' : First})



def file_view(request):
    return render(request, 'File_list.html')

def file_view_math(request):
    File_list = File_math.objects.all().order_by('-time')
    return render(request, 'File.html', {'File_list' : File_list})

def file_view_language(request):
    File_list = File_language.objects.all().order_by('-time')
    return render(request, 'File.html', {'File_list' : File_list})

def file_view_others(request):
    File_list = File_others.objects.all().order_by('-time')
    return render(request, 'File.html', {'File_list' : File_list})


def uploads_file_view(request):
    return render(request, 'uploads_file.html')

def uploads_success_view(request):
    if request.POST['passkey'] == '2017414021' and request.POST['name'] and request.POST['people']:
        File = request.FILES.get('file_ppt', None)
        if File is None:
            return render(request, 'uploads_fail.html')
        else:
            with open('uploads/%s' % File.name , 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            if request.POST['project'] == '1':
                File_math.objects.create(
                    name = request.POST['name'],
                    people = request.POST['people'],
                    file_ppt = 'uploads/' + File.name
                )
            elif request.POST['project'] == '2':
                File_language.objects.create(
                    name = request.POST['name'],
                    people = request.POST['people'],
                    file_ppt = 'uploads/' + File.name
                )
            else:
                File_others.objects.create(
                    name = request.POST['name'],
                    people = request.POST['people'],
                    file_ppt = 'uploads/' + File.name
                )
            return render(request, 'uploads_success.html')
    else:
        return render(request, 'uploads_fail.html')    
    