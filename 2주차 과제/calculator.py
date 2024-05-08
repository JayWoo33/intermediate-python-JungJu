import tkinter as tkt
from tkinter import *

def on_click(number):
    entry.insert(tkt.END, number) # tkt.END means 끝부분에 insert 해주겠다. 
    
def on_clear():
    entry.delete(0, tkt.END) #메모장에서 공부한 내용

# def create_button(text, row, column, command, width=40, height=20, columnspan=1, rowspan=1):
#     button = tkt.Button(root, text=text, padx=width, pady=height, command=command)
#     button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

def create_button(text, row, column, command, width=13, height=9, columnspan=1, rowspan=1, bg=None):
   button = tkt.Button(root, text=text, padx=width, pady=height, command=command, borderwidth=5, bg='gainsboro') #버튼 깔롱 주기 위해 borderwitdth 부여
   button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')
   
def operate(operator):
    global first_num
    global 연산자
    연산자 = operator
    first_num = float(entry.get()) #실수 연산 구하기 위해 입력값 실수로 받음
    if int(first_num) == first_num : #입력값이 정수인 경우 계산 결과에서 소수부 제거하기 위해 int 전환
        first_num = int(first_num)
    entry.delete(0, tkt.END)

def on_equal():
    second_num = float(entry.get()) #실수 연산 구하기 위해 입력값 실수로 받음
    if int(second_num) == second_num : #입력값이 정수인 경우 계산 결과에서 소수부 제거하기 위해 int 전환
        second_num = int(second_num)
    entry.delete(0, tkt.END)

    if 연산자 == "+":
        entry.insert(0, first_num + second_num)
    elif 연산자 == "-":
        entry.insert(0, first_num - second_num)
    elif 연산자 == "*":
        entry.insert(0, first_num * second_num)
    elif 연산자 == "/":
        entry.insert(0, first_num / second_num)
    elif 연산자 == "%":
        entry.insert(0, first_num % second_num) #모듈러 연산 구현

# 창 생성
root = Tk()
root.title("계산기")

# 아이콘 설정
# photo = tkt.PhotoImage(file="C:/Study/해달/부트캠프/2024-1-파이썬응용/2주차/윈도우계산기아이콘.png") == 절대 경로.
icon = PhotoImage(file="E:/haedal/bootcamp_python/2주차/icon.png") # == 상대 경로 / 일반적인 경우는 상대 경로 사용하는 경우 많음. './'은 파일이 있는 위치에서 사용이라는 뜻
root.iconphoto(False, icon)

# 엔트리 생성 (한줄 텍스트)
entry = tkt.Entry(root, width=20, borderwidth=12, justify="right", font=("Verdana", 13))
entry.grid(row=0, column=0, columnspan=4, pady=10)  # 0행, 0열에 배치, 4개의 열을 차지, y축에패딩(여백)추가

# for number in range(9):
#     button = tkt.Button(root, text=str(number + 1), padx=40, pady=20, command=on_click(number+1))
#     button.grid(row=4-number//3, column=number%3) 
#     # 프로그램 실행 시 on_click(number+1) 함수가 실행되고, 그 결과가 command에 할당됨
#     # 이 경우에는 함수의 return값이 없으므로 command에는 아무것도 담기지 않음
    

# for number in range(9):
#     button = tkt.Button(root, text=number+1, padx=40, pady=20, command=lambda n=number+1: on_click(n))
#     button.grid(row=4-number//3, column=number%3)
#     # 이 경우에 command에 담기는 것은 number+1을 인자로 받고, on_click(n)이라는 함수 내용을 가진 람다함수 그 자체
#     # 람다 함수란? 이름조차 짓기귀찮은 간단한 함수 만들 때 사용
# 	    # lambda 인수: 반환값

for number in range(9):
    create_button(str(number + 1), 4-number//3, number%3, lambda n=number+1: on_click(n)) #, bg='gainsboro'
    create_button("0", 5, 0, lambda: on_click(0), columnspan=2) #, bg='gainsboro')

create_button("C", 1, 0, on_clear, bg='gray70') #clear 버튼

create_button("%", 1, 2, lambda: operate("%"), bg='gray70')
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange') # 연산 버튼

root.mainloop()
