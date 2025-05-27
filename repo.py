import tkinter
import uuid
#importing new
import requests
import sqlite3
db_connect = sqlite3.connect('retroboard.db')

#api path
api_path = 'http://127.0.0.1:5000'
#integrate boards
def create_board_api(board_name, description=""):
    try:
        payload = {
            "board_name": board_name,
            "description": description
        }
        response = requests.post("http://127.0.0.1:5000/boards", json=payload)

        if response.status_code == 201:
            result = response.json()
            print("oard created with ID:", result['board_id'])
        else:
            print("Failed to create board:", response.json())
    except Exception as e:
        print(" API call failed:", str(e))
        
        


         
#to store comments of each cards
card_comments = {}
board_id = None
ticard_comments = {}
aicard_comments = {}

#main window/page
root = tkinter.Tk()
root.title("Retro Board")
root.geometry('800x600')
#frames container
container = tkinter.Frame(root)
container.pack(fill = 'both', expand = 'true')
#frame stacking
frame1 = tkinter.Frame(container, bg= 'Sky blue')
frame2 = tkinter.Frame(container, bg= 'white')
frame3 = tkinter.Frame(container, bg= 'white')
frame4 = tkinter.Frame(container, bg= 'beige')
for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0, column=0, sticky="nsew")

#displaying boardname on next page
board_name = tkinter.StringVar()
#back button1
tkinter.Button(frame2, bg= 'white', fg= 'black', text= '< Template',
               font=('bold', 24), command=lambda: frame1.tkraise()).pack()
#create custom button
butt2 = tkinter.Button(frame2, bg='brown', fg='black',
               text= 'Create custom \n template\n   +', font=('Courier', 20),
               relief= tkinter.RAISED, borderwidth= 2, command=lambda: frame3.tkraise())
butt2.pack(padx= 50, pady=100)
#page 3 title
title_label = tkinter.Label(frame3, text='Create Custom Board Template', font=('Bold', 18))
title_label.pack(pady=(20, 10))
#input storing of board name
input_frame = tkinter.Frame(frame3, bg='white')
input_frame.pack()
tkinter.Label(input_frame, text="Board name:").pack(side='left', padx=10, pady=20)
#entry frame for board name
e1 = tkinter.Entry(input_frame, relief=tkinter.RAISED, width=25, font= ('Bold', 18),
                   textvariable=board_name)
e1.pack(side='left')
#input for description frame
input_frame2 = tkinter.Frame(frame3, bg='white')
input_frame2.pack()
#red
description_entry = tkinter.Entry(input_frame2, relief=tkinter.RAISED, width=25)
description_entry.pack(side='left')
#red added
create_board_api(e1.get(), description_entry.get())



#entry field for description
e1 = tkinter.Entry(input_frame2, relief=tkinter.RAISED, width=25)
e1.pack(side='left')
#next button of page 3
next_butt= tkinter.Button(frame3,bg= 'blue', fg= 'black', text ='NEXT', relief= tkinter.RAISED,
                          borderwidth= 1, #red change 
                          command=lambda: frame4.tkraise())
next_butt.pack()
#bind page 3 to enter

#back button of page 3
back_butt= tkinter.Button(frame3, bg='black', fg= 'white', text= 'Back',
                          command=lambda: frame2.tkraise())
back_butt.pack(padx=10, pady=5)
#page 4 title as board name input from page 3
tkinter.Label(frame4, textvariable=board_name, font= ('Times New Roman', 20), fg= 'black').pack()
#grids for frames container, location or size
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
#container 2 for page 4 comment sections
container2 = tkinter.Frame(frame4, bg= 'beige')
container2.pack(fill='both', expand=True, padx=10, pady=10)
#went well comment section frame
wentwell_frame = tkinter.Frame(container2, bg='light pink', borderwidth=2, relief=tkinter.RIDGE)
wentwell_frame.pack(side='left', fill='both', expand=True, padx=5)
#went well label
tkinter.Label(wentwell_frame,
             text='Went Well', bg='light pink', fg='black', font=('Arial', 14, 'bold'),
             pady=5).pack(fill='x')
