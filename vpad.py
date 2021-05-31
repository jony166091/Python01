import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os 

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Vpad text editor')

########################   main menu ##################
main_menu = tk.Menu()
#file icons
new_icon = tk.PhotoImage(file='icone/new.png')
open_icon = tk.PhotoImage(file='icone/open.png')
save_icon = tk.PhotoImage(file='icone/save.png')
save_as_icon = tk.PhotoImage(file='icone/save_as.png')
exit_icon = tk.PhotoImage(file='icone/exit.png')


file = tk.Menu(main_menu,tearoff=False)

file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N')
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O')
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S')
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S')
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q')

#### Edit #####
# edit icons
copy_icon = tk.PhotoImage(file='icone/copy.png')
paste_icon = tk.PhotoImage(file='icone/paste.png')
cut_icon = tk.PhotoImage(file='icone/cut.png')
clear_icon = tk.PhotoImage(file='icone/clear_all.png')
find_icon = tk.PhotoImage(file='icone/find.png')

## command #####
edit = tk.Menu(main_menu,tearoff=False)
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit.add_command(label='Paste',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+V')
edit.add_command(label='Cut',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit.add_command(label='Clear All',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X')
edit.add_command(label='Find',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+F')

###  Tool bar icone 
#-------------------------------------------

tool_bar_icon = tk.PhotoImage(file='icone/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icone/status_bar.png')

view = tk.Menu(main_menu,tearoff=False)
view.add_checkbutton(label='Tool Bar', image=tool_bar_icon,compound=tk.LEFT)
view.add_checkbutton(label='Status Bar',image=status_bar_icon,compound=tk.LEFT)

##################color theme #########################

light_default_icon=tk.PhotoImage(file='icone/light_default.png')
light_plus_icon=tk.PhotoImage(file='icone/light_plus.png')
dark_icon=tk.PhotoImage(file='icone/dark.png')
red_icon=tk.PhotoImage(file='icone/red.png')
monokai_icon=tk.PhotoImage(file='icone/monokai.png')
night_blue_icon=tk.PhotoImage(file='icone/night_blue.png')
color_theme = tk.Menu(main_menu,tearoff=False)
theme_choice= tk.StringVar() 
color_icons = (light_default_icon,light_plus_icon,dark_icon,monokai_icon,night_blue_icon)
 
color_dict1 = {
     'Light Default' : ('#000000', '#ffffff'),
     'Light Plus' : ('#474747','#e0e0e0'),
     'Dark' : ('#c4c4c4', '#2d2d2d'),
     'Red' : ('#2d2d2d', '#ffe8e8'),
     'Monokai' : ('#d3b774','#474747'),
     'Night Blue' :('#ededed','#6b9dc2')
  } 
count = 0
i = 0
for i in "color_dict1":
  color_theme.add_radiobutton(label = i, image=color_icons [count], variable = theme_choice , compound = tk.LEFT )
  count += 1


#cascade
main_menu.add_cascade(label='File',menu=file)  
main_menu.add_cascade(label='edit',menu=edit)  
main_menu.add_cascade(label='View',menu=view)  
main_menu.add_cascade(label='Color Theme',menu=color_theme)




#----------------------- End main menu -----------------
########################   tool bar ##################
#----------------------- End tool bar -----------------
########################   text editor  ###############
#----------------------- End text editor ---------------
######################## main status bar ###############
#----------------------- End status bar --------------
################# main menu functinality #############
#----------- End main menu functinality ----------------

main_application.config(menu=main_menu)
main_application.mainloop()