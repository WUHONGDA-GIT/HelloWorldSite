from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
"""
url 和 view内函数 的对应关系
render函数: templates模板库, 查找模板;
"""

def url2view_fun(request):
    return HttpResponse("url2view_helloworld")

def url2view2templates2html_fun(request):
    return render(request,"blank.html")

def url2view2templates2html_with_static_fun(request):
    return render(request,"with_static_file.html")


def url2view2templates2html_with_data_fun(request):
    name = "xiaomiing"
    roles = ["学生","班长"]
    return render(request, "with_data.html",{"var1":name,"var2":roles})