scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}


things_that_bite = snakes.union(spiders)
print("Things that bite: ", things_that_bite)

things_that_sting = scorpions.union(vespas)
print("Things that sting: ", things_that_sting)

arachnids = spiders.union(scorpions)
print("Arachnids: ", arachnids)