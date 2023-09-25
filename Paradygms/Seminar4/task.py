from statistics import mean

massX = [1, 5, 3, 8, 2]
massY = [122, 7, 3, 9, 0]

meanX = mean(massX)
meanY = mean(massY)

print(meanX, meanY)

raznX = list(map(lambda x: x - meanX, massX))
# print(raznX)
raznY = list(map(lambda x: x - meanY, massY))
# print(raznY)
chislitel = sum(list(map(lambda x, y: (x - meanX)*(y-meanY), massX, massY)))

znamenatel = ((sum(list(map(lambda x: x**2, raznX)))) * (sum(list(map(lambda x: x**2, raznY)))))**0.5

print(chislitel/znamenatel)




