import pywhatkit


def sent_message_inst():
    mobile = input('Введите номер получателя: ')

    message = input('Ввдите текст сообщения: ')
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

def sent_message():
    mobile = input('Введите номер получателя: ')
    message = input('Ввдите текст сообщения: ')
    hour = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))
    pywhatkit.sendwhatmsg(phone_no=mobile, message=message, time_hour=hour, time_min=minutes)

def main():
    sent_message_inst()

if __name__ == '__main__':
    main()

