import requests, sys, tty

USER_ID = 'oop'
USER_PASS = 'me hungry'

def on_key_press(key):
    apicall = 'https://keypantry.herokuapp.com/toggleitem/' + str(key)
    try:
        r = requests.get(apicall, auth = (USER_ID, USER_PASS)) # , auth =  (USER_ID, USER_PASS)
    except Exception as e:
        print(e)
    print(r)

tty.setcbreak(sys.stdin)
try:
    while True:
        on_key_press(ord(sys.stdin.read(1)))
except KeyboardInterrupt:
    exit()
