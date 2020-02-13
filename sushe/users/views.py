from django.shortcuts import render, redirect
from .form import RegisterForm, PerfectForm
from .models import UserInfo, School, Floor, Building, RoomNum


def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                # 注册成功，跳转回首页
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})

def index(request):
    is_perfect = 0
    try:
        if request.user.is_authenticated:
            is_perfect = UserInfo.objects.get(username = request.user.id).is_perfect
    except:
        print()
    return render(request, 'index.html', {'is_perfect': is_perfect})

def perfectInfo(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 用这些数据实例化一个用户注册表单
        form = PerfectForm(request.POST)
        # form.is_perfect = 1
        # form.username = request.user.id
        # print(form)
        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                # 成功，跳转回首页
                return redirect('/')
        else:
            print('hellolllll')
    else:
        form = PerfectForm()

    return render(request, 'users/perfectInfo.html', context={'form': form, 'next': redirect_to})


    return render(request, 'users/perfectInfo.html')


def seeInfo(request):
    perfectInfo = {}
    info = UserInfo.objects.get(username = request.user.id)
    perfectInfo['phone'] = info.phone
    perfectInfo['gonghao'] = info.gonghao
    perfectInfo['school'] = School.objects.get(school = info.school)
    if info.unit:
        perfectInfo['sushe'] = '分配在{}栋{}楼{}号房间'.format(Building.objects.get(unit=info.unit),Floor.objects.get(floor=info.floor), RoomNum.objects.get(room=info.room))
    else:
        perfectInfo['sushe'] = '暂时没有分配宿舍'
    return render(request, 'users/seeInfo.html', context={"perfectInfo": perfectInfo})
