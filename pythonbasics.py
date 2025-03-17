# %%
import numpy as np

# %%
def gnrlist():
    gnr = np.random.default_rng(1)
    list4 = np.round(gnr.random(5) * 100, 2)
    return  list4

# %%
list1 = gnrlist()
print("Generated array: %s" %list1)


# %%
def amplitude(list1):
    maxvalue = max(list1)
    minvalue = min(list1)
    amplitudevalue = maxvalue - minvalue
    return amplitudevalue

# %%
amplitudecalc = amplitude(list1)
print("Generated array: %s \nMaximum value: %s \nMinimum value: %s \nAmplitude calculated : %s" % (list1, max(list1), min(list1), amplitudecalc))

# %%
list2 = input()
print("Typed sentence: %s" % list2)

# %%
def verticalstring(list2):
    result = ""
    for i in range(0, len(list2)):
        result += list2[i] + "\n"
    return result 

# %%
vertical = verticalstring(list2)
print(vertical)

# %%
def weightcalc():
    weight = int(input("Type your weight: "))
    if(weight <= 10):
        print("The total value is: $50.00" )
    elif(weight <= 20):
        print("The total value is: $80.00")
    else:
        print("The value is not accepted")
    return ""

# %%
weightresult = weightcalc()
print(weightresult)



# %%
