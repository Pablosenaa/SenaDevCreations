import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        root.title("Calculadora")
        root.config(bg="black")

        self.display = tk.Entry(root, font=('Arial', 20), bd=5, bg="white", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, font=('Arial', 20), bd=5, bg="gray", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        root.grid_columnconfigure((0,1,2,3), weight=1)
        root.grid_rowconfigure((1,2,3,4), weight=1)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        else:
            self.display.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    root.resizable(False, False)
    calc = Calculadora(root)
    root.mainloop()
