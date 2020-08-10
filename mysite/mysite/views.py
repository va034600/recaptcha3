from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'mysite/index.html', {})


@csrf_exempt
def post_next(request):
    import json
    import urllib.request
    import urllib.parse
    url = "https://www.google.com/recaptcha/api/siteverify"
    server_key = "TODO"
    token = request.POST.get("g-recaptcha-response")
    parameters = {
        "secret": server_key,
        "response": str(token)
    }
    data = urllib.parse.urlencode(parameters).encode("utf-8")
    response = urllib.request.urlopen(url, data=data)
    result = json.loads(response.read().decode("utf-8"))
    flag = result["success"]
    print(flag)
    return render(request, 'mysite/next.html', {"flag": flag})
