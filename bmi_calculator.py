import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from database import (
    save_record,
    get_records,
    get_statistics,
    export_csv,
    update_record,
    delete_record
)

from graph import show_graph


# -----------------------------
# Main Window
# -----------------------------
window = tk.Tk()
window.title("Professional BMI Calculator")
window.geometry("700x780")
window.configure(bg="#F2F6FC")
window.resizable(False, False)


# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    window,
    text="BMI HEALTH CALCULATOR",
    font=("Arial", 24, "bold"),
    fg="#0B5D8A",
    bg="#F2F6FC"
)
title.pack(pady=15)


# -----------------------------
# Main Frame
# -----------------------------
frame = tk.Frame(
    window,
    bg="white",
    bd=2,
    relief="groove"
)
frame.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)


# -----------------------------
# Name
# -----------------------------
tk.Label(
    frame,
    text="Name",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(pady=(20,5))

name_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial",12)
)
name_entry.pack()


# -----------------------------
# Weight
# -----------------------------
tk.Label(
    frame,
    text="Weight (kg)",
    font=("Arial",12,"bold"),
    bg="white"
).pack(pady=(15,5))

weight_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial",12)
)
weight_entry.pack()


# -----------------------------
# Height
# -----------------------------
tk.Label(
    frame,
    text="Height (m)",
    font=("Arial",12,"bold"),
    bg="white"
).pack(pady=(15,5))

height_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial",12)
)
height_entry.pack()


# -----------------------------
# Result Label
# -----------------------------
result_label = tk.Label(
    frame,
    text="",
    font=("Arial",18,"bold"),
    bg="white"
)
result_label.pack(pady=15)


# -----------------------------
# Advice
# -----------------------------
advice_label = tk.Label(
    frame,
    text="",
    bg="white",
    justify="left",
    wraplength=550,
    font=("Arial",11)
)
advice_label.pack()


# -----------------------------
# Healthy Weight
# -----------------------------
healthy_label = tk.Label(
    frame,
    text="",
    bg="white",
    fg="blue",
    font=("Arial",11,"bold")
)
healthy_label.pack(pady=10)


# -----------------------------
# Statistics
# -----------------------------
stats_label = tk.Label(
    frame,
    text="",
    bg="white",
    justify="left",
    font=("Arial",11)
)
stats_label.pack()


# -----------------------------
# Calculate BMI
# -----------------------------
def calculate_bmi():

    try:

        name = name_entry.get().strip()

        if name == "":
            messagebox.showwarning(
                "Input Error",
                "Please enter your name."
            )
            return

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)

        if bmi < 18.5:

            category = "Underweight"
            color = "blue"

            advice = (
                "• Eat nutritious foods.\n"
                "• Increase calorie intake.\n"
                "• Consult a nutritionist."
            )

        elif bmi < 25:

            category = "Normal"
            color = "green"

            advice = (
                "• Maintain a balanced diet.\n"
                "• Exercise regularly.\n"
                "• Drink enough water."
            )

        elif bmi < 30:

            category = "Overweight"
            color = "orange"

            advice = (
                "• Reduce sugary foods.\n"
                "• Walk daily.\n"
                "• Eat more vegetables."
            )

        else:

            category = "Obese"
            color = "red"

            advice = (
                "• Consult a doctor.\n"
                "• Follow a healthy diet.\n"
                "• Exercise regularly."
            )

        result_label.config(
            text=f"BMI : {bmi:.2f}\nCategory : {category}",
            fg=color
        )

        advice_label.config(text=advice)

        min_weight = 18.5 * (height ** 2)
        max_weight = 24.9 * (height ** 2)

        healthy_label.config(
            text=f"Healthy Weight Range : {min_weight:.1f} kg - {max_weight:.1f} kg"
        )

        save_record(
            name,
            weight,
            height,
            bmi,
            category
        )

        total, highest, lowest, average = get_statistics(name)

        stats_label.config(
            text=f"""
Total Records : {total}

Highest BMI : {highest:.2f}

Lowest BMI : {lowest:.2f}

Average BMI : {average:.2f}
"""
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid positive numbers."
        )
        # -----------------------------
