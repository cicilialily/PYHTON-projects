def print_number(x):
    print("NUMVER IS", x)

rename_print = print_number
rename_print(100)
print_number(100)

color = 'RED'

corvette = {
    "color": color
}

print("LITTLE", corvette["color"], "CORVETTE")

def run():
    print("VROOM")

corvette = {
    "color": "Red",
    "run": run
}

print("my", corvette["color"], "can go")
corvette["run"] ()

#get the run function out of the corvette dict
myrun = corvette["run"]
#run it
myrun()