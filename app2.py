from flask import Flask
app = Flask(__name__, static_folder="static")
app.env = 'development'
app.debug = True

# def get_template():
#     with open('./web/template.html', 'r', encoding='utf8') as f:
def get_template(filename):
    with open(f'./web/{filename}', 'r', encoding='utf8') as f:
        content = f.read()
    return content

@app.route('/')
def main():
    # f = open('./web/index.html', 'r', encoding='utf8')
    # content = f.read()
    # f.close()
    # return content
    template = get_template('index.html')
    return template

# @app.route('/<path>')
# def content(path1, path2):
#     return f"{path1}{path2}"

@app.route('/html')
def html():
    # temlate = get_template()
    # return temlate.format('HTML', "HTML is ...")
    # title = 'html'
    template = get_template('template.html')
    with open(f"./content/{title}", 'r', encoding='utf8') as f:
        content = f.read()
    return template.format(title, content)

@app.route('/css')
def css():
    # temlate = get_template()
    # return temlate.format('CSS', "CSS is ...")
    template = get_template('template.html')
    return template.format('CSS', "CSS is ...")

@app.route('/js')
def js():
    # temlate = get_template()
    # return temlate.format('CSS', "CSS is ...")
    template = get_template('template.html')
    return template.format('js', "js is ...")

@app.route('/python')
def python():
    # temlate = get_template()
    # return temlate.format('CSS', "CSS is ...")
    template = get_template('template.html')
    return template.format('python', "python is ...")   
app.run(port=5002) 