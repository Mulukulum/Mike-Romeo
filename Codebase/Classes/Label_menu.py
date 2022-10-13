from priority import priority
import PySimpleGUI as sg
def label_select(taskname):
    a=taskname.labels()
    sg.theme('Dark Amber')
    layout1= [[sg.Text("Choose your letter",size=(30,1),font='Georgia',justification="left")],\
        [sg.Listbox(values=a,select_mode="extended",key="label",size=(50,10))],\
            [sg.Button('SAVE', font=('Times New Roman',12)),sg.Button('CANCEL', font=('Times New Roman',12))]]
    win=sg.Window("Dropdown Box", layout1)
    e,v=win.read()
    win.close()
    st=""
    for val in v["label"]: 
        st+=" "+val+","
    sg.popup("Label(s) Chosen: "+st[1:len(st)-1])
