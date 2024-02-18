import tkinter as tk

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.ticker import MaxNLocator

import datetime

from Calendar import myCalendar #カレンダー機能
from Content import Content #
from Form import Form #
from ManageDB import ManageDB #データベース管理

#main
class HEALTH(tk.Frame):
    def __init__(self, master=None,cnf={},**kw):

        tk.Frame.__init__(self,master,cnf,**kw)
        
        mainFrame = tk.Frame(master,width=400,height=800,bg="black") #メイン
        mainFrame.grid_propagate(False)
        mainFrame.grid(row=0,column=0)
        
        contentFrame = tk.Frame(master,width=400,height=800) #コンテンツ表示
        contentFrame.grid(row=0,column=0)
        
        
        ketu = KETU(mainFrame) #血圧
        ketu.grid(row=0,column=0)
        
        cal = myCalendar(mainFrame,sub=contentFrame) #カレンダー
        cal.grid(row=1,column=0)
        
        
        
        mainFrame.tkraise()
        
        

#mainに表示する血圧
class KETU(tk.Frame):
    def __init__(self,master=None,cnf={},**kw):
        super().__init__(master,cnf,**kw)

        frame_top = tk.Frame(self.master, width=400, height=300, relief='solid')
        frame_top.grid(row=0,column=0)
        
        fig = Figure(dpi=100,figsize=(4, 3))
        ax = fig.add_subplot(1, 1, 1)
        
        fig_canvas = FigureCanvasTkAgg(fig, frame_top)
        fig_canvas.get_tk_widget().pack(fill=tk.Y, expand=False)
        
        date = datetime.datetime.now()
        date_num = date.day
        x = [date_num-4, date_num-3, date_num-2, date_num-1, date_num]
        y = self.get_BP()
        # for num in y:
        #     if num == 0:
        #         num = np.nan
        
        ax.plot(x, y, marker='.', color="red")
        
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        #ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xticks([date_num-4, date_num-3, date_num-2, date_num-1, date_num])
        ax.set_yticks([80,100,120,140,160,180,200])
        ax.set_ylim(60,220)
        
        # 表示
        fig_canvas.draw()


        frame_top.propagate(False)
    
    def get_BP(self):
        date = datetime.datetime.now()
        manage = ManageDB()
        BP = [0] * 5
        for i in reversed(range(5)):
            date_str = str(date.year)+"/"+str(date.month)+"/"+str(date.day-i)
            date_num = date.day
            BP[i] = manage.query_data(date=date_str,op="BP_max")

            if not BP[i]:
                BP[i] = [(0,0)]
            for data in BP[i]:
                BP[i] = data[0]
            
        return BP
        


class TMP(tk.Frame):
    def __init__(self,master=None,cnf={},**kw):
        super().__init__(master)
        B = tk.Button()
        B.pack()
        
        self.pack()
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title("App")
    root.geometry("400x800") 
    app = HEALTH(master=root)
    app.mainloop()
