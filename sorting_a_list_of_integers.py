data = [64, 34, 25, 12, 22, 11, 90, 5, 1, 4, 3, 100, 290, 25, 13, 80, 41]
sorted_data = []
is_lowest = False

while len(data) > 0:
    for i in data:
        for j in data:
            # print(f"i = {i}, j = {j}")
            if i <= j:
                is_lowest = True
            else:
                is_lowest = False
                break

        if is_lowest:
            # print(i)
            sorted_data.append(i)
            data.remove(i)


        is_lowest = False
        # print("=================================")

print(sorted_data)