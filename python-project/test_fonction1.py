from fonction1 import toto

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
        assert toto() == 5, "toto doit renvoyer 5"
        success()

        send_msg("Félicitation 🌟", "C'est bien ça !")

    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Revoyez les fonctions ! 🤔")

if __name__ == "__main__":
   test()
