from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Video


def home(request):
    """
    الصفحة الرئيسية
    - عرض جميع الفيديوهات
    - متاحة للجميع (مستخدم أو زائر)
    """
    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'videos/home.html', {
        'videos': videos
    })


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
