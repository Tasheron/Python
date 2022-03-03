def show(file_format):
    if file_format == 1:
        return open("users.scv", 'r', encoding="utf-8")
    else:
        return open("users-sec.scv", 'r', encoding="utf-8")

def write(user_data):
    data = open("users.scv", "a", encoding="utf-8")
    data.write("\n")
    for i in range(0, len(user_data)):
        data.write(f"\n{user_data[i].replace(' ', '')}")
    data.close()
    data = open("users-sec.scv", "a", encoding="utf-8")
    data.write(f"\n{user_data[0].replace(' ', '')}")
    for i in range(1, len(user_data)):
        data.write(f", {user_data[i].replace(' ', '')}")
    data.write(";")