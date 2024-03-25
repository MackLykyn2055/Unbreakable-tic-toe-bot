from random import choice


def get_missing(li):
    for i in range(3):
        for j in range(3):
            if li[i][j] is None:
                return [i, j]


def get_all(li):
    ans = None
    ch = False
    for i in range(3):
        tru = 0
        fal = 0
        tie = [0, [None, None]]
        for j in range(3):
            if li[i][j]:
                tru += 1
            elif li[i][j] is False:
                fal += 1
            else:
                tie = [tie[0] + 1, [i, j]]
        if fal == 2 and tie[0]:
            ans = tie[1]
            ch = True
        elif tru == 2 and tie[0] and not ch:
            ans = tie[1]
    for j in range(3):
        tru = 0
        fal = 0
        tie = [0, [None, None]]
        for i in range(3):
            if li[i][j]:
                tru += 1
            elif li[i][j] is False:
                fal += 1
            else:
                tie = [tie[0] + 1, [i, j]]
        if fal == 2 and tie[0]:
            ans = tie[1]
            ch = True
        elif tru == 2 and tie[0] and not ch:
            ans = tie[1]
    tie = [0, [None, None]]
    tru = 0
    fal = 0
    if li[0][0]:
        tru += 1
    elif li[0][0] is False:
        fal += 1
    elif li[0][0] is None:
        tie = [tie[0] + 1, [0, 0]]
    if li[1][1]:
        tru += 1
    elif li[1][1] is False:
        fal += 1
    elif li[1][1] is None:
        tie = [tie[0] + 1, [1, 1]]
    if li[2][2]:
        tru += 1
    elif li[2][2] is False:
        fal += 1
    elif li[2][2] is None:
        tie = [tie[0] + 1, [2, 2]]
    if fal == 2 and tie[0]:
        ans = tie[1]
        ch = True
    elif tru == 2 and tie[0] and not ch:
        ans = tie[1]
    fal = 0
    tru = 0
    tie = [0, [None, None]]
    if li[0][2]:
        tru += 1
    elif li[0][2] is False:
        fal += 1
    elif li[0][2] is None:
        tie = [tie[0] + 1, [0, 2]]
    if li[1][1]:
        tru += 1
    elif li[1][1] is False:
        fal += 1
    elif li[1][1] is None:
        tie = [tie[0] + 1, [1, 1]]
    if li[2][0]:
        tru += 1
    elif li[2][0] is False:
        fal += 1
    elif li[2][0] is None:
        tie = [tie[0] + 1, [2, 0]]
    if fal == 2 and tie[0]:
        ans = tie[1]
        ch = True
    elif tru == 2 and tie[0] and not ch:
        ans = tie[1]
    return ans


def start():
    cho = choice([[0, 0], [0, 2], [2, 0], [2, 2]])
    return cho


