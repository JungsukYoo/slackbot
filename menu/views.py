from database.models import Restaurent, Restaurent_menu


def search_all():
    lists = Restaurent.query.all()
    return lists

