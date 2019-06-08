# -*- coding: UTF-8 -*-
import os
os.getcwd()
import vk_api
from interface.size import Size


def main():
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
    size = Size()
    size.getSize()
    size.printSize()
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
