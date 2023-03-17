import PySimpleGUI as sg

sg.theme("Reddit")
# layout=[[sg.I("",key="input",enable_events=True)],
#         [sg.T(key="output")],
#         [sg.Ok(),sg.Cancel()]
#         ]

# root=sg.Window("My App",layout)
# while True:
#     event,values=root.read()
#     if event in ["Cancel",sg.WIN_CLOSED]:
#         root.close()
#         break
#     elif event == "Ok" and values["input"]:
#         root["output"].update(values["input"])
#     print(event,values)
# print(sg.theme_list())
layout = [
    [sg.T("Choose situation")],
    [
        sg.Rad(text="Single",key="single", group_id=1, default=True,enable_events=True),
        sg.Rad(
            text="Married",
            key="married",
            group_id=1,
            enable_events=True
        ),
    ],
    [sg.T("Children num:",key="Chlnum",visible=False),sg.I(key="children",visible=False,size=(10,1)),],
    [sg.Ok(), sg.Cancel()],
]
root = sg.Window("My App", layout)
while True:
    event,values=root.read()
    if event in ["Cancel",sg.WINDOW_CLOSED]:
        root.close()
        break
    elif event=="married":
        root["Chlnum"].update(visible=True)
        root["children"].update(visible=True)
    elif event=="single":
        root["Chlnum"].update(visible=False)
        root["children"].update(visible=False)

    print(event,values)