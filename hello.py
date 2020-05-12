import random
#로또번호 만들기 로직

#lottos 변수에 빈 리스트를 지정
lottos=[]
#반복 lottos가 6개가 아닌 동안
while len(lottos) < 6:
    #렌덤하게 숫자를 만들어요. 1~46 사이의 임의의 수를 변수 new에 담아요
    new = random.randint(1,46)
    if new not in lottos:
        lottos.append(new)
    
    # 만약 new가 lottos에 없으면,
        #lottos에 new를 추가합니다.

# vip message
message_vip = """
안녕하세요. {0}님, 파이썬 수업에 오신 걸 환영합니다.
오늘은 첫째날입니다. {0}님의 메일주소 {1}로 학습내용을 보내드립니다.
20% 특별 할인권을 보내드렸습니다.
로또번호 {2} 추천드립니다.
"""

# 일반회원 message
message1 = """
안녕하세요. {0}님, 파이썬 수업에 오신 걸 환영합니다.
오늘은 첫째날입니다. {0}님의 메일주소 {1}로 학습내용을 보내드립니다.
로또번호 {2} 추천드립니다.
"""

# 비회원 message
message2 = """
안녕하세요. {0}님, 
파이썬 수업을 소개합니다. 참여하고 싶으시면 접수를 부탁드려요.
로또번호 {1} 추천드립니다.
"""

# 보낼사람의 이름과 이메일주소를 입력을 받는다.
name = input("이름을 입력해 주세요.")
email = input("이메일을 입력해 주세요.")
회원등급 = input("회원등급이 어떻게 되나요? (1. VIP / 2. 일반회원 / 3. 비회원)")

# 메일 내용을 완성해서 출력한다.
if 회원등급 == '1':
    complete = message_vip.format(name, email, lottos)
elif 회원등급 == '2':
    complete = message1.format(name, email, lottos)
else:
    complete = message2.format(name, lottos)

print(complete)
# send_email(complete, to=email)
