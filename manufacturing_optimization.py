# Python code using PuLP for optimization

from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Create the model
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Define the decision variables
lemonade = LpVariable(name="lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

# Add constraints
model += (2 * lemonade + 1 * fruit_juice <= 100, "water_constraint")
model += (1 * lemonade <= 50, "sugar_constraint")
model += (1 * lemonade <= 30, "lemon_juice_constraint")
model += (2 * fruit_juice <= 40, "fruit_puree_constraint")

# Set the objective function
model += lpSum([lemonade, fruit_juice])

# Solve the problem
model.solve()

# Get the results
lemonade_qty = lemonade.varValue
fruit_juice_qty = fruit_juice.varValue

print(f"Lemonade: {lemonade_qty}")
print(f"Fruit Juice: {fruit_juice_qty}")
