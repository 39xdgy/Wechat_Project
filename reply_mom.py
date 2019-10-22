import itchat
import cv2

itchat.auto_login(hotReload = True)

cv2.namedWindow("preview")
while(True):
    
    raw_msg = itchat.get_msg()
    
    if(not (raw_msg == (None, None) or raw_msg == ([], []))):
        if(not raw_msg[0][0].get('FromUserName') == raw_msg[0][0].get('ToUserName')):
            print(raw_msg)
        '''
        try:
            msg_content = raw_msg[0][0].get('Content')
            msg_tousername = raw_msg[0][0].get('FromUserName')
            if(not msg_content == ""):
                print(msg_tousername)
                print()
                print(msg_content)
        except:
            print("looool")
        '''
        
    
    key = cv2.waitKey(20)
    if key == 27:
        break
cv2.destroyWindow("preview")

itchat.logout()
