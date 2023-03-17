import PySimpleGUI as sg

FONT = ("Ubuntu", 15, "normal")
header = [
    [
        sg.CalendarButton("Set date", size=(10, 1), key="time"),
        sg.T("-- -- -- --", key="calendar", font=FONT),
    ],
    [sg.T("Write Task:", font=FONT), sg.I(key="task", font=FONT, size=(32, 1))],
]
task_display = [
    [
        sg.Table(
            values="",
            headings=["Index", "Date", "Time", "Task"],
            font=FONT,
            size=(500, 10),
            auto_size_columns=False,
            key="table",
            col_widths=[5, 9, 7, 30],
            vertical_scroll_only=False,
            justification="l",
            enable_events=True,
        )
    ]
]
footer = [
    [
        sg.B("Add", key="add", size=(5, 1), button_color="green"),
        sg.B("Delete", key="del", size=(5, 1), button_color="red"),
        sg.Exit(size=(5, 1)),
    ]
]
layout = [
    [sg.Fr("Task Entry", header, border_width=0)],
    [sg.Fr("", task_display, border_width=0)],
    [sg.Fr("", footer, border_width=0)],
]
root = sg.Window("To Do App", layout)
index_count = 1
task_list = []
while True:
    event, values = root.read()
    if event in [
        "Exit",
        sg.WINDOW_CLOSED,
    ]:
        root.close()
        break
    elif event == "add":
        try:
            time_list = root["calendar"].get().split()
            date = time_list[0]
            time = time_list[1]
        except IndexError:
            sg.popup_auto_close(
                "Enter the valid date.",
                title="Date Invalid",
            )
        else:
            task = [[index_count, date, time, values["task"]]]
            task_list += task
            root["table"].update(task_list)
            root["task"].update("")
            root["calendar"].update("-- -- -- --")
            index_count += 1
    elif event == "del":
        if values["table"]:
            index = values["table"][0]
            print(index)
            del task_list[index]
            root["table"].update(task_list)
