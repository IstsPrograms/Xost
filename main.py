# Xost professional code
def functsss(code: str) -> bool:
    every_type_vars = []

    strings_of_code = []
    strings_value = 0
    functs = []

    strings_value = code.count("\n") + 1
    strings_of_code = code.splitlines()
    for i in range(strings_value-1):

        this_split_line = strings_of_code[i].split()

        for u in range(len(this_split_line)):

            if this_split_line[u] == "$int":

                breaked = False
                for c in range(len(every_type_vars)):
                    if every_type_vars[c][0] == this_split_line[u + 1]:
                        if this_split_line[u + 2] == "=":
                            every_type_vars[c][1] = int(this_split_line[u + 3])
                        if this_split_line[u + 2] == "-=":
                            every_type_vars[c][1] -= int(this_split_line[u + 3])
                        if this_split_line[u + 2] == "+=":
                            every_type_vars[c][1] += int(this_split_line[u + 3])
                        if this_split_line[u + 2] == "*=":
                            every_type_vars[c][1] *= int(this_split_line[u + 3])
                        if this_split_line[u + 2] == "/=":
                            every_type_vars[c][1] /= int(this_split_line[u + 3])
                        breaked = True
                        break
                if breaked == False:
                    create_var = []
                    create_var.append(this_split_line[u + 1])
                    create_var.append(int(this_split_line[u + 3]))
                    every_type_vars.append(create_var)
            elif this_split_line[u] == "$string":
                breaked = False
                for c in range(len(every_type_vars)):

                    if every_type_vars[c][0] == this_split_line[u + 1]:
                        new_string = ""
                        str_new_list = []

                        str_new_list = this_split_line.copy()
                        str_new_list.remove("$string")
                        str_new_list.remove(str_new_list[0])
                        str_new_list.remove(str_new_list[0])

                        for p in range(len(str_new_list)):
                            new_string += str_new_list[p]
                            new_string += " "
                        breaked = True
                        every_type_vars[c][1] = new_string
                        break
                if breaked == False:
                    new_string = ""
                    nnn = []
                    nnn.append(this_split_line[u + 1])
                    str_new_list = []
                    str_new_list = this_split_line.copy()
                    str_new_list.remove("$string")
                    str_new_list.remove(str_new_list[0])
                    str_new_list.remove(str_new_list[0])

                    for p in range(len(str_new_list)):
                        new_string += str_new_list[p]
                        new_string += " "
                    nnn.append(new_string)
                    every_type_vars.append(nnn)
                    new_string = ""

            elif this_split_line[u] == "$%out":

                if this_split_line[u + 1] == "var":
                    for p in range(len(every_type_vars)):
                        if this_split_line[u + 2] == every_type_vars[p][0]:
                            print(every_type_vars[p][1])

                            break
                if this_split_line[u + 1] == "const":
                    print(this_split_line[u + 2])
            elif this_split_line[u] == "$%in":

                if this_split_line[u + 1] == "integer":

                    for p in range(len(every_type_vars)):

                        if this_split_line[u + 2] == every_type_vars[p][0]:
                            every_type_vars[p][1] = int(input("> "))
            elif this_split_line[u] == "$$func":
                code_lines = int(this_split_line[u + 2]) - 1
                name = this_split_line[u + 1]
                codee = ""
                for y in range(i + 1, code_lines + 2):
                    codee += strings_of_code[y] + "\n"
                print(code_lines)
                fun_list_first = []
                fun_list_first.append(name)
                fun_list_first.append(codee)
                functs.append(fun_list_first)

            elif this_split_line[u] == "$$run":
                name_f = this_split_line[u + 1]
                for t in range(len(functs)):
                    if name_f == functs[t][0]:

                        functsss(functs[t][1])

                        break
            elif this_split_line[u] == "$@for":
                iterats = int(this_split_line[u + 1])
                func_name = this_split_line[u + 2]
                for e in range(len(functs)):
                    if func_name == functs[e][0]:
                        for b in range(iterats):
                            functsss(functs[e][1])
                        break
            elif this_split_line[u] == "$@if":
                fv = None
                sv = None
                action = this_split_line[u+3]

                fc = ""

                for p in range(len(functs)+1):
                    if this_split_line[u+6] == functs[p][0]:
                        fc = functs[p][1]
                        break

                if this_split_line[u+1] == "const_int":
                    fv = int(this_split_line[u+2])
                elif this_split_line[u+1] == "const_str":
                    fv = this_split_line[u+2]
                elif this_split_line[u+1] == "integer":
                    for p in range(len(every_type_vars)):
                        if this_split_line[u+2] == every_type_vars[p][0]:
                            fv = every_type_vars[p][1]
                            break
                elif this_split_line[u+1] == "str":
                    for p in range(len(every_type_vars)):
                        if this_split_line[u+2] == every_type_vars[p][0]:
                            fv = every_type_vars[p][1]
                            break


                if this_split_line[u+4] == "const_int":
                    sv = int(this_split_line[u+5])
                elif this_split_line[u+4] == "const_str":
                    sv = this_split_line[u+5]
                elif this_split_line[u+4] == "integer":
                    for p in range(len(every_type_vars)):
                        if this_split_line[u+5] == every_type_vars[p][0]:
                            sv = every_type_vars[p][1]
                            break
                elif this_split_line[u+4] == "str":
                    for p in range(len(every_type_vars)):
                        if this_split_line[u+5] == every_type_vars[p][0]:
                            sv = every_type_vars[p][1]
                            break
                print(fv, sv)

                if action == "==":
                    if fv == sv:

                        functsss(fc)

                elif action == "<=":
                    if fv <= sv:

                        functsss(fc)

                elif action == "=>":
                    if fv >= sv:

                        functsss(fc)

                elif action == "!=":
                    if fv != sv:

                        functsss(fc)

                elif action == "<":
                    if fv < sv:

                        functsss(fc)

                elif action == ">":
                    if fv > sv:

                        functsss(fc)




