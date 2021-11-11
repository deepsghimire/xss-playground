from flask import Flask,request
from markupsafe import escape

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def xxs_playground():
    if  request.method == "GET":
        return page_view()
    elif request.method == "POST":
        return render_unsafe(request.form["payload"],request.form["context"])


view_templ = """
        <html>
        <head>
            <title> XSS playground </title>
        </head>
        <body>
            <p> Try payload here </p>
            <form action="/" method=POST>
            <textarea name="payload" row="10" cols=60>payload</textarea>
            <br>
            <textarea name="context" row="10" cols=60>context</textarea>
            <input type=submit value=submit>
            </form>
            
        </html>
        """

result_templ = """
        <html>
        <head>
            <title> XSS playground </title>
        </head>
        <body>
            <p> Try payload here </p>
            <form action="/" method=POST>
            <textarea name="payload" row="10" cols=60>{epayload}</textarea>
            <br>
            <textarea name="context" row="10" cols=60>{econtext}</textarea>
            <input type=submit value=submit>
            </form>
            <p>Result: </p>
            <p> {eresult} </p>
            <br>
            {contexed_payload} 
        </html>
        """


def page_view():
    return view_templ


def render_unsafe(payload,context):
    return  result_templ.format(epayload=escape(payload),
                eresult=escape(context.format(payload)),
                econtext=escape(context),
                contexed_payload=context.format(payload))

