with open('query.sql', 'r') as file:
    contents = file.read()

parsed_list = contents.split("/")

queryList = []

for item in parsed_list:
    flag = 0
    for char in item:
        if char != "\n":
            flag = 1
        if flag == 1:
            break
    if flag == 1:
        queryList.append(list(item))

final = []

for i in range (len(queryList)):
    for j in range(len(queryList[i])):
        if (queryList[i][j] == '\n'):
            queryList[i][j] = ' '
    temp = ''.join(queryList[i])
    final.append(temp)

for item in final:
    print(item, "\n")


    