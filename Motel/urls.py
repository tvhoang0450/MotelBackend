from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import PhongTroListCreateAPIView
# from .views import ModelByMakerList, PhongTroList

app_name = 'Motel'

router = routers.DefaultRouter()
router.register(r'posts', views.PhongTroListCreateAPIView, basename="Posts")
router.register(r'posts', views.PhongTroUpdateDeleteAPIView, basename="Posts")
# user có quyền thêm, xóa, sửa bài đăng tin  => method: POST bài đăng
# user có thể sửa thông tin của mình => POST information
# những hoạt động k cần xác thực user => method: GET bài đăng (tất cả nhà trọ, nhà trọ có chọn lọc)
urlpatterns = [
    path('api/', include(router.urls)),
    # url('^api(?P<DichVu__TenDV>.+)/$', PhongTroList.as_view()),
    # url('^model/by(?P<DichVu>\w+)/$', ModelByMakerList.as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]