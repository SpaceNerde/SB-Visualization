import pandas as pd
import tkinter as tk

class SSD_CNEOS(tk.Frame):
    def __init__(self, root, data, *args):
        super().__init__(root, *args)

        self.root = root
        self.frame = tk.Frame(self.root)
        self.df = data
        self.create_table()
        
    def data_processing(self, e, r, c):
        value = e.widget.get()
        self.df.iloc[r,c] = value
        print(self.df)

    def create_table(self):
        rows, cols = self.df.shape
        for r in range(rows):
            for c in range(cols):
                e = tk.Entry(self)
                e.insert(0, self.df.iloc[r, c])
                e.grid(row=r, column=c)
                e.bind('<Return>', lambda event, y=r, x=c: self.data_processing(event,y,x))
                e.bind('<KP_Enter>', lambda event, y=r, x=c: self.data_processing(event,y,x))
                e.bind('<KeyRelease>', lambda event, y=r, x=c: self.data_processing(event, y,x))

        '''
        canvas = tk.Canvas(self.root, scrollregion="0 0 2000 1000", width=400, height=400)
        canvas.grid(row=0, column=0, sticky=tk.NSEW)

        scroll = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=canvas.yview)
        scroll.grid(row=0, column=1, sticky=tk.NS)   
        canvas.config(yscrollcommand =scroll.set)
        
        for fila in range(20):
            for col in range(5):
                btn = tk.Button(self.frame, text = f"{fila}-{col}")
                btn.grid(row = fila, column = col, sticky = tk.NSEW)
        '''
        '''
        for row in range(len(self.df)):
            for column in range(len(self.df.columns)):
                e = tk.Entry(self.frame, fg='blue', font=('Arial', 16, 'bold'))
                e.grid(row=row, column=column, sticky=tk.NSEW)
        '''
        '''
        item = canvas.create_window(( 2, 2 ), anchor = tk.NW,  window = self.frame )
        '''
        
        
        

        