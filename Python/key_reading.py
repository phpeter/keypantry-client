import requests, readchar

USER_ID = 'tindell'
USER_PASS = 'abc123'

def on_key_press(key):
    apicall = 'https://keypantry.herokuapp.com/toggleitem/' + str(key)
    try:
        r = requests.get(apicall, headers={"username":USER_ID, "password":USER_PASS}) # , auth =  (USER_ID, USER_PASS)
    except Exception as e:
        print(e)
    print(r)
    print(r.text)

try:
    while True:
        on_key_press("".join(str(x) for x in [ord(c) for c in (readchar.readkey())]))
except KeyboardInterrupt:
    exit()