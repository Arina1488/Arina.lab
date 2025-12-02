a = [46, 58, 18, 3, 2, 7, 772, 99, 6, 21, "ягода", "кавун", "апельсин", "абрикос", "саванна", "хліб", "олівець", "монітор", "санчоус", "ківі"]

int_list = []
str_list = []

for item in a:
    if isinstance(item, int):
        int_list.append(item)


for item in a:
    if isinstance(item, str):
        str_list.append(item)

int_list.sort()
str_list.sort()

b = int_list + str_list

c = []
for item in int_list:
    if item % 2 == 0:
        c.append(item)

cups = []
for item in str_list:
    cups.append(item.upper())



print("Головний список:", a)
print("Відсортований список (int по зростанню, str а-я):", b)
print("Числа кратні 2:", c)
print("Список з капсом:", cups)
