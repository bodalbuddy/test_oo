from flask import Flask

app = Flask(__name__)
app.env = 'development'
app.dubug = True



@app.route('/')
def main():
    f = open('./WEB/index.html', 'r', encoding='utf8')
    content = f.read()
    f.close()
    return content

@app.route('/html')
def html():
    # f = open('.web/1.html', 'r', encoding='utf8')
    # content = f.read()
    # f.close()
    with open('./WEB/template.html', 'r', encoding='utf8') as f:
        content = f.read()
    return content.format('HTML', "HTML is..")

@app.route('/css')
def css():
    with open('./WEB/template.html', 'r', encoding='utf8') as f:
        content = f.read()
    return content.format('CSS', "CSS is..")

app.run(port=5001)