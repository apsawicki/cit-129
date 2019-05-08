import csv
import pandas
import matplotlib.pyplot as plt

# REad in energy csv with csv and feed into a DataFrame which pandas can visualize

with open('usaPowerSources2001-2018.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    energy = [row for row in reader]
energyDF = pandas.DataFrame(energy)

energyPD = pandas.read_csv('usaPowerSources2001-2018.csv', index_col='Month')
print(energyPD.solar.describe())
plt.plot(energyPD)
plt.show()
