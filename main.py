# -*- coding: UTF-8 -*-
#os.getcwd()
#import vk_api
#from interface.size import Size
from src.size import ConsoleSize
import curses
from curses import wrapper
from src.tui.boxes.textbox import TextBox


def main(stdscr):
    textbox1 = TextBox(10, 3, [2,10])
    size = ConsoleSize()

    stdscr.clear()

    textbox1.draw(size.getSize())
    stdscr.getkey()
    #stdscr = curses.initscr()
    #stdscr.clear()
    # stdscr.addstr(0, 0, "Current mode: Typing mode",
    #               curses.A_REVERSE)
    # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    # stdscr.addstr(10, 10, "RED ALERT!", curses.color_pair(1))
    # stdscr.refresh()
    # stdscr.getkey()
    # stdscr = curses.initscr()
    # stdscr.clear()
    #
    # for i in range(0, 10):
    #     v = i - 10
    #     stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10 / v))
    #
    # stdscr.refresh()
    # stdscr.getkey()

wrapper(main)
    # size = ConsoleSize()
    # if(size.isSizeWork()):
    #     print(size.getSize())
    # vk_session = vk_api.VkApi(login, password, token = token, scope = '4096')
    # try:
    #     vk_session.auth(token_only=True)
    # except vk_api.AuthError as error_msg:
    #     print(error_msg)
    #     return


    #vk = vk_session.get_api()

    #wall = tools.get_all('wall.get', 100, {'owner_id': 1})
    #friends = vk.friends.get(count = 10, order= 'name', fields = 'id,first_name,last_name')
    #response = vk.wall.get(count=1)
    #size = Size()
    #size.getSize()
    #size.printSize()
    # if response['items']:
    #     print(response['items'][0])
    # print("===============================================")


    #size = Size()
    #_rows , _columns = size.getSize()
    #size = Size()
    #print(size.getSize())
    #lol = os.popen('stty size', 'r').read().split()
    #print(lol)
    #print("rows: ", {}, "columns:", {}).format(_rows, _columns)


if __name__ == '__main__':
    main()
