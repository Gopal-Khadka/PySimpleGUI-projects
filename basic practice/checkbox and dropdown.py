import PySimpleGUI as sg
lang_list=["Python","C++","Java"]
Col1 = [
    [sg.T("Type your Name:")],
    [
        sg.I(key="Name", size=(10, 2)),
    ],
    [sg.CB("Python", key="CB1")],
    [sg.CB("C++", key="CB2")],
    [sg.Ok(), sg.Cancel()],
]

Col2 = [
    [sg.T("Type your Address:")],
    [sg.I(key="Address", size=(15, 1))],
    [sg.CB("Java", key="CB3")],
    [sg.CB("JS", key="CB4")],
    [sg.Ok(), sg.Cancel()],
]
layout = [
    [sg.Col(Col1), sg.VerticalSeparator(), sg.Col(Col2)],
    [sg.HorizontalSeparator()],
    [sg.DD(lang_list,size=(10,2),default_value=lang_list[2])]
    ]
root = sg.Window("Buttons App", layout)
event, value = root.read()
if event == "Cancel":
    root.close()
elif event == "Ok":
    sg.popup_auto_close("Your Name is", value["Name"])

print(event, value)
