from django.shortcuts import render,redirect

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