def justify(text, width):
    while text.find('  ') != -1:
        text = text.replace('  ', ' ')

    if len(text) >= width + 1:
        text = text.replace(' ', '©')
        arr = text.split('©')

        while len(max(arr, key=len)) > width:
            for i in range(len(arr)):
                if len(arr[i]) > width:
                    arr[i] = arr[i][:width] + ' ' + arr[i][width:]
            arr = ' '.join(arr).split()

        arr2, pr = [], ''

        for i in arr:
            if len(pr + ' ' + i) <= width + 1:
                pr += i + ' '
            else:
                arr2.append(pr.strip())
                pr = i + ' '

        arr2.append(pr.rstrip())
        arr2 = [i for i in arr2 if i]
    else:
        arr2 = [text]
    for i, v in enumerate(arr2[:-1]):
        spaces = v.count(' ')
        if v.count(' ') != 0:
            for j in range((width - len(v)) // v.count(' ')):
                arr2[i] = v.replace(' ', '  ' + ' ' * j)
        if arr2[i].count(' ') != 0:
            if len(arr2[i]) < width:
                arr2[i] = arr2[i].replace(' ' * (arr2[i].count(' ') // spaces),
                                          ' ' * (arr2[i].count(' ') // spaces + 1), width - len(arr2[i]))

    return '\n'.join(arr2)


justify(
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.',
    30)
