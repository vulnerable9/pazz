import os
from colorama import *


print("\033[95mPazz v1.0\n")

if os.path.isfile("primary_key"):
    vault = input("\033[96mEnter your primary key - \033[34m")
    key = open("primary_key", "r")
    if vault == key.read():
        print("\033[92mSuccessfully logged in.\n")
        key.close()
        while 1:
            pass_name = input("\033[96mEnter pass name - \033[34m")
            pass_key = input("\033[96mEnter password - \033[34m")
            store = pass_name + "===" + pass_key
            stored_keys = open("keys", "a")
            stored_keys.write("\n" + store)
            stored_keys.close()
            stored_keys = open("keys", "r")
            print("\033[33m"+stored_keys.read()+"\n")
            stored_keys.close()
            input("\033[97mPress enter to enter some more passwords. Ctrl+C for exiting\n")

    else:
        print("\033[91mError.")
        input("\033[97mPress enter to exit\n")
else:
    k_w = open("primary_key", "w")
    new_key = input("\033[96mEnter your primary key - \033[34m")
    k_w.write(new_key)
    k_w.close()
    print("\033[92mSuccessfully set new key.")
    os.system("cls")
    if os.path.isfile("primary_key"):
        vault = input("\033[96mEnter your primary key - \033[34m")
        key = open("primary_key", "r")
    if vault == key.read():
        print("\033[92mSuccessfully logged in.\n")
        key.close()
        while 1:
            pass_name = input("\033[96mEnter pass name - \033[34m")
            pass_key = input("\033[96mEnter password - \033[34m")
            store = pass_name + "===" + pass_key
            stored_keys = open("keys", "a")
            stored_keys.write("\n" + store)
            stored_keys.close()
            stored_keys = open("keys", "r")
            print("\033[33m"+stored_keys.read()+"\n")
            stored_keys.close()
            input("\033[97mPress enter to enter some more passwords. Ctrl+C for exiting\n")

    store_keys = open("keys", "w")
    store_keys.close()
