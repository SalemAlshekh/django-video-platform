from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

urlpatterns = [

    # لوحة تحكم Django
    path('admin/', admin.site.urls),

    # تطبيق الحسابات (login / signup / logout)
    path('accounts/', include('accounts.urls')),

    # التطبيق الرئيسي (الفيديوهات)
    path('', include('videos.urls')),
]
def maintenance_view(request):
    return render(request, 'maintenance.html')

if settings.MAINTENANCE_MODE:
    urlpatterns = [
        path('', maintenance_view),
    ]

# عرض ملفات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
