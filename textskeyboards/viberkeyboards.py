from vibertelebot.utils.tools import keyboard_consctructor

LOGO = 'https://i.ibb.co/VNpXPB5/1.png'

category_keyboard = keyboard_consctructor([
            ('Стиральные машины', 'category-Stiralki', ''),
            ('Стирально-сушильные машины', 'category-Stiralki_Sushilki', ''),
            ('Посудомоечные машины', 'category-Posudomoyki', ''),
            ('Холодильные и морозильные камеры', 'category-Holodilnik_Morozilnik', ''),
            ('Плиты / встроенные духовые шкафы и варочные поверхности', 'category-Plity_Duhovye_Shkafi', ''),
            ('Микроволновые печи', 'category-Mikrovolnovki', ''),
            ('Пылесосы', 'category-Pylesosy', ''),
            ('Другое', 'category-Drugoe', '')
            ])

end_chat_keyboard = keyboard_consctructor([
            ('Завершити чат', 'end_chat', '')
            ])

menu_keyboard = keyboard_consctructor([
            ('Запис на відео чат', 'video', ''),
            ("Зв'язок з оператором", 'operator', 'https://i.ibb.co/6ZZqWPM/image.png')
            ])

confirmation_keyboard = keyboard_consctructor([
            ('Меню', 'menu', 'https://i.ibb.co/Kbm7kvb/image.png'),
            ('Продовжити', 'continue', 'https://i.ibb.co/9Vs7RC8/image.png')
            ])

opeartor_keyboard = keyboard_consctructor([
            ("Зв'язок з оператором", 'operator', 'https://i.ibb.co/6ZZqWPM/image.png')
            ])

brand_keyboard = keyboard_consctructor([
            ('Candy', 'brand-Candy', 'https://i.ibb.co/Jjw3XMc/Candy.png'),
            ('Hoover', 'brand-Hoover', 'https://i.ibb.co/TbcgHGC/Hoover.png'),
            ('Rosieres', 'brand-Rosieres', 'https://i.ibb.co/s32RqHn/Rosieres.png')
            ])

upload_keyboard = keyboard_consctructor([
            ("Зв'язок з оператором", 'operator', 'https://i.ibb.co/6ZZqWPM/image.png'),
            ("Продовжити", 'upload', 'https://i.ibb.co/9Vs7RC8/image.png')
            ])

return_keyboard = keyboard_consctructor([
            ('Меню', 'menu', 'https://i.ibb.co/Kbm7kvb/image.png')
            ])

phone_keyboard = [
            ("Зв'язок з оператором", 'operator', 'https://i.ibb.co/6ZZqWPM/image.png'),
            ('Подiлитись номером', 'phone_reply', 'https://i.ibb.co/KzHgfzN/image.png')
            ]
