import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tkinter.constants import CENTER
import myLib

win = tk.Tk()
win.title('健康管理系統')
myHy = myLib.Healthy()

window_width = win.winfo_screenwidth()  # 取得螢幕寬度
window_height = win.winfo_screenheight()  # 取得螢幕高度
left = int((window_width - 400)/2)       # 計算左上 x 座標
top = int((window_height - 240)/2)      # 計算左上 y 座標
win.geometry(f"{400}x{240}+{left}+{top}")
win.configure(background='#CCEEFF')   # 設定背景色


# window_width = win.winfo_screenwidth()    # 取得螢幕寬度
# window_height = win.winfo_screenheight()  # 取得螢幕高度
# width = 400
# height = 240
# left = int((window_width - width)/2)       # 計算左上 x 座標
# top = int((window_height - height)/2)      # 計算左上 y 座標
# win.geometry(f'{width}x{height}+{left}+{top}')
# win.configure(background='#CCEEFF')   # 設定背景色


def BMI():
    if txtHigh.get() !="" and txtWeight.get() !="":
        bmi = myHy.BMI(int(txtHigh.get()), int(txtWeight.get()))
        # print(bmi)
        labMsg['text'] = (f'你的BMI={bmi}')
    elif txtHigh.get() =="" and txtWeight.get() =="":
        msg.showerror("錯誤","未輸入身高、體重")
    elif txtHigh.get() =="":
        msg.showerror("錯誤", "未輸入身高")
    elif txtWeight.get() =="":
        msg.showerror("錯誤", "未輸入體重")

def BMR():
    if cmbSex.get() !="" and txtHigh.get() !="" and txtWeight.get() !="" and txtAge.get() !="":
        bmr = myHy.BMR(cmbSex.get(), int(txtHigh.get()), int(txtWeight.get()), int(txtAge.get()))
        # print(bmr)
        labMsg['text'] = (f'你的BMR={bmr}')
    elif cmbSex.get() =="":
        msg.showerror("錯誤", "未選擇性別")
    elif txtAge.get() =="":
        msg.showerror("錯誤", "未輸入年齡")
    elif txtHigh.get() =="":
        msg.showerror("錯誤", "未輸入身高")
    elif txtWeight.get() =="":
        msg.showerror("錯誤", "未輸入體重")

def TDEE():
    if cmbSex.get() !="" and txtHigh.get() !="" and txtWeight.get() !="" and txtAge.get() !="" and cmbSport.get() !="":
        tdee = myHy.TDEE(cmbSex.get(), int(txtHigh.get()), int(txtWeight.get()), int(txtAge.get()), cmbSport.get())
        labMsg['text'] = (f'你的TDEE={tdee}')
    elif cmbSex.get() =="":
        msg.showerror("錯誤", "未選擇性別")
    elif txtAge.get() =="":
        msg.showerror("錯誤", "未輸入年齡")
    elif txtHigh.get() =="":
        msg.showerror("錯誤", "未輸入身高")
    elif txtWeight.get() =="":
        msg.showerror("錯誤", "未輸入體重")
    elif cmbSport.get() =="":
        msg.showerror("錯誤", "未選擇活動量")


labSex = tk.Label(win, text="性            別",background="#FF3333")
labSex.grid(row=0, column=0)
cmbSex = ttk.Combobox(win, values=['男','女'], width=15)  #下拉選單選項
cmbSex.grid(row=0, column=1)


labAge = tk.Label(win, text="年            齡",background="#FFCC22")
labAge.grid(row=1, column=0)
txtAge = tk.Entry(win)  #文字輸入框
txtAge.grid(row=1, column=1)

labHigh = tk.Label(win, text="身            高",background="#FFFF00")
labHigh.grid(row=2, column=0)
txtHigh = tk.Entry(win)
txtHigh.grid(row=2, column=1)

labWeight = tk.Label(win, text="體            重",background="#00FF00")
labWeight.grid(row=3, column=0)
txtWeight = tk.Entry(win)
txtWeight.grid(row=3, column=1)


labSport = tk.Label(win, text="日常活動量",background="#00FFFF")
labSport.grid(row=4, column=0)
cmbSport = ttk.Combobox(win, values=['幾乎沒動','運動1~3天','運動3~5天','運動6~7天','7天以上'], width=20)
cmbSport.grid(row=4, column=1)

#   做一個空位顯示結果
labMsg = tk.Label(text="檢測結果",width=20,background='#DDDDDD')
# labMsg = tk.Label(win, text="", width=20)
labMsg.grid(row=5, column=1)

#   按鈕
btnScale = tk.Button(win, text="BMI",command=BMI,background="#BBFFEE")
btnScale.grid(row=6, column=0)
btnScale2 = tk.Button(win, text="BMR",command=BMR,background="#BBFFEE")
btnScale2.grid(row=6, column=1)
btnScale3 = tk.Button(win, text="TDEE",command=TDEE,background="#BBFFEE")
btnScale3.grid(row=6, column=2)


win.mainloop()