# 📦 Parcel and Locker Management System

### Smart Parcel Allocation Using Python

A Python-based application that assigns parcels to suitable lockers based on **zone compatibility, available capacity, parcel priority, and arrival deadlines**. The system also generates zone-wise reports to summarize parcel assignments, locker availability, and capacity utilization.

---

## ✨ Key Features

* **📦 Priority-Based Allocation** — Processes parcels in descending order of priority.
* **🏷️ Zone-Based Matching** — Assigns parcels only to lockers in the same zone.
* **📏 Capacity Validation** — Ensures a parcel fits within the remaining locker capacity.
* **🔢 Parcel Limit Management** — Prevents lockers from exceeding their maximum parcel count.
* **📅 Cutoff-Day Filtering** — Considers only parcels that arrive on or before the specified cutoff day.
* **🔄 Locker Selection** — Processes lockers in ascending order of locker ID.
* **📊 Zone-Wise Reporting** — Displays total parcels, assigned parcels, locker counts, and capacity utilization.
* **🧬 Deep Copy Handling** — Uses Python's `copy.deepcopy()` to preserve the original input data for reporting.

---

## 🛠️ Tech Stack

| Technology                        | Purpose                                               |
| --------------------------------- | ----------------------------------------------------- |
| Python 3                          | Core programming language                             |
| Object-Oriented Programming (OOP) | Organizes parcels, lockers, and allocation logic      |
| `copy` module                     | Creates independent copies of input objects           |
| Lists and Dictionaries            | Stores and manages parcel, locker, and reporting data |
| Lambda Functions                  | Defines custom sorting criteria                       |
| Sorting                           | Orders parcels by priority and lockers by ID          |

---

## 🏗️ Project Structure

```text
Parcel-Locker-Management/
│
├── main.py          # Main application and allocation logic
└── README.md        # Project documentation
```

*Note: Replace `main.py` with your actual Python filename if it differs.*

---

## ⚙️ How It Works

### 1. Input Collection

The application accepts parcel and locker details from standard input.

**Parcel attributes:**

* Parcel ID
* Zone
* Arrival day
* Required capacity
* Priority

**Locker attributes:**

* Locker ID
* Zone
* Available capacity
* Maximum number of parcels

### 2. Parcel Sorting

Parcels are sorted by priority in descending order, ensuring higher-priority parcels are considered first.

### 3. Locker Sorting

Lockers are sorted by locker ID in ascending order to establish a consistent selection order.

### 4. Allocation Process

A parcel is assigned to the first locker that satisfies all the following conditions:

* The parcel's arrival day is on or before the cutoff day.
* The parcel and locker belong to the same zone.
* The parcel's required capacity does not exceed the locker's remaining capacity.
* The locker has space for at least one more parcel.

After a successful assignment, the locker’s remaining capacity and parcel limit are updated.

### 5. Report Generation

The application generates a zone-wise summary containing:

* Total number of parcels.
* Number of parcels assigned.
* Number of lockers available in the zone.
* Percentage of locker capacity utilized.

If a zone has no lockers, the report displays `No_Lockers`.

---

## ▶️ Getting Started

### Prerequisites

* Python 3.x
* Any Python-compatible IDE or code editor, such as VS Code or PyCharm.

### Installation

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Navigate to the project directory**

```bash
cd Parcel-Locker-Management
```

**3. Run the application**

```bash
python main.py
```

**4. Enter the input**

Provide the parcel count, parcel details, locker count, locker details, and cutoff day in the expected input format.

---

## 🧪 Input Format

### Number of Parcels

```text
3
```

### Parcel Details

Each parcel follows this format:

```text
<Parcel_ID> <Zone> <Arrival_Day> <Required_Capacity> <Priority>
```

Example:

```text
P101 A 2 20 3
P102 B 1 30 5
P103 A 3 15 2
```

### Number of Lockers

```text
2
```

### Locker Details

Each locker follows this format:

```text
<Locker_ID> <Zone> <Capacity> <Max_Parcels>
```

Example:

```text
L101 A 100 3
L102 B 80 2
```

### Cutoff Day

```text
3
```

---

## 📤 Sample Output

The following output illustrates the expected format for the example input above.

```text
P102 L102 50
P101 L101 80
P103 L101 65
A 2 2 1 35
B 1 1 1 37
```

**Output explanation:**

* `P102` is assigned to locker `L102`.
* `P101` and `P103` are assigned to locker `L101`.
* The remaining capacity is displayed after each successful assignment.
* The final report summarizes parcel assignments and locker capacity utilization by zone.

*Note: This sample illustrates the allocation output format. The exact report values depend on the implementation and the state of the locker objects used during reporting.*

---

## 🧠 Core Concepts Demonstrated

This project demonstrates practical Python programming concepts:

* Classes and objects.
* Constructors and instance attributes.
* Encapsulation of application logic within classes.
* List sorting using `sorted()` and lambda expressions.
* Conditional statements and nested loops.
* Dictionary-based aggregation and reporting.
* Deep copying of objects.
* Resource allocation and constraint validation.
* Percentage-based capacity utilization calculations.

---

## 🚀 Future Improvements

Potential enhancements include:

* Add a separate list of unassigned parcels and reasons for allocation failure.
* Implement more efficient locker-selection strategies.
* Add input validation and exception handling.
* Introduce file-based or database storage.
* Generate reports in CSV or Excel format.
* Build a graphical interface or REST API.
* Add unit tests for allocation and reporting logic.

---

## 🎯 Project Objective

The primary objective is to develop a structured parcel allocation system that demonstrates how Python can be used to manage limited resources, enforce allocation constraints, and generate meaningful operational reports.

---

## 👨‍💻 Author

**Manohar Reddy**

Python | Object-Oriented Programming | Problem Solving

---

⭐ If you find this project useful, consider giving the repository a star!
