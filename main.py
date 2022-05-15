from select import select
from tkinter import *
from tkinter import ttk
import requests
import json
import datetime


# API
api_g = requests.get("https://covid19.mathdro.id/api")
data_g = json.loads(api_g.text)

att = (data_g['lastUpdate'])
att = datetime.datetime.strptime(att, "%Y-%m-%dT%H:%M:%S.000Z")

api_c = requests.get('https://covid19.mathdro.id/api/countries')
data_c = json.loads(api_c.text)

# list
countries = ['World']
for x in range(0, len(data_c['countries'])):
    countries.append(data_c['countries'][x]['name'])

# variables
case = ''
recov = ''
death = ''

once = '1'
resultado = ''
# colors
white = '#ffffff'
black = '#000000'
gray = '#c7d2d4'
yellow = '#eded18'
green = '#37d108'
red = '#d11c08'

# window
window = Tk()
window.resizable(0, 0)
window.geometry('835x380')
window.title('Covid-19 Dashboard')
window.config(bg=gray)

title_frame = Frame(window, width=835, height=80, bg=white)
title_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

case_frame = Frame(window, bg=white)
case_frame.grid(row=1, column=0, pady=5)

recov_frame = Frame(window, bg=white)
recov_frame.grid(row=1, column=1, pady=5)

death_frame = Frame(window, bg=white)
death_frame.grid(row=1, column=2, pady=5)

select_frame = Frame(window, bg=gray)
select_frame.grid(row=2, column=1)

att_frame = Frame(window)
att_frame.grid(row=2, column=0)


# image
img_title = PhotoImage(file='c_world.png')

img_case = PhotoImage(file='mask.png')
img_recov = PhotoImage(file='wash.png')
img_death = PhotoImage(file='distance.png')

### label:

# title
title = Label(title_frame, text='Covid-19', width=20, height=1,
              pady=0, padx=0, bg=white, fg=black, font='Helvetica 25 bold')
title.place(x=240, y=18)

title_img = Label(title_frame, image=img_title, bg='white')
title_img.place(x=285, y=0)

# confirmed cases
case_label = Label(case_frame, width=22, height=1,
                    pady=16, font=("Courier 15 bold"), bg=white, fg=black)
case_label.grid(row=0, column=0, pady=10)

number_case = Label(case_frame, text=case, width=12, height=1,
                     pady=15, font=("Courier 25 bold"), bg=white, fg=black)
number_case.grid(row=1, column=0, pady=1)

att_case = Label(case_frame, width=25,
                  height=1, pady=15, font=("Ivy 11 bold"), text='WEAR MASK', bg=white, fg=black)
att_case.grid(row=2, column=0, pady=1)

stripe_case = Label(case_frame, font=(
    "Courier 1 bold"), bg=white)
stripe_case.grid(row=3, column=0, sticky=NSEW)

case_img = Label(case_frame, image=img_case, bg='white')
case_img.place(x=65, y=5)

# recovered
recov_label = Label(recov_frame, width=22, height=1,
                    pady=16, font=("Courier 15 bold"), bg=white, fg=black)
recov_label.grid(row=0, column=0, pady=10)

number_recov = Label(recov_frame, text=recov, width=12, height=1,
                     pady=15, font=("Courier 25 bold"), bg=white, fg=black)
number_recov.grid(row=1, column=0, pady=1)

att_recov = Label(recov_frame, width=25,
                  height=1, pady=15, font=("Ivy 11 bold"), text='WASH YOUR HANDS', bg=white, fg=black)
att_recov.grid(row=2, column=0, pady=1)

stripe_recov = Label(recov_frame, font=(
    "Courier 1 bold"), bg=white)
stripe_recov.grid(row=3, column=0, sticky=NSEW)

recov_img = Label(recov_frame, image=img_recov, bg='white')
recov_img.place(x=65, y=12)

# deaths
death_label = Label(death_frame, width=22, height=1,
                    pady=16, font=("Courier 15 bold"), bg=white, fg=black)
death_label.grid(row=0, column=0, pady=10)

number_death = Label(death_frame, text=death, width=12, height=1,
                     pady=15, font=("Courier 25 bold"), bg=white, fg=black)
number_death.grid(row=1, column=0, pady=1)

att_death = Label(death_frame, width=25,
                  height=1, pady=15, font=("Ivy 11 bold"), text='KEEP SOCIAL DISTANCING', bg=white, fg=black)
att_death.grid(row=2, column=0, pady=1)

stripe_death = Label(death_frame, font=(
    "Courier 1 bold"), bg=white)
stripe_death.grid(row=3, column=0, sticky=NSEW)

death_img = Label(death_frame, image=img_death, bg='white')
death_img.place(x=40, y=20)

# select box
select = Label(select_frame, text='Location:',
               font=("Ivy 12 bold"), bg=gray, fg=black)
select.grid(row=0, column=0, pady=20)

select_box = ttk.Combobox(select_frame, width=15, font=('Ivy 11'))
select_box.grid(row=0, column=1)

select_box["values"] = countries

# att
att_label = Label(att_frame, text=f'Data updated: {att}', width=27, bg=white)
att_label.grid(row=0, column=0)

# ZikaLabs.
zl_label = Label(att_frame, text='©Zika Labs.', width=27, bg=white, fg=black)
zl_label.grid(row=1, column=0)

# function
def selection(eventObject):

    global once

    if once == '1':
        case_label.configure(text='Confirmed Cases')
        att_case.configure(text='')
        stripe_case.configure(bg='yellow')
        case_img.configure(image='')

        recov_label.configure(text='Recovereds')
        att_recov.configure(text='')
        stripe_recov.configure(bg='green')
        recov_img.configure(image='')

        death_label.configure(text='Deaths')
        att_death.configure(text='')
        stripe_death.configure(bg='red')
        death_img.configure(image='')

        once = '2'

    if select_box.get() == "World":
        api_g = requests.get("https://covid19.mathdro.id/api")
        data_g = json.loads(api_g.text)
        
        case = data_g['confirmed']['value'] 
        case = '{0:,}'.format(case).replace(',','.')
        
        recov = data_g['recovered']['value']
        recov = '{0:,}'.format(recov).replace(',','.')

        death = data_g['deaths']['value']
        death = '{0:,}'.format(death).replace(',','.')

        number_case.configure(text=case)
        number_recov.configure(text=recov)
        number_death.configure(text=death)

    else:
        sel_location = select_box.get()

        api_sel = requests.get(
            f"https://covid19.mathdro.id/api/countries/{sel_location}")
        data_sel = json.loads(api_sel.text)

        case = data_sel['confirmed']['value']
        case = '{0:,}'.format(case).replace(',','.')
        
        recov = data_sel['recovered']['value']
        recov = '{0:,}'.format(recov).replace(',','.')
        
        death = data_sel['deaths']['value']
        death = '{0:,}'.format(death).replace(',','.')

        number_case.configure(text=case)
        number_recov.configure(text=recov)
        number_death.configure(text=death)

select_box.bind("<<ComboboxSelected>>", selection)

window.mainloop()
