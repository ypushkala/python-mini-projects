
---

# **Mini-Projects Repository**

Welcome to the Mini-Projects repository! 🚀  
This repository contains practical Python projects designed to showcase skills in programming, problem-solving, and the use of various libraries. Each project demonstrates unique functionalities and aims to deliver hands-on experience with coding.

---

## **Current Projects**

### **1. Budget Tracker**

#### Video Demo: [Link to Video](https://youtu.be/YOUR_VIDEO_LINK_HERE)  

#### **Description**  
The **Budget Tracker** is a Python program that helps users manage their personal finances by tracking income and expenses. It uses core Python libraries and persists data through a CSV file. Users can interact via a text-based menu to add, view, delete transactions, and summarize financial data by category or date range.

#### **Features**  
- **Add Transactions**: Record income, expenses, or other activities with descriptions, categories, amounts, and dates.  
- **Unique Transaction IDs**: Each transaction has a unique ID for easy referencing and deletion.  
- **View Transactions**: Display all transactions with details and a running balance.  
- **Filter by Date**: Filter transactions within specific date ranges for targeted insights.  
- **Monthly Summary**: Generate summaries of transactions for any given month.  
- **Delete Transactions**: Remove transactions using their unique IDs.  
- **Data Persistence**: Transactions are stored in a CSV file, ensuring data is available between program runs.  

#### **Project Structure**  
- **`project.py`**: Main program logic.  
- **`test_project.py`**: Unit tests for functionality.  
- **`transactions.csv`**: Stores transaction data.  
- **`requirements.txt`**: Dependencies (e.g., `pytest`).  

#### **Testing**  
This project includes unit tests using `pytest`. Mock file I/O ensures tests do not modify real data.  
- Tests include adding, deleting, and summarizing transactions, and filtering by date.  
Run tests with:
```bash
pytest test_project.py
```

---

### **2. PDF to Audio Converter**

#### **Description**  
This project extracts text from a PDF file and converts it into spoken audio using Python. It leverages **PyMuPDF** for text extraction and **Google Text-to-Speech (gTTS)** for audio conversion. 

#### **Features**  
- Extracts text from each PDF page.  
- Combines text into a single cohesive string.  
- Converts text to an MP3 file.  

#### **Usage**  
1. Provide the path to the PDF file.  
2. Run the script to generate an MP3 file in the project directory.

---

## **How to Contribute**

Contributions are welcome!  
1. Fork the repository.  
2. Create a new branch for your changes.  
3. Submit a pull request describing your additions or improvements.  

---

## **Getting Started**

Clone the repository and start working on the projects:  
```bash
git clone https://github.com/ypushkala/python-mini-projects.git
cd python-mini-projects
```
