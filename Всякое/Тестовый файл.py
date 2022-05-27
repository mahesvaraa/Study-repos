COW = r'''        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(a):
    while '  ' in a:
        a = a.replace('   ', ' ')
    a = a.replace(' ', '*')

    arr = a.split('*')
    while len(max(arr, key=len)) > 39:
        for i in range(len(arr)):
            if len(arr[i]) > 39:
                arr[i] = arr[i][:39] + ' ' + arr[i][39:]

        arr = ' '.join(arr).split()
    arr2 = []
    pr = ''
    for i in arr:
        if len(pr + ' ' + i) <= 40:
            pr += i + ' '
        else:
            arr2.append(pr.strip())
            pr = i + ' '
    arr2.append(pr.rstrip())
    arr2 = [i for i in arr2 if i]
    res = '\n'
    if len(arr2) > 1:
        mx = max(arr2, key=len)
        res += ' ' + "_" * (len(mx) + 2) + '\n'
        for i in arr2:
            if i == arr2[0]:
                res += r'/ ' + i + ' ' * ((len(mx) + 1) - len(i)) + "\\" + '\n'
            elif i == arr2[-1]:
                res += r'\ ' + i + ' ' * ((len(mx) + 1) - len(i)) + r'/' + '\n'
            else:
                res += r'| ' + i + ' ' * ((len(mx) + 1) - len(i)) + '|' + '\n'
        res += ' ' + "-" * (len(mx) + 2) + '\n'
    else:
        res += ' ' + '_' * (len(arr2[0]) + 2) + '\n'
        res += r'< ' + arr2[0] + " >" + '\n'
        res += ' ' + '-' * (len(arr2[0]) + 2) + '\n'
    res += COW
    return res


if __name__ == '__main__':
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                               'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines

    enter = input('Введи текст: ')
    while enter != 0:
        print(cowsay(enter))
        enter = input('Введи текст: ')
