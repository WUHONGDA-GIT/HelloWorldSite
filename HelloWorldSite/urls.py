"""
URL configuration for HelloWorldSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""
url 和 view内函数 的对应关系
"""

from django.contrib import admin
from django.urls import path
import app01.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url2view/',app01.views.url2view_fun),
    path('url2view2templates2html/',app01.views.url2view2templates2html_fun),
    path('url2view2templates2html_with_static)/',app01.views.url2view2templates2html_with_static_fun),
    path('url2view2templates2html_with_data)/',app01.views.url2view2templates2html_with_data_fun)
]
