import matplotlib.pyplot as plt

class Category:

    def __init__(self, name, limit):

        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):

        self.spent += amount

        if self.spent > self.limit:
            print(
                f"{self.name} exceeded budget!"
            )


food = Category("Food", 5000)
travel = Category("Travel", 3000)

food.add_expense(4500)
food.add_expense(1000)

travel.add_expense(2000)

labels = ["Food", "Travel"]

sizes = [
    food.spent,
    travel.spent
]

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Monthly Budget")
plt.show()