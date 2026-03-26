def change_text(w):
    w = w + " World"
    print("Inside function:", w)

text = "Hi"
change_text(text)
print("Outside function:", text)