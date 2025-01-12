from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    template = "superlists/lists/templates/home_page.html"

    body = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>To-Do lists</title>
</head>
<body>

</body>
</html>"""

    return HttpResponse(body)