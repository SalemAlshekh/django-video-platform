from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Video


@login_required
def home(request):
    return render(request, 'videos/home.html')


@staff_member_required
def upload_video(request):
    """
    صفحة رفع الفيديو
    - متاحة للمدير فقط
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        video_file = request.FILES.get('video')

        if title and video_file:
            Video.objects.create(
                title=title,
                video=video_file
            )
            return redirect('home')

    return render(request, 'videos/upload.html')
