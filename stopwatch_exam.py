from tkinter import *
import time
import tkinter
from turtle import right

# stopwatch 
class StopWatch(Frame):                                                           
    def __init__(self, parent=None):        
        Frame.__init__(self, parent)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.laps = []
        self.timestr = StringVar()
        self.makeWidgets()
        self.prevLapHolder = 0
        self.lapcounter = 1

# stopwatch widget design
    def makeWidgets(self):                     
        self.e = Entry(self)
        l = Label(self, textvariable=self.timestr, fg= '#ffffff')
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, padx=2, pady =30)
        l.config(font=('Verdana Bold',30))
        l.config(bg='#333333')
        List = Label(self, text='', fg= '#664826')
        List['background']='#333333'
     
  
        List.pack(expand=NO, pady=90, padx=30)
        scrollbar = Scrollbar(self, orient=VERTICAL, bg='#333333')
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(bg='#333333')
        self.m = Listbox(self,selectmode=EXTENDED, height = 7, width = 50, yscrollcommand=scrollbar.set)
        self.m.place(x=20, y=40)
        self.m.config(font=('Verdana Bold',8), fg= ('#ffffff'))
        self.m.config(bg='#333333')
        self._setTime(self._elapsedtime)
        self.minitimer = Label(text="00:00:00", font=('Verdana Bold', 14), fg= ('#ffffff'))
        self.minitimer.place(x=150,y=160, anchor=CENTER)
        self.minitimer.config(bg='#333333')
        laplabel = Label(text='PREVIOUS LAP TIME:', font=('Verdana Bold', 10), bg= ('#333333'), fg= ('#ffffff')).place(x=150,y=140,anchor=CENTER)



        self.m.pack(side=LEFT, expand=10, padx=2)
        scrollbar.config(command=self.m.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        
    def _update(self): 
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
        

    def _setTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

# split/lap time 
    def _setLapTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)            
        return '%02d:%02d:%02d' % (minutes, seconds, hseconds)
    
    
    def Start(self):                                          
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1 
    
# stop command for stopwatch     
    def Stop(self):                                    
        if self._running:
            tempo = self._elapsedtime - self.prevLapHolder
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self.laps.append("#" + f"{str(self.lapcounter)} {self._setLapTime(tempo)}  {self._setLapTime(self._elapsedtime)} ")
            self.lapcounter += 1
            self.m.insert(END, self.laps[-1])
            self.m.yview_moveto(1)
            self._running = 0
    
  # reset command  
    def Reset(self):                                  
        self.minitimer.config(text=((self._setLapTime(self._elapsedtime))))
        self._start = time.time()         
        self._elapsedtime = 0.0
        self.prevLapHolder = 0
        self.laps = []   
        self.lapcounter = 1
        self.m.delete(0,END)
        self._setTime(self._elapsedtime)
        self.after_cancel(self._timer)            
        self._elapsedtime = time.time() - self._start    
        self._running = 0
    
    def Split(self):
        tempo = self._elapsedtime - self.prevLapHolder
        if self._running:
            self.laps.append("#" + f"{str(self.lapcounter)} {self._setLapTime(tempo)} {self._setLapTime(self._elapsedtime)}")
            self.lapcounter += 1
            self.m.insert(END, self.laps[-1])
            self.m.yview_moveto(1)
            self.prevLapHolder = self._elapsedtime
        
    
# stopwatch functions and other buttons             
def main():
    root = Tk()
    root.title('STOPWATCH')
    root.geometry("300x400")
    root['background']='#333333'
    root.resizable(False,False)
    root.wm_attributes("-topmost", 1)
    sw = StopWatch(root)
    sw.pack(side=TOP)
    sw.config(bg='#333333')
    Button1=tkinter.Button(text = "START", fg= '#ffffff', command=sw.Start, width = 10, height = 2)
    Button1.place(x=100, y=220, anchor='center')
    Button1.config(font=('Verdana Bold',9))
    Button1['background']='#101214'
    Button2=tkinter.Button(text = "SPLIT", fg= '#ffffff',command=sw.Split, width = 10, height = 2)
    Button2.place(x=200, y=220, anchor='center')
    Button2.config(font=('Verdana Bold',9))
    Button2['background']='#101214'
    Button3=tkinter.Button(text = "STOP",fg= '#ffffff',command=sw.Stop, width = 10, height = 2)
    Button3.place(x=100, y=270, anchor='center')
    Button3.config(font=('Verdana Bold',9))
    Button3['background']='#101214'
    Button4=tkinter.Button(text = "RESET", fg= '#ffffff', command=sw.Reset, width = 10, height = 2)
    Button4.place(x=200, y=270, anchor='center')
    Button4.config(font=('Verdana Bold',9))
    Button4['background']='#101214'
    root.mainloop()

    
if __name__ == '__main__':
    main()
