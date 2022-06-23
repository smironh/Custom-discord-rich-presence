from asyncio import BaseTransport
from cProfile import label
from pypresence import Presence
from time import time

print("""

−•• ••• −•−• •••••• −−• −−• −••−• •••− ••−• •− −− •• •−•• −•−− 


  ____    ___    ____   _   _     ____    _____   _   _   _____
 |  _ \  |_ _|  / ___| | | | |   | __ )  | ____| | \ | | |__  /
 | |_) |  | |  | |     | |_| |   |  _ \  |  _|   |  \| |   / / 
 |  _ <   | |  | |___  |  _  |   | |_) | | |___  | |\  |  / /_ 
 |_| \_\ |___|  \____| |_| |_|   |____/  |_____| |_| \_| /____|
                                                               



    """)


prens = input("Discord Application ID: ")
stat = input("state: ")
detal = input('detals: ')
large_imag = input('Большая картинка: ')
large_tex = input('Текст к большой картинки: ')
small_imag = input('Маленькая картинка: ')
small_tex = input('Текст к маленькой картинки: ')


def start(prens = prens, stat = stat, detal = detal, large_imag = large_imag, large_tex = large_tex, small_imag = small_imag, small_tex = small_tex):
    vib = input('Хотите ли вы добавить кнопки? (y/n):')
    while True:
        RPC = Presence(prens)
        try:
            print() 
        except DiscordError:
            print('ERROR')
            continue


        RPC.connect()
        if vib == 'y':
            label = input("Название кнопки: ")
            url = input("ССылка: ")
            label2 = input("Название 2 кнопки: ")
            url2 = input("2 Ссылка: ")
            btns = [
                {
                    "label": label,
                    "url": url
                },
                {
                    "label": label2,
                    "url": url2
                },
            ]

            RPC.update(
                state = stat,
                details = detal,
                start = time(),
                buttons=btns,
                large_image = large_imag,
                large_text=large_tex,
                small_image = small_imag,
                small_text = small_tex
            )
            input()
        if vib == 'n':
            RPC.update(
                state = stat,
                details = detal,
                start = time(),
                large_image = large_imag,
                large_text=large_tex,
                small_image = small_imag,
                small_text = small_tex
            )
            input()

start()