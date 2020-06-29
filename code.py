class CoffeMachine:
    coffee_types = ["espresso", "latte", "cappuccino"]
    action = None
    coffee_type = None
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money
        
        self.needs = [[250, 0, 16, 1] , [350, 75, 20, 1], [200, 100, 12, 1]]
    def send_action(self, action):
        self.action = action

    def send_coffee_type(self, choice):
        self.coffee_type = self.coffee_types[int(choice) - 1]
    
    def send_coffee(self):
        if self.check_supplier():
            if self.coffee_type == self.coffee_types[0]:
                self.send_espresso()
            elif self.coffee_type == self.coffee_types[1]:
                self.send_latte()
            elif self.coffee_type == self.coffee_types[2]:
                self.send_cappuccino()
  
    def send_espresso(self):
        self.water -= 250
        self.coffee_beans -= 16
        self.cups -= 1
        self.money += 4

    def send_latte(self):
        self.water -= 350
        self.milk -= 75
        self.coffee_beans -= 20
        self.cups -= 1
        self.money += 7

    def send_cappuccino(self):
        self.water -= 200
        self.milk -= 100
        self.coffee_beans -= 12
        self.cups -= 1
        self.money += 6
    
    def check_supplier(self):
        index = self.coffee_types.index(self.coffee_type)
        if self.water - self.needs[index][0] < 0:
            print("Sorry, not enough water!")
        elif self.milk - self.needs[index][1] < 0:
            print("Sorry, not enough milk!")
        elif self.coffee_beans - self.needs[index][2] < 0:
            print("Sorry, not enough coffee beans!")
        elif self.cups - self.needs[index][3] < 0:
            print("Sorry, not enough cup!")
        else:
            print("I have enough resources, making you a {}!".format(self.coffee_types[index]))
            return True
        return False
    
    def take_money(self):
        print("A gave you {}".format(self.money))
        self.money = 0

    def fill(self,water, milk, coffee_beans, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.cups += cups

    def __str__(self):
        return """The coffee machine has:\n{} of water\n{} of milk\n{} of coffee_beans\n{} of disposable cups\n{} of money""".format(self.water, self.milk, self.coffee_beans, self.cups, self.money)

ICoffee = CoffeMachine(400,540,120,9,550)

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    ICoffee.send_action(input())
    if(ICoffee.action == "buy"):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

        choice = input()
        if choice != 'back':
            ICoffee.send_coffee_type(choice)
            ICoffee.send_coffee()
    elif(ICoffee.action == "fill"):
        print("Write how many ml of water do you want to add:")
        water = int(input())
        print("Write how many ml of milk do you want to add:")
        milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        coffee_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups = int(input())
        ICoffee.fill(water, milk, coffee_beans, cups)
    elif(ICoffee.action == "take"):
        ICoffee.take_money()
    elif(ICoffee.action == "remaining"):
        print(ICoffee)
    elif(ICoffee.action == "exit"):
        exit()