#went well entry field
wentwell_entry = tkinter.Entry(wentwell_frame,
                              font=('Arial', 12),
                              relief=tkinter.SUNKEN, borderwidth=2)
wentwell_entry.pack(fill='x', padx=5, pady=5)
#went well entry binding
wentwell_entry.insert(0, "Press enter to add card (@ to tag)")
wentwell_entry.bind("<FocusIn>", lambda e: wentwell_entry.delete(0, 'end')
if wentwell_entry.get() == "Press enter to add card (@ to tag)" else None)
#frame for went well cards
wentwell_cards_frame = tkinter.Frame(wentwell_frame, bg='light pink')
wentwell_cards_frame.pack(fill='both', expand=True)
#function to store cards stack
def store_wentwell(event):
    wwcard_text = wentwell_entry.get() #gets user input
    if wwcard_text.strip(): #if the entry field is empty
        
        


        card_id = str(uuid.uuid4()) #create unique ids for card
        card_comments[card_id] = [] #initialize comments list for this card
        #container to hold icon and card
        card_container = tkinter.Frame(wentwell_cards_frame, bg= 'light pink')
        card_container.pack(fill='x', padx=5, pady=2)
        #content
        content_frame = tkinter.Frame(card_container, bg='white', relief=tkinter.RIDGE, borderwidth=1)
        content_frame.pack(fill='x')
        #comment icon button container
        wwbutt_container = tkinter.Frame(content_frame, bg='white')
        wwbutt_container.pack(side='right')
        #comment pop up window container
        def open_wwcomment():
            wwcomment_container= tkinter.Toplevel(frame4, bg='beige')
            wwcomment_container.title(wwcard_text[:20] + 'comments')
            wwcomment_container.geometry('300x600')
            #my code frame for comments window
            framebgn = tkinter.Frame(wwcomment_container, bg='white')
            framebgn.pack(fill='x')
            #container for comments window
            container3 = tkinter.Frame(framebgn, bg='beige')
            container3.pack(fill='both', expand=True, padx=10, pady=10)
            #frame to display existing comments
            existing_comments_frame = tkinter.Frame(container3, bg='white')
            existing_comments_frame.pack(fill='both', expand=True, padx=5, pady=5)
            #label for existing comments
            tkinter.Label(existing_comments_frame,
                          text='Existing Comments:',
                          bg='white',
                          fg='black',
                          font=('Arial', 12, 'bold')).pack(anchor='w')
            comments_canvas = tkinter.Canvas(existing_comments_frame, bg='white')
            comments_canvas.pack(side='left', fill='both', expand=True)
            #scrollable canvas for comments, can store as much comments want user can view by scrolling
            scrollbar = tkinter.Scrollbar(existing_comments_frame, orient='vertical',
                                          command=comments_canvas.yview)
            scrollbar.pack(side='right', fill='y')
            comments_canvas.configure(yscrollcommand=scrollbar.set)
            #a frame to contain all comments inside canvas
            comments_frame = tkinter.Frame(comments_canvas, bg='white')
            comments_canvas.create_window((0, 0), window=comments_frame, anchor='nw')
            #function to display existing comments.
            def display_comments():
                for widget in comments_frame.winfo_children():
                    widget.destroy() #clears any existing widgets in comments
                #display each comment
                if card_id in card_comments and card_comments[card_id]:
                    for i, comment_text in enumerate(card_comments[card_id]):
                        comment_container = tkinter.Frame(comments_frame, bg='white',
                                                          bd=1, relief=tkinter.GROOVE)
                        comment_container.pack(fill='x', padx=5, pady=2, anchor='w')

                        #label for adding each comment
                        tkinter.Label(comment_container,
                                      text=f"Comment {i + 1}:",
                                      bg='white',
                                      fg='blue',
                                      font=('Arial', 10, 'bold')).pack(anchor='w')
                        pass
                        #label for comments text
                        tkinter.Label(comment_container,
                                      text=comment_text,
                                      bg='white',
                                      fg='black',
                                      font=('Arial', 10),
                                      wraplength=220,
                                      justify='left').pack(anchor='w', padx=5)
                        pass
                    else:
                        tkinter.Label(comments_frame,
                                      text="No comments yet.",
                                      bg='white',
                                      fg='gray',
                                      font=('Arial', 10, 'italic')).pack(pady=10)
                        pass
                    #update scroll region
                    comments_frame.update_idletasks()
                    comments_canvas.configure(scrollregion=comments_canvas.bbox('all'))
                    #update the comment count on button
                    update_comment_count()

                #call function to display



            # went well comment section frame
            cco_frame = tkinter.Frame(container3, bg='white', borderwidth=2, relief=tkinter.RIDGE)
            cco_frame.pack(side='left', fill='both', expand=True, padx=5)
            # went well label
            tkinter.Label(cco_frame,
                          text='comments', bg='white', fg='black', font=('Arial', 14, 'bold'),
                          pady=5).pack(fill='x')
            # went well entry field
            cc_entry = tkinter.Text(cco_frame,
                                     font=('Arial', 12),
                                     height = 4,
                                     relief=tkinter.SUNKEN, borderwidth=2)
            cc_entry.pack(fill='x', padx=5, pady=5)
            # went well entry binding
            cc_entry.insert("1.0", "add comments")
            cc_entry.bind("<FocusIn>", lambda e: cc_entry.delete("1.0", 'end')
            if cc_entry.get("1.0", "end-1c") == "add comments" else None)

            ccoo_frame = tkinter.Frame(cco_frame, bg='white')
            ccoo_frame.pack(fill='both', expand=True)

            # function to store cards stack
            def store_comm(event):
                comment_text = cc_entry.get("1.0", "end-1c").strip()  # gets user input
                if comment_text: # if the entry field is not empty
                    card_comments[card_id].append(comment_text)
                    cc_entry.delete("1.0", "end") #clear the entry
                    display_comments() #refresh the comment display
                    update_comment_count()# update comments count


             #save button for comment entry
            save_butt =  tkinter.Button(wwcomment_container, text='Save', command= lambda: store_comm(None))
            save_butt.pack(pady=10)
            display_comments()
           #binding entry
            cc_entry.bind("<Control-Return>", lambda event: store_comm())
            #close button for comments section
            close_button = tkinter.Button(wwcomment_container,
                                         text='Close', command=wwcomment_container.destroy)
            close_button.pack(pady=10)

        # function to update comment count on button
        def update_comment_count():
            comment_count = len(card_comments.get(card_id, []))
            if comment_count > 0:
                wwcomment_icon.config(text=f"💬 {comment_count}")
            else:
                wwcomment_icon.config(text="💬")

        #comment icon
        wwcomment_icon = tkinter.Button(wwbutt_container, text= '💬', bg='white', fg='blue'
                                        , font=('Arial', 12), command=open_wwcomment)
        wwcomment_icon.pack(side='right', padx=2, pady=2)
        #card label
        wwcard_label = tkinter.Label(content_frame, text = wwcard_text, bg= 'white',
                                        fg= 'black', font=('Arial', 12), wraplength= 200, justify='left',
                                        anchor='w', relief=tkinter.RIDGE)
        wwcard_label.pack(fill='x', padx=5, pady=2)
        wentwell_entry.delete(0, 'end')
