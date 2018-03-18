from fonction2 import toto

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
        assert toto(0,0) == 0, "toto(0,0) doit renvoyer 0"
        assert toto(0,5) == 5, "toto(0,5) doit renvoyer 5"
        assert toto(-1,0) == 0, "toto(-1,0) doit renvoyer -1"
        assert toto(-5,3) == 0, "toto(-5,3) doit renvoyer -2"
        success()

        send_msg("Félicitation 🌟", "C'est bien ça !")

    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Revoyez les variables ! 🤔")


if __name__ == "__main__":
    test()
