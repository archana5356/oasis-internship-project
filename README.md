# 🩺 BMI Calculator

A professional Python-based **Body Mass Index (BMI) Calculator** with a graphical user interface (GUI). This application calculates BMI, classifies the result into health categories, stores records in an SQLite database, displays BMI history, and shows BMI trends using graphs.

---

## 📌 Project Description

The BMI Calculator helps users monitor their health by calculating Body Mass Index (BMI) from their weight and height. It stores user records in a database and provides graphical visualization of BMI changes over time.

---

## ✨ Features

- ✅ User-friendly GUI using Tkinter
- ✅ BMI Calculation
- ✅ BMI Categories
  - Underweight
  - Normal Weight
  - Overweight
  - Obese
- ✅ Health Advice
- ✅ Healthy Weight Range
- ✅ SQLite Database Storage
- ✅ Multi-user Support
- ✅ View BMI History
- ✅ BMI Trend Graph
- ✅ Export Records to CSV
- ✅ Input Validation
- ✅ Error Handling
- ✅ Edit Records
- ✅ Delete Records
- ✅ Clear Fields
- ✅ Exit Confirmation

---

## 🛠 Technologies Used

- Python 3
- Tkinter
- SQLite3
- Matplotlib
- CSV

---

## 📂 Project Structure

```
BMI_Calculator/
│── bmi_calculator.py
│── database.py
│── graph.py
│── bmi.db
│── BMI_Report.csv
│── README.md
```

---

## 🧮 BMI Formula

```
BMI = Weight (kg) / Height² (m²)
```

---

## 📊 BMI Categories

| BMI Range | Category |
|-----------|----------|
| Less than 18.5 | Underweight |
| 18.5 – 24.9 | Normal Weight |
| 25.0 – 29.9 | Overweight |
| 30.0 and Above | Obese |

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/archana5356/BMI_Calculator.git
```

### Open the Project Folder

```bash
cd BMI_Calculator
```

### Install Required Library

```bash
pip install matplotlib
```

### Run the Application

```bash
python bmi_calculator.py
```

---

## 💻 How to Use

1. Enter your name.
2. Enter your weight (kg).
3. Enter your height (m).
4. Click **Calculate BMI**.
5. View your BMI and health category.
6. Save the BMI record.
7. Click **View History** to see previous records.
8. Click **Show Graph** to display your BMI trend.
9. Click **Export CSV** to save records.
10. Use **Edit Record** to update an existing record.
11. Use **Delete Record** to remove a record.
12. Click **Clear** to reset all fields.
13. Click **Exit** to close the application.

---

## 📸 Sample Output

### Input

```
Name   : Archana
Weight : 55 kg
Height : 1.60 m
```

### Output

```
BMI : 21.48

Category : Normal Weight

Healthy Weight Range :
47.4 kg - 63.7 kg

Health Advice :
✔ Maintain a balanced diet.
✔ Exercise regularly.
✔ Drink enough water.
```

---

## 📈 Future Improvements

- 🌙 Dark Mode
- 📄 PDF Report Generation
- 🖨 Print BMI Report
- 🔍 Search Records
- ☁ Cloud Database Support
- 🔐 User Login System
- 📱 Responsive Interface

---

## 👩‍💻 Author

**Archana T S**

GitHub: **https://github.com/archana5356**

---

## 📜 License

This project is developed for educational purposes as part of the **Oasis Infobyte Python Programming Internship**.

---

## 🙏 Acknowledgements

- Oasis Infobyte
- Python Documentation
- Tkinter Documentation
- Matplotlib Documentation
- SQLite Documentation

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.