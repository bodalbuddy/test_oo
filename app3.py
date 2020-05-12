import os
from flask import Flask, request, redirect, session

app = Flask(__name__, static_folder="static")
app.env = 'development'
app.debug = True
app.secret_key = "anykey" # session 사용할 때

def get_template(filename):
    with open(f'./web/{filename}', 'r', encoding='utf8') as f:
        content = f.read()
    return content

def get_menu():
    menus = []
    for filename in os.listdir('./content'):
        menus.append(f"<li><a href='/{filename}'>{filename}</a></li>")
    return '\n'.join(menus)

@app.route('/')
def main():
    # menus = []
    # for filename in os.listdir('./content'):
    #     menus.append(f"<li><a href='/{filename}'>{filename}</a></li>")
    if 'user' in session:
        print(session['user'])
    else:
        print('not login')
        
    template = get_template('index.html')
    return template.format(menu=get_menu())

# @app.route('/<path1>/<path2>')
# def content(path1, path2):
#     return f"{path1} {path2}"
@app.route('/<title>')
def html(title):
    template = get_template('template.html')
    with open(f"./content/{title}", 'r', encoding="utf8") as f:
        content = f.read()
    return template.format(title, content, get_menu())


@app.route('/create', methods=['get', 'post'])
def create():
    if request.method == 'POST':
        print(request.form.get('title'))
        print(request.form.get('descript'))
        title = request.form.get('title')
        content = request.form.get('descript')
        with open(f'./content/{title}', 'w', encoding='utf8') as f:
            f.write(content)
        return redirect(f'{title}')   
 
    template = get_template('create.html')
    return template.format(menu=get_menu())

@app.route('/<title>/delete')
def delete(title):
    #해당 컨텐츠를 삭제하고
    os.remove(f'./content/{title}')
    #메인으로 이동
    return redirect('/')

members = [
    {'id':'junoh', 'pw':'123456','profile':'developer'},
    {'id':'son', 'pw':'1234','profile':'engineer'},
]



@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'POST':
        userid = request.form.get('id')
        pw = request.form.get('pw')
        # 로그인
        user = None
        for m in members:
            if m['id'] == userid and m['pw'] == pw: 
                # seccess login
                session['user'] = m
                print('success')        
        if 'user' not in session:
                # fail login
            print('fail')

    template = get_template('login.html')
    return template.format(menu=get_menu())
app.run(port=5001)