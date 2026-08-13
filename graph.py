import matplotlib.pyplot as plt
from tkinter import messagebox

from database import get_records


# -----------------------------------
# BMI Progress Dashboard
# -----------------------------------

def show_graph(name):

    if name.strip() == "":

        messagebox.showwarning(
            "Input Error",
            "Please enter your name first."
        )

        return


    records = get_records(name)


    if len(records) == 0:

        messagebox.showinfo(
            "No Data",
            "No BMI records found."
        )

        return



    dates = []
    bmi_values = []
    categories = []



    # record format:
    # id,date,weight,height,bmi,category

    for record in records:

        dates.append(
            record[1][:10]
        )

        bmi_values.append(
            record[4]
        )

        categories.append(
            record[5]
        )



    # ==================================
    # Create Dashboard Window
    # ==================================


    plt.figure(
        figsize=(12,8)
    )


    # -----------------------------
    # BMI Trend Chart
    # -----------------------------

    plt.subplot(2,1,1)


    plt.plot(
        dates,
        bmi_values,
        marker="o",
        linewidth=2
    )


    plt.title(
        f"{name}'s BMI Progress"
    )


    plt.xlabel(
        "Date"
    )


    plt.ylabel(
        "BMI"
    )


    plt.grid(True)


    plt.xticks(
        rotation=45
    )




    # -----------------------------
    # BMI Category Analysis
    # -----------------------------


    plt.subplot(2,1,2)


    category_count={}



    for category in categories:

        if category in category_count:

            category_count[category]+=1

        else:

            category_count[category]=1



    plt.bar(
        category_count.keys(),
        category_count.values()
    )


    plt.title(
        "BMI Category Analysis"
    )


    plt.xlabel(
        "Category"
    )


    plt.ylabel(
        "Count"
    )



    plt.tight_layout()


    plt.show()




# -----------------------------------
# Test
# -----------------------------------

if __name__=="__main__":

    user=input(
        "Enter Name:"
    )

    show_graph(user)