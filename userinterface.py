from tkinter import *
from tkinter.font import Font


WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 600

TEXT_COLOR = "#666666"
BACKGROUND_COLOR = "#1E1E1E"
BUTTON_COLOR = "#FFC000"

WORD_INDEX = 0
word_fill_index = 0
fg_color_index = 0
TIMER = None


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
        self.app_font = Font(family="Segoe UI", size=16, slant="italic")

    # ********************************************** TYPING TEST SCREEN ************************************************

    def add_typing_test_screen(self):
        """this method add background image in home screen"""

        # add home screen image
        self.img = PhotoImage(file="img/bg.png")
        image_label = Label(self, image=self.img)
        image_label.pack()

    # ************************************************ WIDGET  BUTTON **************************************************

    def all_widget_button(self):

        # reset button
        reset_btn = Button(self, text="⭮", font=("Arial", 25, "bold"), fg=BUTTON_COLOR,
                           bd=0, bg=BACKGROUND_COLOR, height=1, width=3)
        reset_btn.place(x=510, y=450)

        # Create a shared Tkinter variable
        selected_option = StringVar(self, value="Option 1")

        #  Create the Radiobutton widgets
        easy_radio_btn = Radiobutton(self, text="Easy", variable=selected_option, value="Option 1",
                                     bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial"),
                                     activebackground=BACKGROUND_COLOR,
                                     activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                     )

        normal_radio_btn = Radiobutton(self, text="Normal", variable=selected_option, value="Option 2",
                                       bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial",),
                                       activebackground=BACKGROUND_COLOR,
                                       activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                       )

        hard_radio_btn = Radiobutton(self, text="Hard", variable=selected_option,
                                     value="Option 3",
                                     bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial"),
                                     activebackground=BACKGROUND_COLOR,
                                     activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                     )

        # 3. Display the radio button on the screen
        easy_radio_btn.place(x=200, y=470)
        normal_radio_btn.place(x=300, y=470)
        hard_radio_btn.place(x=410, y=470)

        #  Create the Radiobutton widgets
        second_60_btn = Radiobutton(self, text="60", variable=selected_option, value="Option 1",
                                    bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial"),
                                    activebackground=BACKGROUND_COLOR,
                                    activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                    command=lambda: self.timer_countdown(60, "60_seconds")
                                    )

        second_120_btn = Radiobutton(self, text="120", variable=selected_option, value="Option 2",
                                     bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial",),
                                     activebackground=BACKGROUND_COLOR,
                                     activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                     command=lambda: self.timer_countdown(120, "120_seconds")
                                     )

        second_180_btn = Radiobutton(self, text="180", variable=selected_option,
                                     value="Option 3",
                                     bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial"),
                                     activebackground=BACKGROUND_COLOR,
                                     activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                     command=lambda: self.timer_countdown(180, "180_seconds")
                                     )

        # 3. Display the radio button on the screen
        second_60_btn.place(x=620, y=470)
        second_120_btn.place(x=715, y=470)
        second_180_btn.place(x=820, y=470)

        # entry field
        self.entered_text_input = Text(self, font=("Arial", 30), width=10, height=1, relief="flat")
        self.entered_text_input.place(x=440, y=-50)
        self.entered_text_input.focus_set()

        # timer label
        seconds_left = None
        self.timier_text = Label(self, text=f"{seconds_left}", font=("Arial", 30), relief="flat", bg=BACKGROUND_COLOR,
                                 fg=BUTTON_COLOR)

    # ******************************************** ADD TYPING TEXT AREA ************************************************

    def check_typing_text(self, typing_text):
        """this method add typing text on screen so that user can start typing."""

        self.display_text = Text(self, font=self.app_font, fg=TEXT_COLOR, height=10, width=70, wrap="word",
                                 bg=BACKGROUND_COLOR, bd=0, pady=15, padx=15)
        self.display_text.insert("1.0", typing_text)
        self.display_text.place(x=145, y=120)

    def check_retrieved_text(self, event):
        """this method will check user entered text vs typing text and highlight character with white color if correct and red if wrong character"""

        global fg_color_index

        # gets text input and gets display typing text display text.
        text_input = self.entered_text_input.get("1.0", "end-1c")
        display_text_string = self.display_text.get("1.0", "end-1c")

        # ignores the shift Left side btn while using
        if event.keysym in ("Shift_L"):
            return

        # this method will give the current text color so that it will update the text color if not filled gives white color, if filled with red & white color than gives red & white color
        fg_color = self.get_foreground_at_index(self.display_text, f"1.{fg_color_index}")

        # this for loop checks the user input char and typing text char and change color based on match and mismatch.
        for char_index, (display_char, input_char) in enumerate(zip(display_text_string, text_input)):

            if fg_color == TEXT_COLOR:
                tag_name = f"char_{char_index}"  # unique tag per position

                if display_text_string[char_index] == input_char:
                    self.display_text.tag_config(tag_name, foreground="white")
                    fg_color_index += 1

                elif display_text_string[char_index] != input_char:
                    self.display_text.tag_config(tag_name, foreground="red")
                    fg_color_index += 1

                self.display_text.tag_add(tag_name, f"1.{char_index}")

            else:
                pass

    def get_foreground_at_index(self, text_widget, index):
        """this method will give us the current text character of typing text, text color for checking."""

        tags_at_index = text_widget.tag_names(index)

        for tag in tags_at_index:
            fg_color = text_widget.tag_cget(tag, "foreground")
            if fg_color:
                return fg_color

        # 3. Fallback to the text widget's global default foreground configuration
        return text_widget.cget("foreground")

    # ************************************************ WIDGET  BUTTON **************************************************

    def timer_countdown(self, seconds_left, selected_timer_option):

        global TIMER,count_second
        self.timier_text.config(text = seconds_left)
        self.timier_text.place(x=510, y=70)


        if selected_timer_option == "60_seconds":
            count_second = seconds_left % 60
        elif selected_timer_option == "120_seconds":
            count_second = seconds_left % 120
        elif selected_timer_option == "180_seconds":
            count_second = seconds_left % 180


        # this if statement will help in bypassing the issue of when seconds are left less than 10 so it will show then as an 09 08 and so on
        if count_second == 0:

            count_second = seconds_left
            if count_second == 0:
                self.timier_text.place_forget()
                return

        elif count_second < 10:
            count_second = f"0{count_second}"

        self.timier_text.config(text=f"{count_second}")

        # if seconds will be greater than 0 than .after() method will call the time_countdown function again & also subtract the second each second.
        if seconds_left > 0:
            global timer
            timer = self.after(300, self.timer_countdown, seconds_left - 1, selected_timer_option)





