from django.shortcuts import HttpResponse,render,redirect
from app01 import models
# Create your views here.

def yimi(request):
    #request参数保存了所有和用户浏览器相关请求的数据
    # with open("templates/yimi.html","r",encoding="utf-8") as f:
    #     data = f.read()
    # return HttpResponse(data)
    return render(request,"yimi.html")

def xiaohei(request):
    #request参数保存了所有和用户浏览器相关请求的数据
    return render(request,'word-clock.html')

def APuser(request):
    return render(request,"AP_user.html")
def LiveRoom_in(request):
    return render(request,"Liveroom_in.html")

def login(request):
    error_msg = ""
    if request.method == 'GET':  #这里必须是大写
        return render(request,'login.html')
    else:
        #如果你是POST请求，我就取出提交的数据，做登录判断
        email = request.POST.get("email",None)
        pwd = request.POST.get('pwd',None)
        print(email,pwd)

    #做是否登陆成功的判断
    if email == "598941324@qq.com" and pwd == "598941324":
        return redirect("https://www.cjzshilong.cn")
    else:
        error_msg = "邮箱或者密码错误"
    # 不是POST请求就走下面这一句
    return render(request,"login.html",{"error": error_msg})

def user_list(request):
    #去数据库中查询所有用户
    #利用ORM这个工具去查询数据库，不用自己查询
    ret = models.UserInfo.objects.all() #[UserInfo object,UserInfo object]
    # print(ret[0].id,ret[1].name)
    return render(request,"user_list.html",{"user_list":ret})
    # return HttpResponse('1234')

#添加用户的函数
def add_user(request):
    if request.method == "POST":
        #用户填写了新的用户名，并发送了POST请求过来
        new_name = request.POST.get("username",None)
        #去数据库中新建一条用户记录
        models.UserInfo.objects.create(name=new_name)
        # return HttpResponse("tianjia")
        #添加用户成功后直接跳转到user_list页面
        return redirect("/user_list/")
    #第一次请求页面时，页面上有两个框让用户添加
    return render(request,"add_user.html")