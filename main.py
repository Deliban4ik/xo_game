def xo():
    """Осторожно говнокод
    мб в будущем будет оптимизирован и станет более читабельным"""
    team1 = str(input("Choose your team\n"))

    def check_input(slot, value_of_input, count, field):
        def clear_dict():
            for i in slot.keys():
                slot[i] = " "
        match count:
            case 2:
                sym = "o"
                if slot[value_of_input] == " " and value_of_input in slot.keys():
                    slot[value_of_input] = sym
                    print(field.format(slot["1"], slot["2"], slot["3"], slot["4"], slot["5"],
                                       slot["6"], slot["7"], slot["8"], slot["9"]))
                    if slot["1"] == slot["2"] == slot["3"] == sym:
                        print(f"o win")
                        clear_dict()
                    elif slot["4"] == slot["5"] == slot["6"] == sym:
                        print(f"o win")
                        clear_dict()
                    elif slot["7"] == slot["8"] == slot["9"] == sym:
                        print(f"o win")
                        clear_dict()
                    elif slot["1"] == slot["4"] == slot["7"] == sym:
                        print(f"o win")
                        clear_dict()
                    elif slot["2"] == slot["5"] == slot["8"] == sym:
                        print(f"o win")
                        clear_dict()
                    elif slot["3"] == slot["6"] == slot["9"] == sym:
                        print(f"o win")
                        clear_dict()
                    elif slot["1"] == slot["5"] == slot["9"] == sym:
                        print(f"o win")
                        clear_dict()
                    elif slot["7"] == slot["5"] == slot["3"] == sym:
                        print(f"o win")
                        clear_dict()
                else:
                    pass
            case 1:
                sym = "x"
                if slot[value_of_input] == " " and value_of_input in slot.keys():
                    slot[value_of_input] = sym
                    print(field.format(slot["1"], slot["2"], slot["3"], slot["4"], slot["5"],
                                       slot["6"], slot["7"], slot["8"], slot["9"]))
                    if slot["1"] == slot["2"] == slot["3"] == sym:
                        print(f"x win")
                        clear_dict()
                    elif slot["4"] == slot["5"] == slot["6"] == sym:
                        print(f"x win")
                        clear_dict()
                    elif slot["7"] == slot["8"] == slot["9"] == sym:
                        print(f"x win")
                        clear_dict()
                    elif slot["1"] == slot["4"] == slot["7"] == sym:
                        print(f"x win")
                        clear_dict()
                    elif slot["2"] == slot["5"] == slot["8"] == sym:
                        print(f"x win")
                        clear_dict()
                    elif slot["3"] == slot["6"] == slot["9"] == sym:
                        print(f"x win")
                        clear_dict()
                    elif slot["1"] == slot["5"] == slot["9"] == sym:
                        print(f"x win")
                        clear_dict()
                    elif slot["7"] == slot["5"] == slot["3"] == sym:
                        print(f"x win")
                        clear_dict()
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
    field1 = "|---|---|---|\n| {} | {} | {} |\n|---|---|---|\n| {} | {} | {} |\n"
    field = field1+"|---|---|---|\n| {} | {} | {} |\n|---|---|---|"
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
