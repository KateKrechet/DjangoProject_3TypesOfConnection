from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def index(req):
    return render(req, 'index.html')


def add(req):
    # Company.objects.create(title='J7')
    # Company.objects.create(title='DOBRY')
    p1 = Product(name='orange', price=140)
    p2 = Product(name='apple', price=150)
    p3 = Product(name='multy', price=155)
    p4 = Product(name='melon', price=155)
    p5 = Product(name='pear', price=155)
    p6 = Product(name='tomato', price=155)
    c1 = Company.objects.get(title='J7')
    c2 = Company.objects.get(title='DOBRY')
    # c1.product_set.add(p1,bulk=False)
    # c1.product_set.add(p2,bulk=False)
    # c1.product_set.add(p3,bulk=False)
    # c2.product_set.add(p4,bulk=False)
    # c2.product_set.add(p5,bulk=False)
    # c2.product_set.add(p6,bulk=False)
    # print(c2.product_set.count())
    # print(c2.product_set.values_list())
    # Product.objects.filter(id=1).update(volume=0.5, pack='пакет', commend=False)
    # Product.objects.filter(id=2).update(volume=1, pack='бутылка', commend=True)
    # Product.objects.filter(id=3).update(volume=0.5, pack='пакет', commend=False)
    # Product.objects.filter(id=4).update(volume=1, pack='бутылка', commend=True)
    # Product.objects.filter(id=5).update(volume=0.5, pack='пакет', commend=False)
    # Product.objects.filter(id=6).update(volume=1, pack='бутылка', commend=True)
    # s1 = Student.objects.create(name='Victor', group='G001')
    # s2 = Student.objects.create(name='Boris', group='G001')
    # s3 = Student.objects.create(name='Maxr', group='G001')
    # s4 = Student.objects.create(name='Igor', group='G002')
    # s5 = Student.objects.create(name='Zahar', group='G002')
    # k1 = Course.objects.create(title='Math')
    # k2 = Course.objects.create(title='Geo')
    # k1.student_set.add(s1)
    # k1.student_set.add(s3)
    # k1.student_set.add(s5)
    # k2.student_set.add(s1, s2, s3)

    # u1 = User.objects.create(name='Sasha')
    # ac1 = Account.objects.create(login='rty', password='678910', user=u1)

    return redirect('home')


def table1(req):
    # заходим на страницу
    baza = Product.objects.all()
    anketa = FormaJuice()
    bd = []
    if req.POST:  # нажали на кнопку submit
        anketa = FormaJuice(req.POST)  # форма с прошлым запросом
        a = req.POST['firma']  # собираем данные
        b = req.POST['juice']
        print(a, b, '##########################')
        # выбираем таблицу для вывода
        if a and not b:
            baza = Product.objects.filter(firma_id=a)
        elif b and not a:
            c = Product.objects.get(id=b).name
            baza = Product.objects.filter(name=c)
        elif a and b:
            c = Product.objects.get(id=b).name
            baza = Product.objects.filter(firma_id=a, name=c)

        else:
            baza = Product.objects.all()
    # заполняется таблица для вывода
    for i in baza:
        bd.append([i.name, i.price, i.firma.title, i.volume, i.pack, i.commend])

    print(bd)
    title = ['Название сока', 'Цена', 'Фирма', 'Объем', 'Упаковка',
             'Рекомендован/Не рекомендован']  # строка с заголовком
    data = {'table': bd, 'title': title, 'forma': anketa}  # данные для вывода
    return render(req, 'totable.html', context=data)


def table2(req):
    # заходим на страницу
    baza = Student.objects.all()
    anketa = FormaStudents()
    if req.POST:
        anketa = FormaStudents(req.POST)
        s = req.POST['student']
        c = req.POST['course']
        if c and not s:
            baza = Student.objects.filter(course__in=c)
        elif s and not c:
            baza = Student.objects.filter(id=s)
        elif c and s:
            baza = Student.objects.filter(course__in=c, id=s)
        else:
            baza = Student.objects.all()
    bd = []
    for i in baza:
        temp = i.course.all()
        kurs = ''
        for t in temp:
            kurs += t.title + '/'
        bd.append([i.name, i.group, kurs])
    title = ['Имя', 'Группа', 'Курсы']  # строка с заголовком
    data = {'table': bd, 'title': title, 'forma': anketa}  # данные для вывода
    return render(req, 'totable.html', context=data)


def table3(req):
    baza = User.objects.all()
    anketa = FormaUser()
    if req.POST:
        anketa = FormaUser(req.POST)
        u = req.POST['user']
        if u:
            baza = User.objects.filter(id=u)
        else:
            baza = User.objects.all()
    bd = []
    for i in baza:
        bd.append([i.name, i.account.login, i.account.password])
    print(bd)
    title = ['Имя', 'Логин', 'Пароль']
    data = {'table': bd, 'title': title, 'forma': anketa}  # данные для вывода
    return render(req, 'totable.html', context=data)
