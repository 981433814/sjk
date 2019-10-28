from django.contrib.auth import get_permission_codename
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.http import HttpResponse, response
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import get_object_or_404

from .form import HrForm
from .models import Hr, Detail, Applicant, Record
from django.utils import timezone
from django.views.generic import ListView


# Create your views here.
class HrListView(ListView):
    model = Hr

    def head(self, request, *args, **kwargs):
        return response


def index(request):
    detail_list = Detail.objects.all().filter(statue=0)
    detail_count = Detail.objects.all().filter(statue=0).count()
    print(detail_count)
    paginator = Paginator(detail_list, 6)
    page = request.GET.get('page')
    details = paginator.get_page(page)
    context = {
        'detail': details,
        'count': detail_count,
    }
    return render(request, 'index.html', context)


def index1(request):
    user_id = request.session.get("member_id")
    user_info = Applicant.objects.all().filter(id=user_id)
    detail_list = Detail.objects.all().filter(statue=0)
    detail_count = Detail.objects.all().filter(statue=0).count()
    print(detail_count)
    paginator = Paginator(detail_list, 6)
    page = request.GET.get('page')
    details = paginator.get_page(page)
    context = {
        'detail': details,
        'count': detail_count,
        'user_info': user_info,
    }
    return render(request, 'index1.html', context)


def login(request):
    time_now = timezone.now()
    if request.method == 'POST':
        role = request.POST.get('role')
        print("角色" + role)
        name = request.POST.get('name')
        password = request.POST.get('password')
        if role == "option1":
            a = Applicant.objects.all().filter(a_account=name, password=password)
            if a:
                request.session['member_id'] = a[0].id
                print(request.session.get('member_id'))
                return redirect('index1')
            else:
                error = "密码错误"
            return render(request, 'login.html', {'error': error})
        else:
            a = Hr.objects.all().filter(username=name, password=password)
            if a:
                request.session['hr_id'] = a[0].id
                print(request.session.get('hr_id'))
                return redirect('useradmin')
            else:
                error = "密码错误"
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html', locals())


def hlogin(request):
    time_now = timezone.now()
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        a = Hr.objects.all().filter(username=name, password=password)
        if a:
            request.session['hr_id'] = a[0].id
            print(request.session.get('hr_id'))
            return redirect('useradmin')
        else:
            error = "密码错误"
        return render(request, 'hlogin.html', {'error': error})

    return render(request, 'hlogin.html', locals())


def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return redirect('./')


def logout_hr(request):
    try:
        del request.session['hr_id']
    except KeyError:
        pass
    return redirect('./')


def register(request):
    hr = Hr.objects.all()
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        Hr.objects.create(name=name, password=password)
        h = Hr.objects.all()
        return redirect('./login')
    else:
        return render(request, 'register.html', locals())


def forms(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        hrs = Hr.objects.all()
    return render(request, 'test.html', locals())


def detail(request, post):
    detail = Detail.objects.all().filter(id=post)
    baseurl = request.build_absolute_uri()
    request.session['url'] = baseurl
    print("路径" + baseurl)
    return render(request, 'detail.html', {'detail': detail})


def send(request):
    s = request.POST.get("data")
    query_str = request.GET.get('_list_filter')
    print(s)
    if s == "1":
        print(s)
    else:
        print("空")
    a = request.session.get('member_id')

    url = request.session.get('url')
    u = url[-2]
    print("获取" + u)
    hr_info = Detail.objects.get(id=u)
    obj = hr_info.hr

    # for b in b:
    #     b_id = b.id
    #     print("b的值"+b_id)
    if a:
        user = Applicant.objects.get(id=a)
        c = 0

        b = Record.objects.all().filter(applicant=user, detail=hr_info)
        if not b:
            c = 1
            ap = Applicant.objects.get(id=a)
            hr = Hr.objects.get(id=obj.id)
            de = Detail.objects.get(id=u)
            Record.objects.create(applicant=ap, hr=hr, detail=de)
            request.session['statue_info'] = c
        return redirect('index1')
    else:
        error = "请先登录"
        c = 0
        request.session['statue_info'] = c
        return redirect('./')

    return render(request, 'index.html')


def has_saler_permission(self, obj=None):
    codename = get_permission_codename('saler', self.opts)
    print(codename)
    return ('saler' in self.remove_permissions) and self.user.has_perm('%s.%s' % (self.app_label, codename))


def hradmin(request):
    h = request.session.get('hr_id')
    h_info = Hr.objects.get(id=h)
    hinfo = Hr.objects.all().filter(id=h)
    detail_list = Detail.objects.all().filter(hr=h_info).order_by(Lower('pub_date').desc())
    record = Record.objects.all().filter(hr=h_info)
    print(record)
    applicant = Applicant.objects.all()
    print(applicant)
    paginator = Paginator(detail_list, 3)
    page = request.GET.get('page')
    details = paginator.get_page(page)
    # if request.method == 'GET':
    #     record.statue(statue=5)
    context = {
        'applicant': applicant,
        'record': record,
        'hinfo': hinfo,
        'detail_list': detail_list,
        'detail': details,
    }
    return render(request, 'useradmin.html', context)


def apadmin(request):
    a = request.session.get('member_id')
    ap1 = Applicant.objects.all().filter(id=a)
    ap = Applicant.objects.get(id=a)
    record = Record.objects.all().filter(applicant=ap)
    context = {
        'ap': ap1,
        'record': record,
    }
    return render(request, 'apadmin.html', context)
