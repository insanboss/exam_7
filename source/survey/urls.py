"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from survey_app.views import (
    IndexPolls,
    PollView,
    PollCreate,
    PollUpdate,
    PollDelete,
)

from survey_app.views.answers import (
    AddAnswer, UpdateAnswer, DeleteAnswer
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPolls.as_view(), name='index_polls'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/create/', PollCreate.as_view(), name='poll_create'),
    path('poll/<int:pk>/update/', PollUpdate.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='poll_delete'),
    path('answer/<int:pk>/add_answer/', AddAnswer.as_view(), name='add_answer'),
    path('answer/<int:pk>/update/', UpdateAnswer.as_view(), name='update_answer'),
    path('answer/<int:pk>/delete/', DeleteAnswer.as_view(), name='delete_answer'),

]
