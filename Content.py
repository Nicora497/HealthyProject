import tkinter as tk
from tkinter import ttk

from ManageDB import ManageDB
from Form import Form #

class Content(tk.Frame):
    def __init__(self,master=None,mine=None,date=None,cnf={},**kw):#引数にrootとdateを入れて使って
        #
        # date : (str) 日付 year/month/day
        #
        tk.Frame.__init__(self,master,cnf,**kw)
        
        #コンテンツ
        frame_cont = tk.Frame(self,width=400,height=800,bg="red")
        frame_cont.propagate(False)
        frame_cont.grid(row=0,column=0)
        
        #フォーム
        frame_form = Form(self,preFrame=frame_cont)
        frame_form.grid(row=0,column=0)
        
        #コンテンツを一番上に表示
        frame_cont.tkraise()
        
        #クエリ
        manage = ManageDB()
        content = manage.query_data(date=date)
        print(content)
        
        #戻るボタン
        back_button = ttk.Button(frame_cont,text = "戻る",command=lambda:self.mv_main(mine))
        back_button.pack()
        #入力フォームへページを変えるボタン
        form_button = ttk.Button(frame_cont,text = "入力",command=lambda:self.mv_form(frame_form))
        form_button.pack()
        
        ### ここにコンテンツの内容つくってね
        # sleep_time 睡眠時間
        ent_sleep_time = ttk.Label(frame_cont,text = "aaaaaaa")
        ent_sleep_time.pack()
        # body_temp 体温
        # exer_time 運動時間 
        # exer_kind 運動の種類 
        # wight 体重
        # BP_max 最高血圧 
        # BP_min 最低血圧
        
    def mv_main(self,sub=None):
        sub.tkraise()
        
    def mv_form(self,frame_form):
        frame_form.tkraise()
        
if __name__ == '__main__':  
    root = tk.Tk()
    root.title("Form App")
    root.geometry("400x800")
    cont = Content(root, "2024/2/14")
    cont.pack()
    root.mainloop()