def main(code: str) -> bool:
    every_type_vars = []

    strings_of_code = []
    strings_value = 0
    functs = []

    strings_value = code.count("\n") + 1
    strings_of_code = code.splitlines()
    for i in range(strings_value):

        this_split_line = strings_of_code[i].split()

        for u in range(len(this_split_line)):

            if this_split_line[u] == "int":

                breaked = False
                for c in range(len(every_type_vars)):
                    if every_type_vars[c][0] == this_split_line[u + 1]:
                        if this_split_line[u + 2] == "=":
                            every_type_vars[c][1] = int(this_split_line[u + 3])
                        if this_split_line[u + 2] == "-=":
                            every_type_vars[c][1] -= int(this_split_line[u + 3])
                        if this_split_line[u + 2] == "+=":
                            every_type_vars[c][1] += int(this_split_line[u + 3])
                        if this_split_line[u + 2] == "*=":
                            every_type_vars[c][1] *= int(this_split_line[u + 3])
                        if this_split_line[u + 2] == "/=":
                            every_type_vars[c][1] /= int(this_split_line[u + 3])
                        breaked = True
                        break
                if breaked == False:
                    create_var = []
                    create_var.append(this_split_line[u + 1])
                    create_var.append(int(this_split_line[u + 3]))
                    every_type_vars.append(create_var)
            elif this_split_line[u] == "string":
                breaked = False
                for c in range(len(every_type_vars)):

                    if every_type_vars[c][0] == this_split_line[u + 1]:
                        new_string = ""
                        str_new_list = []

                        str_new_list = this_split_line.copy()
                        str_new_list.remove("string")
                        str_new_list.remove(str_new_list[0])
                        str_new_list.remove(str_new_list[0])

                        for p in range(len(str_new_list)):
                            new_string += str_new_list[p]
                            new_string += " "
                        breaked = True
                        every_type_vars[c][1] = new_string
                        break
                if breaked == False:
                    new_string = ""
                    nnn = []
                    nnn.append(this_split_line[u + 1])
                    str_new_list = []
                    str_new_list = this_split_line.copy()
                    str_new_list.remove("string")
                    str_new_list.remove(str_new_list[0])
                    str_new_list.remove(str_new_list[0])

                    for p in range(len(str_new_list)):
                        new_string += str_new_list[p]
                        new_string += " "
                    nnn.append(new_string)
                    every_type_vars.append(nnn)
                    new_string = ""

            elif this_split_line[u] == "%out":
                if this_split_line[u + 1] == "var":
                    for p in range(len(every_type_vars)):
                        if this_split_line[u + 2] == every_type_vars[p][0]:
                            print(every_type_vars[p][1])

                            break
                if this_split_line[u + 1] == "const":
                    print(this_split_line[u + 2])
            elif this_split_line[u] == "%in":

                if this_split_line[u + 1] == "integer":

                    for p in range(len(every_type_vars)):

                        if this_split_line[u + 2] == every_type_vars[p][0]:
                            every_type_vars[p][1] = int(input("> "))
            elif this_split_line[u] == "$func":
                code_lines = int(this_split_line[u + 2]) - 1
                name = this_split_line[u + 1]
                codee = ""
                for y in range(i + 1, code_lines + 2):
                    codee += strings_of_code[y] + "\n"
                fun_list_first = []
                fun_list_first.append(name)
                fun_list_first.append(codee)
                functs.append(fun_list_first)


            elif this_split_line[u] == "$run":
                name_f = this_split_line[u + 1]
                for t in range(len(functs)):
                    if name_f == functs[t][0]:

                        functsss(functs[t][1])

                        break
            elif this_split_line[u] == "@for":
                iterats = int(this_split_line[u + 1])
                func_name = this_split_line[u + 2]
                for e in range(len(functs)):
                    if func_name == functs[e][0]:
                        for b in range(iterats):
                            functsss(functs[e][1])
                        break
            elif this_split_line[u] == "@if":
                fv = None
                sv = None
                action = this_split_line[u+3]

                fc = ""


                for r in range(len(functs)+1):

                    if this_split_line[u+6] == functs[r][0]:
                        fc = functs[r][1]

                        break

                if this_split_line[u+1] == "const_int":
                    fv = int(this_split_line[u+2])
                elif this_split_line[u+1] == "const_str":
                    fv = this_split_line[u+2]
                elif this_split_line[u+1] == "integer":

                    for p in range(len(every_type_vars)):
                        if this_split_line[u+2] == every_type_vars[p][0]:
                            fv = every_type_vars[p][1]
                            break
                elif this_split_line[u+1] == "str":
                    for p in range(len(every_type_vars)):
                        if this_split_line[u+2] == every_type_vars[p][0]:
                            fv = every_type_vars[p][1]
                            break


                if this_split_line[u+4] == "const_int":
                    sv = int(this_split_line[u+5])
                elif this_split_line[u+4] == "const_str":
                    sv = this_split_line[u+5]
                elif this_split_line[u+4] == "integer":
                    for p in range(len(every_type_vars)):
                        if this_split_line[u+5] == every_type_vars[p][0]:
                            sv = every_type_vars[p][1]
                            break
                elif this_split_line[u+4] == "str":
                    for p in range(len(every_type_vars)):
                        if this_split_line[u+5] == every_type_vars[p][0]:
                            sv = every_type_vars[p][1]
                            break



                if action == "==":
                    if fv == sv:
                        print(1)
                        functsss(fc)

                elif action == "<=":
                    if fv <= sv:

                        functsss(fc)

                elif action == "=>":
                    if fv >= sv:

                        functsss(fc)

                elif action == "!=":
                    if fv != sv:

                        functsss(fc)

                elif action == "<":
                    if fv < sv:

                        functsss(fc)

                elif action == ">":
                    if fv > sv:

                        functsss(fc)











