#!/usr/bin/env python3
"""Convert Fahrenheit temperature to Celsius (GUI)."""
import tkinter


class DegreesConvertGUI:
    """Main class of GUI window."""

    def __init__(self):
        """Create main window."""
        self.main_window = tkinter.Tk()
        self.main_window.title("Fahrenheit to Celsius")

        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Top Frame
        self.prompt_label = tkinter.Label(
            self.top_frame, text="Enter a value (\u00b0F): "
        )
        self.fahr_entry = tkinter.Entry(self.top_frame, width=7)
        self.prompt_label.pack(side="left")
        self.fahr_entry.pack(side="left")

        # Middle Frame
        self.result_label = tkinter.Label(
            self.middle_frame, text="\u00b0F is equal to \u00b0C: "
        )
        self.value = tkinter.StringVar()
        self.cels_label = tkinter.Label(
            self.middle_frame, textvariable=self.value
        )
        self.result_label.pack(side="left")
        self.cels_label.pack(side="left")

        # Bottom Frame
        self.convert_button = tkinter.Button(
            self.bottom_frame, text="Convert", command=self.convert
        )
        self.quit_button = tkinter.Button(
            self.bottom_frame, text="Quit", command=self.main_window.destroy
        )
        self.convert_button.pack(side="left", padx=(0, 10))
        self.quit_button.pack(side="left", padx=(10, 0))

        self.top_frame.pack(padx=20, pady=(20, 10))
        self.middle_frame.pack(padx=20, pady=10)
        self.bottom_frame.pack(padx=20, pady=(10, 20))

        tkinter.mainloop()

    def convert(self):
        """Convert Fahrenheit temperature to Celsius."""
        fahr = float(self.fahr_entry.get())
        cels = str(round(((fahr - 32) / 1.8), 2))

        self.value.set(cels)


if __name__ == "__main__":
    f_2_c = DegreesConvertGUI()
