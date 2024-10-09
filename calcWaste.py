# Carbon emissions for landfilling various types of waste, metric tons CO2 / short ton material
LANDFILL_EMISSIONS = {
    "mixed_paper": 0.89,
    "mixed_plastics": 0.02,
    "mixed_recyclables": 0.75,
    "food_waste": 0.68
}

# Carbon emissions for recycling various types of waste, metric tons CO2 / short ton material
RECYCLED_EMISSIONS = {
    "mixed_paper": 0.07,
    "mixed_plastics": 0.22,
    "mixed_recyclables": 0.09
}

# Average waste per US person in kg/day
AVERAGE_WASTE = {
    "mixed_paper": .81,
    "mixed_plastics": .61,
    "mixed_recyclables": .64,
    "food_waste": .45
}

COMPOST_EMISSIONS = .11

def calculatePaperLandfillEmissions(paperWaste):
    if paperWaste is None:
        paperWaste = AVERAGE_WASTE["mixed_paper"]
    return paperWaste * LANDFILL_EMISSIONS["mixed_paper"]

def calculatePaperRecycledEmissions(paperWaste):
    if paperWaste is None:
        paperWaste = AVERAGE_WASTE["mixed_paper"]
    return paperWaste * RECYCLED_EMISSIONS["mixed_paper"]

def calculatePlasticLandfillEmissions(plasticWaste):
    if plasticWaste is None:
        plasticWaste = AVERAGE_WASTE["mixed_plastics"]
    return plasticWaste * LANDFILL_EMISSIONS["mixed_plastics"]

def calculatePlasticRecycledEmissions(plasticWaste):
    if plasticWaste is None:
        plasticWaste = AVERAGE_WASTE["mixed_plastics"]
    return plasticWaste * RECYCLED_EMISSIONS["mixed_plastics"]

def calculateRecyclableLandfillEmissions(recyclableWaste):
    if recyclableWaste is None:
        recyclableWaste = AVERAGE_WASTE["mixed_recyclables"]
    return recyclableWaste * LANDFILL_EMISSIONS["mixed_recyclables"]

def calculateRecyclableRecycledEmissions(recyclableWaste):
    if recyclableWaste is None:
        recyclableWaste = AVERAGE_WASTE["mixed_recyclables"]
    return recyclableWaste * RECYCLED_EMISSIONS["mixed_recyclables"]

def calculateFoodLandfillEmissions(foodWaste):
    if foodWaste is None:
        foodWaste = AVERAGE_WASTE["food_waste"]
    return foodWaste * LANDFILL_EMISSIONS["food_waste"]

def calculateFoodCompostedEmissions(foodWaste):
    if foodWaste is None:
        foodWaste = AVERAGE_WASTE["food_waste"]
    return foodWaste * COMPOST_EMISSIONS