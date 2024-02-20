import tkinter as tk


class MainWindow:
    def __init__(self):
        # Initialize window
        self.root = tk.Tk()
        self.root.title("InOut")
        self.root.geometry("920x540")

        self.draw("Welcome to InOut!")

        self.buttons()

        # Main Ui Loop
        self.root.mainloop()

    def draw(self, msg):
        self.text_box = tk.Text(height=10, width=50)
        self.text_box.insert(1.0, msg)
        self.text_box.grid(row=0, column=0)
        # self.text_box.pack()

    def buttons(self):
        self.frame = tk.Frame(self.root, height=1, width=50)
        self.frame.grid(row=0, column=1)
        self.entry = tk.Entry(self.frame, font=12)

        self.cal_budget = tk.Button(
            self.frame,
            text="Calculate Budget",
            width=20,
        )

        self.view_budget = tk.Button(
            self.frame,
            text="View Budget Plan",
            width=20,
        )

        self.view_spending = tk.Button(
            self.frame,
            text="View Spending Budget",
            width=20,
        )

        items = [self.entry, self.cal_budget, self.view_budget, self.view_spending]
        for item in items:
            item.pack()


if __name__ == "__main__":
    main_window = MainWindow()
