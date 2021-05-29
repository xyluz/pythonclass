class Budget:
    class Food:
        def __init__(self, balance):
            self.bal = balance

    def getBalance(self):
        return self.bal

    def setBalance(self, value):
        self.bal = value


class Clothing:
    def __init__(self, balance):
        self.bal = balance

    def getBalance(self):
        return self.bal

    def setBalance(self, value):
        self.bal = value


class Entertainment:
    def __init__(self, balance):
        self.bal = balance

    def getBalance(self):
        return self.bal

    def setBalance(self, value):
        self.bal = value


class Budget:
    def __init__(self):
        """Instantiate the food, clothing ang entertainment class and initialize them with a balance of zero"""
        self.food = Food(0)
        self.clothing = Clothing(0)
        self.entertainment = Entertainment(0)
        self.pairs = {"food": self.food,
                      "clothing": self.clothing,
                      "entertainment": self.entertainment
                      }

    def categoryIsValid(self, category):
        """Verifies if the category is valid"""
        if category in self.pairs:
            return True
        return False

    def deposit(self, amount, categ):
        """Deposit into the specified category"""
        if self.categoryIsValid(categ) == True:
            category = self.pairs[categ]
            curBal = category.getBalance()
            balAfterDeposit = amount + curBal
            category.setBalance(balAfterDeposit)
            print("Deposit successful.")
        else:
            print("Invalid category.")

    def withdrawal(self, amount, categ):
        """Withdraws from the specified category"""
        if self.categoryIsValid(categ) == True:
            category = self.pairs[categ]
            curBal = category.getBalance()
            if curBal < amount:
                print("Error. Insufficient funds.")
            else:
                balAfterWithdrawal = curBal - amount
                category.setBalance(balAfterWithdrawal)
                print("Take your cash...#{amount}")
        else:
            print("Invalid category.")

    def showCategoryBalances(self):
        """Displays balance for all categories"""
        foodBalance = self.food.getBalance()
        clothingBalance = self.clothing.getBalance()
        entertainmentBalance = self.entertainment.getBalance()
        print("The balance for the food category is: {foodBalance}")
        print("The balance for the clothing category is: {clothingBalance}")
        print("The balance for the entertainment category is: {entertainmentBalance}")

    def transfer(self, amount, srcCateg, destCateg):
        """Tranfers from the source category to another category"""
        if (self.categoryIsValid(srcCateg) and self.categoryIsVald(destCateg)) == True:
            src, dest = self.pairs[srcCateg], self.pairs[destCateg]
            srcBalance = src.getBalance()
            if srcBalance >= amount:
                srcRemBalance = srcBalance - amount
                src.setBalance(srcRemBalance)
                destCurBalance = dest.getBalance()
                destFinBalance = destCurBalance + amount
                dest.setBalance(destFinBalance)
                print("Transfer Succesful.")
            else:
                print("Error. Insufficient funds.")
        else:
            print("Invalid category.")


#Instantiate the Budget Class
  
