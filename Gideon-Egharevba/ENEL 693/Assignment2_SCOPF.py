#Assignment 2D-SCOPF

#Import pyomo package
from pyomo.environ import*
#import pi from math library
from math import pi

#Create a concrete model
model = ConcreteModel()

#Define domain of variables to represent generator outputs for base case
model.PG1 = Var(within = NonNegativeReals)
model.PG2 = Var(within = NonNegativeReals)
model.QG1 = Var(within = Reals)
model.QG2 = Var(within = Reals)
model.V1 = Var(within = NonNegativeReals)
model.V2 = Var(within = NonNegativeReals)
model.d1 = Var(within = Reals)
model.d2 = Var(within = Reals)

#Define domain of variables to represent generator outputs for contingency
model.PG1w = Var(within = NonNegativeReals)
model.PG2w = Var(within = NonNegativeReals)
model.QG1w = Var(within = Reals)
model.QG2w = Var(within = Reals)
model.V1w = Var(within = NonNegativeReals)
model.V2w = Var(within = NonNegativeReals)
model.d1w = Var(within = Reals)
model.d2w = Var(within = Reals)


#Define objective function
model.objective = Objective (expr= model.PG1 + 2* (model.PG2), sense =minimize)

#-------------------------------------Define constraints---------------#

#Define constraints for base case

#Active power balance constraints
model.constraint1 = Constraint (expr = model.PG1 - 0.8==(model.V1)**2 * 9.9504 * cos(-1.4711) - model.V1*model.V2*9.9504*cos(model.d1 - model.d2 +1.4711) +(model.V1)**2 * 9.9504 * cos(-1.4711) - model.V1*model.V2*9.9504*cos(model.d1 - model.d2 +1.4711))
model.constraint2 = Constraint (expr =model.PG2 - 1.2 ==(model.V2)**2 * 9.9504 * cos(-1.4711) - model.V1*model.V2*9.9504*cos(model.d2 - model.d1 +1.4711)+(model.V2)**2 * 9.9504 * cos(-1.4711) - model.V1*model.V2*9.9504*cos(model.d2 - model.d1 +1.4711))

#Active reactive balance constraints
model.constraint3 = Constraint (expr = model.QG1 - 0.6   == - (model.V1)**2 * 9.9504 * sin(-1.4711) - model.V1*model.V2*9.9504*sin(model.d1 - model.d2 +1.4711) - (model.V1)**2 * 9.9504 * sin(-1.4711) - model.V1*model.V2*9.9504*sin(model.d1 - model.d2 +1.4711))
model.constraint4 = Constraint (expr = model.QG2 - 0.6 == - (model.V2)**2 * 9.9504 * sin(-1.4711) - model.V1*model.V2*9.9504*sin(model.d2 - model.d1 +1.4711)- (model.V2)**2 * 9.9504 * sin(-1.4711) - model.V1*model.V2*9.9504*sin(model.d2 - model.d1 +1.4711))

# #Capacity constraints of transmission lines in directions 1-2a
model.constraint5 = Constraint(expr = ((model.V1)**2 * 9.9504 * cos(-1.4711) - model.V1*model.V2*9.9504*cos(model.d1 - model.d2 +1.4711))**2 +  ((model.V1)**2 * -9.9504 * sin(-1.4711) - model.V1*model.V2*9.9504*sin(model.d1 - model.d2 +1.4711))**2 <= 0.25)


# #Capacity constraints of transmission lines in directions 1-2b
model.constraint6 = Constraint(expr = ((model.V1)**2 * 9.9504 * cos(-1.4711) - model.V1*model.V2*9.9504*cos(model.d1 - model.d2 +1.4711))**2 +
                                       ((model.V1)**2 * -9.9504 * sin(-1.4711) - model.V1*model.V2*9.9504*sin(model.d1 - model.d2 +1.4711))**2 <= 0.25)


# #Capacity constraints of transmission lines in directions 2-1a
model.constraint7 = Constraint(expr = ((model.V2)**2 * 9.9504 * cos(-1.4711) - model.V2*model.V1*9.9504*cos(model.d2 - model.d1 +1.4711))**2 +
                                       ((model.V2)**2 * -9.9504 * sin(-1.4711) - model.V2*model.V1*9.9504*sin(model.d2 - model.d1 +1.4711))**2  <= 0.25)

# #Capacity constraints of transmission lines in directions 2-1b
model.constraint8 = Constraint(expr = ((model.V2)**2 * 9.9504 * cos(-1.4711) - model.V2*model.V1*9.9504*cos(model.d2 - model.d1 +1.4711))**2 +
                                       ((model.V2)**2 * -9.9504 * sin(-1.4711) - model.V2*model.V1*9.9504*sin(model.d2 - model.d1 +1.4711))**2  <= 0.25)


#Active power limits
model.constraint9 = Constraint (rule = (0, model.PG1, 3))
model.constraint10 = Constraint (rule = (0, model.PG2, 0.8))

#Reactive power limits
model.constraint11 = Constraint (rule = (-2, model.QG1, 2))
model.constraint12 = Constraint (rule = (-2, model.QG2, 2))

#Voltage magnitude limits
model.constraint13 = Constraint (rule = (0.95, model.V1, 1.1))
model.constraint14 = Constraint (rule = (0.95, model.V2, 1.1))

