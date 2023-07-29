import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from functools import partial
import pandas as pd
from system import calculate
from flask import Flask, render_template, request
# Sample DataFrame (Replace this with your actual DataFrame)
df = pd.read_csv('df_test.csv')

app = Flask(__name__)


def validateLogin(id):
    customer_id = str(id)
    customer_unique_id = df.loc[df['customer_id'] == customer_id, 'customer_id'].values
    if len(customer_unique_id) > 0:
        print("Customer ID:", customer_unique_id[0])
        return True
    return False

"""def result_window(id):
    result = calculate(id)S
    res = Toplevel()
    res.title('Recommendations')
    res.geometry('500x500')
    res.configure(bg='#fff')
    #res.wm_attributes('-transparentcolor', '#aabbcc')
    res.resizable(False, False)
    background_image = Image.open("img.png")
    background_image = ImageTk.PhotoImage(background_image)
    bglabel = tk.Label(res, image=background_image)
    bglabel.place(x=0, y=0, relwidth=1, relheight=1)

    rec = Label(res, text='These are some item categories recommendations for you', font=('Arial', 14))
    rec.place(relx=0.5, rely=0.2, anchor=CENTER)

    resultframe = tk.Frame(master=res, height=200, width=200)
    for i in range(len(result)):
        val = StringVar(value=result[i])
        data = Entry(resultframe, textvariable=val, font=('Arial', 18))
        data.pack()
    resultframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    #resultframe.pack_propagate(0)

    root.image = background_image
    
    \"\"\"   bg = Image.open("img.png")
        bg = ImageTk.PhotoImage(bg)

        bglabel = tk.Label(res, image=bg)
        bglabel.pack() 



root = tk.Tk()
root.title('Customer Login')
root.geometry('500x500')
root.configure(bg='#fff')
root.resizable(False, False)

# Load the image using PIL
background_image = Image.open("img.png")
background_image = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

idLabel = Label(root, text="Customer ID")
idLabel.place(relx=0.4, rely=0.4, anchor=CENTER)

id = StringVar()
idEntry = Entry(root, textvariable=id)
idEntry.place(relx=0.6, rely=0.4, anchor=CENTER)

#validateLogin = partial(validateLogin, id)

loginButton = Button(root, text="Login", command=validateLogin)
loginButton.place(relx=0.5, rely=0.5, anchor=CENTER)

# Attach the image to the root window to keep the reference
root.image = background_image"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommendations", methods=["POST"])
def show_recommended():
    print(request.form['customer_id'])
    #customer_segmentation = calculate(request.form['customer_id'])
    if request.form['customer_id'] != "" and validateLogin(request.form['customer_id']):
        #customer_segmentation = calculate(request.form['customer_id'])
        test = calculate(request.form['customer_id'])
        return render_template("recommendations.html", recommendations=test)
    #return "404: Invalid Customer ID"
    return render_template("error.html")


#root.mainloop()

if __name__ == "__main__":
    app.run()