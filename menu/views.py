from database.models import Restaurent, Restaurent_menu


def search_all():
    list = Restaurent.query.all()
    return list

