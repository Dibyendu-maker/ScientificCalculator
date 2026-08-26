import customtkinter as ctk


class CalculatorGUI:

    def __init__(self, root):

        self.root = root

        self.root.title("Scientific Calculator")

        # Square window
        self.root.geometry("900x900")

        self.root.minsize(700, 700)

        # Display
        self.display = ctk.CTkEntry(
            self.root,
            width=800,
            height=60,
            font=("Arial", 28),
            justify="right"
        )

        self.display.pack(pady=20)

        # Button Frame
        self.button_frame = ctk.CTkFrame(self.root)

        self.button_frame.pack(expand=True, fill="both", padx=20, pady=20)

        self.create_buttons()

    def create_buttons(self):

        buttons = [

            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for r, row in enumerate(buttons):

            self.button_frame.grid_rowconfigure(r, weight=1)

            for c, text in enumerate(row):

                self.button_frame.grid_columnconfigure(c, weight=1)

                btn = ctk.CTkButton(

                    self.button_frame,

                    text=text,

                    font=("Arial", 22),

                    height=70,

                    corner_radius=12,

                    command=lambda t=text: self.button_clicked(t)

                )

                btn.grid(

                    row=r,

                    column=c,

                    padx=10,

                    pady=10,

                    sticky="nsew"

                )

    def button_clicked(self, value):

        if value == "=":

            try:

                result = str(eval(self.display.get()))

                self.display.delete(0, "end")

                self.display.insert(0, result)

            except:

                self.display.delete(0, "end")

                self.display.insert(0, "Error")

        else:

            self.display.insert("end", value)