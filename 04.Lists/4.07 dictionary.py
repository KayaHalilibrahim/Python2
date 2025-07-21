# Key-value
# sortable
# can be updated


cities = ["Şanlıurfa","Ankara"]
plate = [63,6]


print(plate[0],cities[0])
print(plate[1],cities[1])

print(plate[cities.index('Ankara')])
print(plate[cities.index('Şanlıurfa')])


plates = {'Şanlıurfa':63,
          'Ankara':6}


plates['Balıkesir']=10

print(plates['Ankara'])
print(plates['Şanlıurfa'])
print(plates['Balıkesir'])

