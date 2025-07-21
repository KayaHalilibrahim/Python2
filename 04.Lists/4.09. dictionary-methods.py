recipe = {
    "yemekAdi": "Musakka",
    "yemekTarifi": "Recipe description",
    "resim": "1.jpg"
}

# access items
result = recipe["yemekAdi"]
print(result)

result = recipe.get("yemekAdi")
print(result)

result = recipe.keys()
print(result)

result = recipe.values()
print(result)

result = recipe.items()
print(result)


# update items
print()

# recipe["yemekAdi"] = "Çiğköfte"
# result = recipe
# print(result)

recipe.update({"yemekAdi": "Çiğköfte"})
result = recipe
print(result)

print()

recipe.update({"yemekAdi2": "Kebab"})
result = recipe
print(result)


# delete items

recipe.pop("resim")
result = recipe
print(result)

print()
recipe.popitem()
result = recipe
print(result)

recipe.clear()
result = recipe
print(result)


"""
Output:
Musakka
Musakka
dict_keys(['yemekAdi', 'yemekTarifi', 'resim'])
dict_values(['Musakka', 'Recipe description', '1.jpg'])
dict_items([('yemekAdi', 'Musakka'), ('yemekTarifi', 'Recipe description'), ('resim', '1.jpg')])

{'yemekAdi': 'Çiğköfte', 'yemekTarifi': 'Recipe description', 'resim': '1.jpg'}

{'yemekAdi': 'Çiğköfte', 'yemekTarifi': 'Recipe description', 'resim': '1.jpg', 'yemekAdi2': 'Kebab'}
{'yemekAdi': 'Çiğköfte', 'yemekTarifi': 'Recipe description', 'yemekAdi2': 'Kebab'}

{'yemekAdi': 'Çiğköfte', 'yemekTarifi': 'Recipe description'}
{}
"""


