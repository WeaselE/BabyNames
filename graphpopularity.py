import pandas as pd
from matplotlib import pyplot as plt

#Loading file into pandas
fl = open("baby-names-by-state.csv", "r")
df = pd.read_csv("baby-names-by-state.csv")
df.drop("state", axis=1, inplace=True)
df.drop("sex", axis=1, inplace=True)
fl.close()

def filter_name(df, name):
    new_df = df[df['name'] == name]
    new_df.groupby("year", group_keys=False)
    new_df.nsmallest(len(new_df), "year")
    print(new_df["year"])
    return x, new_df["number"]

def create_graph(graphplt):
    plt.plot(graphplt["year"], graphplt["number"], label=nm)
    plt.xlabel("Year")
    plt.ylabel("Count of name that year")
    plt.legend()
    plt.xlim([1960, 2008])
    plt.xticks([i for i in range(2008, 1960, -15)])
    plt.show()
    # plt.savefig("count of " + nm + ".png", dpi=1000)

if __name__ == "__main__":
    nm = input("Please enter a name here: ")
    nm = nm.strip()
    print(nm)
    if nm == "":
        nm = "David"
    filtered = filter_name(df, nm)
    create_graph(filtered)


    