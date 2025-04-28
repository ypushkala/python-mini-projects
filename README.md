# Budget Tracker

#### Video Demo: [Link to Video](https://youtu.be/YOUR_VIDEO_LINK_HERE)

#### Description:

The **Budget Tracker** is a simple Python program designed to help users manage their personal finances by tracking both income and expenses. This project is implemented with core Python libraries and features persistent data storage via a CSV file. Users can interact with the program through a text-based menu that allows them to add, view, and delete transactions, as well as summarize financial data by category and date range.

This project was created for the **CS50’s Introduction to Programming with Python** course to demonstrate my understanding of Python fundamentals, including working with files, user input, handling exceptions, and structuring a program with multiple functions. 

The primary goals of this project were:
- To provide an intuitive way for users to manage their finances by tracking various types of transactions.
- To develop Python skills such as handling CSV files, working with `datetime`, and using Python's built-in modules.
- To build a testable and maintainable Python application using unit testing with `pytest`.

---

### ✅ Features

- **Add Transactions:** Users can add transactions with a unique description, category, amount, and date. This allows for easy recording of income, expenses, or any other financial activity.
- **Unique Transaction IDs:** Every transaction gets a unique ID (UUID) that ensures each transaction is individually identifiable and can be referenced or deleted easily.
- **View Transactions:** Users can view all recorded transactions along with their details (date, description, category, and amount). A running balance is also displayed, helping the user to monitor their financial status at any point in time.
- **Filter Transactions by Date:** The program allows users to filter and display transactions that fall within a specific date range. This is useful for monthly or quarterly reports.
- **Monthly Summary:** The application can calculate and display a summary of all transactions within a given month. It helps users get an overview of their financial activities each month.
- **Delete Transactions:** If a user needs to remove a transaction (for example, a mistake was made), they can delete it by entering the unique transaction ID.
- **Data Persistence:** All transactions are stored in a CSV file (`transactions.csv`), which allows data to persist across program executions.

---

### 📁 Project Structure

The project consists of the following files:


- **`project.py`**: This file contains the main program logic, including all the functions for adding, viewing, deleting, and summarizing transactions.
- **`test_project.py`**: Contains unit tests for ensuring the core functions of the program work correctly.
- **`transactions.csv`**: Stores the transaction data in a comma-separated values format, making it easy to read and write.
- **`requirements.txt`**: Lists all external dependencies for the project (currently only `pytest`).

---

### 🧪 Testing

The project includes unit tests for the core functionalities of the program. These tests are written using **`pytest`** and mock file I/O to ensure no actual file modification is done during testing. The tests include:

- **Adding a transaction:** Ensures the correct format is written to the CSV file.
- **Deleting a transaction:** Verifies that a transaction can be removed by its unique ID.
- **Summarizing by month:** Checks that the program calculates totals for each month correctly.
- **Viewing transactions by date:** Ensures that transactions are filtered correctly by date.

Run the tests by executing the following command in the project directory:

```bash
pytest test_project.py
