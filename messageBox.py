from tkinter import messagebox

'''The tkinter.messagebox module provides a template base class
 as well as a variety of convenience methods for commonly used configurations. 
The message boxes are modal and will return a subset of 
(True, False, OK, None, Yes, No) based on the user’s selection. 
Common message box styles and layouts include but are not limited to:'''

messagebox.showinfo(title='',
                    message='')
messagebox.showwarning(title='',
                       message='')
messagebox.showerror(title='',
                     message='')
messagebox.askquestion(title='',
                       message='')
messagebox.askokcancel(title='',
                       message='')
messagebox.askretrycancel(title='',
                          message='')
messagebox.askyesno(title='',
                    message='')
messagebox.askyesnocancel(title='',
                          message='')
