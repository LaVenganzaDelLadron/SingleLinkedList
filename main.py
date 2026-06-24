from sllist import SingleLinkedList

food = SingleLinkedList()

def test_push():
    food.store_first("Sushi")
    food.store_first("Ramen")
    food.store_first("Instant Noodles")
    food.store_first("Bulalo")
    food.store_first("Adobo")
    food.store_first("Paksiw")

def test_insert_last():
    food.store_last("Fish Ball")

def test_pop_first():
    food.pop_first()

def test_pop_last():
    food.pop_last()

def test_show():
    return food.show_specific("Ramen")

def test_get_all():
    food.get_all()

def test_remove():
    return food.remove("Bulalo")

def test_show_first():
    return food.show_first()

def test_show_last():
    return food.show_last()

def test_count():
    return food.count()

def test_unshift():
    return food.unshift()


test_push()
test_get_all()
print("====================================")
print(test_show())
print(test_remove())
print("====================================")
print(test_show_first())
print(test_show_last())
print("====================================")
test_get_all()
print("====================================")
print(test_count())
print("====================================")
print(test_unshift())
print("====================================")
test_get_all()