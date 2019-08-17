baseItems = {
    "BF": "B.F. Sword",
    "CV": "Chain Vest",
    "GB": "Giant's Belt",
    "NLR": "Needlessly Large Rod",
    "RB": "Recurve Bow",
    "Tear": "Tear of the Goddess",
    "Spat": "Spatula"
}
userInventory = []

def printInventory():
    inventoryString = ', '.join([baseItems[item] for item in userInventory])
    print("Your current items: " + inventoryString)

def printBaseItems():
    print(f"""These are the available item codes, followed by their name
    BF: {baseItems["BF"]}
    CV: {baseItems["CV"]}
    GB: {baseItems["GB"]}
    NLR: {baseItems["NLR"]}
    RB: {baseItems["RB"]}
    Tear: {baseItems["Tear"]}
    Spat: {baseItems["Spat"]}
    """)

def getItems():
    print("Enter your items, separated by Enter.  When you are done press enter again.")
    isEmpty = False
    while isEmpty == False:
        newItem = input("Item? ")
        if len(newItem) > 0:
            if newItem in baseItems:
                userInventory.append(newItem)
                print(f"You added a {baseItems[newItem]}")
            else:
                print("Invalid Item Code.  Try again.")
        else:
            isEmpty = True
            printInventory()


printBaseItems()
getItems()

