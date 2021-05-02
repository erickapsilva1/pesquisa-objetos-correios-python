import requests
from bs4 import BeautifulSoup
from tkinter import *

def getStatus(obj):
    try:
        req = requests.post(url='https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?', data={'objetos':obj})
        soup = BeautifulSoup(req.text, 'html.parser')

        status = soup.find('div', id='UltimoEvento').strong
        date = soup.find('div', id='UltimoEvento').text.split()[-1]
        last_item = soup.find('table', class_='listEvent sro').strong

        resp = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
        resp += 'Objeto: ' + obj + '\n'
        resp += 'Status: ' + status.string.strip() + '\n'
        resp += 'Data: ' + date + '\n'
        resp += 'Último evento: ' + last_item.string.strip() + '\n'
        resp += '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n'

        return resp

    except:
        resp = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
        resp += 'Objeto: ' + obj + '\n'
        resp += 'Status não disponível.\n'
        resp += '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n'
        return resp


if __name__ == '__main__':
    app=Tk()
    app.title('Status Entrega Correios')
    app.geometry('500x300')

    scrollbar = Scrollbar(app)
    scrollbar.pack(side=RIGHT, fill=Y)
    textbox = Text(app)
    textbox.pack()

    textbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=textbox.yview)

    order_list = open('objetos.txt', 'r')
    for o in order_list:    
        textbox.insert(END, getStatus(o))

    app.mainloop()
    order_list.close()