from vibertelebot.utils.tools import keyboard_consctructor

LOGO = 'https://i.ibb.co/VNpXPB5/1.png'

category_keyboard = keyboard_consctructor([
            ('Пральні машини', 'category-Stiralki', ''),
            ('Прально-сушильні машини', 'category-Stiralki_Sushilki', ''),
            ('Посудомийні машини', 'category-Posudomoyki', ''),
            ('Холодильні та морозильні камери', 'category-Holodilnik_Morozilnik', ''),
            ('Плити / вбудовані духові шафи та варочні поверхні', 'category-Plity', ''),
            ('Мікрохвильові пічі', 'category-Mikrovolnovki', ''),
            ('Пилососи', 'category-Pylesosy', ''),
            ('Інше', 'category-Drugoe', '')
            ])

end_chat_keyboard = keyboard_consctructor([
            ('Завершити чат', 'end_chat', '')
            ])

menu_keyboard = keyboard_consctructor([
            ('Запис на відео чат', 'video', ''),
            ("Зв'язок з оператором", 'operator', '')
            ])

confirmation_keyboard = keyboard_consctructor([
            ('Меню', 'menu', ''),
            ('Продовжити', 'continue', '')
            ])

opeartor_keyboard = keyboard_consctructor([
            ("Зв'язок з оператором", 'operator', '')
            ])

brand_keyboard = keyboard_consctructor([
            ('Candy', 'brand-Candy', ''),
            ('Hoover', 'brand-Hoover', ''),
            ('Rosieres', 'brand-Rosieres', '')
            ])

upload_keyboard = keyboard_consctructor([
            ("Зв'язок з оператором", 'operator', ''),
            ("Продовжити", 'upload', '')
            ])

return_keyboard = keyboard_consctructor([
            ('Меню', 'menu', '')
            ])

phone_keyboard = [
            ("Зв'язок з оператором", 'operator', ''),
            ('Подiлитись номером', 'phone_reply', '')
            ]
