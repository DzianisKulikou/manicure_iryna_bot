evidence: dict[int, str] = {
    1: '<b>Интересный факт:</b>\nВ древнем Египте выщипанные брови символизировали скорбь по умершей… кошке. '
       'Священное животное провожали в мир иной всей семьей, заворачивали в шелковую ткань и торжественно хоронили, '
       'после чего вся семья полностью выщипывала брови и ходила так, пока волоски не отрастали вновь. Увидев на '
       'улице человека с выщипанными бровями, прохожие выражали ему или ей свои соболезнования.',
    2: '<b>Интересный факт:</b>\nПарфюмерная композиция первых духов была секретной и включала всего семь '
       'компонентов. За разглашение рецептуры парфюмеру грозила смертная казнь. Эдмонд Дюбеле, создатель первого '
       'аромата, просто разрешил своей молодой жене попользоваться духами, не называя их компонентов, но тем не менее '
       'был обезглавлен.',
    3: '<b>Интересный факт:</b>\nЗа год ты съедаешь 2,5 тюбика помады. Это при условии, что ты наносишь ее 1−2 раза в '
       'день. Если поправлять макияж чаще,количество съеденного больше. Но не волнуйся: калорийность помады — всего 8 '
       'калорий на 100 граммов, так что ешь на здоровье!',
    4: '<b>Интересный факт:</b>\nИзначально отращивать ногти стало модным в Китае. Таким образом девушки из '
       'благородных семейств подчеркивали, насколько далеки они от любых домашних обязанностей. Чем длиннее ногти — '
       'тем реже их обладательница что-то делала руками. Некоторым удавалось отрастить «ноготочки» в 25 сантиметров!',
    5: '<b>Интересный факт:</b>\nВ Великобритании времен королевы Виктории использовать косметику считалось жутким '
       'моветоном. Бледная кожа, бледные губы и в целом бледный вид считались признаком утонченности, использование '
       'помад и румян считалось вульгарным и недопустимым способом привлекать к себе внимание.',
    6: '<b>Интересный факт:</b>\nКонтуринг появился в 17 веке. Правда, своеобразный: девушки корректировали овал '
       'лица, приподнимая скулы, просто кладя за щеку шарик из пробкового дерева.',
    7: '<b>Интересный факт:</b>\nСенат Франкфурта-на-Майне в свое время издал указ, согласно которому мужчина мог '
       'расторгнуть брак с супругой, если выяснялось, что при помощи макияжа она выглядела красивее, чем оказывалось '
       'на самом деле (до свадьбы вероятность увидеть невесту не при параде стремилась к нулю). Вот такой факт о '
       'косметике: обманщицу судили за колдовство(!!!), а мужчина получал свободу незамедлительно.',
    8: '<b>Интересный факт:</b>\nЕкатерина Медичи (королева Франции с 1547 по 1559 год) запретила брюнеткам появляться '
       'при дворе. Одним из ключевых '
       'условий для приглашения на королевский бал или устройство на работу при дворе было наличие натуральных '
       'светлых вьющихся волос. Считается, что технология осветления волос с помощью различных химических растворов '
       'возникла именно тогда.',
    9: '<b>Интересный факт:</b>\nНа Руси существовала косметика для ягодиц. Потому что изначально ягодицами назывались '
       'щеки. Красавицы натирали их листьями травы «синяк красный» (ничего так название, да?), и краска держалась '
       'несколько дней.',
    10: '<b>Интересный факт:</b>\nДля коррекции бровей использовали мышей. В 18 веке в Европе вошли в моду широкие и '
        'густые брови. Чтобы выглядеть стильно, дамы сбривали собственные брови, а на их место наклеивали '
        'искусственные, сделанные из мышиных шкурок.',
    11: '<b>Интересный факт:</b>\nВ 1930-м году был в моде радиоактивный макияж. В моде были средства, содержащие '
        'бромистый радий и хлористый торий! Торговые марки с гордостью рекламировали тот факт, что в составе их '
        'средств — радиоактивные вещества.',
    12: '<b>Интересный факт:</b>\nСегодня натуральным составом духов можно удивить '
        '— самые известные и стойкие ароматы мира созданы с применением синтетических веществ. А когда-то натуральный '
        'состав парфюма был нормой.В Древнем Египте были очень популярны духи под названием Kyphi. Они были созданы '
        'на основе меда, цветов, ягод и вина. Египтяне не только душились ими, но и употребляли внутрь, духи вызывали '
        'легкое опьянение.',
    13: '<b>Интересный факт:</b>\nПервые тени для век появились не для того, чтобы сделать женщину прекраснее. '
        'Этот продукт красоты задумывался как профилактическое средство, призванное уберечь своего обладателя от '
        'воспалений слизистой оболочки глаза — конъюнктивита.',
    14: '<b>Интересный факт:</b>\nПомада является не просто широко растиражированным бьюти-трендом, но и самым '
        'продаваемым продуктом всех '
        'времен! В 18 веке красный оттенок помады считался символом куртизанок, а в начале 20-го — знаком протеста '
        'у суфражисток! Новая глава в истории красной помады — эпоха самой Мерлин Монро. Культовая блондинка '
        'превратила алые губы в свой фирменный знак отличия. Теперь красная помада в макияже — стопроцентная '
        'классика, а ведущие визажисты с завидной периодичностью экспериментируют в своих коллекциях макияжа с '
        'алой палитрой. Абсолютный тренд сегодняшнего дня — сочные ягодные губы с сияющим тоном и пышными ресницами. '
        'Кроме того, из сезона в сезон меняется и способ нанесения помады - так последние годы прочно удерживает '
        'лидерство градиент, а также эффект зацелованных губ.',
    15: '<b>Интересный факт:</b>\nРоботы добрались и до бьюти-индустрии! Так вот, уже несколько компаний создали '
        'гаджеты, которые представляют собой принтер для макияжа. Он был создан для того, чтобы девушки не тратили '
        'много времени на нанесение макияжа. С помощью принтера можно выбрать свой стиль. Сам процесс нанесения '
        'макияжа очень интересный: пользователю необходимо прислонить лицо, после чего система сканирует общую '
        'геометрию и все неровности кожи, а затем наносит макияж с помощью 2 000 микро сопел. Наносится макияж '
        'несколькими слоями.',
    16: '<b>Интересный факт:</b>\nПо данным агентства Research & Markets, в ближайшие 5 лет рынок косметических услуг '
        'для старших поколений вырастет на 58% и достигнет почти 80 млрд. долларов. Старение сейчас стало одним из '
        'самых ключевых направлений бьюти-индустрии! Поэтому всё больше бьюти-компаний используют в качестве моделей '
        'известных женщин в возрасте 45+.',
    17: '<b>Секрет красоты девушек в Турции:</b>\nВ Турции айран употребляют не только в пищу, но также используют '
        'для лица.Способ приготовления: несколько столовых ложек айрана соедините с одной каплей эфирного масла '
        'лаванды. Такой состав можно использовать и в качестве маски, и в качестве тоника для лица. Айран прекрасно '
        'увлажняет кожу, а лаванда придает свежесть и румянец.',
    18: '<b>Французская маска для упругости лица и тела:</b>\nСмешайте 50 мл молока и 1 стакан минеральной воды. '
        'Такой коктейль наносят на всю поверхность лица и тела. Оставляют на 15 минут. Результатом такой маски '
        'является питание, смягчение и увлажнение кожи.',
    19: '<b>Английская маска для молодости рук:</b>\nСмешайте использованную чайную заварку с солью и медом, примерно '
        'в равных пропорциях. Нанесите на чистые влажные руки. Оставьте на 20-30 минут. Смойте и нанесите на влажную '
        'кожу питательный крем.',
    20: '<b>Малазийский любовный эликсир для лица и тела:</b>\nСмешайте 1/4 стакана кокосовой стружки с 1/2 стакана '
        'порошка какао, добавьте три столовые ложки оливкового масла и несколько капель эфирного масла "иланг-иланг". '
        'Нанесите на влажную кожу лица и тела на 20-40 минут. Смойте теплой водой. После такого состава ваша кожа '
        'засияет и скажет вам большое спасибо.',
    21: '<b>Интересный факт:</b>\nГубная помада считалась незаменимым предметом для медсестер в вооруженных силах '
        'во время Второй мировой войны, поскольку она напоминала женщинам, что они в первую очередь женщины, а во '
        'вторую — военная, а также потому, что она могла иметь успокаивающее действие на солдат-мужчин. '
        '(Хотя сейчас большинство экспертов говорят, что парней по-настоящему возбуждает, когда девушка носит '
        'красную помаду).',
    22: '<b>Интересный факт:</b>\nДо того, как L’Oréal выпустили в 1960 году первый массовый лак для волос, женщинам '
        'приходилось выбирать между причесыванием волос жирным бриллиантином или нанесением на них механического '
        'распылителя шеллака, растворенного в растворе воды и спирта.',
    23: '<b>Интересный факт:</b>\nИсследование 1991 года показало, что женщины-политики, которые нанимали '
        'голливудских визажистов и фотографов, имели на 30% больше шансов выиграть выборы, просто причесав брови, '
        'надев блузки определенных цветов и улыбнувшись.',
    24: '<b>Интересный факт:</b>\nОрганический макияж — понятие, ставшее популярным в начале 2000-х, когда в тренд '
        'вошла экомода. В целом для биомакияжа используется косметика на натуральной основе. Однако четких и общих '
        'мировых правил о том, каким должен быть органический макияж практически не существует. У каждой страны можно '
        'встретить свои требования к органическим продуктам косметики. Нередко слово «органический» или «природный», '
        'которое красуется на упаковках, является лишь очередным рекламным ходом.',
    25: '<b>Интересный факт:</b>\nТоповые бренды косметики — это предприятия с фабриками и офисами по всему миру, '
        'которые зарабатывают миллионы долларов в год от продажи помад, пудры и туши и других подобных продуктов. '
        'Косметическая промышленность в целом стоит около 200 миллиардов долларов в год и входит в десятку самых '
        'крупных отраслей в мире.',
    26: '<b>Интересный факт:</b>\nВ отличие от фармацевтической промышленности косметика и ее производство не так '
        'жестко контролируются, и строгих правил тестирования косметической продукции практически нет. По примерной '
        'статистике, около 80% ингредиентов, используемых в косметических продуктах для макияжа, никогда не '
        'подвергались надлежащим клиническим испытаниям на людях.',
    27: '<b>Интересный факт:</b>\nКосметика с цветочными ароматами — одна из самых покупаемых. Однако в большинстве '
        'подобных продуктах содержатся ароматы, полученные не из натуральных цветов, а с помощью химических веществ в '
        'лаборатории. На сегодняшний день люди научились искусственно получать практически все известные ароматы '
        'парфюмерии и косметики. Продукция с натуральными экстрактами растений и цветов, как правило, стоит на '
        'порядок дороже.',
    28: '<b>Интересный факт:</b>\nСогласно международным исследованиям, в Европе больше и чаще всего покупают '
        'косметику именно россиянки. Они тратят на это дело (помимо салонных и клинических процедур) около 180-210$ '
        'в год. К примеру, жительницы Франции и Англии раскошеливаются на «красоту» примерно на 160-170$ в год, а '
        'немки и того меньше — всего 150$. В России самый большой оборот косметической промышленности — около 15 млрд '
        'американских долларов в год.',
    29: '<b>Интересный факт:</b>\nНа зарубежной, а иногда и на российской косметике можно встретить такие пометки, '
        'как «cruelty-free» — «произведены без насилия и сделаны с любовью». Однако эти факты не имеют реального '
        'смысла, поскольку понятия «насилие» и «жестокость» могут восприниматься по-разному. То, что один человек '
        'считает жестоким, другому покажется вполне приемлемым. Поэтому покупка продукции с такими пометками ничего '
        'особо не гарантирует.',
    30: '<b>Интересный факт:</b>\nВ местечке Морризвилл, что в штате Пенсильвания, официально приняли закон, '
        'согласно которому женщины в этом городе не могут носить макияж в общественных местах без специального на то '
        'разрешения. Конечно, в наши дни этот закон соблюдается не так строго, как в прошлом веке, но все же он '
        'продолжает существовать, поэтому в Морризвилле за макияж можно получить настоящий штраф.',
    31: '<b>Интересный факт:</b>\nНесмотря на то, что у помады в настоящее время существуют разные конкуренты '
        '(блески, тинты, бальзамы, лаки для губ), мировые продажи помады остаются одними из самых впечатляющих — '
        'около 900 000 000 штук в год. Это делает помаду одним из самых востребованных косметических средств для '
        'макияжа.',
    32: '<b>Интересный факт:</b>\nОдна из самых дорогих помад в мире — KissKiss Gold and Diamonds от Guerlain. Ее '
        'примерная стоимость — 62 000 долларов. В то время как обычная помада KissKiss от той же компании стоит '
        'всего 34 доллара. Причина такой высокой цены кроется в дорогих металлах, которые были использованы для '
        'производства упаковки KissKiss Gold and Diamonds: 110 г золота и 199 бриллиантов (2,2 карата). В качестве '
        'бонуса покупатель получает в подарок 15 эксклюзивных оттенков этой помады.',
    33: '<b>Интересный факт:</b>\nДавно известно, что многие косметические продукты пусть и в малых дозах, но '
        'содержат химические вещества, вредные для человеческого организма. Поэтому слишком злоупотреблять '
        'косметикой и макияжем не стоит. Помимо токсичных ингредиентов, косметика для лица может содержать не совсем '
        'обычные компоненты: животные жиры, овечий пот, бычий мозг и сперму. Один из ингредиентов остается неизменным '
        'уже долгие годы — это рыбья чешуя. Ее используют во многих косметических продуктах для придания коже блеска.',
    34: '<b>Интересный факт:</b>\nВыбирая косметику в магазине, женщины часто пробуют ее наносить на руки, полагая, '
        'что это наиболее простой и доступный способ протестировать цвет и текстуру продукции. Однако кожа на лице и '
        'руках существенно отличаются друг от друга. Оттенок помады, нанесенный на кисти рук, может не совпадать с '
        'тем, который будет потом на губах. По сравнению с лицом, руки больше подвержены воздействию УФ-излучения и '
        'обычно имеет более темный оттенок, чем кожа лица. Некоторые визажисты советуют пробовать косметику не на '
        'кистях рук, а на подушечках пальцев, поскольку их оттенок больше приближен к цвету лица. Кожа на пальцах '
        'мягче и нежнее. Она менее подвержена излучению солнца, поэтому больше совпадает с кожей лица по текстуре и '
        'цвету. Во избежание заражения инфекциями никогда не стоит наносить макияж на лицо с помощью тестеров. '
        'Желательно всегда брать с собой в магазин дезинфицирующие салфетки.',
    35: '<b>Интересный факт:</b>\n«Без парабенов» - увидели? Не ведитесь - это маркетинг и не более! Вместо '
        'консерванта здесь значит просто использовали другое вещество и это не говорит о том, что средство более '
        'натуральное (кстати, вред парабенов на сегодняшний день научно не доказан).',
    36: '<b>Интересный факт:</b>\n«Органический», «природный», «натуральный» - мы часто видим такие надписи на '
        'любимых баночках. На сегодняшний день пока ещё нет конкретных требований к косметике категории БИО или ЭКО. '
        'Да и вообще, у каждой страны эти критерии свои. Поймите, невозможно исключить применение консервантов, так '
        'как средства только из органических веществ будут иметь ну очень короткий срок годности и очень строгие '
        'условия хранения!',
    37: '<b>Интересный факт:</b>\nБотокс! Раннее применение может вызывать преждевременное старение кожи! Вот в '
        'чём дело: ткани лица достаточно быстро изнашиваются и истончаются. И используя процедуру до 30 лет, '
        'снижается собственный тонус лицевых мышц. Поэтому не злоупотребляйте ботоксом и используйте только для '
        'решения конкретной проблемы!',
    38: '<b>Интересный факт:</b>\nЕсли один и тот же бренд или марка произведены для разных стран, их качество '
        'различается. Почему? У всех стран есть свои стандарты качества и, конечно, они у всех разные. Стандарты у '
        'Европы выше, чем у России и стран СНГ.',
    39: '<b>Интересный факт:</b>\nCтоимость косметики не равнозначна себестоимости состава и не гарантирует того, '
        'что она сделана только из натуральных веществ! Цена косметики сильно завязана на узнаваемости и престижности '
        'бренда. И иногда более дешевые средства могут оказаться куда эффективнее дорогих аналогов.',
    40: '<b>Полезный совет:</b>\nВо время насморка мы часто сталкиваемся с возникновением сухости и шелушения кожи '
        'носа, чтобы избавиться от этого - используйте обычную гигиеническую помаду (она справится гораздо лучше, '
        'чем крем).',
    41: '<b>Полезный совет:</b>\nОгурцы помогут избавиться от отёков и мешков под глазами не хуже косметических '
        'средств! Они содержат антиоксиданты и особые ферменты, уменьшающие припухлости и раздражение!',
    42: '<b>Полезный совет:</b>\nНельзя наносить ночной крем непосредственно перед сном, особенно крем вокруг глаз! '
        'Утром вы можете проснуться с отёками. Используйте ночной крем за 1,5–2 часа до сна. И не забывайте про '
        'очищение!',
    43: '<b>Интересный факт:</b>\n«Косметика» с греческого от слова «космос» - означает «украшать» (журнал '
        '«Cosmopolitan» использует его в своём названии).',
    44: '<b>Интересный факт:</b>\nПрофессия косметолога возникла впервые в Древней Греции. Человек, который с помощью '
        'специальных средств помогал женщинам устранить дефекты кожи, назывался «косметом». Он прописывал массаж, '
        'водные процедуры, кремы, а также помогал маскировать изъяны при помощи косметики.',
    45: '<b>Интересный факт:</b>\nВ Риме косметике уделялось столь большое значение, что Сенат вынужден был принять '
        'законы, ограничивающие ввоз ее из других стран, так как закупка косметических средств из Египта, Китая, '
        'стран Аравии серьезно ударила по казне. Стремящихся к красоте римских женщин не пугало ничего, даже пигменты '
        'из различных ядовитых веществ (вроде киновари), которые содержались в прообразе губной помады.',
    46: '<b>Интересный факт:</b>\nПомаду впервые использовали в Месопотамии и изготавливали ее из красного пигмента, '
        'пчелиного воска и жира животного происхождения. Позднее помада появилась в Древнем Египте, Греции и Риме. '
        'Само слово «помада» происходит от латинского pomum, что буквально означает «яблоко». Именно из яблок '
        'изготавливались первые помады для губ.',
    47: '<b>Интересный факт:</b>\nХристианская церковь крайне отрицательно относилась к любым изменениям во внешности '
        'и обвиняла в святотатстве женщин, пользующихся косметикой. Также был издан закон, считавший недействительным '
        'брак, в который женщина вовлекала мужчину, не демонстрируя свой естественный вид и скрывая косметикой '
        'недостатки. Такую женщину обвиняли в колдовстве.',
    48: '<b>Интересный факт:</b>\nЛак для ногтей был изобретен в Китае в 30 веке до н.э. Длинные ногти считались '
        'признаком высшего сословия. Для демонстрации того, что они не занимаются ручным трудом, женщины отращивали '
        'ногти длиною до 25 сантиметров, а мужчины видели в длинных ногтях амулет от зла.',
    49: '<b>Интересный факт:</b>\nВ XVII веке в моду вошла пудра — ее накладывали на волосы и лицо как мужчины, '
        'так и женщины. Позднее стали использоваться мушки и накладные брови из кусочков мышиных шкурок, а за щеки '
        'прятали пробковые шарики, чтобы подчеркнуть округлость лица. Предстать в обществе в своем естественном виде '
        'считалось верхом неприличия.',
    50: '<b>Интересный факт:</b>\nПервая компания, выпустившая тушь для ресниц, была «Юджин Риммель» в XIX веке. '
        'Rimmel переводится как «тушь» с португальского, турецкого, румынского и других языков. Первая современная '
        'тушь (1913 год) была создана химиком Уильямсом для своей сестры Мабель и представляла собой смесь угольной '
        'сыпи и вазелина. От соединения имени Mabel и названия компонента туши — Vaseline — появилось название одной '
        'из ведущих косметических компаний Maybelline. Упаковка туши получила нынешний вид (туба) лишь 40 лет спустя, '
        'благодаря Елене Рубенштейн.',
    51: '<b>Интересный факт:</b>\nЕдиница измерения красоты называется «миллиелен». В честь Елены Троянской, которая '
        'по легенде, была настолько красива, что сдвинула с места тысячу кораблей. Мера конечно же шуточная и '
        'красоту ей никто не измеряет.',
    52: '<b>Интересный факт:</b>\nЛюди покупают продукцию меньше, если в рекламе слишком красивые модели. Идеально '
        'выглаженные волосы или тело без единого изъяна. Аудитории хочется видеть натуральность и естественность. '
        'Ведь каждый красив по-своему.',
    53: '<b>Интересный факт:</b>\nСуществует синдром, при котором переизбыток красоты вызывает у человека '
        'головокружение, учащенное сердцебиение и галлюцинации. Это называется синдром Стендаля. Этому подвержены '
        'впечатлительные люди. Как правило, такие симптомы возникают при созерцании искусства, прослушивании музыки '
        'или любовании архитектурой. Так что будьте осторожны. Красота штука опасная.',
    54: '<b>Интересный факт:</b>\nМеждународный день красоты отмечают 9 сентября.',
    55: '<b>Интересный факт:</b>\nСамый необычный конкурс красоты прошел в ОАЭ. Выбирали самого красивого верблюда.',
    56: '<b>Интересный факт:</b>\nНа групповом фото человек выглядит более симпатичным, чем на индивидуальных.',
    57: '<b>Интересный факт:</b>\nВ племени майя косоглазие считалось неоспоримым признаком красоты.',
    58: '<b>Интересный факт:</b>\nЖенщины племени падаунг, для красоты удлиняют свою шею с помощью колец из латуни.',
    59: '<b>Интересный факт:</b>\nБольший процент привлекательных людей считает себя счастливыми.',
    60: '<b>Интересный факт:</b>\nЛевая сторона лица красивее, чем правая.',
    61: '<b>Интересный факт:</b>\nЗарплаты у красавчиков на 5% выше, чем у их коллег с заурядной внешностью.',
    62: '<b>Интересный факт:</b>\nУровень интеллекта у красивых людей в среднем выше на 11 пунктов.',
    63: '<b>Интересный факт:</b>\nТолько 10% женщин имеют фигуру в форме песочных часов.',
    64: '<b>Интересный факт:</b>\nЖенщины находят улыбающихся мужчин менее привлекательными.',
    65: '<b>Интересный факт:</b>\nБольшинству мужчин привлекательными кажутся женщины, чьи лица наделены детскими '
        'чертами.',
    66: '<b>Интересный факт:</b>\nВ результате эволюции женщины становятся привлекательней, а мужская внешность не '
        'подвержена столь радикальным изменениям.',
    67: '<b>Интересный факт:</b>\nВ эпоху Людовика XIV придворные дамы украшали свое лицо накладными мушками, '
        'маскируя так шрамы от оспы.',
    68: '<b>Интересный факт:</b>\nНа Востоке до самой середины XX века ярким признаком женской красоты считались '
        'черные зубы. Окрашенные таким образом зубы дольше оставались здоровыми.',
    69: '<b>Интересный факт:</b>\nВ Китае признаком мужской красоты являются густые усы и борода.',
    70: '<b>Интересный факт:</b>\nПридворные француженки питались исключительно протертыми супами, так как считали, '
        'что пережевывание пищи способствует появлению морщин.',
    71: '<b>Интересный факт:</b>\nВ Китае маленький размер ноги считался одним из главных признаков красоты. Девочкам '
        'туго бинтовали стопы, те деформировалась и в обуви казались миниатюрными.',
    72: '<b>Интересный факт:</b>\nВ Японии в моде цветные линзы, которые делают женщин похожими на героинь аниме.',
    73: '<b>Интересный факт:</b>\nПо версии гонконгского журнала Travelers Digest самые красивые мужчины живут в '
        'Швеции, а украинки возглавили женский рейтинг.',
    74: '<b>Интересный факт:</b>\nКлассические японские красавицы имеют плоскую грудь, длинную шею, короткие и '
        'кривоватые ноги.',
    75: '<b>Интересный факт:</b>\nВ мире наиболее популярной пластической операцией является липосакция.',
    76: '<b>Интересный факт:</b>\nВ пластической хирургии ринопластика стоит на первом месте по популярности у мужчин.',
    77: '<b>Интересный факт:</b>\nПервый Всемирный конкурс красоты состоялся в городе Спа в 1888 году.',
    78: '<b>Интересный факт:</b>\nВ Турции светловолосые и голубоглазые барышни автоматически считаются красивыми.',
    79: '<b>Интересный факт:</b>\nВ Конго настоящая красавица не может иметь во рту ни одного зуба.',
    80: '<b>Интересный факт:</b>\nДля мусульманок выщипывание бровей находится под строжайшим запретом.',
    81: '<b>Интересный факт:</b>\nВо многих африканских странах ради красоты, женщины покрывают свое тело множеством '
        'шрамов.',
    82: '<b>Интересный факт:</b>\nЧаще всего титул Мисс Мира доставался представительницам Венесуэлы.',
    83: '<b>Интересный факт:</b>\nМодели 90-х были на 8% легче среднестатистических американок, сейчас эта разница '
        'выросла до 23%.',
    84: '<b>Интересный факт:</b>\nВеснушки украшают женщину, так считает 75% мужчин.',
    85: '<b>Совет:</b>\nНе стоит принимать горячие ванны накануне выхода из дома, например, перед важным мероприятием, '
        'иначе покраснения на лице обеспечены. То же относится к пилингам и скрабам, даже мягким. Очищайте лицо '
        'абразивами за 1–2 дня до предполагаемого события. По утрам полезно просто умыться прохладной водой без '
        'применения очищающих средств.',
    86: '<b>Совет:</b>\nРасчесывайте брови не по росту волосков, а двигаясь вверх или по диагонали. Так они будут '
        'казаться объемнее.',
    87: '<b>Совет:</b>\nЕсли у вас постоянно трескаются и шелушатся губы, возможно, вам не хватает воды. Пейте '
        'достаточно жидкости в течение дня — до 1,5–2 литров чистой воды.',
    88: '<b>Совет:</b>\nУвлажняющие маски лучше держать в холодильнике. Следите, чтобы тюбики были герметично закрыты.',
    89: '<b>Совет:</b>\nТщательно мойте кисти и спонжи для макияжа не реже 1 раза в неделю. Для этого подойдет обычный '
        'шампунь, после чего нужно промокнуть их полотенцем.',
    90: '<b>Совет:</b>\nНаносите крем для век всегда слабым пальцем — безымянным или мизинцем. Так вы не растянете '
        'кожу под глазами.',
    91: '<b>Совет:</b>\nУдалить следы от неровно нанесенного автозагара поможет оливковое масло и скраб.',
    92: '<b>Совет:</b>\nЕсли в любимой туши для ресниц появились комочки, не торопитесь ее разбавлять. Оптимальный '
        'способ — подогреть закрытый тюбик в стакане с теплой водой.',
    93: '<b>Совет:</b>\nНаносите лосьоны и кремы для тела сразу после душа на слегка влажную кожу.',
    94: '<b>Совет:</b>\nЧтобы помада держалась идеально, регулярно отшелушивайте кожу губ. Но не перебарщивайте со '
        'скрабами. Идеально для этого подойдет (отдельная) зубная щетка с мягкой щетиной.',
    95: '<b>Совет:</b>\nПодпиливая ногти, двигайте пилочку в одном направлении, а не «туда-сюда». Это поможет '
        'избежать расслаивания ноготка.',
    96: '<b>Совет:</b>\nСмягчить сухую и грубую кожу стоп поможет старый-добрый вазелин. Его нужно нанести на ночь '
        'и надеть носочки. Утром вы не узнаете ваши ножки.',
    97: '<b>Совет:</b>\nЛимонный сок отбелит пожелтевшие кончики ногтей.',
    98: '<b>Совет:</b>\nНанося вечерний макияж, помните: акцент либо на глаза, либо на губы. Если ярко накрасить то, '
        'и то, образ может получиться грубым.',
    99: '<b>Совет:</b>\nЕсли у вас есть привычка перебарщивать с духами, попробуйте следующую хитрость: распылите '
        'парфюмерную воду в воздух (точно над головой) и встаньте под «водопад» капель. Аромат попадет на волосы и '
        'одежду и будет очень деликатным и тонким, как надо.',
    100: '<b>Совет:</b>\n'
}
