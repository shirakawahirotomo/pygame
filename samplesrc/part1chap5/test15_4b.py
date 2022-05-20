def gap(score):
    if score >= 90:
        return "S"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

scorelist = [95,75,30,85]
for score in scorelist:
    print(score,"点は、",gap(score))