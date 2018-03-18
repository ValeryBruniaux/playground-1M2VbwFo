from variable1 import a

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
        assert a == 5, "a doit contenir 5"
        success()

        send_msg("Felicitation 🌟", "C'est bien ça !")

    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Revoyez les variables ! 🤔")

if __name__ == "__main__":
   test()
