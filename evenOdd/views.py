from django.shortcuts import render



def evenodd_checker(request):
    result = None
    if request.method == "POST":
        try:
            number = int(request.POST.get("number"))
            if number % 2 == 0:
                result = f"{number} is Even"
            else:
                result = f"{number} is Odd"
        except ValueError:
            result = "Please enter a valid integer."
    return render(request, "evenOdd/evenodd.html", {"result": result})
