
import openai
import pyperclip
import tkinter as tk
from tkinter import messagebox, font

openai.api_key = ""


def generate_response():
    # Input data into the model and generate response
    data = prompt_entry.get()
    prompt = (f"{data}")
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=4000,temperature=0.7,frequency_penalty=0,
  presence_penalty=0.7, top_p=1,best_of=1)
    message = completions.choices[0].text
    return message

def on_submit():
    try:
        data = prompt_entry.get()
        response = generate_response()
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", response)
    except Exception as e:
        messagebox.showerror("Error", e)

root = tk.Tk()
root.title("DaVinci Desktop")

# Use a font for a more professional look
font_type = font.Font(family="Helvetica", size=12)

prompt_label = tk.Label(root, text="Ask Me Anything ", font=font_type)
prompt_label.pack(pady=10)

prompt_entry = tk.Entry(root, width= 60, font=font_type)
prompt_entry.pack(padx=30, pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit, font=font_type)
submit_button.pack(pady=10)

output_text = tk.Text(root, wrap=tk.WORD, font=font_type)
output_text.pack(padx=10, pady=10)

root.mainloop()




