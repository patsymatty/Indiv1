#!/usr/bin/env python
# coding: utf-8

# In[8]:


gross_pay = int(input("Gross pay: "))
tax_rate = float(input("Tax rate: "))
expenses = int(input("Expenses: "))

def savings(gross_pay, tax_rate, expenses):
    import math
    s = (1-tax_rate)*gross_pay - expenses
    return math.floor(s)

result = savings(gross_pay, tax_rate, expenses)
print(result)


# In[2]:


total_material = int(input("Total Material: "))
material_units = str(input("Material Units: "))
num_jobs = int(input("Number of Jobs: "))
job_consumption = int(input("Job Consumption: "))

def material_waste(total_material, material_units, num_jobs, job_consumption):
    waste = str(total_material - num_jobs*job_consumption) + material_units
    return waste

result = material_waste(total_material, material_units, num_jobs, job_consumption)
print(result)


# In[12]:


principal = int(input("Amount invested: "))
rate = float(input("Rate per period: "))
periods = int(input("Number of Periods: "))

def interest(principal, rate, periods):
    import math
    i = (principal*rate*periods) + principal
    return math.floor(i)

result = interest(principal, rate, periods)
print(result)


# In[11]:


weight = float(input("Weight in pounds: "))
height = list(map(int, input("Height in inches: ").split()))

def body_mass_index(weight, height):
    weight_kg = weight*0.45
    height_inches = height[0] * 12 + height[1]
    height_m = int(height_inches) * 0.0254
    bmi = weight_kg / (height_m ** 2)
    return(bmi)

result = body_mass_index(weight, height)
print(result)

