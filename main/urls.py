from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth.decorators import user_passes_test

admin_site = user_passes_test(lambda u: u.is_superuser)(admin.site.urls)

urlpatterns = [      
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('blog/', include('blog.urls')),
    path('review/', include('review.urls')),
    path('', include('basecamp.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "NewCovenant Administration"
admin.site.site_title = "NewCovenant Administration"
admin.site.index_title = "NewCovenant admin"
admin.site.block_title = "NewCovenant Admin"


