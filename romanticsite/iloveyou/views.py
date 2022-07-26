from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from .models import *
import random as rand
from django.views import View
from django.views.generic import ListView


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
# ------------------------------------------------------------------
def home(request):
    context = {
        'title': 'Дашка',
        'url': 'question1',
        'proffer': 'Этот тест был сделан для Дарьи Расолько!',
        'question': 'Готова приступить к нему?',
        'right': '123qwe',
    }

    return render(request, 'iloveyou/options.html', context)
# ------------------------------------------------------------------
def question1(request):
    context = {
        'title': 'Дашка',
        'url': 'question1_t',
        'ago': 'home',
        'proffer': 'Вопрос 1',
        'question': 'В каком году мы познакомились?',
    }
    if request.method == 'POST':
        form = request.POST
        answer = form['answer']
        if answer == '2020':
            context['right'] = 'Молодец, так держать'
        else:
            context['error'] = 'Подумай еще'

    return render(request, 'iloveyou/answer.html', context)

def question1_t(request):
    post = Question.objects.get(title='qest1')
    context = {
        'post': post,
        'proffer': 'Первый вопрос осилила',
        'proffer2': 'А если быть точным то 17 октября 2020 года:)',
        'title': 'Дашка',
        'url': 'question2',
        'ago': 'question1',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question2(request):
    context = {
        'title': 'Daria',
        'url': 'question2_t',
        'ago': 'question1_t',
        'proffer': 'Вопрос 2',
        'question': 'Где мы впервые с тобой встретились?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Все ответы верны'},
            'no2': {'values': 'Как бы верно но не совсем', 'name_button': 'Возле магазина ZOObazar'},
            'no3': {'values': 'Подумай еще', 'name_button': """53°52'05.4"N 27°36'00.2"E"""},
            'no4': {'values': 'Не совсем так', 'name_button': "По адресу проспект Рокоссовского 62"},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'А ты не промах! Все верно'

    return render(request, 'iloveyou/options.html', context)

def question2_t(request):
    post = Question.objects.get(title='qest2')
    context = {
        'post': post,
        'proffer': 'Второй вопрос осилила',
        'proffer2': 'Это место изменило все!',
        'title': 'Дашка',
        'url': 'question3',
        'ago': 'question2',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question3(request):
    context = {
        'title': 'Daria',
        'url': 'question3_t',
        'ago': 'question2_t',
        'proffer': 'Вопрос 3',
        'question': 'В каком маке я работал до знакомства?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Ни в каком, я просто соврал'},
            'no2': {'values': 'не правда', 'name_button': 'Который на ст.м. Октябрьская'},
            'no3': {'values': 'Не угадала', 'name_button': 'Который на ст.м. Пушкинская'},
            'no4': {'values': 'Ты не права', 'name_button': 'Я вообще работал в БургерКинг'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Правильно, я просто соврал как и ты про то, что работала в ментовке'

    return render(request, 'iloveyou/options.html', context)

def question3_t(request):
    post = Question.objects.get(title='qest3')
    context = {
        'post': post,
        'proffer': 'Третий вопрос осилила',
        'proffer2': 'Хоть в маке я и не работал но фастфуды мы любим!',
        'title': 'Дашка',
        'url': 'question4',
        'ago': 'question3',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question4(request):
    context = {
        'title': 'Daria',
        'url': 'question4_t',
        'ago': 'question3_t',
        'proffer': 'Вопрос 4',
        'question': 'Где было наше первое свидание?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Сначала в лошицком парке потом в кфс'},
            'no2': {'values': 'Подумай еще', 'name_button': 'Сначала в кфс потом в лошицком парке'},
            'no3': {'values': 'От части верно', 'name_button': 'В лошицком парке'},
            'no4': {'values': 'Не совсем так', 'name_button': 'В кфс'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Молодец, ты все помнишь'

    return render(request, 'iloveyou/options.html', context)

def question4_t(request):
    post = Question.objects.get(title='qest4')
    context = {
        'post': post,
        'proffer': 'Четвертый вопрос осилила',
        'proffer2': 'Начало было положено здесь!',
        'title': 'Дашка',
        'url': 'question5',
        'ago': 'question4',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question5(request):
    context = {
        'title': 'Daria',
        'url': 'question5_t',
        'ago': 'question4_t',
        'proffer': 'Вопрос 5',
        'question': 'Где был наш первый поцелуй?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'В машине возле твоего подъезда'},
            'no2': {'values': 'Не совсем так', 'name_button': 'Возле твоего подъезда'},
            'no3': {'values': 'Не правда', 'name_button': 'Внутри подъезда'},
            'no4': {'values': 'Подумай еще', 'name_button': 'В тамбуре'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Молодец, именно там все произошло, после того как я помог тебе с подарком для твоей мамы'

    return render(request, 'iloveyou/options.html', context)

def question5_t(request):
    post = Question.objects.get(title='qest5')
    context = {
        'post': post,
        'proffer': 'Пятый вопрос осилила',
        'proffer2': 'Немного нашей милоты:)',
        'title': 'Дашка',
        'url': 'question6',
        'ago': 'question5',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question6(request):
    context = {
        'title': 'Daria',
        'url': 'question6_t',
        'ago': 'question5_t',
        'proffer': 'Вопрос 6',
        'question': 'Где мы взяли елку на 2021 Новый Год?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Срубили в лесу в Уручье'},
            'no2': {'values': 'Подумай еще', 'name_button': 'Купили в магазине'},
            'no3': {'values': 'Это было на НГ 2022', 'name_button': 'Взяли у тебя на дачу'},
            'no4': {'values': 'Не правильно', 'name_button': 'Встречали НГ без елки'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Молодец, так держать'

    return render(request, 'iloveyou/options.html', context)

def question6_t(request):
    post = Question.objects.get(title='qest6')
    context = {
        'post': post,
        'proffer': 'Шестой вопрос осилила',
        'proffer2': 'Новый год 2021 был наш первый Новый Год:)',
        'title': 'Дашка',
        'url': 'question7',
        'ago': 'question6',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question7(request):
    context = {
        'title': 'Дашка',
        'url': 'question7_t',
        'ago': 'question6_t',
        'proffer': 'Вопрос 7',
        'question': 'Что такое космос?',
    }
    if request.method == 'POST':
        form = request.POST
        answer = form['answer']
        if answer in ['Саша', 'саша', 'Санька', 'санька', 'Сашка', 'сашка', 'Сашулик', 'сашулик']:
            context['error'] = 'Попробуй написать полное имя'
        elif answer in ['Александр', 'александр']:
            context['right'] = 'Молодец, валишь будь здоров!'
        elif answer != ['Саша', 'саша', 'Санька', 'санька', 'Сашка', 'сашка', 'Сашулик', 'сашулик']:
            context['error'] = 'Даю подсказку, это чье-то мужское имя'

    return render(request, 'iloveyou/answer.html', context)

def question7_t(request):
    post = Question.objects.get(title='qest7')
    context = {
        'post': post,
        'proffer': 'Седьмой вопрос осилила',
        'proffer2': 'Космос это я:)',
        'title': 'Дашка',
        'url': 'question8',
        'ago': 'question7',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question8(request):
    context = {
        'title': 'Daria',
        'url': 'question8_t',
        'ago': 'question7_t',
        'proffer': 'Вопрос 8',
        'question': 'Какая марка и модель моей машины?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Mercedes w203'},
            'no2': {'values': 'У меня поновее', 'name_button': 'Mercedes w202'},
            'no3': {'values': 'Хотелось бы, но у меня постарше', 'name_button': 'Mercedes w204'},
            'no4': {'values': 'Вообще то я мерсовод', 'name_button': 'BMW f10'},
            'no5': {'values': 'right', 'name_button': 'Красивая, серенькая'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Именно такая у меня машина'

    return render(request, 'iloveyou/options.html', context)

def question8_t(request):
    post = Question.objects.get(title='qest8')
    context = {
        'post': post,
        'proffer': 'Восьмой вопрос осилила',
        'proffer2': 'Это наш член семьи, Мерсик:)',
        'title': 'Дашка',
        'url': 'question9',
        'ago': 'question8',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question9(request):
    context = {
        'title': 'Дашка',
        'url': 'question9_t',
        'ago': 'question8_t',
        'proffer': 'Вопрос 9',
        'question': 'Какой у нее гос номер (4 цифры)? не подсматривать!',
    }
    if request.method == 'POST':
        form = request.POST
        answer = form['answer']
        if answer == '8371':
            context['right'] = 'Молодец'
        elif answer != 'Саша':
            context['error'] = 'Не правильно, вспоминай'

    return render(request, 'iloveyou/answer.html', context)

def question9_t(request):
    context = {
        'title': 'Дашка',
        'url': 'question10',
        'ago': 'question9',
        'proffer': 'Девятый вопрос осилила',
        'proffer2': 'Но я все равно уверен что ты подсмотрела, Вонючка:)',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question10(request):
    context = {
        'title': 'Дашка',
        'url': 'question10_t',
        'ago': 'question9_t',
        'proffer': 'Вопрос 10',
        'question': 'Какой пароль от моего телефона?',
    }
    if request.method == 'POST':
        form = request.POST
        answer = form['answer']
        if answer != '671940':
            context['error'] = 'Даю подсказку, пароль связан с номером телефона)'
        elif answer == '671940':
            context['right'] = 'Молодец, ты справилась'

    return render(request, 'iloveyou/answer.html', context)

def question10_t(request):
    context = {
        'title': 'Дашка',
        'url': 'question11',
        'ago': 'question10',
        'proffer': 'Десятый вопрос осилила',
        'proffer2': 'Неплохо справляешься, продолжай в том же духе, Мышка-сосиска:)',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question11(request):
    context = {
        'title': 'Дашка',
        'url': 'question11_t',
        'ago': 'question10_t',
        'proffer': 'Вопрос 11',
        'question': 'Какую еврейскую кличку я тебе дал с недавних пор?',
    }
    if request.method == 'POST':
        form = request.POST
        answer = form['answer']
        if answer not in ['Жидик', 'жидик', 'Жидок', 'жидок']:
            context['error'] = 'Даю подсказку, слово начинается на жи...'
        elif answer in ['Жидик', 'жидик', 'Жидок', 'жидок']:
            context['right'] = 'Ну ты конечно молоток!'

    return render(request, 'iloveyou/answer.html', context)

def question11_t(request):
    post = Question.objects.get(title='qest11')
    context = {
        'post': post,
        'proffer': 'Одиннадцатый вопрос осилила',
        'proffer2': 'Посмотри на эти фото, и потом не говори что не похожа:)',
        'title': 'Дашка',
        'url': 'question12',
        'ago': 'question11',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question12(request):
    context = {
        'title': 'Daria',
        'url': 'question12_t',
        'ago': 'question11_t',
        'proffer': 'Вопрос 12',
        'question': 'Кто круче Соня или Бубен?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Бубен'},
            'no2': {'values': 'Как ты посмела такое выбрать? Не верно', 'name_button': 'Соня'},
            'no3': {'values': 'Кто то один из них круче', 'name_button': 'Оба хороши'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Правильно, он кому угодно горло перегрызет'

    return render(request, 'iloveyou/options.html', context)

def question12_t(request):
    post = Question.objects.get(title='qest12')
    context = {
        'post': post,
        'proffer': 'Двенадцатый вопрос осилила',
        'proffer2': 'Вот для примера Сонька обосранка и Бубен милашка:)',
        'title': 'Дашка',
        'url': 'question13',
        'ago': 'question12',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question13(request):
    context = {
        'title': 'Daria',
        'url': 'question13_t',
        'ago': 'question12_t',
        'proffer': 'Вопрос 13',
        'question': 'Кого Сашка любит сильнее: Мерса, Бубена или Дашку?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Всех люблю, но Данюньку больше всех'},
            'no2': {'values': 'Его тоже люблю, но ответ не верный', 'name_button': 'Конечно Мерсик'},
            'no3': {'values': 'Его тоже люблю, но подумай еще', 'name_button': 'Бубена милашку'},
            'no4': {'values': 'Ее тоже очень люблю, но и остальных тоже люблю', 'name_button': 'Дашку какашку=)'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Молодец, это правильный ответ'

    return render(request, 'iloveyou/options.html', context)

def question13_t(request):
    post = Question.objects.get(title='qest13')
    context = {
        'post': post,
        'title': 'Дашка',
        'url': 'question14',
        'proffer': 'А теперь пойдут самые сложные вопросы, готова? Тогда жми далее!',
        'proffer2': 'Это все мои любимчики, Мерсика не хватает на фото, но ничего страшного, он все равно с нами!',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question14(request):
    context = {
        'title': 'Дашка',
        'url': 'question14_t',
        'ago': 'question13_t',
        'proffer': 'Вопрос 14',
        'question': 'Как сильно любит тебя Сашка (от 1 до 100)?',
    }
    if request.method == 'POST':
        form = request.POST
        answer = form['answer']
        if answer == '':
            answer = 0
        answer = int(answer)
        if 0 <= answer < 100:
            context['error'] = 'Как то маловато, попробуй больше!'
        elif 100 <= answer < 102:
            context['error'] = 'Неплохо, но мне кажется что должно быть еще больше'
        elif 102 <= answer <= 1000:
            context['right'] = 'Молодец, именно на столько он тебя любит)'
        elif answer >= 1001:
            context['error'] = 'Столько много процентов не бывает, попробуй сократить до 1000'

    return render(request, 'iloveyou/answer.html', context)

def question14_t(request):
    post = Question.objects.get(title='qest14')
    context = {
        'post': post,
        'proffer': 'Четырнадцатый вопрос осилила',
        'proffer2': 'Наши совместные фото:)',
        'title': 'Дашка',
        'url': 'question15',
        'ago': 'question14',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question15(request):
    context = {
        'title': 'Daria',
        'url': 'question15_t',
        'ago': 'question14_t',
        'proffer': 'Вопрос 15',
        'question': 'Ты меня любишь?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Да'},
            'no2': {'values': 'Неправильный ответ, нужно сказать Да', 'name_button': 'Нет'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Молодец, это правильный ответ'

    return render(request, 'iloveyou/options.html', context)

def question15_t(request):
    post = Question.objects.get(title='qest15')
    context = {
        'post': post,
        'proffer': 'Пятнадцатый вопрос осилила',
        'proffer2': 'Я тоже тебя люблю!',
        'title': 'Дашка',
        'url': 'question16',
        'ago': 'question15',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question16(request):
    context = {
        'title': 'Daria',
        'url': 'question16_t',
        'ago': 'question15_t',
        'proffer': 'Вопрос 16',
        'question': 'Как сильно меня любишь?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Очень очень сильно'},
            'no2': {'values': 'Мне кажется должно быть сильнее', 'name_button': 'Сильно'},
            'no3': {'values': 'Не верно', 'name_button': 'Так себе'},
            'no4': {'values': 'Не ври, Врушка', 'name_button': 'Не люблю'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Молодец, это правильный ответ'

    return render(request, 'iloveyou/options.html', context)

def question16_t(request):
    context = {
        'title': 'Дашка',
        'url': 'question17',
        # 'ago': 'question16',
        'proffer': 'Шестнадцатый вопрос осилила',
        'proffer2': 'Остался последний и самый главный вопрос',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
def question17(request):
    context = {
        'title': 'Daria',
        'url': 'question17_t',
        # 'ago': 'question16_t',
        'proffer': 'Последний вопрос',
        'question': 'Ты выйдешь за мена замуж?',
        'nous': {
            'no1': {'values': 'right', 'name_button': 'Да'},
            'no2': {'values': 'Очень жаль, можешь закрывать вкладку=(', 'name_button': 'Нет'},
        },
    }

    nous1 = {}
    keys = rand.sample(list(context['nous'].keys()), len(context['nous']))
    for key in keys:
        nous1[key] = context['nous'][key]
    context['nous2'] = nous1.values()

    if request.method == 'POST':
        form = request.POST
        context['error'] = form['no']
        if context['error'] == 'right':
            context['right'] = 'Я очень рад и благодарен за твой выбор! Я тебя очень сильно люблю!'
            subject = 'Сообщение от Дашки'
            mail = 'Дашка сказала ДА!!!!'
            try:
                send_mail(subject, mail, 'alexander_misyuta@mail.ru', ['alexander_misyuta@mail.ru'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('<h1>Error</h1>')

    return render(request, 'iloveyou/options.html', context)

def question17_t(request):
    post = Question.objects.get(title='qest17')
    context = {
        'post': post,
        'title': 'Дашка',
        'url': 'home',
        'proffer': 'Это был последний и самый главный вопрос',
        'proffer2': 'Сашка был успешно уведомлен, жди его в ближайший момент с цветами и кольцом!!!',
    }
    return render(request, 'iloveyou/transition.html', context)
# ------------------------------------------------------------------
