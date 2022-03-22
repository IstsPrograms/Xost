# Xost
 A new programming lang based-on Python

Xost делится на две версии: версию от Ксонти и от меня - Иста
Файл с версией от меня называется main.py, а от Ксонти - Xost(2).py

Для запуска кода на обеих версиях надо: 
1. Зайти в код языка
2. Написать: main(<тут ваш код>)
3. Запустить файл (для запуска необходим Python не ниже версии 3.9)

Синтаксис моей версии языка:
int <название переменной> = <значение переменной>
string <название переменной> = <значение переменной> (например: string str1 = first string)
%out <var/const (var когда надо вывести переменную, а const когда надо вывести текст)> <переменная или текст>
%in int <название int переменной, в которую вы хотите записать значение>
$func <название функции> <сколько строк будет входить в функцию>
Подробности: перед каждой строкой, входящей в функцию надо писать "$", для разных функций все переменные разные.
$run <название функции> - запустить функцию
@for <количество итераций> <функция> - цикл
@if <const_str/const_int/integer/str> <название переменной/текст> <==/<=/=>/</>/!=> <const_str/const_int/integer/str> <название переменной/текст> <название  функции> - условный оператор

Основные команды версии от Ксонти и как их записывать

------------------------------------

$out - вывод в консоль

Синтаксис: {text} < $out
С переменной: /var/ < $out

Примеры:

Hello world! < $out
/sum/ < $out

------------------------------------

$in - ввод значения в переменную (Вводится ТОЛЬКО значение типа string)

Синтаксис: {var} < $out

Примеры:

age < $in

------------------------------------

.toInt() - преобразование в int

Синтаксис: {var}.toInt()

Примеры:

age.toInt()

------------------------------------

.toFloat() - преобразование в float

Синтаксис: {var}.toFloat()

Примеры:

sum.toFloat()

------------------------------------

while - преобразование в int

Синтаксис: while!command?...?command

Примеры:

while!/age/<$out?age++

------------------------------------

def() - создание функции

Синтаксис: def(name,command,command)

Примеры:

def(in,a<$in)

------------------------------------

lof() - запуск функции

Синтаксис: lof(name)

Примеры

lof(in)

------------------------------------

if - условие

Синтаксис: if'var1==var2'command
