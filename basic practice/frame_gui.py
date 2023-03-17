import PySimpleGUI as sg

lang_list = ["Python", "C++", "Java"]
menu_button = [
    ["Basic", ["File", "Edit", "View", "Settings"]],
    ["Advanced", ["Audio", "Video", "Graphics"]],
]


frame1 = [
    [sg.T("Type your Name:")],
    [
        sg.I(key="Name", size=(10, 2)),
    ],
    [sg.LB(lang_list, size=(10, 4))],
    [sg.CB("Python", key="CB1")],
    [sg.CB("C++", key="CB2")],
]
frame2 = [
    [sg.T("Type your Address:")],
    [sg.I(key="Address", size=(15, 1))],
    [sg.CB("Java", key="CB3")],
    [sg.CB("JS", key="CB4")],
]
img_frame = [
    [sg.Image(key="-IMG-")],
    [sg.Menu(menu_button)],
    [sg.Multiline(key="MULTI",size=(50,15))]
]
layout = [
    [
        sg.Frame("Frame No 1", frame1, border_width=10, background_color="lightblue"),
    ],
    [sg.VerticalSeparator()],
    [sg.I(key="-PATH-"), sg.FileBrowse()],
    [sg.Fr("Image", img_frame)],
    [sg.Ok(), sg.Cancel()],
]
root = sg.Window("Buttons App", layout, size=(600, 600))
event, value = root.read()
if event == "Cancel":
    root.close()
elif event == "Ok":
    root["-IMG-"].update(value["Browse"])
print(event, value)
