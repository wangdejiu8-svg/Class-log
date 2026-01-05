import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


def json_response(success, message, data=None, status=200):
    return JsonResponse({
        'success': success,
        'message': message,
        'data': data
    }, status=status)


@csrf_exempt
def login_view(request):
    if request.method != 'POST':
        return json_response(False, '仅支持POST请求', status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return json_response(False, '请求体需要是JSON', status=400)

    username = data.get('username', '').strip()
    password = data.get('password', '')

    if not username or not password:
        return json_response(False, '缺少用户名或密码', status=400)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return json_response(False, '用户名或密码错误', status=401)

    login(request, user)
    return json_response(True, '登录成功', {
        'username': user.username,
        'name': user.name,
        'user_type': user.user_type
    })


@csrf_exempt
def register_view(request):
    if request.method != 'POST':
        return json_response(False, '仅支持POST请求', status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return json_response(False, '请求体需要是JSON', status=400)

    username = data.get('username', '').strip()
    password = data.get('password', '')
    name = data.get('name', '').strip()

    if not username or not password or not name:
        return json_response(False, '缺少必填字段', status=400)

    if len(username) < 3:
        return json_response(False, '用户名至少3个字符', status=400)

    if len(password) < 6:
        return json_response(False, '密码至少6个字符', status=400)

    if User.objects.filter(username=username).exists():
        return json_response(False, '用户名已存在', status=400)

    user = User.objects.create_user(
        username=username,
        password=password,
        name=name,
        user_type='student'
    )

    return json_response(True, '注册成功', {
        'username': user.username,
        'name': user.name
    })
