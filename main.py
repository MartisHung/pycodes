from pypinyin import pinyin, Style
import tkinter as tk
from tkinter import messagebox

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("拼音和注音轉換器")

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=20, padx=20)

        self.selected_mode = tk.StringVar(value="拼音")  # 默認選擇拼音模式

        # 添加提交按鈕
        submit_button = tk.Button(self.root, text="提交", command=self.on_submit)
        submit_button.pack(pady=10)

        # 添加模式選擇按鈕
        pinyin_radio = tk.Radiobutton(self.root, text="拼音", variable=self.selected_mode, value="拼音")
        zhuyin_radio = tk.Radiobutton(self.root, text="注音", variable=self.selected_mode, value="注音")
        pinyin_radio.pack()
        zhuyin_radio.pack()

    def convert_to_zhuyin(self, text):
        zhuyin_list = pinyin(text, style=Style.BOPOMOFO)
        result = ''.join([item[0] for item in zhuyin_list])
        return result

    def convert_to_pinyin(self, text):
        pinyin_list = pinyin(text, style=Style.NORMAL)
        result = ' '.join([item[0] for item in pinyin_list])
        return result

    def show_result(self, result_text):
        result_window = tk.Toplevel(self.root)
        result_window.title("翻譯結果")
        result_label = tk.Label(result_window, text=result_text, font=("Arial", 14))
        result_label.pack(pady=20, padx=20)

    def on_submit(self):
        input_text = self.entry.get()
        if self.selected_mode.get() == "注音":
            zhuyin_text = self.convert_to_zhuyin(input_text)
            self.show_result(zhuyin_text)
        elif self.selected_mode.get() == "拼音":
            pinyin_text = self.convert_to_pinyin(input_text)
            self.show_result(pinyin_text)
        else:
            messagebox.showerror("錯誤", "請選擇轉換模式")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()