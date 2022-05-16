from tkinter import *
import tkinter as tk
import requests
import time

# handles the api request and organizes it to each variable


def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        city + "apitoken"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    humidity = json_data['main']['humidity']
    sun_rise = time.strftime("%I:%M:%S", time.gmtime(
        json_data['sys']['sunrise']-18000))
    sun_set = time.strftime("%I:%M:%S", time.gmtime(
        json_data['sys']['sunset']-18000))

    final_info = city.upper() + "\n" + condition + "\n" + str(temp) + "°c"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "°c" + "\n" + "Min Temp: " + str(min_temp) + "°c" + "\n" + "Humidity: " + str(
        humidity) + "%" "\n" + "Sunrise Time: " + sun_rise + " AM" + "\n" + "Sunset Time: " + sun_set + " PM"

    label1.config(text=final_info)
    label2.config(text=final_data)

# tkinter does not support placeholder text like HTML, so i have to make a new function to
# clear the text when the text box is clicked.


def clear_entry(event, entry):
    textfield.delete(0, "end")


# specify the application window
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ('Helvetica', 15, "bold")
t = ('Helvetica', 20, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.insert(0, "Enter The City")


textfield.pack(pady=(20, 10))
# textfield.focus()
textfield.bind("<Button-1>", lambda event: clear_entry(event, textfield))
# textfield.bind("<BackSpace>", lambda event: clear_entry(event, textfield))
textfield.bind('<Return>', getWeather)

btn = Button(canvas, height=2, width=10,
             text="Search")
btn.bind('<Button 1>', getWeather)
btn.pack()

label1 = tk.Label(canvas, font=t)
label1.pack(pady=(30, 0))
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
