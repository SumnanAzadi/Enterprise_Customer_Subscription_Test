from django.contrib import admin
from django.urls import path, include

from ecs.router import router as ecs_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(ecs_router.urls)),

]
