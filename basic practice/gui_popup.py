from turtle import title
import PySimpleGUI as sg

a = sg.popup_get_text(
    "Enter your name",
    default_text="Bullshit",
    button_color="red",
    text_color="white",
    background_color="gray",
    font=("Arial", 10, "bold"),
    keep_on_top=True,
    location=(50, 50),
)
# b=sg.popup("dfciuciiucui",title="Nothing",text_color="red")
# c=sg.popup_get_file()
# d=sg.popup_get_folder()
# e=sg.popup_get_date()
# f=sg.popup_auto_close()
# g=sg.popup_scrolled()
# h=sg.popup_timed()
# i=sg.popup_no_frame()
# j=sg.popup_ok_cancel()
# k=sg.popup_yes_no()
# l=sg.popup_no_titlebar()
# Parameters=[title,background_color,text_color,button_color,auto_close,auto_close_duration,icon,font,image,location,keep_on_top]
print(a)
