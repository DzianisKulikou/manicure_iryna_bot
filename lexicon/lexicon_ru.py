lexicon_dict_ru: dict[str, str] = {
    '/start': '<b>Привет!\nЯ бот Ирины Куликовой!</b>\n'
              'Я могу рассказать вам всю информацию о её деятельности мастером по маникюру!\n'
              '<span class="tg-spoiler">_____________________________________</span>',
    '/help': 'У меня вы можете узнать всё, о работе Ирины Куликовой Мастером по маникюру!\n'
             'Если у вас возникают какие-то проблемы с работой бота(что-то не открывается), значит бот был '
             'перезагружен. Чтоб всё корректно заработало, просто перезапустите его, '
             'прописав в чате команду: "<b>/start</b>". Или же нажмите на команду: "<b>/start</b>" - '
             'в <b>Меню</b> Бота!',
    'unknown_message': 'Я не знаю, что вам ответить...',
    'menu': 'Что бы вы хотели узнать?\n(Воспользуйтесь встроенной клавиатурой внизу👇)',
    'adres': 'Warszawa 02-582, ul. Wiktorska 83/87\nРайон Старый Мокотов\n300 метров от станции метро Racławicka',
    'phone': '+48-451-117-579 Ирина',
    'nails': 'Это фотографии моих работ:',
    'me': 'Если вы хотите написать мне в Telegram, нажмите на кнопку под сообщением и вам откроется чат со мной!',
    'start_manicure': 'В данном разделе вы сможете ознакомиться с моими работами, процессами, материалами и '
                      'инструментом!\n(Воспользуйтесь встроенной клавиатурой внизу👇)',
    'kontakt': 'В данном разделе вы сможете найти мой адрес и контактные данные.'
                      '\n(Воспользуйтесь встроенной клавиатурой внизу👇)',
    'start_menu': 'Вы вошли в главное меню!',
    'photo_selection': 'Выбираю для вас фотографию!',
    'developer': 'Данного бота разработал Денис Куликов. Если вы хотите для себя разработать Телеграмм бота, можете '
                 'связаться со мной по телефону: +48789137022. Или нажав на кнопку под этим сообщением, вы можете '
                 'написать мне личное сообщение в телеграмме. Я могу разработать для вас бота в соответствии с вашими '
                 'желаниями под ключ!',
    'price list': '<u><b>Маникюр:</b></u>\n\n'
                  '<b>1.</b> Маникюр + гель-лак - 20 zl\n'
                  '<b>2.</b> Маникюр + укрепление гелем - 20 zl\n'
                  '<b>3.</b> Маникюр + укрепления гелем + гель-лак - 30 zl\n'
                  '<b>4.</b> Маникюр - 10 zl\n'
                  '<b>5.</b> Снятие гель-лака/акрила (без покрытия) - 10 zl\n'
                  '<b>6.</b> Наращивание ногтей - бесплатно\n\n'
                  '<u><b>Дизайны:</b></u>\n\n '
                  '<b>1.</b> Френч, Омбре, Лунки - бесплатно\n'
                  '<b>2.</b> Дизайн 1/10 ногтей - бесплатно\n\n'
                  '<u><b>Ремонт:</b></u>\n\n'
                  '<b>1.</b>Ремонт 1/10 ногтей - бесплатно\n'
                  '<b>2.</b> Наращивание 1 ногтя - бесплатно'
}

lexicon_menu_ru: dict[str, str] = {'/st': 'Запусти меня с начала!',
                                   '/he': 'Справка по работе бота'
                                   }

lexicon_pagination_kb: dict[str, str] = {'forward': '>>',
                                         'backward': '<<'
                                         }

lexicon_button: dict[str, str] = {'button_1': 'Мой адрес',
                                  'button_2': 'Мой контактный телефон',
                                  'button_3': 'База фотографий моих работ маникюра',
                                  'button_4': 'Показать случайную фотографию моего маникюра',
                                  'button_5': 'Написать Ирине в Telegram',
                                  'button_6': 'Вся информация о работе мастера',
                                  'button_7': 'Дезинфекция и стерилизация инструмента',
                                  'button_8': 'Прайс лист',
                                  'button_9': 'Мои контактные данные',
                                  'button_10': 'Вернуться в главное меню',
                                  'button_100': 'Информация о разработчике бота',
                                  'url_button_1': 'Написать Ирине в Telegram',
                                  'url_button_2': 'Написать Денису в Telegram'
                                  }

lexicon_button_in: dict[str, str] = {'button_in_1': 'Дальше'}

lexicon_disinfection: dict[str, str] = {
    'phrase1': 'Все что нужно для проведения дезинфекции и стерилизации инструментов маникюрных!',
    'phrase2': '<b>Этапы дезинфекции и стерилизации которые проходит мой маникюрный инструмент после каждого '
               'использования:</b>\n<b>1.</b> Наливаю дезинфицирующие средство <b>Medisept Viruton Forte</b>(одно '
               'из лучших средств, используется в медицинских учреждениях всего мира для дезинфекции инструмента) '
               'в специальный контейнер.',
    'phrase3': '<b>2.</b> Помещаю инструмент в дезинфицирующий раствор на 30 минут',
    'phrase4': '<b>3.</b> Достаю инструмент спустя 30 мин. и промываю его мыльным раствором.',
    'phrase5': '<b>4.</b> После промывания инструмент необходимо просушить.',
    'phrase6': '<b>5.</b> Далее для дополнительной дезинфекции я использую гласперленовый (шариковый) стерилизатор, '
               'который предназначен для дезинфекционной обработки маникюрных инструментов, путем погружения их '
               'в колбу со стеклянными шариками, разогретыми до температуры от 175 до 200°С.',
    'phrase7': '<b>6.</b> Вставляю инструмент в стерилизатор, в котором он дезинфицируется 1 минуту.',
    'phrase8': '<b>7.</b> После стерилизатора повторно промываю инструмент мыльным раствором и просушиваю его.',
    'phrase9': 'На этом я заканчиваю процедуру дезинфекции и стерилизации. <u><b>Наш инструмент чист, стерилен и '
               'готов к дальнейшей эксплуатации.</b></u>\nА вы можете ознакомиться с другой информацией по моей '
               'работе, используя клавиатуру внизу экрана👇'
}
