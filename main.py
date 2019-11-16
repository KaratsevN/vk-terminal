# -*- coding: UTF-8 -*-
#os.getcwd()
#import vk_api
from src.size import ConsoleSize
# import curses
from curses import wrapper
from src.tui.boxes.textbox import TextBox


def main(stdscr):

    size = ConsoleSize()
    # Columns - x
    # Rows    - y
    size.getSize()

    # textbox1 = TextBox(size.getColumns() - 1, size.getRows() - 1, [0,0])
    textbox1 = TextBox(round(size.getColumns()/2), round(size.getRows()/2), [0,0])
    textbox2 = TextBox(round(size.getColumns()/2), round(size.getRows()/2), [0,round(size.getRows()/2)])
    textbox3 = TextBox(round(size.getColumns()/2), round(size.getRows()/2), [round(size.getColumns()/2),0])
    textbox4 = TextBox(round(size.getColumns()/2), round(size.getRows()/2), [round(size.getColumns()/2), round(size.getRows()/2)])
    stdscr.clear()

    textbox1.draw(size.getSize())
    textbox2.draw(size.getSize())
    textbox3.draw(size.getSize())
    # textbox4.draw(size.getSize())
    stdscr.getkey()

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    wrapper(main)

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
