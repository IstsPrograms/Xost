varsName = [] #Список имен переменных
varsVal = [] #Список значений перменных

funcName = [] #Список имен функций
funcComm = [] #Список команд функций

#Главная функция
def main(command):
	
	#Ищет совпадение с $in (Вводом)
	if (command.find("$in") >= 0 and command.find("<") > 0 and command.find("while") == -1 and command.find("def") == -1 and command.find("if") == -1):
		command = command.replace("$in", "") #Удаляет часть $in
		command = command.replace("<", "") #Уберает <
		varsVal[varsName.index(command)] = input("[" + command + "] <- ") #Заменяет значение перменной на введёное (Всегда будет строка)
	
	#Ищет совпадение на вывод
	if (command.find("$out") >= 0 and command.find("<") >= 0 and command.find("while") == -1 and command.find("def") == -1 and command.find("if") == -1):
		command = command.replace("$out", "") #Заменяет часть $out
		#Ищет / для начала вывода переменной
		if (command.find("/") >= 0 and command.find("") >= 0):
			command = command.replace("<","") #Уберает <
			command = command.replace(" ", "") #Уберает пробелы
			command = command.split("/") #Разделяет на 3 части оставшуюся команду
			print(f"[{command[1]}] ->", varsVal[varsName.index(command[1])]) #Выводит значение переменной найденной по оставшейся команде (Команда поделена на 3 части, 2 - название перменной)
			command = "" #Очищает команду
		else:
			command = command.split("<") #Разделяет команду по символу <
			print("[I/O] " + command[0]) #Выводит текст
			command = "" #Очищает команду
	
	#Ищет "=" для инициализации переменной
	if (command.find("=") >= 0 and command.find("while") == -1 and command.find("def") == -1 and command.find("if") == -1):
		var = command.replace(" ", "") #Удаляет пробелы
		var = var.split("=") #Разделяет по символу равно
		#Ищет #і для типа int
		if (var[0].find("int") >= 0):
			varsName.append(str(var[0]).replace("int", "")) #Добавляет в названия переменных название новой переменной
			varsVal.append(int(var[1].replace(" ", "")))
		#Ищет #f для типа float
		if (var[0].find("float") >= 0):
			varsName.append(var[0].replace("float", "")) #Добавляет в названия переменных название новой переменной
			varsVal.append(float(var[1].replace("float", "")))
		#Ищет & для типа string
		if (var[1].find('"') >= 0 and var[0].find("string") >= 0):
			varsName.append(var[0].replace("string", "")) #Добавляет в названия переменных название новой переменной
			varsVal.append(var[1].replace('"', "")) #Добавляет в список значений переменных новое значение, равное второй части команды
		#Ищет bool для типа bool
		if (var[0].find("bool") >= 0):
			varsName.append(var[0].replace("bool"))
			if (var[1].replace(" ", "") == "True"):
				varsVal.append(True) #Добавляет True в список значений переменных
			else:
				varsVal.append(False) #Добавляет False в список значений переменных
		#Ищет * для копирования другой переменной
		if (var[0].find("*") == 0):
			varsName.append(var[0].replace("*", "")) #Добавляет в названия переменных название новой переменной
			varsVal.append(varsVal[varsName.index(var[1])]) #Добавляет в varsVal значение из (команды) списка, под индексом 1
	
	#Ищет .toInt() для запуска кода
	if (command.find(".toInt()") >= 0 and command.find("while") == -1 and command.find("def") == -1 and command.find("if") == -1):
		var = command.replace(" ", "") #Удаляет пробелы
		var = var.replace(".toInt()", "") #Удаляет .toInt()
		varsVal[varsName.index(var)] = int(varsVal[varsName.index(var)]) #Изменяет значение в varsVal по индексу, равному в varsName, найденому по тексту оставшейся команды
	
	#Ищет .toFloat() для запуска кода
	if (command.find(".toFloat()") >= 0 and command.find("while") == -1 and command.find("def") == -1 and command.find("if") == -1):
		var = command.replace(" ", "") #Удаляет пробелы
		var = var.replace(".toFloat()", "") #Удаляет .toFloat()
		varsVal[varsName.index(var)] = float(varsVal[varsName.index(var)]) #Изменяет значение в varsVal по индексу, равному в varsName, найденому по тексту оставшейся команды
	
	#Ищет %exit для остановки программы
	if (command.find("%exit") >= 0 and command.find("while") == -1 and command.find("def") == -1 and command.find("if") == -1):
		exit()
	
	#Ищет %import для открвтия файла/библиотеки
	if (command.find("%import") >= 0 and command.find("while") == -1 and command.find("def") == -1 and command.find("if") == -1):
		var = command.replace(" ", "") #Удаляет пробелы
		var = var.replace("%import", "") #Удаляет %import
		file = open(f"{var}") #Открывает файл по имени + расширение
		for command in file:
			if (command.find("def") >= 0 and command.find(":") >= 0):
				fn = command.split(":") #Разделяет команду по символу :
				fnc = fn[2].split(";") #Берём часть с командами и делим символом ;
				funcName.append(fn[1].replace(" ", "")) #Добавляем в список имен функций введёное имя
				funcComm.append(fnc) #Добавляем в список команд функций введёные функции
			#Ищет "=" для инициализации переменной
			if (var[0].find("int") >= 0):
				varsName.append(str(var[0]).replace("int", "")) #Добавляет в названия переменных название новой переменной
				varsVal.append(int(var[1].replace(" ", "")))
				#Ищет float для типа float
				if (var[0].find("float") >= 0):
					varsName.append(var[0].replace("float", "")) #Добавляет в названия переменных название новой переменной
					varsVal.append(float(var[1].replace("float", "")))
				#Ищет string и " для типа string
				if (var[1].find('"') >= 0 and var[0].find("string") >= 0):
					varsName.append(var[0].replace("string", "")) #Добавляет в названия переменных название новой переменной
					varsVal.append(var[1].replace('"', "")) #Добавляет в список значений переменных новое значение, равное второй части команды
				#Ищет bool для типа bool
				if (var[0].find("bool") >= 0):
					varsName.append(var[0].replace("bool"))
					if (var[1].replace(" ", "") == "True"):
						varsVal.append(True) #Добавляет True в список значений переменных
					else:
						varsVal.append(False) #Добавляет False в список значений переменных
		#Ищет * для копирования другой переменной
				if (var[0].find("*") == 0):
					varsName.append(var[0].replace("*", "")) #Добавляет в названия переменных название новой переменной
					varsVal.append(varsVal[varsName.index(var[1])]) #Добавляет в varsVal значение из (команды) списка, под индексом 1
	
	#Ищет ++ для прибавления 1 к переменной
	if (command.find("++") >= 0 and command.find("while") == -1 and command.find("def") == -1 and command.find("if") == -1):
		var = command.replace(" ", "") #Удаляет пробелы
		var = var.replace("++", "") #Удаляет ++
		varsVal[varsName.index(var)] = varsVal[varsName.index(var)] + 1
		#Прибавляет 1 к переменной
	
	#Ищет -- для отнимания 1 от переменной
	if (command.find("--") >= 0 and command.find("while") == -1 and command.find("def") == -1 and command.find("if") == -1):
		var = command.replace(" ", "") #Удаляет пробелы
		var = var.replace("--", "") #Удаляет --
		varsVal[varsName.index(var)] = varsVal[varsName.index(var)] - 1
		#Убавляет 1 от переменной
	
	#Ищет while и : для начала цикла
	if (command.find("while") >= 0 and command.find(":") >= 0 and command.find("def") == -1 and command.find("if") == -1):
		whi = command.replace(" ", "") #Удаляет пробелы
		wh = whi.split(".") #Разделяет командк по символу .
		wh = wh[1].split(",") #Берём часть с командами и делим символом ,
		while True: #Создаём бесконечный цикл
			for i in range(len(wh)): #Проходимся по всем командам
				if (wh[i] != "%break"):
					main(wh[i]) #Обрабатываем команду
				else:
					break
	
	#Ищет def и : для инициализации функции
	if (command.find("def(") >= 0 and command.find(")") >= 0 and command.find("while") == -1 and command.find("if") == -1):
		fn = command.replace("def(", "") #Убераем def(
		fn = fn.replace(")", "") #Убераем )
		fna = fn.split(",") #Разделяет команду по символу ,
		fnn = fna[0] #Берём первый элемент (имя)
		fnc = fna #Берём часть с командами
		del fnc[0] #Удаляем первый элемент
		funcName.append(fnn)
		#Добавляем в список имен функций введёное имя
		funcComm.append(fnc) #Добавляем в список команд функций введёные функции
	
	#Ищет lof( и ) для инициализации функции
	if (command.find("lof(") >= 0 and command.find(")") >= 0 and command.find("while") >= -1 and command.find("def") >= -1 and command.find("if") >= -1):
		fnl = command.split("(") #Разделяет командy по символу :
		fnn = fnl[1].replace(")", "")
		print(fnn)
		print(funcComm[funcName.index(fnn)]) #Получаем команды
		comm = []
		for i in range(len(comm)): #Проходимся по всем командам
			main(comm[i]) #Обрабатываем команду
	
	#Ищет def и : для инициализации функции
	if (command.find("if") >= 0 and command.find("'") >= 0 and command.find("while") == -1 and command.find("def") == -1):
		ifa = command.split("'") #Разделяет команду по символу '
		ifb = ifa[2].split("`") #Берём часть с командами и делим символом `
		if (ifa[1].find("==") >= 0):
			ifc = ifa[1].split("==") #Разделяет по
			ifv1 = ifc[0].replace(" ", "") #Задает имя первой переменной
			ifv2 = ifc[1].replace(" ", "") #Задает имя второй переменной
			#Сравнивает на то, одинаковы ли 2 переменные
			if (varsVal[varsName.index(ifv1)] == varsVal[varsName.index(ifv2)]):
				#Проходится по всем командам
				for i in range(len(ifb)):
					main(ifb[i])
	
	#Находит %clear для oчстки консоли
	if (command.find("%clear") >= 0 and command.find("while") == -1 and command.find("def") == -1):
		for i in range(200):
			print("\n")
	
	command = "" #очищает команду