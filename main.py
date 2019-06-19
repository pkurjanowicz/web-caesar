from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="rot">Rotate by:
            <input type="text" name="rot" value="{rot}"><br>
            <textarea name="text" rows="10" cols="30">{string}</textarea><br>
            <input type="submit" value="Submit Query">
        </form>
    </body>
</html>'''


@app.route("/")
def index():
    return form.format(rot='0', string='')

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    string = rotate_string(text,rot)
    return form.format(rot='0', string=string)

app.run()