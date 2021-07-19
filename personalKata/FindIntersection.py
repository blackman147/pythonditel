def find_intersection():
    elements = ["1, 3, 4, 7, 15", "1, 2, 4, 13, 15"]
    first_element = elements[0].split(", ")
    second_element = elements[1].split(", ")
    common_element = ""
    for i in first_element:
        for x in second_element:
            if i == x:
                common_element += i + ", "

    if common_element == 0:
        return "false"

    return common_element + " "


print(find_intersection())