#Voltage angle limits
model.constraint15 = Constraint (rule = ((-1 * pi), model.d1, pi))
model.constraint16 = Constraint (expr = model.d2 ==0)


#Define constraints for Contingency-----

#Active power balance constraints
model.constraint17 = Constraint (expr = model.PG1w - 0.8==
                                       (model.V1w)**2 * 9.9504 * cos(-1.4711) - model.V1w*model.V2w*9.9504*cos(model.d1w - model.d2w +1.4711))

model.constraint18 = Constraint (expr =model.PG2w - 1.2 ==
                                       #(model.V2w)**2 * 19.9008 * cos(-1.4711) - model.V1w*model.V2w*19.9008*cos(model.d2w - model.d1w +1.4711))
                                       (model.V2w)**2 * 9.9504 * cos(-1.4711) - model.V1w*model.V2w*9.9504*cos(model.d2w - model.d1w +1.4711))

#Active reactive balance constraints
model.constraint19 = Constraint (expr = model.QG1w - 0.6 ==
                                        - (model.V1w)**2 * 9.9504 * sin(-1.4711) - model.V1w*model.V2w*9.9504*sin(model.d1w - model.d2w +1.4711))

model.constraint20 = Constraint (expr = model.QG2w - 0.6 ==
                                        - (model.V2w)**2 * 9.9504 * sin(-1.4711) - model.V1w*model.V2w*9.9504*sin(model.d2w - model.d1w +1.4711))


 #Capacity constraints of transmission lines in directions 1-2b
model.constraint22 = Constraint(expr = ((model.V1w)**2 * 9.9504 * cos(-1.4711) - model.V1w*model.V2w*9.9504*cos(model.d1w - model.d2w +1.4711))**2 +
                                       ((model.V1w)**2 * -9.9504 * sin(-1.4711) - model.V1w*model.V2w*9.9504*sin(model.d1w - model.d2w +1.4711))**2 <= 0.5**2)

# #Capacity constraints of transmission lines in directions 2-1b
model.constraint24 = Constraint(expr = ((model.V2w)**2 * 9.9504 * cos(-1.4711) - model.V2w*model.V1w*9.9504*cos(model.d2w - model.d1w +1.4711))**2 +
                                       ((model.V2w)**2 * -9.9504 * sin(-1.4711) - model.V2w*model.V1w*9.9504*sin(model.d2w - model.d1w +1.4711))**2  <= 0.5**2)


#Active power limits
model.constraint25 = Constraint (rule = (0, model.PG1w, 3))
model.constraint26 = Constraint (rule = (0, model.PG2w, 0.8))

#Reactive power limits
model.constraint27 = Constraint (rule = (-2, model.QG1w, 2))
model.constraint28 = Constraint (rule = (-2, model.QG2w, 2))

#Voltage magnitude limits
model.constraint29 = Constraint (rule = (0.95, model.V1w, 1.1))
model.constraint30 = Constraint (rule = (0.95, model.V2w, 1.1))

#Voltage angle limits
model.constraint31 = Constraint (rule = ((-1 * pi), model.d1w, pi))
model.constraint32 = Constraint (expr = model.d2w ==0)

#Ramp limits at node 1
model.constraint33 = Constraint (expr = model.PG1w -model.PG1 <= 0.8)
model.constraint34 = Constraint (expr = model.PG1 - model.PG1w <= 0.8)

#Ramp limits at node 2
model.constraint35 = Constraint (expr = model.PG2w -model.PG2 <= 0.3)
model.constraint36 = Constraint (expr = model.PG2 - model.PG2w <= 0.3)

#Call the ipopt solver to solve the model and save output to "results"
opt = SolverFactory ("ipopt")
results = opt.solve(model)


#Print out solutions to optimization problem
print("Value of Objective function is:", value(model.objective))
print("Optimal Active Power Value of Generator 1 is:",value(model.PG1))
print("Optimal Active Power Value of Generator 2 is:",value(model.PG2))
print("Optimal Reactive Power Value of Generator 1 is:",value(model.QG1))
print("Optimal Reactive Power Value of Generator 2 is:",value(model.QG2))
print("Optimal Voltage magnitude Generator 1 is:",value(model.V1))
print("Optimal Voltage magnitude Generator 2 is:",value(model.V2))
print("Voltage angle of generator 1:",value(model.d1))
print("Voltage angle of generator 2:",value(model.d2))

# print ("\n")
print ("After contingency")
# print ("\n")
print("Optimal Active Power Value of Generator 1  is:",value(model.PG1w))
print("Optimal Active Power Value of Generator 2 is:",value(model.PG2w))
print("Optimal Reactive Power Value of Generator 1 is:",value(model.QG1w))
print("Optimal Reactive Power Value of Generator 2 is:",value(model.QG2w))
print("Optimal Voltage magnitude Generator 1 is:",value(model.V1w))
print("Optimal Voltage magnitude Generator 2 is:",value(model.V2w))
print("Voltage angle of generator 1:",value(model.d1w))
print("Voltage angle of generator 2:",value(model.d2w))
print("Power transfer from 1-2b is",value(model.constraint22))
print("Power transfer from 2-1b is",value(model.constraint24))

print ("\n")

