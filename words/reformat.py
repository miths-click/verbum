dict = {
    "Romam": ["to Rome"],
    "romanus, romani, m.": ["Roman"],
    "arx, arcis, f.": ["citadel"]
}
list = []
stage = []

idx = 848

for key in dict:
    parts = key.split(", ")
    short = parts[0]
    hasPOS = False
    pos = ""
    full = ""
    if (len(parts[-1]) == 2 and parts[-1][1] == '.'):
        pos = parts[-1]
    if (hasPOS):
        full = ", ".join(parts[:-1])
    else :
        full = ", ".join(parts)
    translations = dict[key]

    list.append([short, full, pos, translations])

for i in range(848, 848 + len(dict)):
    stage.append(i)

for entry in list:
    print(str(entry) + ",")

print(str(stage))
