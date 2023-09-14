import numpy as np
import random
#-----
#import tkinter as tk #built in GUI

#def click_button():
#   n = int(en_number.get())
#   l = [random.randint(1, 100) for i in range(num)]
#   v = np.array(l, dtype='int16')
#   lbl_result.config(text=v)
#window = tk.Tk()
#window.title('numpy gui version v0.7')
#window.geometry('300x150')

##create widget
#lbl_result = tk.Label(text="random numpy array")
#en_number = tk.Entry()
#btn_click = tk.Button(text="click me!", command=click_button)

##widget layout
#lbl_result.pack()
#en_number.pack(fill='x')
#btn_click.pack(fill='x')

#window.mainloop()
#-----

#v = np.array([1, 3, -9, 2])
#v = np.array([1, 3, -9, 2], dtype='int64')
#v = np.array([
#	[1, 3, -9, 2],
#	[71, 13, -22, 7]])
#print(v.ndim, v.shape, v.data, v.dtype, v.strides)
#print(v)
num = int(input("변수 입력 : "))
l = [random.randint(1, 100) for i in range(num)]

v = np.array(l, dtype='int16')
print(v)
