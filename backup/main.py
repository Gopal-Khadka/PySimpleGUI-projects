import PySimpleGUI as sg
import zipfile
import os
import shutil

header = [
    [
        sg.T("Source Folder:", size=(15, 1)),
        sg.I(key="SOURCE", enable_events=True),
        sg.FolderBrowse(size=(12, 1)),
    ],
    [
        sg.T("Destination Folder:", size=(15, 1)),
        sg.I(key="TARGET"),
        sg.FolderBrowse(size=(12, 1)),
    ],
    [
        sg.T("Folder Name:", size=(15, 1)),
        sg.I(key="FNAME"),
        sg.CB("Compress", key="COMPRESS", default=True),
    ],
]
body = [
    [
        sg.LB(values="", key="LISTBOX", size=(80, 15), enable_events=True),
    ]
]
footer = [
    [
        sg.B("Backup", button_color="green", key="BACKUP"),
        sg.B("Delete", key="DEL", button_color="blue"),
        sg.Exit(button_color="red"),
    ]
]
layout = [
    [sg.Fr("", header, border_width=0)],
    [sg.Fr("File List", body, border_width=0)],
    [sg.Fr("", footer, border_width=0)],
]
root = sg.Window("Folder Compressor", layout)

while True:
    event, values = root.read()
    if event in [
        "Exit",
        sg.WINDOW_CLOSED,
    ]:
        root.close()
        break
    elif event == "SOURCE":
        file_list = os.listdir(values["SOURCE"])
        root["LISTBOX"].update(file_list)
    elif event == "BACKUP":
        if not (values["SOURCE"] or values["TARGET"] or values["FNAME"]):
            sg.popup_auto_close("Don't leave any inputs empty", title="Empty Fields")
        else:
            source_folder = values["SOURCE"]
            target_folder = values["TARGET"]
            filename = values["FNAME"]
            folder_name = os.path.basename(source_folder)
            if values["COMPRESS"]:
                compress = zipfile.ZIP_DEFLATED
                with zipfile.ZipFile(
                    f"{filename}.zip", "w", compression=compress
                ) as t_file:
                    for file in file_list:
                        finalfile = os.path.join(source_folder, file)
                        t_file.write(
                            finalfile, arcname=os.path.join(f"{folder_name}/", file)
                        )
                shutil.move(os.path.join(os.getcwd(), f"{filename}.zip"), target_folder)
                sg.popup("Compression successful.")
    print(event, values)
