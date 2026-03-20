import pytest
from unittest.mock import patch, MagicMock
from app.crud import finance as crud
from app.models.finance import AccountCreate, AccountType, CategoryCreate, TransactionCreate, TransactionType, InstallmentGroupCreate
from datetime import datetime

class TestFinanceCRUD:

    @patch("app.crud.finance.get_db_connection")
    def test_create_account(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        mock_cur.fetchone.return_value = (1, datetime.now(), datetime.now())

        account = AccountCreate(name="Bank X", account_type=AccountType.CHECKING, balance=1000.0)
        result = crud.create_account(user_id=1, account=account)

        assert result["id"] == 1
        assert result["name"] == "Bank X"
        mock_conn.commit.assert_called_once()

    @patch("app.crud.finance.get_db_connection")
    def test_get_accounts(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        mock_cur.fetchall.return_value = [
            (1, 1, "Bank X", "checking", 1000.0, datetime.now(), datetime.now())
        ]

        results = crud.get_accounts(user_id=1)
        assert len(results) == 1
        assert results[0]["name"] == "Bank X"

    @patch("app.crud.finance.get_db_connection")
    def test_create_category(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        mock_cur.fetchone.return_value = (1, datetime.now())

        category = CategoryCreate(name="Food", parent_id=None)
        result = crud.create_category(user_id=1, category=category)

        assert result["id"] == 1
        assert result["name"] == "Food"

    @patch("app.crud.finance.get_db_connection")
    def test_get_categories(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        mock_cur.fetchall.return_value = [
            (1, 1, "Food", None, datetime.now())
        ]

        results = crud.get_categories(user_id=1)
        assert len(results) == 1
        assert results[0]["name"] == "Food"

    @patch("app.crud.finance.get_db_connection")
    def test_create_transaction(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        mock_cur.fetchone.return_value = (1, datetime.now())

        transaction = TransactionCreate(
            account_id=1, category_id=1, date=datetime.now(), 
            amount=50.0, description="Pizza", transaction_type=TransactionType.EXPENSE
        )
        result = crud.create_transaction(user_id=1, transaction=transaction)

        assert result["id"] == 1
        assert result["amount"] == 50.0

    @patch("app.crud.finance.get_db_connection")
    def test_get_transactions(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        mock_cur.fetchall.return_value = [
            (1, 1, 1, datetime.now(), 50.0, "Pizza", "expense", False, None, None, datetime.now())
        ]

        results = crud.get_transactions(user_id=1)
        assert len(results) == 1
        assert results[0]["description"] == "Pizza"
