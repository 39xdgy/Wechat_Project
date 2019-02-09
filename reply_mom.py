import itchat

itchat.auto_login(hotReload = False)


while(True):
    raw_msg = itchat.get_msg()
    if(not raw_msg == ([],[])):

        msg_content = raw_msg[0][0].get('Content')
        msg_tousername = raw_msg[0][0].get('ToUserName')
        if(not msg_content == ""):
            print(msg_tousername)
            print()
            print(msg_content)
