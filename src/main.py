import tkinter as tk
# import customtkinter as ctk

class MainWindow:
    def __init__(self):
        # Initialize window
        self.root = tk.Tk()
        self.root.geometry("920x540")
        self.root.title("InOut")
        self.style = ("Monospace", 18)
        self.draw("Welcome to InOut!")

        self.buttons()

        # Main Ui Loop
        self.root.mainloop()

    def draw(self, msg):
        self.frame_text = tk.Frame(self.root, height=20, width=50)
        self.text_box = tk.Text(
            self.frame_text,
            height=19,
            width=50,
            relief="flat",
            bg="light yellow",
            font=self.style,
        )
        self.text_box.insert(1.0, msg)
        self.text_box.config(state="disabled")
        self.frame_text.grid(row=0, column=0)
        self.text_box.pack(padx=5, pady=5)

    def buttons(self):
        self.frame_button = tk.Frame(self.root, height=1, width=50)
        self.frame_button.grid(row=0, column=1)
        self.label = tk.Label(self.frame_button, text="Your Budget:")

        self.entry = tk.Entry(self.frame_button, font=12)

        self.cal_budget = tk.Button(
            self.frame_button,
            text="Calculate Budget",
            command=self.calculate_budget,
            width=20,
        )

        self.view_budget = tk.Button(
            self.frame_button,
            text="View Budget Plan",
            command=self.view_budget_plan,
            width=20,
        )

        self.view_spending = tk.Button(
            self.frame_button,
            text="View Spending Budget",
            command=self.pop_up,
            width=20,
        )

        items = [
            self.label,
            self.entry,
            self.cal_budget,
            self.view_budget,
            self.view_spending,
        ]
        for item in items:
            item.pack(padx=5, pady=5)

    def pop_up(self):
        self.pop_up = tk.Tk()
        self.pop_up.geometry("300x200")
        self.pop_up.title("Rent & Bills")
        self.pop_up.resizable(False, False)
        self.rent_label = tk.Label(self.pop_up, text="Rent: ")
        self.rent_entry = tk.Entry(self.pop_up, width=25)
        self.bills_label = tk.Label(self.pop_up, text="Monthly Bills: ")
        self.bills_entry = tk.Entry(self.pop_up, width=25)
        self.done = tk.Button(self.pop_up, text="Done", command=self.calculate_spending)
        items = [
            self.rent_label,
            self.rent_entry,
            self.bills_label,
            self.bills_entry,
            self.done,
        ]
        for item in items:
            item.pack(padx=5, pady=5)

    def calculate_budget(self):
        self.budget = float(self.entry.get() or 0)
        self.speding = self.budget * 0.5
        self.draw(
            f"Total Budget\t\t: €{self.budget:.2f} \nSpending Budget\t\t: €{self.speding:.2f}"
        )

    def view_budget_plan(self):
        self.budget = float(self.entry.get() or 0)
        self.spending = self.budget * 0.5
        self.savings = self.budget * 0.3
        self.extra = self.budget - self.spending - self.savings
        self.draw(
            f"Total Budget\t\t: ${'{:.2f}'.format(self.budget)}\nSpending Money\t\t: ${'{:.2f}'.format(self.spending)} \
            \nTo Save\t\t: ${'{:.2f}'.format(self.savings)}\nExtra\t\t: ${'{:.2f}'.format(self.extra)}"
        )

    def calculate_spending(self):
        self.rent = float(self.rent_entry.get() or 0)
        self.bills = float(self.bills_entry.get() or 0)
        self.pop_up.destroy()
        self.budget = float(self.entry.get() or 0)
        self.food = (self.budget * 0.5) - self.rent - self.bills
        self.draw(f"### TOTAL BUDGET ###\nTotal\t\t: ${'{:.2f}'.format(self.budget)}\nSpending Money\t\t: ${'{:.2f}'.format(self.budget*0.5)} \
            \n\n### EXPENSES ###\nRent\t\t: ${'{:.2f}'.format(self.rent)}\nBills\t\t: ${'{:.2f}'.format(self.bills)}\nFood\t\t: ${'{:.2f}'.format(self.food)}")

if __name__ == "__main__":
    main_window = MainWindow()
