def alphanumeric_sort(value):
    numbs = []
    lowercase = []
    uppercase = []
    sort_list = []

    for char in value:

        if (char.islower):
            lowercase.append(char)

        if (char.isnumeric):
            numbs.append(char)

        if (char.isupper):
            uppercase.append(char)

    sort_list.extend(sorted(numbs))
    print(sort_list)
    sort_list.extend(sorted(lowercase))
    print(sort_list)
    sort_list.extend(sorted(uppercase))

    return sort_list


print(alphanumeric_sort('i11u6'))
