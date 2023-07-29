import tkinter as tk
import PIL
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