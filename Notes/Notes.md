# Notes de cours

## Boucle dans les tableau

Compréhension de liste :

- Boucle sur un tableau avec une condition

```python
l = [1, 22, 76, 49, 50]
[num for num in l if num % 2 == 0]
```

- Utilisation d'une fonction sur un tableau pour chaque élément

```python
l = [1, 22, 76, 49, 50]
[func(i) for i in l]
```

## Fonction && Objet

- Définir une fonction

```python
def nomFunc(param):
    pass
```
Ps : pass sert juste à avoir du code qui compile. Sinon c'est le corps de fonction

- Définir une class
* Les class ont toujours une majuscule

```python
class MyClass:
    pass
```
* Héritage 
```python
class A:
    pass

class B:
    pass

class MyClass(A):
    pass

class MultiHeritage(A, B)
    pass
```

* En python, toutes méthode accepte en premier paramètre son instanciation, par convention on l'appelle self

```python
class Person:
    def __init__(self, name, lastname):
        self.name =  name
        self.lastname = lastname

    def display(self):
        print("La personne est :", self.name, self.lastname)

abd = Person('Abd', 'Mouz')
print('Le prénom de abd est ', abd.name)
abd.display()
```
Ps(1) : Pour de l'utilisation interne d'une méthode la convention est de nommer la méthode en mettant _ en tout premier
Ps(2) : Pour appeler une méthode parente, on utilise super()

```python
class A:
    def talk(self, name):
        print(name)

class B:
    def talk(self, name):
        print("I'm in B")

class C:
    def talk(self, name):
        print("I'm in C")

class D(A, B, C):


    def talk(self, name):
        super().talk(name)
```

-> Explication : D hérite de A, B et C. quand on lui appelle une méthode parente il récupère la première hérité