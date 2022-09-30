import main
import function

def button_click():
    menu = main.menu()
    choice = main.control_menu()
    if choice:
        go_to = {
            '1': function.add,
            '2': function.delete_entery,
            '3': function.import_format1,
            '4': function.import_format2,
            '5': function.export_format1,
            '6': function.export_format2,
            '7': function.view_contakt,
            '8': function.find_contakt_surname,
            '9': function.exit
        }
        go_to[menu]()