#binding the went will card function with enter key.
wentwell_entry.bind("<Return>", store_wentwell)

#to improve comment section frame
to_improve_frame = tkinter.Frame(container2, bg='beige', borderwidth=2, relief=tkinter.RIDGE)
to_improve_frame.pack(side='left', fill='both', expand=True, padx=5)
#to improve label
tkinter.Label(to_improve_frame, text='To Improve', bg='beige', fg='black', font=('Arial', 14, 'bold'),
             pady=5).pack(fill='x')
#to improve entry field
to_improve_entry = tkinter.Entry(to_improve_frame, font=('Arial', 12), relief=tkinter.SUNKEN,
                               borderwidth=2)
to_improve_entry.pack(fill='x', padx=5, pady=5)
#to improve entry binding
to_improve_entry.insert(0, "Press enter to add card (@ to tag)")
to_improve_entry.bind("<FocusIn>", lambda e: to_improve_entry.delete(0, 'end')
if to_improve_entry.get() == "Press enter to add card (@ to tag)" else None)
#frame for to improve cards
toimprove_cards_frame = tkinter.Frame(to_improve_frame, bg='beige')
toimprove_cards_frame.pack(fill='both', expand=True)
#function to store cards stack
def store_toimprove(event):
    ticard_text = to_improve_entry.get() #gets user input
    if ticard_text.strip(): #if the entry field is empty
        ticard_id = str(uuid.uuid4()) #create unique ids for card
        ticard_comments[ticard_id] = [] #initialize comments list for this card
        #container to hold icon and card
        ticard_container = tkinter.Frame(toimprove_cards_frame, bg= 'beige')
        ticard_container.pack(fill='x', padx=5, pady=2)
        #content
        ticontent_frame = tkinter.Frame(ticard_container, bg='white', relief=tkinter.RIDGE, borderwidth=1)
        ticontent_frame.pack(fill='x')
        #comment icon button container
        tibutt_container = tkinter.Frame(ticontent_frame, bg='white')
        tibutt_container.pack(side='right')
        #comment pop up window container
        def open_ticomment():
            ticomment_container= tkinter.Toplevel(frame4, bg='beige')
            ticomment_container.title(ticard_text[:20] + 'comments')
            ticomment_container.geometry('300x600')
            #my code frame for comments window
            framebgn1 = tkinter.Frame(ticomment_container, bg='white')
            framebgn1.pack(fill='x')
            #container for comments window
            container4 = tkinter.Frame(framebgn1, bg='beige')
            container4.pack(fill='both', expand=True, padx=10, pady=10)
            #frame to display existing comments
            existing_comments_frame1 = tkinter.Frame(container4, bg='white') #is it necesary for every cards!!??? idk *cries*
            existing_comments_frame1.pack(fill='both', expand=True, padx=5, pady=5)
            #label for existing comments
            tkinter.Label(existing_comments_frame1,
                          text='Existing Comments:',
                          bg='white',
                          fg='black',
                          font=('Arial', 12, 'bold')).pack(anchor='w')
            comments1_canvas = tkinter.Canvas(existing_comments_frame1, bg='white')
            comments1_canvas.pack(side='left', fill='both', expand=True)
            #scrollable canvas for comments, can store as much comments want user can view by scrolling
            scrollbar1 = tkinter.Scrollbar(existing_comments_frame1, orient='vertical',
                                          command=comments1_canvas.yview)
            scrollbar1.pack(side='right', fill='y')
            comments1_canvas.configure(yscrollcommand=scrollbar1.set)
            #a frame to contain all comments inside canvas
            ticomments_frame = tkinter.Frame(comments1_canvas, bg='white')
            comments1_canvas.create_window((0, 0), window=ticomments_frame, anchor='nw')
            #function to display existing comments.
            def displayti_comments():
                for widget in ticomments_frame.winfo_children():
                    widget.destroy() #clears any existing widgets in comments
                #display each comment
                if ticard_id in ticard_comments and ticard_comments[ticard_id]:
                    for i, comment_text in enumerate(ticard_comments[ticard_id]):
                        ti_comment_container = tkinter.Frame(ticomments_frame, bg='white',
                                                          bd=1, relief=tkinter.GROOVE)
                        ti_comment_container.pack(fill='x', padx=5, pady=2, anchor='w')

                        #label for adding each comment
                        tkinter.Label(ti_comment_container,
                                      text=f"Comment {i + 1}:",
                                      bg='white',
                                      fg='blue',
                                      font=('Arial', 10, 'bold')).pack(anchor='w')
                        pass
                        #label for comments text
                        tkinter.Label(ti_comment_container,
                                      text=comment_text,
                                      bg='white',
                                      fg='black',
                                      font=('Arial', 10),
                                      wraplength=220,
                                      justify='left').pack(anchor='w', padx=5)
                        pass
                    else:
                        tkinter.Label(ticomments_frame,
                                      text="No comments yet.",
                                      bg='white',
                                      fg='gray',
                                      font=('Arial', 10, 'italic')).pack(pady=10)
                        pass
                    #update scroll region
                    ticomments_frame.update_idletasks()
                    comments1_canvas.configure(scrollregion=comments1_canvas.bbox('all'))
                    #update the comment count on button
                    update_ticomment_count()

                #call function to display



            # to improve comment section frame
            ticco_frame = tkinter.Frame(container4, bg='white', borderwidth=2, relief=tkinter.RIDGE)
            ticco_frame.pack(side='left', fill='both', expand=True, padx=5)
            # to improve label
            tkinter.Label(ticco_frame,
                          text='comments', bg='white', fg='black', font=('Arial', 14, 'bold'),
                          pady=5).pack(fill='x')
            # to improve entry field
            ticc_entry = tkinter.Text(ticco_frame,
                                     font=('Arial', 12),
                                     height = 4,
                                     relief=tkinter.SUNKEN, borderwidth=2)
            ticc_entry.pack(fill='x', padx=5, pady=5)
            # to improve entry binding
            ticc_entry.insert("1.0", "add comments")
            ticc_entry.bind("<FocusIn>", lambda e: ticc_entry.delete("1.0", 'end')
            if ticc_entry.get("1.0", "end-1c") == "add comments" else None)

            ticcoo_frame = tkinter.Frame(ticco_frame, bg='white')
            ticcoo_frame.pack(fill='both', expand=True)

            # function to store cards stack
            def store_ticomm(event):
                ti_comment_text = ticc_entry.get("1.0", "end-1c").strip()  # gets user input
                if ti_comment_text: # if the entry field is not empty
                    ticard_comments[ticard_id].append(ti_comment_text)
                    ticc_entry.delete("1.0", "end") #clear the entry
                    displayti_comments() #refresh the comment display
                    update_ticomment_count()# update comments count


             #save button for comment entry
            tisave_butt =  tkinter.Button(ticomment_container, text='Save', command= lambda: store_ticomm(None))
            tisave_butt.pack(pady=10)
            displayti_comments()
           #binding entry
            ticc_entry.bind("<Control-Return>", lambda event: store_ticomm())
            #close button for comments section
            ti_close_button = tkinter.Button(ticomment_container,
                                         text='Close', command=ticomment_container.destroy)
            ti_close_button.pack(pady=10)

        # function to update comment count on button
        def update_ticomment_count():
            ticomment_count = len(ticard_comments.get(ticard_id, []))
            if ticomment_count > 0:
                ticomment_icon.config(text=f"💬 {ticomment_count}")
            else:
                ticomment_icon.config(text="💬")

        #comment icon
        ticomment_icon = tkinter.Button(tibutt_container, text= '💬', bg='white', fg='blue'
                                        , font=('Arial', 12), command=open_ticomment)
        ticomment_icon.pack(side='right', padx=2, pady=2)
        #card label
        ticard_label = tkinter.Label(ticontent_frame, text = ticard_text, bg= 'white',
                                        fg= 'black', font=('Arial', 12), wraplength= 200, justify='left',
                                        anchor='w', relief=tkinter.RIDGE)
        ticard_label.pack(fill='x', padx=5, pady=2)
        to_improve_entry.delete(0, 'end')
