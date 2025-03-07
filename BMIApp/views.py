from django.shortcuts import render
from django.views import View

class BMIForm(View):
    def get(self,request):
        errorMessage = []
        bmi = 0
        #case 1: arrive at page for first time, no data sent
        errorMessage.append("Welcome! Enter your height and weight then click submit.")
        return render(request, "form.html", {"message": errorMessage})
        
    def post(self,request):
        errorMessage = []
        bmi = 0
        #case 1: arrive at page for first time, no data sent
        if len(request.GET)==0:
            errorMessage.append("Welcome! Enter your height and weight then click submit.")
            return render(request, "form.html", {"message": errorMessage})

        #case 2: arrive at page from form submission, check data validity
        try:
            weight = int(request.GET["weight"])
        except(ValueError):
            errorMessage.append("invalid weight: " + request.GET["weight"])
        else:
            if weight <= 0:
                errorMessage.append( "weight must be > 0; weight = " + str(weight))

        try:
            ft = int(request.GET["ft"])
        except(ValueError):
            errorMessage.append("invalid feet: " + request.GET["ft"])
        else:
            if ft <= 0:
                errorMessage.append("feet must be > 0; ft = " + str(ft))

        try:
            strInch = request.GET["in"]
            if strInch != "":
                inch = int(strInch)
            else:
                inch = 0 #leaving in blank is ok
        except(ValueError):
            errorMessage.append("invalid inches: " + request.GET["in"])
        else:
            if inch < 0:
                errorMessage.append("inches must be >= 0; in = " + str(inch))

        if len(errorMessage) == 0:
            bmi = 703*weight/((ft*12+inch)**2)
        return render(request,"form.html",{"bmi":bmi,"message":errorMessage})
        #bonus question: what should be done to this code to eliminate redundancy?



