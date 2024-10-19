def main():
    message = input("entre an string: ")
    print(convert(message))



def convert(message):
    msg1 = message.replace(":)", "🙂")
    msg2 = msg1.replace(":(", "🙁")
    return msg2

main()