#binding the went will card function with enter key.
to_improve_entry.bind("<Return>", store_toimprove)

#action items comment section frame
actionitems_frame = tkinter.Frame(container2, bg='blue', borderwidth=2, relief=tkinter.RIDGE)
actionitems_frame.pack(side='left', fill='both', expand=True, padx=5)
#action items label
tkinter.Label(actionitems_frame, text='Action items', bg='blue', fg='black', font=('Arial', 14, 'bold'),
             pady=5).pack(fill='x')
#action items entry field
actionitems_entry = tkinter.Entry(actionitems_frame, font=('Arial', 12), relief=tkinter.SUNKEN,
                               borderwidth=2)
actionitems_entry.pack(fill='x', padx=5, pady=5)

#action items entry binding
actionitems_entry.insert(0, "Press enter to add card (@ to tag)")
actionitems_entry.bind("<FocusIn>", lambda e: actionitems_entry.delete(0, 'end')
if actionitems_entry.get() == "Press enter to add card (@ to tag)" else None)
#frame for action item cards
actionitems_cards_frame = tkinter.Frame(actionitems_frame, bg='blue')
actionitems_cards_frame.pack(fill='both', expand=True)
#function to store cards stack
def store_actionitems(event):
    aicard_text = actionitems_entry.get() #gets user input
    if aicard_text.strip(): #if the entry field is empty
        aicard_id = str(uuid.uuid4()) #create unique ids for card
        aicard_comments[aicard_id] = [] #initialize comments list for this card
        #container to hold icon and card
        aicard_container = tkinter.Frame(actionitems_cards_frame, bg= 'blue')
        aicard_container.pack(fill='x', padx=5, pady=2)
        #content
        aicontent_frame = tkinter.Frame(aicard_container, bg='white', relief=tkinter.RIDGE, borderwidth=1)
        aicontent_frame.pack(fill='x')
        #comment icon button container
        aibutt_container = tkinter.Frame(aicontent_frame, bg='white')
        aibutt_container.pack(side='right')
        #comment pop up window container
        def open_aicomment():
            aicomment_container= tkinter.Toplevel(frame4, bg='beige')
            aicomment_container.title(aicard_text[:20] + 'comments')
            aicomment_container.geometry('300x600')
            #my code frame for comments window
            framebgn2 = tkinter.Frame(aicomment_container, bg='white')
            framebgn2.pack(fill='x')
            #container for comments window
            container5 = tkinter.Frame(framebgn2, bg='beige')
            container5.pack(fill='both', expand=True, padx=10, pady=10)
            #frame to display existing comments
            existing_comments_frame2 = tkinter.Frame(container5, bg='white')
            existing_comments_frame2.pack(fill='both', expand=True, padx=5, pady=5)
            #label for existing comments
            tkinter.Label(existing_comments_frame2,
                          text='Existing Comments:',
                          bg='white',
                          fg='black',
                          font=('Arial', 12, 'bold')).pack(anchor='w')
            aicomments_canvas = tkinter.Canvas(existing_comments_frame2, bg='white')
            aicomments_canvas.pack(side='left', fill='both', expand=True)
            #scrollable canvas for comments, can store as much comments want user can view by scrolling
            aiscrollbar = tkinter.Scrollbar(existing_comments_frame2, orient='vertical',
                                          command=aicomments_canvas.yview)
            aiscrollbar.pack(side='right', fill='y')
            aicomments_canvas.configure(yscrollcommand=aiscrollbar.set)
            #a frame to contain all comments inside canvas
            ai_comments_frame = tkinter.Frame(aicomments_canvas, bg='white')
            aicomments_canvas.create_window((0, 0), window=ai_comments_frame, anchor='nw')
            #function to display existing comments.
            def display_aicomments():
                for widget in ai_comments_frame.winfo_children():
                    widget.destroy() #clears any existing widgets in comments
                #display each comment
                if aicard_id in aicard_comments and aicard_comments[aicard_id]:
                    for i, comment_text in enumerate(aicard_comments[aicard_id]):
                        aicomment_container = tkinter.Frame(ai_comments_frame, bg='white',
                                                          bd=1, relief=tkinter.GROOVE)
                        aicomment_container.pack(fill='x', padx=5, pady=2, anchor='w')

                        #label for adding each comment
                        tkinter.Label(aicomment_container,
                                      text=f"Comment {i + 1}:",
                                      bg='white',
                                      fg='blue',
                                      font=('Arial', 10, 'bold')).pack(anchor='w')
                        pass
                        #label for comments text
                        tkinter.Label(aicomment_container,
                                      text=comment_text,
                                      bg='white',
                                      fg='black',
                                      font=('Arial', 10),
                                      wraplength=220,
                                      justify='left').pack(anchor='w', padx=5)
                        pass
                    else:
                        tkinter.Label(ai_comments_frame,
                                      text="No comments yet.",
                                      bg='white',
                                      fg='gray',
                                      font=('Arial', 10, 'italic')).pack(pady=10)
                        pass
                    #update scroll region
                    ai_comments_frame.update_idletasks()
                    aicomments_canvas.configure(scrollregion=aicomments_canvas.bbox('all'))
                    #update the comment count on button
                    update_aicomment_count()

                #call function to display



            # action item comment section frame
            aicco_frame = tkinter.Frame(container5, bg='white', borderwidth=2, relief=tkinter.RIDGE)
            aicco_frame.pack(side='left', fill='both', expand=True, padx=5)
            # action item label
            tkinter.Label(aicco_frame,
                          text='comments', bg='white', fg='black', font=('Arial', 14, 'bold'),
                          pady=5).pack(fill='x')
            # action item entry field
            ai_cc_entry = tkinter.Text(aicco_frame,
                                     font=('Arial', 12),
                                     height = 4,
                                     relief=tkinter.SUNKEN, borderwidth=2)
            ai_cc_entry.pack(fill='x', padx=5, pady=5)
            # action item entry binding
            ai_cc_entry.insert("1.0", "add comments")
            ai_cc_entry.bind("<FocusIn>", lambda e: ai_cc_entry.delete("1.0", 'end')
            if ai_cc_entry.get("1.0", "end-1c") == "add comments" else None)

            ai_ccoo_frame = tkinter.Frame(aicco_frame, bg='white')
            ai_ccoo_frame.pack(fill='both', expand=True)

            # function to store cards stack
            def store_aicomm(event):
                aicomment_text = ai_cc_entry.get("1.0", "end-1c").strip()  # gets user input
                if aicomment_text: # if the entry field is not empty
                    aicard_comments[aicard_id].append(aicomment_text)
                    ai_cc_entry.delete("1.0", "end") #clear the entry
                    display_aicomments() #refresh the comment display
                    update_aicomment_count()# update comments count


             #save button for comment entry
            aisave_butt =  tkinter.Button(aicomment_container, text='Save', command= lambda: store_aicomm(None))
            aisave_butt.pack(pady=10)
            display_aicomments()
           #binding entry
            ai_cc_entry.bind("<Control-Return>", lambda event: store_aicomm())
            #close button for comments section
            aiclose_button = tkinter.Button(aicomment_container,
                                         text='Close', command=aicomment_container.destroy)
            aiclose_button.pack(pady=10)

        # function to update comment count on button
        def update_aicomment_count():
            aicomment_count = len(aicard_comments.get(aicard_id, []))
            if aicomment_count > 0:
                aicomment_icon.config(text=f"💬 {aicomment_count}")
            else:
                aicomment_icon.config(text="💬")

        #comment icon
        aicomment_icon = tkinter.Button(aibutt_container, text= '💬', bg='white', fg='blue'
                                        , font=('Arial', 12), command=open_aicomment)
        aicomment_icon.pack(side='right', padx=2, pady=2)
        #card label
        aicard_label = tkinter.Label(aicontent_frame, text = aicard_text, bg= 'white',
                                        fg= 'black', font=('Arial', 12), wraplength= 200, justify='left',
                                        anchor='w', relief=tkinter.RIDGE)
        aicard_label.pack(fill='x', padx=5, pady=2)
        actionitems_entry.delete(0, 'end')
#binding the went will card function with enter key.
actionitems_entry.bind("<Return>", store_actionitems)

#back button for page 4
tkinter.Button(frame4, bg='black', fg='white', text= 'BACK',
               command=lambda :frame3.tkraise()).pack(padx=10, pady=20)
#first button for page 1 to create new board
main_butt = tkinter.Button(frame1, bg= 'Blue',
                           fg= 'white',
                           text= 'Create new \n board\n+',
                           font= ('Times New Roman', 14),
                           relief= tkinter.RAISED,
                           borderwidth= 3,
                           command=lambda: frame2.tkraise())
main_butt.pack(padx= 100, pady= 200)

frame1.tkraise()

root.mainloop()
