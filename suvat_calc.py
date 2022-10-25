import math

print("SuvatCalc V1.0 by Konstantin")
print("Enter the numbers you know, and leave the ones you do not know blank")
print()


def find_displacement(u, v, a, t):
    if u is None:  # u occurs in all equations
        return None, None

    if t is not None:
        if v is not None:
            return (v + u) * t * 0.5, "s = (v + u)t / 2"
        if a is not None:
            return u * t + 0.5 * a * t ** 2, "s = ut + 0.5at^2"

    if a is not None and v is not None:
        return (v ** 2 - u ** 2) / (2 * a), "v^2 = u^2 + 2as"

    return None, None


def find_initial_velocity(s, v, a, t):
    if v is not None:
        if a is not None:
            if t is not None:
                return v - a * t, "v = u + at"
            elif s is not None:
                return math.sqrt(v ** 2 - 2 * a * s), "v^2 = u^2 + 2as"
        elif t is not None and s is not None:
            return (2 * s) / t - v, "s = (v + u)t / 2"
    elif s is not None and t is not None and a is not None:
        return (s - 0.5 * a * t ** 2) / t, "s = ut + 0.5at^2"

    return None, None


def find_final_velocity(s, u, a, t):
    if u is None:  # u occurs in all equations
        return None, None

    if a is not None:
        if t is not None:
            return u + a * t, "v = u + at"
        elif s is not None:
            return math.sqrt(u ** 2 + 2 * a * s), "v^2 = u^2 + 2as"
    elif s is not None and t is not None:
        return (2 * s) / t - u, "s = (v + u)t / 2"

    return None, None


def find_acceleration(s, u, v, t):
    if u is None:  # u occurs in all equations
        return None, None

    if v is not None:
        if t is not None:
            return (v - u) / t, "v = u + at"
        elif s is not None:
            return (v ** 2 - u ** 2) / (2 * s), "v^2 = u^2 + 2as"
    elif s is not None and t is not None:
        return (s - u * t) / (0.5 * t ** 2), "s = ut + 0.5at^2"

    return None, None


def find_time(s, u, v, a):
    if u is None:  # u occurs in all equations
        return None, None

    if a is not None and a != 0:
        if v is not None:
            return (v - u) / a, "v = u + at"
        if s is not None:
            return (math.sqrt(2 * a * s + u ** 2) - u) / a, "s = ut + 0.5at^2"
    elif s is not None and v is not None:
        return (2 * s) / (v - u), "s = (v + u)t / 2"


def input_variable(symbol, unit):
    v = input(symbol + "(" + unit + ")=")
    return None if v == "" else float(v)


suvat_letters = "Suvat"
suvat_units = ["m", "ms^-1", "ms^-1", "ms^-2", "s"]
suvat = [input_variable(suvat_letters[index], suvat_units[index]) for index in range(len(suvat_letters))]
equations = [find_displacement, find_initial_velocity, find_final_velocity, find_acceleration, find_time]

if suvat.count(None) >= 3:
    print("ERROR! Insufficient knowledge: at least 3 variables need to be known")
    exit(0)

print()
print("Calculating...")
print()

equations_used = []
variables_solved = []

while None in suvat:
    for index in range(len(suvat)):
        value = suvat[index]
        if value is None:
            args = suvat.copy()
            del args[index]
            solved_value, equation_used = equations[index](*args)
            if solved_value is not None:
                suvat[index] = solved_value
                equations_used.append(equation_used)
                variables_solved.append(suvat_letters[index])

print("Chronological use of equations:")
for i in range(len(equations_used)):
    print(str(i) + ". " + variables_solved[i] + ": " + equations_used[i])
print()

print("\n".join(suvat_letters[i] + "(" + suvat_units[i] + ")=" + str(suvat[i]) for i in range(len(suvat))))
