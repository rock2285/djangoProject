from django.shortcuts import render, redirect
from django.views import View

class Test(View):
    def get(self,request):
        print("test")
        return render(request, "form.html", {})
    def post(self,request):
        if request.POST.get("password","")=="stop":
            return redirect("/stop")
        return render(request, "form.html", {"message": request.POST.get("password", "<error>")})

class Stop(View):
    def get(self, request):
        return render(request, "stop.html", {})