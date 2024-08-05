import tkinter as tk
from tkinter import messagebox

# 메시지를 표시하는 함수
def show_message(tickers):
    root = tk.Tk()  # tkinter의 루트 창 생성
    root.withdraw()  # 루트 창을 숨깁니다
    root.attributes('-topmost', True)  # 창을 항상 최상위에 표시
    messagebox.showinfo("알림", f'{tickers}')
    root.destroy()  # 메시지 박스가 닫힌 후 루트 창 종료
