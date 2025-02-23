from controller import ContactController
from model import ContactBook
from view import ContactView

if __name__ == "__main__":
    contact_book = ContactBook()
    view = ContactView()
    controller = ContactController(contact_book, view)
    controller.run()