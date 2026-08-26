"""
Scientific Calculator
Version : 1.0

Main Entry Point
"""

import customtkinter as ctk
from gui import CalculatorGUI


def main():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()

    app = CalculatorGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()