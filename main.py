def xo():
    """Осторожно говнокод
    мб в будущем будет оптимизирован и станет более читабельным"""
    team1 = str(input("Choose your team\n"))

    def check_input(slot, value_of_input, count, field):
        match count:
            case 2:
                sym = "o"
                if slot[value_of_input] == " " and value_of_input in slot.keys():
                    slot[value_of_input] = sym
                    print(field.format(c1=slot["1"], c2=slot["2"], c3=slot["3"], c4=slot["4"], c5=slot["5"],
                                       c6=slot["6"], c7=slot["7"], c8=slot["8"], c9=slot["9"]))
                    if slot["1"] == slot["2"] == slot["3"] == sym:
                        print(f"o win")
                    elif slot["4"] == slot["5"] == slot["6"] == sym:
                        print(f"o win")
                    elif slot["7"] == slot["8"] == slot["9"] == sym:
                        print(f"o win")
                    elif slot["1"] == slot["4"] == slot["7"] == sym:
                        print(f"o win")
                    elif slot["2"] == slot["5"] == slot["8"] == sym:
                        print(f"o win")
                    elif slot["3"] == slot["6"] == slot["9"] == sym:
                        print(f"o win")
                    elif slot["1"] == slot["5"] == slot["9"] == sym:
                        print(f"o win")
                    elif slot["7"] == slot["5"] == slot["3"] == sym:
                        print(f"o win")
                else:
                    pass
            case 1:
                sym = "x"
                if slot[value_of_input] == " " and value_of_input in slot.keys():
                    slot[value_of_input] = sym
                    print(field.format(c1=slot["1"], c2=slot["2"], c3=slot["3"], c4=slot["4"], c5=slot["5"],
                                       c6=slot["6"], c7=slot["7"], c8=slot["8"], c9=slot["9"]))
                    if slot["1"] == slot["2"] == slot["3"] == sym:
                        print(f"x win")
                    elif slot["4"] == slot["5"] == slot["6"] == sym:
                        print(f"x win")
                    elif slot["7"] == slot["8"] == slot["9"] == sym:
                        print(f"x win")
                    elif slot["1"] == slot["4"] == slot["7"] == sym:
                        print(f"x win")
                    elif slot["2"] == slot["5"] == slot["8"] == sym:
                        print(f"x win")
                    elif slot["3"] == slot["6"] == slot["9"] == sym:
                        print(f"x win")
                    elif slot["1"] == slot["5"] == slot["9"] == sym:
                        print(f"x win")
                    elif slot["7"] == slot["5"] == slot["3"] == sym:
                        print(f"x win")
                else:
                    pass

    slots = {
        "1": " ",
        "2": " ",
        "3": " ",
        "4": " ",
        "5": " ",
        "6": " ",
        "7": " ",
        "8": " ",
        "9": " ", }
    field1 = "|---|---|---|\n| {c1} | {c2} | {c3} |\n|---|---|---|\n| {c4} | {c5} | {c6} |\n"
    field = field1+"|---|---|---|\n| {c7} | {c8} | {c9} |\n|---|---|---|"
    while True:
        if team1 == "x":
            x = str(input())
            count = 1
            if x == "quit" or x == "":
                break
            check_input(slots, x, count, field)
            o = str(input())
            count += 1
            if o == "quit" or o == "":
                break
            check_input(slots, o, count, field)
            count = 0
        elif team1 == "o":
            o = str(input())
            count = 2
            if o == "quit" or o == "":
                break
            check_input(slots, o, count, field)

            x = str(input())
            count -= 1
            if x == "quit" or x == "":
                break
            check_input(slots, x, count, field)
        else:
            break


xo()
