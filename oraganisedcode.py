import tkinter

#main window/page
root = tkinter.Tk()
root.title("Retro Board")
root.geometry("800x600")

#frames container
frame_container = tkinter.Frame(root)
frame_container.pack(fill = 'both', expand = 'true')
frame_container.grid_rowconfigure(0, weight=1)
frame_container.grid_columnconfigure(0, weight=1)

#all frames
create_board_frame = tkinter.Frame(frame_container, bg="lightblue")
create_board_frame.grid(row=0, column=0, sticky="nsew")

board_frame = tkinter.Frame(frame_container, bg="beige")
board_frame.grid(row=0, column=0, sticky="nsew")

cards_frame = tkinter.Frame(frame_container, bg="lightgreen")
cards_frame.grid(row=0, column=0, sticky="nsew")


# Function to create a board
def create_board():
    
    new_board_butt = tkinter.Button(create_board_frame, text="Create New \n Board\n+", bg='Blue', fg='white', font=('Arial', 14),
                                    relief=tkinter.RAISED, borderwidth=2, command=lambda: board_name_description())
    new_board_butt.pack(padx= 100, pady= 200)
    new_board_butt.bind("<Button-1>", lambda e: print("New Board Button Clicked!"))

#gloabal variable for board name and description
board_name_entry, description_entry, board_name, board_description = None, None, None, None

#  function for next page board name and description
def board_name_description():
    global board_name_entry, description_entry, board_name, board_description
# Clear the board_frame before adding new widgets
    for widget in board_frame.winfo_children():
        widget.destroy()
    
    board_name = tkinter.StringVar()
    board_description = tkinter.StringVar()
    # Label for board name
    board_name_label = tkinter.Label(board_frame, text="Board Name:", bg='tan', font=('Arial', 14))
    board_name_label.pack(pady=(20, 5))
    board_name_entry = tkinter.Entry(board_frame, relief=tkinter.RAISED, width=25, font= ('Bold', 18),
                   textvariable=board_name)
    board_name_entry.pack(pady=5)
    # Label for board description
    description_label = tkinter.Label(board_frame, text="Description:", bg='tan', font=('Arial', 14))
    description_label.pack(pady=(20, 5))
    description_entry = tkinter.Entry(board_frame, relief=tkinter.RAISED, width=25)
    description_entry.pack(pady=5)

    next_butt= tkinter.Button(board_frame,bg= 'blue', fg= 'black', text ='NEXT', relief= tkinter.RAISED,
                          borderwidth= 1, command=lambda: create_cards())
    next_butt.pack(pady=20)
    
    board_back_butt= tkinter.Button(board_frame, bg= 'black', fg= 'white', text= '< Back',
               font=('bold', 14), command=lambda:create_board_frame.tkraise())
    board_back_butt.pack(side=tkinter.BOTTOM, padx=10, pady=10)
    board_frame.tkraise()

#function for cards
def create_cards():
    for widget in cards_frame.winfo_children():
        widget.destroy()
    
    #clearing the board name and description
    def back_to_board():
        board_name.set("")          
        board_description.set("")   
        board_name_description()

    back_button = tkinter.Button(cards_frame, text="< Back", command=lambda: board_name_description())
    back_button.pack(side=tkinter.BOTTOM, padx=10, pady=10)
    cards_frame.tkraise()

create_board()
create_board_frame.tkraise()

root.mainloop()