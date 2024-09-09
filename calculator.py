import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x600")
        self.window.resizable(0, 0)
        self.window.title("task-1 Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.total_label, self.label = self.create_display_labels(self.create_display_frame())
        self.digits = {
            7: (3, 1), 8: (3, 2), 9: (3, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (1, 1), 2: (1, 2), 3: (1, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "/", "*": "*", "-": "-", "+": "+"}
        self.create_buttons()
        self.bind_keys()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg="#F5F5F5")
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self, frame):
        total_label = tk.Label(frame, text=self.total_expression, anchor=tk.E, bg="#F5F5F5", fg="#25265E", padx=0, font=("Arial", 16))
        total_label.pack(expand=True, fill='both')
        label = tk.Label(frame, text=self.current_expression, anchor=tk.E, bg="#F5F5F5", fg="#25265E", padx=0, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill='both')
        return total_label, label

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except:
            self.current_expression = "Error"
        self.update_label()

    def button(self, text, row, col, command, colspan=1):
        buttons = tk.Button(self.buttons_frame, text=text, bg="#F8FAFF", fg="#25265E", font=("Arial", 20), borderwidth=0, command=command)
        buttons.grid(row=row, column=col, columnspan=colspan, sticky=tk.NSEW)

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            self.button(str(digit), grid_value[0], grid_value[1], lambda x=digit: self.add_to_expression(x))

    def create_operator_buttons(self):
        for i, (operator, symbol) in enumerate(self.operations.items()):
            self.button(symbol, i, 4, lambda x=operator: self.append_operator(x))

    def create_buttons(self):
        self.buttons_frame = self.create_buttons_frame()
        for i in range(1,5):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.button("C", 0, 1, self.clear)
        self.button("(", 0, 2, lambda: self.add_to_expression('('))
        self.button(")", 0, 3, lambda: self.add_to_expression(')'))
        self.button("=", 4, 3, self.evaluate, colspan=2)
        

    def clear(self):
        self.total_expression, self.current_expression = "", ""
        self.update_total_label()
        self.update_label()

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
