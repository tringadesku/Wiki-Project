
def counter(sequence: list) -> dict:
    count = {}
    for element in sequence:
        if len(element) >= 1 and not element.isnumeric() and element !=" ":
            if element in count:
                count[element] += 1
            else:
                count[element] = 1
    return dict(sorted(count.items(), key=lambda item: item[1]))
