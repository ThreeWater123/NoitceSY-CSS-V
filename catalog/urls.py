from django.urls import path
from . import views
app_name='catalog'

urlpatterns = [
    path('',views.group_list.as_view(),name='group' ),
    path('<slug:slug>',views.group_detail.as_view(),name="group_detail"),
    path('<slug:slug>/update/',views.group_notice_update.as_view(),name="update"),
    path('<slug:slug>/get',views.get_notice.as_view(),name='get'),
    path('create/',views.group_create.as_view(),name='create'),
    path('<slug:slug>/delete/',views.group_delete.as_view(),name='delete'),
    
]