# View History
# -----------------------------
def view_history():

    name = name_entry.get().strip()

    if name == "":
        messagebox.showwarning(
            "Warning",
            "Please enter your name."
        )
        return

    records = get_records(name)

    if len(records) == 0:
        messagebox.showinfo(
            "History",
            "No records found."
        )
        return

    history = tk.Toplevel(window)
    history.title(f"{name} - BMI History")
    history.geometry("850x400")

    columns = (
        "ID",
        "Date",
        "Weight",
        "Height",
        "BMI",
        "Category"
    )

    tree = ttk.Treeview(
        history,
        columns=columns,
        show="headings"
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    for row in records:
        tree.insert("", tk.END, values=row)

    scrollbar = ttk.Scrollbar(
        history,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True)

    scrollbar.pack(side="right", fill="y")


# -----------------------------
# Show Graph
# -----------------------------
def show_user_graph():

    name = name_entry.get().strip()

    if name == "":
        messagebox.showwarning(
            "Warning",
            "Please enter your name."
        )
        return

    show_graph(name)


# -----------------------------
# Export CSV
# -----------------------------
def export_report():

    if export_csv():
        messagebox.showinfo(
            "Success",
            "BMI_Report.csv exported successfully."
        )
    else:
        messagebox.showerror(
            "Error",
            "Unable to export CSV."
        )


# -----------------------------
# Clear Fields
# -----------------------------
def clear_fields():

    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_label.config(text="")
    advice_label.config(text="")
    healthy_label.config(text="")
    stats_label.config(text="")


# -----------------------------
# Delete Record
# -----------------------------
def remove_record():

    record_id = simpledialog.askinteger(
        "Delete Record",
        "Enter Record ID:"
    )

    if record_id is None:
        return

    if delete_record(record_id):

        messagebox.showinfo(
            "Success",
            "Record deleted successfully."
        )

    else:

        messagebox.showerror(
            "Error",
            "Record not found."
        )


# -----------------------------
# Edit Record
# -----------------------------
def edit_record():

    messagebox.showinfo(
        "Edit Record",
        "This feature can be extended to edit the selected record."
    )


# -----------------------------
# Exit
# -----------------------------
def exit_program():

    answer = messagebox.askyesno(
        "Exit",
        "Do you really want to exit?"
    )

    if answer:
        window.destroy()


# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(
    frame,
    bg="white"
)

button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Calculate BMI",
    bg="#4CAF50",
    fg="white",
    width=16,
    font=("Arial",11,"bold"),
    command=calculate_bmi
).grid(row=0,column=0,padx=8,pady=8)

tk.Button(
    button_frame,
    text="View History",
    bg="#2196F3",
    fg="white",
    width=16,
    font=("Arial",11,"bold"),
    command=view_history
).grid(row=0,column=1,padx=8,pady=8)

tk.Button(
    button_frame,
    text="Show Graph",
    bg="#9C27B0",
    fg="white",
    width=16,
    font=("Arial",11,"bold"),
    command=show_user_graph
).grid(row=1,column=0,padx=8,pady=8)

tk.Button(
    button_frame,
    text="Export CSV",
    bg="#FF9800",
    fg="white",
    width=16,
    font=("Arial",11,"bold"),
    command=export_report
).grid(row=1,column=1,padx=8,pady=8)

tk.Button(
    button_frame,
    text="Clear",
    bg="#607D8B",
    fg="white",
    width=16,
    font=("Arial",11,"bold"),
    command=clear_fields
).grid(row=2,column=0,padx=8,pady=8)

tk.Button(
    button_frame,
    text="Exit",
    bg="#F44336",
    fg="white",
    width=16,
    font=("Arial",11,"bold"),
    command=exit_program
).grid(row=2,column=1,padx=8,pady=8)

tk.Button(
    button_frame,
    text="Edit Record",
    bg="#3F51B5",
    fg="white",
    width=16,
    font=("Arial",11,"bold"),
    command=edit_record
).grid(row=3,column=0,padx=8,pady=8)

tk.Button(
    button_frame,
    text="Delete Record",
    bg="#D32F2F",
    fg="white",
    width=16,
    font=("Arial",11,"bold"),
    command=remove_record
).grid(row=3,column=1,padx=8,pady=8)


# -----------------------------
# Footer
# -----------------------------
footer = tk.Label(
    window,
    text="Developed by Archana T S",
    font=("Arial",10,"italic"),
    fg="gray",
    bg="#F2F6FC"
)

footer.pack(pady=10)


# -----------------------------
# Run Application
# -----------------------------
window.mainloop()