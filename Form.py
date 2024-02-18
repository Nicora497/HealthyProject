import tkinter as tk
from tkinter import ttk

from ManageDB import ManageDB

class Form(tk.Frame):
    def __init__(self,master=None,date=None,preFrame=None,cnf={},**kw):#引数にrootとdateを入れて使って
        #
        # date : (str) 日付 year/month/day
        #
        tk.Frame.__init__(self,master,cnf,**kw)
        
        print(date)
        
        frame_top = tk.Frame(self,width=400,height=800,bg="blue")
        frame_top.propagate(False)
        frame_top.pack()
        
        back_button = ttk.Button(frame_top,text="戻る",command=lambda:self.mv_content(preFrame=preFrame))
        back_button.pack()
        
        ent_sleep_time = ttk.Entry(frame_top)
        ent_sleep_time.pack()
        
        
        ### ここにフォームの内容つくってね
        # sleep_time 睡眠時間
        # body_temp 体温
        # exer_time 運動時間 
        # exer_kind 運動の種類 
        # wight 体重
        # BP_max 最高血圧 
        # BP_min 最低血圧
        
        # データベースに送信(追加)
        # btn_insert_data = ttk.Button(frame_top,text="記録",command=self.send_data(date, sleep_time, body_temp, exer_kind, exer_time, wight, BP_max, BP_min))
        # btn_insert_data.pack()
    
    def send_data(self, date,sleep_time, body_temp, exer_kind, exer_time, wight, BP_max, BP_min):
        ManageDB.insert_or_updata_data(date, sleep_time, body_temp, exer_kind, exer_time, wight, BP_max, BP_min)#データベースに追加
        
    def mv_content(self,preFrame):
        preFrame.tkraise()
        
    
# class Status():#データを入れるためのデータクラス
#     #ここにデータを入れてデータベースにぶち込む
#     def __init__(self,sleep_time,body_temp,exer,wight,BP):
#         sleep_time = sleep_time
#         body_temp = body_temp
#         exercise_kind = exer_kind
#         exercise_time = exer_time
#         wight = wight
#         BP_max = BP_max
#         BP_min = BP_min
        
        
        
# class Exercise():#運動のデータを入れるクラス
#     def __init__(self,kind,time):
#         kind = kind
#         time = time
        
# class Blood_pressure():
#     def __init__(self,max,min):
#         max = max
#         min = min
        
if __name__ == '__main__':  
    root = tk.Tk()
    root.title("Form App")
    root.geometry("400x800")
    form = Form(root, "2024/2/2")
    form.pack()
    root.mainloop()