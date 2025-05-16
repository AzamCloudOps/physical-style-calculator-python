import customtkinter as ctk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.expression = ""

        self.display = ctk.CTkEntry(root, height=80, width=500, font=("Segoe UI", 32),
                                    justify='right', corner_radius=10, border_width=2)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5, padx=20, pady=(20, 10), sticky="nsew")

        buttons = [
            ('π', 1, 0),  ('^', 1, 1),  ('√', 1, 2),  ('C', 1, 3),   ('mod', 1, 4),
            ('7', 2, 0),  ('8', 2, 1),  ('9', 2, 2),  ('/', 2, 3),   ('%', 2, 4),
            ('4', 3, 0),  ('5', 3, 1),  ('6', 3, 2),  ('*', 3, 3),   ('(', 3, 4),
            ('1', 4, 0),  ('2', 4, 1),  ('3', 4, 2),  ('-', 4, 3),   (')', 4, 4),
            ('0', 5, 0),  ('.', 5, 1),  ('+', 5, 2),  ('=', 5, 3, 1, 2)
        ]

        for btn in buttons:
            text, row, col = btn[0], btn[1], btn[2]
            rowspan = btn[3] if len(btn) > 3 else 1
            colspan = btn[4] if len(btn) > 4 else 1
            self.create_button(text, row, col, rowspan, colspan)

        # Grid config
        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for j in range(5):
            self.root.columnconfigure(j, weight=1)

    def create_button(self, text, row, col, rowspan=1, colspan=1):
        colors = {
            'C': ("#ff4d4d", "white"),
            '=': ("#00c853", "white"),
            '^': ("#2196f3", "white"),
            'mod': ("#2196f3", "white"),
            '%': ("#2196f3", "white"),
            '/': ("#2196f3", "white"),
            '*': ("#2196f3", "white"),
            '-': ("#2196f3", "white"),
            '+': ("#2196f3", "white"),
            '√': ("#ba68c8", "white"),
            'π': ("#ffa726", "black"),
        }

        bg_color, fg_color = colors.get(text, ("#eeeeee", "black"))

        button = ctk.CTkButton(self.root, text=text, font=("Segoe UI", 24, "bold"),
                               height=70, corner_radius=15, fg_color=bg_color, text_color=fg_color,
                               hover_color="#444" if fg_color == "white" else "#ddd",
                               command=lambda: self.on_click(text))
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan,
                    padx=5, pady=5, sticky="nsew")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.delete(0, ctk.END)
            self.display.insert(0, "0")

        elif char == '=':
            try:
                self.expression = self.display.get()
                expr = self.expression.replace('^', '**').replace('π', str(math.pi)).replace('√', '**0.5')
                result = eval(expr)
                self.display.delete(0, ctk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, ctk.END)
                self.display.insert(0, "Error")
                self.expression = ""

        elif char == 'π':
            self.expression += str(math.pi)
            self.display.insert(ctk.END, 'π')

        elif char == '√':
            self.expression += '**0.5'
            self.display.insert(ctk.END, '√')

        elif char == '%':
            self.expression += '/100'
            self.display.insert(ctk.END, '%')

        elif char == 'mod':
            self.expression += '%'
            self.display.insert(ctk.END, 'mod')

        else:
            if self.display.get() == "0" and char not in ".*/+-":
                self.display.delete(0, ctk.END)
            self.expression += str(char)
            self.display.insert(ctk.END, str(char))


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("700x800")
    app = Calculator(root)
    root.mainloop()
