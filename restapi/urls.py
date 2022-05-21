from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from restapi.views import USER_VIEW_SET, CATEGORY_VIEW_SET, GROUP_VIEW_SET, EXPENSES_VIEW_SET, index, logout, balance, \
    logProcessor


router = DefaultRouter()
router.register('users', USER_VIEW_SET)
router.register('categories', CATEGORY_VIEW_SET)
router.register('groups', GROUP_VIEW_SET)
router.register('expenses', EXPENSES_VIEW_SET)

urlpatterns = [
    path('', index, name='index'),
    path('auth/logout/', logout),
    path('auth/login/', views.obtain_auth_token),
    path('balances/', balance),
    path('process-logs/', logProcessor)
]

urlpatterns += router.urls
