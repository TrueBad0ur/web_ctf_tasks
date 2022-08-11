from flask import Flask, request, render_template
import subprocess

def check_fields(obj, fields):
    res = True
    for f in fields:
        res = res and (f in obj)
    return res

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dynamic_page():
    if request.method == 'POST':
        if request.form.get('action1') == 'get current time':
            out = subprocess.getoutput("date")
            return '''
            <html>
            <h1 style="color:#093657"> your time: '''+out+ '''</h1>
            </html>
            '''
        elif  request.form.get('action2') == 'get user name':
            out = subprocess.getoutput("whoami")
            return '''
            <html>
            <h1 style="color:#093657"> your name: '''+out+ '''</h1>
            </html>
            '''
        elif request.form.get('action3') == 'linux version':
            out = subprocess.getoutput("uname -a")
            return '''
            <html>
            <h1 style="color:#093657"> linux version: '''+out+ '''</h1>
            </html>
            '''
        else:
            text = request.form['text']
            text = text.lower()
            wrong_symbols = ["'", "\"", "cat", "grep", "gzip", "more", "rev", "sed", "tar"]
            for i in wrong_symbols:
                if i in text:
                    return ''' <html> <h1 style="color:#093657"> Looks like y tryna play wid me!11!</h1></html>'''
            out = subprocess.getoutput(text)
            return ''' <html> <h1 style="color:#093657">''' + out + '''</h1></html>'''

    elif request.method == 'GET' and check_fields(request.args, ['command']):
        out = subprocess.getoutput(request.args['command'])
        return '''
        <html>
        <h1 style="color:#093657"> your out: '''+out+'''</h1>
        </html>
        '''
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='31338', debug=False)