def calc(li, to, prev, oppo):
    if to == 0:
        return start()
    elif to == 1:
        if oppo != [1, 1]:
            return [1, 1]
        else:
            return start()
    elif to == 2:
        if oppo == [1, 1]:
            if prev == [0, 0]:
                return [2, 2]
            elif prev == [2, 2]:
                return [0, 0]
            elif prev == [0, 2]:
                return [2, 0]
            else:
                return [0, 2]
        else:
            if prev == [0, 0]:
                if oppo[1] != 1 and oppo != [0, 2]:
                    return [0, 2]
                else:
                    return [2, 0]
            elif prev == [2, 2]:
                if oppo[0] != 1 and oppo != [0, 2]:
                    return [0, 2]
                else:
                    return [2, 0]
            elif prev == [0, 2]:
                if oppo[1] != 1 and oppo != [0, 0]:
                    return [0, 0]
                else:
                    return [2, 2]
            else:
                if oppo[0] != 1 and oppo != [0, 0]:
                    return [0, 0]
                else:
                    return [2, 2]
    elif to == 3:
        if li[0][1] and li[1][0]:
            return [0, 0]
        elif li[1][0] and li[2][1]:
            return [2, 0]
        elif li[0][1] and li[1][2]:
            return [0, 2]
        elif li[1][2] and li[2][1]:
            return [2, 2]
        elif li[0][1] and li[2][1]:
            return choice([[1, 0], [1, 2]])
        elif li[1][0] and li[1][2]:
            return choice([[0, 1], [2, 1]])
        elif li[0][0] == li[2][2] is True or li[0][2] == li[2][0] is True:
            return choice([[0, 1], [1, 0], [2, 1], [1, 2]])
        elif li[1][1] is False:
            if li[0][0] is True:
                if li[1][2]:
                    return [0, 2]
                elif li[2][1]:
                    return [2, 0]
                elif li[0][2]:
                    return [0, 1]
                elif li[0][1]:
                    return [0, 2]
                elif li[2][0]:
                    return [1, 0]
                else:
                    return [2, 0]
            elif li[0][2]:
                if li[1][0]:
                    return [0, 0]
                elif li[2][1]:
                    return [2, 2]
                elif li[0][0]:
                    return [0, 1]
                elif li[0][1]:
                    return [0, 0]
                elif li[2][2]:
                    return [1, 2]
                else:
                    return [2, 2]
            elif li[2][0]:
                if li[0][1]:
                    return [0, 0]
                elif li[1][2]:
                    return [2, 2]
                elif li[0][0]:
                    return [1, 0]
                elif li[1][0]:
                    return [0, 0]
                elif li[2][2]:
                    return [2, 1]
                else:
                    return [2, 2]
            elif li[2][2]:
                if li[0][1]:
                    return [0, 2]
                elif li[1][0]:
                    return [2, 0]
                elif li[0][2]:
                    return [1, 2]
                elif li[1][2]:
                    return [0, 2]
                elif li[2][0]:
                    return [2, 1]
                else:
                    return [2, 0]
        else:
            if oppo == [0, 0] and li[2][2] is None:
                return [2, 2]
            elif oppo == [0, 1] and li[2][1] is None:
                return [2, 1]
            elif oppo == [0, 2] and li[2][0] is None:
                return [2, 0]
            elif oppo == [1, 2] and li[1][0] is None:
                return [1, 0]
            elif oppo == [2, 2] and li[0][0] is None:
                return [0, 0]
            elif oppo == [2, 1] and li[0, 1] is None:
                return [0, 1]
            elif oppo == [2, 0] and li[0][2] is None:
                return [0, 2]
            elif oppo == [1, 0] and li[1][2] is None:
                return [1, 2]
            else:
                for i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                    if li[i[0]][i[1]] is None:
                        return i
    elif to == 4:
        if li[0][0] == li[0][2] is False and li[0][1] is None:
            return [0, 1]
        elif li[0][0] == li[2][0] is False and li[1][0] is None:
            return [1, 0]
        elif li[2][2] == li[0][2] is False and li[1][2] is None:
            return [1, 2]
        elif li[2][2] == li[2][0] is False and li[2][1] is None:
            return [2, 1]
        elif li[1][1] is True:
            if 1 in oppo:
                ind = oppo.index(1)
                ind1 = ind + (1 if ind == 0 else -1)
                if oppo[ind1] == 0:
                    pl = [2, 2]
                    pl[ind] = 1
                    return pl
                else:
                    pl = [0, 0]
                    pl[ind] = 1
                    return pl
            else:
                if oppo == [0, 2]:
                    return [2, 0]
                elif oppo == [2, 0]:
                    return [0, 2]
                elif oppo == [0, 0]:
                    return [2, 2]
                else:
                    return [0, 0]
        else:
            if li[2][2] == li[2][0] is False:
                if li[0][0] == li[1][0] == li[1][1] is None:
                    return [0, 0]
                else:
                    return [0, 2]
            elif li[2][2] == li[0][2] is False:
                if li[0][0] == li[0][1] == li[1][1] is None:
                    return [0, 0]
                else:
                    return [2, 0]
            elif li[0][0] == li[2][0] is False:
                if li[2][2] == li[2][1] == li[1][1] is None:
                    return [2, 2]
                else:
                    return [0, 2]
            else:
                if li[2][2] == li[1][2] == li[1][1] is None:
                    return [2, 2]
                else:
                    return [2, 0]
    elif to == 5:
        x = get_all(li)
        if x is not None:
            return x
        elif li[0][0] == li[0][2] == li[2][0] == li[2][2] is None:
            if li[0][1] is False:
                return choice([[0, 0], [0, 2]])
            elif li[1][0] is False:
                return choice([[0, 0], [2, 0]])
            elif li[1][2] is False:
                return choice([[2, 2], [0, 2]])
            else:
                return choice([[2, 2], [2, 0]])
        else:
            if li[0][1] is None:
                return [0, 1]
            elif li[1][2] is None:
                return [1, 2]
            elif li[1][0] is None:
                return [1, 0]
            else:
                return [2, 1]
    elif to == 6:
        x = get_all(li)
        if x is not None:
            return x
        if li[0][0] == li[0][2] == li[2][0] is False:
            if li[1][1] is None:
                return [1, 1]
            elif li[0][1] is None:
                return [0, 1]
            else:
                return [1, 0]
        elif li[0][2] == li[2][2] == li[2][0] is None:
            if li[1][1] is None:
                return [1, 1]
            elif li[2][1] is None:
                return [2, 1]
            else:
                return [1, 2]
        elif li[2][0] == li[2][2] == li[0][0] is None:
            if li[1][1] is None:
                return [1, 1]
            elif li[1][0] is None:
                return [1, 0]
            else:
                return [2, 1]
        elif li[0][2] == li[2][2] == li[0][0] is None:
            if li[1][1] is None:
                return [1, 1]
            elif li[1][0] is None:
                return [1, 0]
            else:
                return [1, 2]
        elif li[0][0] == li[1][1] is True:
            return [2, 2]
        elif li[0][2] == li[1][1] is True:
            return [2, 0]
        elif li[2][0] == li[1][1] is True:
            return [0, 2]
        elif li[2][2] == li[1][1] is True:
            return [0, 0]
        else:
            if li[0][0] == li[0][1] is False:
                return [0, 2]
            elif li[0][0] == li[1][0] is False:
                return [2, 0]
            elif li[2][2] == li[2][1] is False:
                return [2, 0]
            else:
                return [0, 2]
    elif to == 7:
        x = get_all(li)
        if x is not None:
            return x
        else:
            return get_missing(li)
    else:
        return get_all(li)
