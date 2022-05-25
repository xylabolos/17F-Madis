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

# stopwatch widget design
    def makeWidgets(self):                         
        self.e = Entry(self)
        TimerText = Label(self, text='\nTIME', fg= '#856ff8' )
        TimerText.config(font=('Montserrat Extrabold',15))
        TimerText.pack(fill=X, expand=NO, padx=100)
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, padx=2)
        l.config(font=('Montserrat Extrabold',20))
        List = Label(self, text='')
        List.pack(fill=X, expand=NO, pady=10, padx=90)
        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.m = Listbox(self,selectmode=EXTENDED, height = 7, yscrollcommand=scrollbar.set)
        self.m.pack(side=LEFT, expand=10, padx=2)
        self.m['background']='#856ff8'
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
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
    
  # reset command  
    def Reset(self):                                  
        self._start = time.time()         
        self._elapsedtime = 0.0
        self.laps = []   
        self._setTime(self._elapsedtime)
        self.after_cancel(self._timer)            
        self._elapsedtime = time.time() - self._start    
        self._running = 0
    
    def Split(self):
        tempo = self._elapsedtime - self.prevLapHolder
        if self._running:
            self.laps.append((self._setLapTime(self._elapsedtime)))
            self.m.insert(END, self.laps[-1])
            self.m.yview_moveto(1)
            self.prevLapHolder = self._elapsedtime
        
    
# stopwatch functions and buttons             
def main():
    root = Tk()
    root.title('STOPWATCH')
    root.geometry("300x500")
    root.resizable(True,True)
    root.wm_attributes("-topmost", 1)
    sw = StopWatch(root)
    sw.pack(side=TOP)
    Button1=tkinter.Button(text = "Start",command=sw.Start, width = 12, height = 2)
    Button1.place(x=150, y=300, anchor='center')
    Button1.config(font=('Montserrat Extrabold',9))
    Button2=tkinter.Button(text = "Split",command=sw.Split, width = 12, height = 2)
    Button2.place(x=150, y=350, anchor='center')
    Button2.config(font=('Montserrat Extrabold',9))
    Button3=tkinter.Button(text = "Stop",command=sw.Stop, width = 7, height = 2)
    Button3.place(x=70, y=400, anchor='center')
    Button4=tkinter.Button(text = "Reset", command=sw.Reset, width = 7, height = 2)
    Button4.place(x=150, y=400, anchor='center')
    Button5=tkinter.Button(text = "Exit",command=root.destroy, width = 7, height = 2)
    Button5.place(x=230, y=400, anchor='center')
    root.mainloop()

    
if __name__ == '__main__':
    main()
