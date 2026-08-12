from tkinter import *



WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 600


class UserInterface(Tk):

    def __init__(self):

        super().__init__()

        # this will set the game window center to the screen.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
        center_y = int((screen_height / 2) - (WINDOW_HEIGHT / 2))

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")
        self.resizable(False, False)
        self.title("typing-speed-tester")


        self.add_typing_test_screen()


    # ********************************************** TYPING TEST SCREEN ************************************************

    def add_typing_test_screen(self):
        """this method add background image in home screen"""

        # add home screen image
        img = PhotoImage(file="img/bg.png")
        image_label = Label(self, image=img)
        image_label.pack()

        self.typinig_text_canvas()
        self.all_widget_button()
        self.mainloop()

    # ******************************************** ADD TYPING TEXT AREA ************************************************

    def typinig_text_canvas(self):
        """this method add heading text in home screen"""

        # typing text canvas
        typing_text_canvas = Canvas(width=700, height=300, bg="#242424", highlightthickness=0)
        typing_text_canvas.place(x=190, y=120)



    # ************************************************ WIDGET  BUTTON **************************************************

    def all_widget_button(self):

        # reset button
        reset_btn = Button(self, text="⭮", font=("Arial", 25, "bold"), fg="gray",
                                      bd=0, bg="#242424", height=1, width=3)
        reset_btn.place(x=510, y=450)

        # Create a shared Tkinter variable
        selected_option = StringVar(self, value="Option 1")

        #  Create the Radiobutton widgets
        easy_radio_btn = Radiobutton(self, text="Easy", variable=selected_option, value="Option 1",
                             bg="#242424", fg="#FFC000", font=("Arial"),
                             activebackground="#242424",
                             activeforeground="white", selectcolor="#242424",
                             )

        normal_radio_btn = Radiobutton(self, text="Normal", variable=selected_option, value="Option 2",
                             bg="#242424", fg="#FFC000", font=("Arial",),
                             activebackground="#242424",
                             activeforeground="white", selectcolor="#242424",
                             )

        hard_radio_btn = Radiobutton(self, text="Hard", variable=selected_option,
                             value="Option 3",
                             bg="#242424", fg="#FFC000", font=("Arial"),
                             activebackground="#242424",
                             activeforeground="white", selectcolor="#242424",
                             )


        # 3. Display the radio button on the screen
        easy_radio_btn.place(x=200, y=470)
        normal_radio_btn.place(x=300, y=470)
        hard_radio_btn.place(x=410, y=470)


        #  Create the Radiobutton widgets
        second_60_btn = Radiobutton(self, text="60", variable=selected_option, value="Option 1",
                             bg="#242424", fg="#FFC000", font=("Arial"),
                             activebackground="#242424",
                             activeforeground="white", selectcolor="#242424",
                             )

        second_120_btn = Radiobutton(self, text="120", variable=selected_option, value="Option 2",
                             bg="#242424", fg="#FFC000", font=("Arial",),
                             activebackground="#242424",
                             activeforeground="white", selectcolor="#242424",
                             )

        second_180_btn = Radiobutton(self, text="180", variable=selected_option,
                             value="Option 3",
                             bg="#242424", fg="#FFC000", font=("Arial"),
                             activebackground="#242424",
                             activeforeground="white", selectcolor="#242424",
                             )


        # 3. Display the radio button on the screen
        second_60_btn.place(x=620, y=470)
        second_120_btn.place(x=715, y=470)
        second_180_btn.place(x=820, y=470)


app_window = UserInterface()