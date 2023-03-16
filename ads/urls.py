from django.urls import path
from .views import AdList, AdDetail, AdCreate, AdUpdate, AdDelete, ResponseList, ResponseDetail, ResponseCreate, ResponseDelete

urlpatterns = [
    path('', AdList.as_view(), name='ad_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad_detail'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/edit/', AdUpdate.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
    path('response/', ResponseList.as_view(), name='response_list'),
    path('response/<int:pk>', ResponseDetail.as_view(), name='response_detail'),
    path('response/create/', ResponseCreate.as_view(), name='response_create'),
    path('response/<int:pk>/delete/', ResponseDelete.as_view(), name='response_delete')
]

