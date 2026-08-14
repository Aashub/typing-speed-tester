from tkinter import *

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 600
WORD_INDEX = 0
word_fill_index = 0
fg_color_index = 0

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


    # ********************************************** TYPING TEST SCREEN ************************************************

    def add_typing_test_screen(self):
        """this method add background image in home screen"""

        # add home screen image
        self.img = PhotoImage(file="img/bg.png")
        image_label = Label(self, image=self.img)
        image_label.pack()


    # ******************************************** ADD TYPING TEXT AREA ************************************************

    def check_typing_text(self, typing_text):
        """this method add heading text in home screen"""

        self.display_text = Text(self, font=("Arial", 16, "bold"),fg = "black",  height=13, width=60, wrap="word")
        self.display_text.insert("1.0", typing_text)
        self.display_text.place(x = 180, y = 120)

        self.typing_text_list_length = len(typing_text)

    def check_retrieved_text(self, event):

        global WORD_INDEX, word_fill_index, fg_color_index

        text_input = self.entered_text_input.get("1.0", "end-1c")
        display_text_string = self.display_text.get("1.0", "end-1c")

        if event.keysym in ("Shift_L"):
            return

        fg_color = self.get_foreground_at_index(self.display_text, f"1.{fg_color_index}")
        for char_index, (display_char, input_char) in enumerate(zip(display_text_string, text_input)):


            if fg_color == "black":
                tag_name = f"char_{char_index}"  # unique tag per position

                if display_text_string[char_index] == input_char:
                    self.display_text.tag_config(tag_name, foreground="green")
                    fg_color_index += 1

                elif display_text_string[char_index] != input_char:
                    self.display_text.tag_config(tag_name, foreground="red")
                    fg_color_index += 1

                self.display_text.tag_add(tag_name, f"1.{char_index}")

            else:
                pass

        # if len(display_text_list[WORD_INDEX]) == word_fill_index:
        #
        #     if event.keysym in ("Return"):
        #
        #         print("complete")
        #
        #         WORD_INDEX += 1
        #         word_fill_index = 0
        #
        #         print(WORD_INDEX, word_fill_index)

    def get_foreground_at_index(self, text_widget, index):

        tags_at_index = text_widget.tag_names(index)

        for tag in tags_at_index:
            fg_color = text_widget.tag_cget(tag, "foreground")
            if fg_color:
                return fg_color

        # 3. Fallback to the text widget's global default foreground configuration
        return text_widget.cget("foreground")

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

        # entry field
        self.entered_text_input = Text(self, font=("Arial", 30), width=10, height=1,  relief="flat")
        self.entered_text_input.place(x=440, y=70)

