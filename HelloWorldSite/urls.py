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
    # 基础关系
    path('url2view/',app01.views.url2view_fun),
    path('url2view2templates2html_with_blank/',app01.views.url2view2templates2html_with_blank),
    path('url2view2templates2html_with_static/', app01.views.url2view2templates2html_with_static),
    path('url2view2templates2html_with_var/', app01.views.url2view2templates2html_with_var),
    path('get_repones_content_from_ex_web/', app01.views.get_repones_content_from_ex_web),
    # HTTPS玩法
    path('http_api_case_show/', app01.views.http_api_case_show),
    path('html_create_and_handle_post_request/', app01.views.html_create_and_handle_post_request),
    path('html_create_post_request/', app01.views.html_create_post_request),
    path('html_handle_post_request/', app01.views.html_handle_post_request)
]
