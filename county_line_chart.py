import pandas as pd
import matplotlib.pyplot as plt

salaries_all_years = pd.read_csv("salaries_all_years.csv", delimiter=";"
                                 , engine="python", encoding="utf-8")

salaries_all_years.columns = ["ID", "Region", "2002", "2003", "2004", "2005", \
                              "2006", "2007", "2008", "2009", "2010", "2011", \
                              "2012", "2013", "2014", "2015", "2016", \
                              "2017", "2018", "unnamed"]
salaries_all_years.drop("unnamed", axis=1, inplace=True)
salaries_all_years.iloc[:, 2:] = salaries_all_years.iloc[:, 2:].replace(',', '.', regex=True)
salaries_all_years.iloc[:, 2:] = salaries_all_years.iloc[:, 2:].astype(float)

years = salaries_all_years.columns[2:]

id_region = salaries_all_years.iloc[:, 1]
id_region = id_region.to_dict()

while True:
    print("""
    Please input name of county exactly as in below examples.
    County: Powiat kozienicki. 
    Voivodeship: DOLNOŚLĄSKIE
    """)
    search_region = input("Please input name of county:")
    if search_region not in id_region.values():
        print("You put wrong name of county. Please verify if you \
        correctly input name of county")
        answer = input("Do you want to stop the process?: Y/N ")
        if answer == "Y" or answer == "y" or answer == "yes":
            print("process stopped")
            break
    else:
        print("You choose: ", search_region)
        break

for index, region in id_region.items():
    if region == search_region:
        salaries = salaries_all_years.values[index][2:]

salaries_Poland = salaries_all_years.values[0][2:]

line_chart = plt.figure()

plt.plot(years, salaries, label=search_region)
plt.plot(years, salaries_Poland, label="Polska")
plt.axhline(2500, ls="--", color="k")
plt.axhline(3500, ls="--", color="k")
plt.axhline(4500, ls="--", color="k")
plt.axhline(5500, ls="--", color="k")
l = plt.legend()
for text in l.get_texts():
    text.set_color("red")
plt.title("Average salary by years in Polska and " + search_region, color="k")
plt.xlabel("Year", color="k")
plt.ylabel("Average salary", color="k")
plt.grid(True)
plt.xticks(years, rotation=45)

plt.show()

answer = input("Do you want to save chart?: Y/N ")
if answer == "Y" or answer == "y" or answer == "yes":
    format = input("In what format? pdf/png")
    if format == "pdf" or format == "PDF":
        line_chart.savefig("county_line_chart_pdf.pdf")
        print("picture was saved in pdf")
    elif format == "png" or format == "PNG":
        line_chart.savefig("county_line_chart_png.png", dpi=300)
        print("picture was saved in png")
    else:
        print("You did not choose pdf or png format")
else:
    print("Picture was not saved")