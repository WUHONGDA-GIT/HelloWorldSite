from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import requests
import json
# Create your views here.
"""
url 和 view内函数 的对应关系
render函数: templates模板库, 查找模板;
"""

def url2view_fun(request):
    return HttpResponse("url2view_helloworld")

def url2view2templates2html_with_blank(request):
    return render(request, "app01/blank.html")

def url2view2templates2html_with_static(request):
    return render(request, "app01/with_static_file.html")


def url2view2templates2html_with_var(request):
    name = "xiaomiing"
    roles = ["学生","班长"]
    return render(request, "app01/with_data.html", {"var1":name, "var2":roles})

def get_repones_content_from_ex_web(req):
    res = requests.get("https://jsonplaceholder.typicode.com/")
    print("响应状态码:", res.status_code)
    print("响应头:", res.headers)
    print("响应内容类型:", res.headers['Content-Type'])
    return HttpResponse(f"响应头: {res.headers}")

def http_api_case_show(request):
    # 获取请求方法
    if request.method == 'GET':
        # 获取查询参数
        param1 = request.GET.get('param1', '')
        return HttpResponse(f'这是一个 GET 请求，获取的参数 param1 的值为: {param1}')

    elif request.method == 'POST':
        # 获取表单数据或 JSON 数据
        data = request.POST.get('data', '')  # 表单数据
        # 或
        import json
        try:
            json_data = json.loads(request.body)  # JSON 数据
        except json.JSONDecodeError:
            json_data = {}
        return HttpResponse(f'这是一个 POST 请求，获取的数据为: {data} 或 {json_data}')

    elif request.method == 'PUT':
        # 处理 PUT 请求的数据
        put_data = request.body  # PUT 请求的数据通常在请求体中
        return HttpResponse(f'这是一个 PUT 请求，获取的数据为: {put_data}')

    # 重定向
    elif request.method == 'DELETE':
        # 重定向到其他页面
        return redirect('/another_page/')

    # 返回 JSON 数据
    else:
        data = {'message': '这是一个默认的响应'}
        return JsonResponse(data)


def html_create_and_handle_post_request(request):
    if request.method == 'GET':
        return render(request, "app01/html_create_and_handle_post_request.html")
    elif request.method == 'POST':
        # 获取表单数据或 JSON 数据
        name = request.POST.get('name', '')  # 表单数据
        return HttpResponse(f'这是一个 POST 请求，获取的数据为: {name}')

def html_create_post_request(request):
    return render(request, "app01/html_create_post_request.html")

def html_handle_post_request(request):
    if request.method == 'POST':
        # 获取表单数据或 JSON 数据
        name = request.POST.get('name', '')  # 表单数据
        return HttpResponse(f'这是一个 POST 请求，获取的数据为: {name}')
    elif request.method == 'GET':
        return HttpResponseRedirect("http://127.0.0.1:8000/html_create_post_request/")