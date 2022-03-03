import view
import data as file_data

while not (view.action == 1 or view.action == 2):
    view.error(1)

if view.action == 1:
    while not (view.file_format == 1 or view.file_format == 2):
        view.error(2)
    data = file_data.show(view.file_format)
    view.show_users(data.read())
    data.close()
else:
    user_data = view.add_user().split(",")
    file_data.write(user_data)