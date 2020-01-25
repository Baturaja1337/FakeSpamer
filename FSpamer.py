import datetime
import time
import os

logo = ("""


                        [ PRIVAT TOOLS SPAMMER ]
=======================================================================
 __   ____        _                    _       _ _______________   __
| _| | __ )  __ _| |_ _   _ _ __ __ _ (_) __ _/ |___ /___ /___  | |_ |
| |  |  _ \ / _` | __| | | | '__/ _` || |/ _` | | |_ \ |_ \  / /   | |
| |  | |_) | (_| | |_| |_| | | | (_| || | (_| | |___) |__) |/ /    | |
| |  |____/ \__,_|\__|\__,_|_|  \__,_|/ |\__,_|_|____/____//_/     | |
|__|                                |__/                          |__|
Code by : Sultan Raja Marlindo
        : Ferry Farhan
=======================================================================

""")
print(logo)


def Fake_Spam():
    print()
    Victim_Number = input('Masukan Nomor Target : ')
    if len(Victim_Number) == 0 or len(Victim_Number) <= 11 or len(Victim_Number) >= 13:
        print('Nomor Telepon Tidak Valid !!')
        Fake_Spam()

    Spam_Count = int(input('Masukan Jumlah Spam  : '))
    print()

    if int(Spam_Count) >= 1:
        for x in range(int(Spam_Count)):
            time.sleep(1)
            x += 1
            print('[',str(x),']','Mengirim Spam Ke Nomor :',int(Victim_Number),'[Sukses]')
            time.sleep(2)
        print()

    ask = input('Lanjut(L) / Stop(S) >>> ')

    if ask == ('Lanjut') || ask == ('lanjut') || ask || ('L') || ask || ('l'):
        print()
        os.system('cls')
        print(logo)
        Fake_Spam()
    else:
        print('Tunggu 5 Detik Untuk Keluar')
        time.sleep(5)
        quit()

while (True):
    Fake_Spam()



