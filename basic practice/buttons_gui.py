import PySimpleGUI as sg
menu_button=["Menu",["File","Edit","View","Settings",["Audio","Video","Graphics"]]]
layout = [
    [sg.ButtonMenu("Menu",menu_def=menu_button)],
    [sg.B("Button1", button_color="red")],
    [
        sg.B(
            "Button1",
            button_color="red",
            size=(5, 2),
        )
    ,
        sg.B(
            "Button1",
            button_color="red",
            size=(5, 2),
        )
    ],
    [sg.Ok(),sg.Cancel()]
]
root = sg.Window("Buttons App", layout)
event, value = root.read()
print(event, value)
