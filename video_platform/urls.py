from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # لوحة تحكم Django
    path('admin/', admin.site.urls),

    # تطبيق الحسابات (login / signup / logout)
    path('accounts/', include('accounts.urls')),

    # التطبيق الرئيسي (الفيديوهات)
    path('', include('videos.urls')),
]

# عرض ملفات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
