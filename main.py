import tkinter as tk



def copy_to_clipboard(text):
    #clear
    root.clipboard_clear()  
    #add element
    root.clipboard_append(text)  
    #updating
    root.update()  

#encoding function
def encoding(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            #geting base for uppercase of lowercase
            shift_base = 65 if char.isupper() else 97  
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char  # 
    return result

#decoding function
def decode(text, shift):
    #decoding with shift
    return encoding(text, -shift)  

#encoding
def on_encode():
    #get text from field
    text = entry_encode_text.get()  
    #get shift
    shift = int(entry_encode_shift.get()) 
    #encoding
    encoded_text = encoding(text, shift) 
    #updating data
    label_encoded_text.config(text=f"Encoded text >> {encoded_text}") 

#function for decoding
def on_decode():
    #get text from input
    text = entry_decode_text.get()  
    #get shift
    shift = int(entry_decode_shift.get())  
    #decode text
    decoded_text = decode(text, shift)  
    #update field
    label_decoded_text.config(text=f"Decoded text >> {decoded_text}")  

#main window
root = tk.Tk()
root.title("Caesar Cipher")
root.attributes("-alpha", 0.9)
Font_tuple = ("Bahnschrift", 10, "bold") 

#encode 
label_encode_text = tk.Label(root, text="Enter text to encode:")
label_encode_text.pack(pady=5)
label_encode_text.configure(font = Font_tuple)

#input
entry_encode_text = tk.Entry(root, width=50)
entry_encode_text.pack(pady=5)
entry_encode_text.configure(font = Font_tuple)

#label
label_encode_shift = tk.Label(root, text="Enter shift value:")
label_encode_shift.pack(pady=5)
label_encode_shift.configure(font = Font_tuple)

#input
entry_encode_shift = tk.Entry(root, width=10)
entry_encode_shift.pack(pady=5)
entry_encode_shift.configure(font = Font_tuple)

#btn
button_encode = tk.Button(root, text="Encode", command=on_encode)
button_encode.pack(pady=15)
button_encode.configure(font = Font_tuple)
button_encode.configure(font = Font_tuple)

#updating text
label_encoded_text = tk.Label(root, text="Encoded text >> ")
label_encoded_text.pack(pady=5)
label_encoded_text.configure(font = Font_tuple)

button_copy_encoded = tk.Button(root, text="Copy Encoded Text", command=lambda: copy_to_clipboard(label_encoded_text.cget("text").replace("Encoded text >> ", "")))
button_copy_encoded.pack(pady=10)
button_copy_encoded.configure(font = Font_tuple)

#separator
separator = tk.Canvas(root, height=1, width=400, bg="black")
separator.pack(pady=20)

#decode
label_decode_text = tk.Label(root, text="Enter text to decode:")
label_decode_text.pack(pady=5)
label_decode_text.configure(font = Font_tuple)

#input
entry_decode_text = tk.Entry(root, width=50)
entry_decode_text.pack(pady=5)
entry_decode_text.configure(font = Font_tuple)

#label
label_decode_shift = tk.Label(root, text="Enter shift value:")
label_decode_shift.pack(pady=5)
label_decode_shift.configure(font = Font_tuple)

#input
entry_decode_shift = tk.Entry(root, width=10)
entry_decode_shift.pack(pady=5)
entry_decode_shift.configure(font = Font_tuple)

#btn
button_decode = tk.Button(root, text="Decode", command=on_decode)
button_decode.pack(pady=15)
button_decode.configure(font = Font_tuple)

#updating text
label_decoded_text = tk.Label(root, text="Decoded text >> ")
label_decoded_text.pack(pady=5)
label_decoded_text.configure(font = Font_tuple)

button_copy_decoded = tk.Button(root, text="Copy Decoded Text", command=lambda: copy_to_clipboard(label_decoded_text.cget("text").replace("Decoded text >> ", "")))
button_copy_decoded.pack(pady=10)
button_copy_decoded.configure(font = Font_tuple)

#main loop
root.mainloop()
