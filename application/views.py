from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Application
from .forms import ApplicationForm, UserPositionForm
from user.forms import EmailAuthenticationForm, Emailform

import datetime

def index(request):
    return render(request, "home.html")


def applySuccess(request):
    if((datetime.date.today())>datetime.date(2022, 3, 13)) :
        return redirect("application-impossible")
    return render(request, "application-success.html")


@login_required(login_url="/user/login/email/")  # 로그인 안된 상태라면 로그인 페이지로
def user_info(request):
    if((datetime.date.today())>datetime.date(2022, 3, 13)) :
        return redirect("application-impossible")

    user = request.user
    if request.method == "POST":
        user_form = UserPositionForm(request.POST, instance=user)

        if user_form.is_valid():
            user_form.save()

        return redirect("application")

    else:
        user_form = UserPositionForm(instance=user)
        if (
            request.user.name == "name"
            or request.user.student_id == "student_id"
            or user.major == "major"
        ):
            form = Emailform()
            return render(request, "signup_info.html", {"form": form})

    return render(request, "user_info.html", {"user_form": user_form})


@login_required
def write_application(request):
    if((datetime.date.today())>datetime.date(2022, 3, 13)) :
        return redirect("application-impossible")

    application = Application.objects.filter(user=request.user).first()

    if request.method == "POST":

        if application:  # 지원서 수정
            form = ApplicationForm(
                request.POST, request.FILES, instance=application
            )

        else:  # 지원서 첫 작성
            form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            editApplication = form.save(commit=False)
            editApplication.user = request.user
            editApplication.updated_at = timezone.now()
            editApplication.save()

       
        #일단 지금까지 작성한거 저장하고 글항목 (1-4번) 빈칸 여부 체크 
        for i in range(1,5):
            if len(str(form[f'answer{i}']))-73==0:
        #1) 빈칸 있으면 에러메시지
                error_msg = form.empty_error()
                return render(
                    request, 
                    "application.html", 
                    {
                        "form": form, 
                        "application": application, 
                        "error_msg": error_msg
                    }
                )
        #2) 빈칸 없으면 success 제출
        return redirect("application-success")

    else:
        if application:  # 지원서 수정
            form = ApplicationForm(instance=application)
        else:  # 지원서 첫 작성
            form = ApplicationForm()


    return render(
        request, "application.html", {"form": form, "application": application}
    )


def application_impossible(request):
    """
    기한 만료되면 user_info, 지원서 작성 창, 지원서 제출 성공창에 보이는
    """
    return render(
        request, "application-impossible.html"
    )