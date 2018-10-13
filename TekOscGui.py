# coding: utf-8
import tkinter as tk
import tkinter.ttk as ttk
import visa

# Under construction
class tekvisa():
    def __init__(self):
        # self.rm = visa.ResourceManager()
        # self.rm.list_resources()
        self.insttuple = ("a","b","c")    
    def connect(self, inst, status):
        #self.inst = rm.open_resource(inst)
        print(inst)
        status["text"] = "Successfully Connected to " + inst
    def getdata(self, inst, status):
        if inst==0:
            print("PNG Saved")
            status["text"] = "Screen captured image saved to aaa"
        else:   
            print("CSV Saved")
            status["text"] = "CSV saved to bbb"

def insttest():
    print("visa")

#-----------------------
# 接続機器の取得
#-----------------------
tekinst = tekvisa()
insttuple = tekinst.insttuple

#-----------------------
# GUI
#-----------------------
root = tk.Tk()
root.title("Get Data/Image for Tektronix Oscilloscope")

statusbar = tk.Label(root, text="Select Instrument.",
                           borderwidth=2, relief="groove")
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

inst_frame = tk.Frame(root,bd=2,relief="ridge")
inst_frame.pack(fill="x")
inst_combo = ttk.Combobox(inst_frame, width=50, state='readonly')
inst_combo["values"] = insttuple
inst_combo.current([0])
inst_combo.pack(side="left")
inst_button = tk.Button(inst_frame, text="接続")
inst_button["command"] = lambda:tekinst.connect(inst_combo.get(), statusbar)
inst_button.pack(side="right")

data_frame = tk.Frame(root,bd=2,relief="ridge")
data_frame.pack(fill="x")
data_combo = ttk.Combobox(data_frame, width=50, state='readonly')
data_combo["values"] = ("Screen Capture(PNG)", "Data(CSV)")
data_combo.current([0])
data_combo.pack(side="left")
data_button = tk.Button(data_frame, text="取得")
data_button["command"] = lambda:tekinst.getdata(data_combo.current(), statusbar)
data_button.pack(side="right")

root.mainloop()