try:
    import requests,os,time
    from pystyle import Center, Colors, Colorate
except ImportError:
    os.system('pip install requests pystyle')

from pystyle import Center, Colors, Colorate
import requests,os,time

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    print(Center.XCenter('[1] Delete Webhook   [2] Spam Webhook'))

def ascii():
    art = """
 _    ,              
' )  /       /       
 /--/ __ __ /_  __  , made by
/  (_(_)(_)/ <_/ (_/_     kratz
                  /  
                 '   \n
"""
    ce = Center.XCenter(art)
    co = Colorate.Horizontal(Colors.blue_to_purple, ce)
    clear()
    print(co)

def cla():
    clear()
    ascii()

def main():
    os.system('title Hooky')
    choice = input('    Choice >> ')

    if choice == '1':
        os.system('title Hooky - Webhook Deleter')
        cla()
        hookurl = input('   Webhook url >> ')
        delhook = requests.delete(hookurl)

        if delhook.status_code == 204:
            print(f'Succesfuly deleted webhook - {delhook.status_code}')
        elif delhook.status_code == 404:
            print(f'Webhook does not exist - {delhook.status_code}')
        else:
            print(f'Something went wrong... - {delhook.status_code}')

        input('\nPress enter to return to menu...')

    elif choice == '2':
        os.system('title Hooky - Webhook Spammer')
        cla()
        hookurl = input('    Webhook url >> ')
        cla()
        msg = input('   Messages >> ')
        cla()
        num = int(input('    How many messages? >> '))
        cla()
        delay = input('    Delay >> ')

        for i in range(num):
            data = {
                "content": f"{msg}"
            }

            spam = requests.post(hookurl, json=data)
            time.sleep(int(delay))

            if spam.status_code == 204:
                print(f'Sent {msg} - {spam.status_code}')
            elif spam.status_code == 404:
                print(f'Webhook does not exist - {spam.status_code}')
            else:
                print(f'Error - {spam.status_code}')
        
        input('Press enter to return to menu...')

    cla()
    menu()
    main()

cla()
menu()
main()