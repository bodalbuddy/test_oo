import os
from flask import Flask, request

app = Flask(__name__, static_folder="static2")
app.env = 'development'
app.debug = True

def get_template(filename):
    with open(f'./{filename}', 'r', encoding='utf8') as f:
        content = f.read()
    return content

def get_menu():
    menus = []
    for filename in os.listdir('./content'):
        menus.append(f"<li><a href='/{filename}'>{filename}</a></li>")
    return '\n'.join(menus)

@app.route('/')
def main():   
    template = get_template('index copy.html')
    return template.format(menu=get_menu())

@app.route('/<title>')
def html(title):
    template = get_template('template copy.html')
    with open(f"./{title}", 'r', encoding="utf8") as f:
        content = f.read()
    return template.format(title, content, get_menu())

# 사용자로부터 2 ~ 9 사이의 숫자를 입력 받은 후, 해당 숫자에 대한 구구단을 출력하세요.
# /gugu/<number>
@app.route('/gugu/<number>')
def gugu(number): 
    if not number.isnumeric(): 
        return "not number"

# 빈 리스트를 선언(dan)
    num = int(number)
    if num in range(1,10):
        dan = []
    # range 9 범위 내에서 for문 반복
        i = 1
        while i < 10:
            result = num * i
            dan.append(str(result))
            i = i+1
    # append (number * i)
        return '<br>'.join(dan)
    else: 
        return "not in range"

# <a href="/prime?num=15">15까지소수</a>
# <form action="/prime" method="get">
#     <input type='text' name='num'>
#     <input type='submit'>
# </form>

# 사용자로부터 숫자를 N을 입력받은 후 1부터 N까지의 숫자 중 소수만 출력하세요.
# /prime?num=N
@app.route('/prime')
def prime(): 
    # 빈 리스트 선언
    print(request.args.get('num'))
    n = int(request.args.get('num'))
    sosu = []
    #숫자 N까지 for문을 돌려서
   
        # 2~(N-1) 나머지가 0이 되는 경우, 소수아님
        # 위 사항 외에는 소수임
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i % j == 0:
                break
        if i == j: 
            sosu.append(i)
        
    return str(sosu)
    

# 사용자로부터 숫자를 N을 입력받아. N의 약수를 모두 출력하세요. 
# /common_factor?num=N

@app.route('/common_factor')
def yaksu(): 
    # 빈 리스트 선언
    print(request.args.get('num'))
    n = int(request.args.get('num'))
    yaksu = []
    #숫자 N까지 for문을 돌려서
    
    for j in range(1, n+1):
        if n % j == 0:
            if j not in yaksu:
                yaksu.append(j)

    return str(yaksu)
    





# 사용자로부터 숫자를 N, M을 입력받아 N과 M의 최대공약수와 최소공배수를 출력하세요. 
# /commons?num1=N&num2=M
@app.route('/commons')
def commons(): 
    # 빈 리스트 선언
    
    n1 = int(request.args.get('num1'))
    n2 = int(request.args.get('num2'))

    print(n1, n2)

    Max_yaksu = []
    Min_baesu = []

    for j in range(1, max(n1, n2)):
        if (n1 % j == 0) & (n2 % j == 0) :
            if j not in Max_yaksu:
                Max_yaksu.append(j)
                Max_yaksu.sort()

    for j in range(1, n1 * n2):
        if (j % n1 == 0) & (j % n2 == 0) :
            if j not in Min_baesu:
                Min_baesu.append(j)
                Min_baesu.sort()

    test = []
    test.append(Min_baesu[0])
    test.append(Max_yaksu[-1])

    return str(test)


# 사용자로부터 숫자를 N을 입력받아, 1, 5, 10, 25, 50의 숫자를 이용하여 최소 갯수로 N을 표현해보자 
# 예) 183 = 50 * 3 + 25 * 1 + 5 * 1 + 1 * 3 => 총 8개
# /coins?num=N
@app.route('/coins')
def coins(): 
    with open('./test_coin.html', 'r', encoding='utf8') as f:
        template = f.read()
    result = ''   
    n1 = int(request.args.get('num'))
    n = n1
    print(n)
    coins = []
    mok = []

    div_list =[ 50, 25, 10, 5, 1 ]

    for i in div_list:
        c = n//i
        mok.append(f'{i} * {c}')
        n%=i  

    # c50 = n//50
    # n%=50
    # coins.append(f'50 * {c50}')
    # c25 = n//25
    # n%=25
    # coins.append(f'25 * {c25}')
    # c10 = n//10
    # n%=10
    # coins.append(f'10 * {c10}')
    # c5 = n//5
    # n%=5
    # coins.append(f'5 * {c5}')
    # coins.append(f'1 * {n}')

    result = f'{n1} = ' + ' + '.join(mok)

    return template.format(result=result)



# 주민등록번호를 입력받아 올바른 주민번호인지 검증하라.
# 주민번호 : ① ② ③ ④ ⑤ ⑥ - ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬
# 합계 
# = 마지막수를 제외한 12자리의 숫자에 2,3,4,5,6,7,8,9,2,3,4,5 를 순서대로 곱산수의 합
# = ①×2 + ②×3 + ③×4 + ④×5 + ⑤×6 + ⑥×7 + ⑦×8 + ⑧×9 + ⑨×2 + ⑩×3 + ⑪×4 + ⑫×5
# 나머지 = 합계를 11로 나눈 나머지
# 검증코드 = 11 - 나머지
# 여기서 검증코드가 ⑬자리에 들어 갑니다.
#
# /jumin 
# with form post
@app.route('/jumin', methods=['get', 'post'])
def jumin(): 
    with open('./jumin.html', 'r', encoding='utf8') as f:
        template = f.read()
    a = ''
    answer = ''

    if request.method == 'POST':
        a = request.form.get('text')
        sum1 = int(a[0]) * 2 + int(a[1]) * 3 + int(a[2]) * 4 + int(a[3]) * 5 + int(a[4]) * 6 + int(a[5]) * 7 + int(a[6]) * 8 + int(a[7]) * 9 + int(a[8]) * 2 + int(a[9]) * 3 + int(a[10]) * 4 + int(a[11]) * 5
        mod = sum1 % 11
        verify_code = 11 - mod
        
        if verify_code > 9:
            verify_code = verify_code - 10
        else:
            pass

        if verify_code == int(a[12]):
            answer = "맞는 주민등록번호입니다!!!!"
        else:
            answer = "틀린 주민등록번호입니다ㅠㅠㅠ"
   
    return template.format(a=a, b=answer)

# 원의 원주율을 구해보자
# /pi

@app.route('/pi')
def pi():
    n = 10000000
    s = 0
    for i in range(n):
        s = s + (1/n)*((1-(i/n)**2)**0.5)

    return str(s*4)

app.run(port = 5005)
