import tkinter as tk
import requests
# from tkinter import font

# def show_weather(entry):
#     print("Hiya", entry)

# api: 909bd089bdf492d70fd57add13f124f1
# api.openweathermap.org/data/2.5/weather?q={city name}
# api.openweathermap.org/data/2.5/weather?q={city name},{country code}
# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        pressure = weather['main']['pressure']
        # result = 'City: %s \nConditions: %s \nTemperature (°C): %s \nMinimum Temparature %s \nMaximum Temparature %s \nHumidity %s \nPressure %s' % (name, desc, temp, temp_min, temp_max, humidity, pressure)
        result1 = 'City: %s \nConditions: %s \nTemperature (°C): %s \n' % (name, desc, temp)
        result2 = 'Humidity (%%): %s \nPressure (hPa): %s' % (humidity, pressure)
    except:
        result1 = 'Error: '
        result2 = 'could not retrieve information'
    return result1 + result2


def get_weather(city):
    weather_key = '909bd089bdf492d70fd57add13f124f1'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units':'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    print((response.json()))
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

    label['text'] = format_response(weather)


HEIGHT = 400
WIDTH = 600
frame_color = '#044047'
box_color = '#040112'
button_color = '#157545'
text_color = '#b4babf'
canvas_color = '#071321'
root = tk.Tk()

canvas = tk.Canvas(root, height= HEIGHT, width=WIDTH, bg=canvas_color)
canvas.pack()

# bg_image = tk.PhotoImage(file='dark.png')
# bg_label = tk.Label(root, image = bg_image)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

root.title("utopia")
root.iconbitmap('cloud.ico')

frame = tk.Frame(root, bg= frame_color, bd= 5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Parchment, 12'), bg=box_color, fg=text_color)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, command=lambda: get_weather(entry.get()), font=('Parchment, 12'), text="Get Weather", bg=button_color, fg=text_color)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg=frame_color, bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor='n')

label = tk.Label(lower_frame, text="", bg=box_color, fg=text_color, font=('Parchment, 12'), anchor='nw', justify='left', bd=5)

label.place(relwidth=1, relheight=1)

# print(tk.font.families())

root.mainloop()

