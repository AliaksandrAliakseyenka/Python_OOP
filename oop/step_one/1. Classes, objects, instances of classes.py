'''
Зачем нужны классы?
• Классы – это программные компоненты на
языке Python, точно такие же, как функции
и модули.
Классы имеют три важных отличия:
    • Множество экземпляров
    • Адаптация через наследование
    • Перегрузка операторов
'''

'''
Основными понятиями, используемыми в ООП, являются:
    • класс;
    • объект;
    • наследование;
    • инкапсуляция;
    • полиморфизм.
'''

# The class of this template at create objects
class Car:
    model = "BMW"
    engine = 4.5

# Creating an instance of a class
a = Car()
b = Car()


#get id
print(id(a))
print(id(b))

isinstance(a, Car)
type(b.model)