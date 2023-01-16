def main():

    dict_item, list_item = get_list()

    list_item = list(sorted(set(list_item)))

    for item in list_item:
        print(dict_item[item], item, sep = " ")

def get_list():
    list_item = []
    dict_item = {}
    while True:
        try:
            item = input().upper()
            # reorder alphabetically
            list_item.append(item)
            # add counts of items on the left
            # e.g. if banana typed 3x -> "3 BANANA"
            items_count = list_item.count(item)
            #as dictionary
            dict_item[item] = items_count

        except EOFError:
            break

    return dict_item, list_item

main()
