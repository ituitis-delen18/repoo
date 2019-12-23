import os

from bottle import Bottle, request

IPlist = []
x = request.headers.get
print(x)

content = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>Bottle Web App</title>
</head>
<body>
<h1>First Commit</h1>
<p>There is something that i typed.</p>
%(changable_smthg)s
</body>
</html>
"""

def home_page():
    return content % {"changable_smthg": "HERE IS SOME TEXT!"}
def ip_counter_page():
    content = ""
    for i in IPlist:
        ip_content = """
        <tr>
            <td>%(ipnumber)s</td>
        </tr>
""" % {
    "ipnumber": str(i)
    }
        content = content + ip_content
    return content


def create_app():
    app = Bottle()
    app.route("/ipp", "GET", home_page)
    app.route("/", "GET", ip_counter_page)
    return app


application = create_app()
application.run()
