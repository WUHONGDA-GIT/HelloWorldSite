#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"项目入口"
"""
python .\manage.py startapp app01
python manage.py runserver ：启动开发服务器，默认在 127.0.0.1:8000 运行。
python manage.py startapp <app_name> ：创建一个新的应用。
python manage.py makemigrations ：根据模型的更改生成迁移文件。注意: app要注册到django才会纳入处理范围
python manage.py migrate ：应用迁移文件，将模型的更改同步到数据库。注意: app要注册到django才会纳入处理范围

python manage.py createsuperuser ：创建超级管理员用户。
python manage.py shell ：打开 Django 的交互式 Python shell。
python manage.py collectstatic ：收集所有的静态文件到指定的目录。
python manage.py test ：运行测试用例。
"""
import os
import sys
import django


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HelloWorldSite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
