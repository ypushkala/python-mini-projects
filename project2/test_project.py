import pytest
from project import (
    add_transaction,
    delete_transaction,
    summarize_by_month,
    view_transactions_by_date
)
from unittest.mock import mock_open, patch
from io import StringIO


mock_data = (
    "ID,Date,Description,Category,Amount\n"
    "1234,2025-04-01,Groceries,Food,-50.00\n"
    "5678,2025-04-15,Salary,Income,500.00\n"
    "9012,2025-05-01,Electricity,Bills,-100.00\n"
)


def test_add_transaction():
    m = mock_open()
    with patch("builtins.open", m):
        add_transaction("2025-04-20", "Test", "Misc", 123.45)
        m.assert_called_once_with("transactions.csv", "a", newline="")
        handle = m()
        handle.write.assert_called()  


def test_delete_transaction():
    m = mock_open(read_data=mock_data)
    output_buffer = StringIO()

    def mock_file(*args, **kwargs):
        if args[1] == "r" or args[0].endswith(".csv") and "r" in args[1]:
            return StringIO(mock_data)
        elif args[1] == "w":
            return output_buffer
        return mock_open()()

    with patch("builtins.open", mock_file):
        delete_transaction("5678")
        output_buffer.seek(0)
        output = output_buffer.read()
        assert "5678" not in output
        assert "1234" in output
        assert "9012" in output


def test_summarize_by_month(capsys):
    with patch("builtins.open", mock_open(read_data=mock_data)):
        summarize_by_month()
        captured = capsys.readouterr()
        assert "2025-04" in captured.out
        assert "2025-05" in captured.out
        assert "$450.00" in captured.out  


def test_view_transactions_by_date(capsys):
    with patch("builtins.open", mock_open(read_data=mock_data)):
        view_transactions_by_date("2025-04-01", "2025-04-30")
        captured = capsys.readouterr()
        assert "Groceries" in captured.out
        assert "Salary" in captured.out
        assert "Electricity" not in captured.out  
