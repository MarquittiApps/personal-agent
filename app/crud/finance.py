from typing import List, Optional
from datetime import datetime
import json
from dateutil.relativedelta import relativedelta
from app.core.database import get_db_connection
from app.models.finance import (
    Account, AccountCreate, Category, CategoryCreate, 
    Transaction, TransactionCreate, InstallmentGroup, InstallmentGroupCreate
)

def create_account(user_id: int, account: AccountCreate) -> dict:
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO finance_accounts (user_id, name, account_type, balance) VALUES (%s, %s, %s, %s) RETURNING id, created_at, updated_at",
            (user_id, account.name, account.account_type.value, account.balance)
        )
        row = cur.fetchone()
        conn.commit()
        return {
            "id": row[0],
            "user_id": user_id,
            "name": account.name,
            "account_type": account.account_type,
            "balance": float(account.balance),
            "created_at": row[1],
            "updated_at": row[2]
        }
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def get_accounts(user_id: int) -> List[dict]:
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, user_id, name, account_type, balance, created_at, updated_at FROM finance_accounts WHERE user_id = %s",
            (user_id,)
        )
        rows = cur.fetchall()
        return [
            {
                "id": r[0],
                "user_id": r[1],
                "name": r[2],
                "account_type": r[3],
                "balance": float(r[4]),
                "created_at": r[5],
                "updated_at": r[6]
            } for r in rows
        ]
    finally:
        cur.close()
        conn.close()

def create_category(user_id: int, category: CategoryCreate) -> dict:
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO finance_categories (user_id, name, parent_id) VALUES (%s, %s, %s) RETURNING id, created_at",
            (user_id, category.name, category.parent_id)
        )
        row = cur.fetchone()
        conn.commit()
        return {
            "id": row[0],
            "user_id": user_id,
            "name": category.name,
            "parent_id": category.parent_id,
            "created_at": row[1]
        }
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def get_categories(user_id: int) -> List[dict]:
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, user_id, name, parent_id, created_at FROM finance_categories WHERE user_id = %s",
            (user_id,)
        )
        rows = cur.fetchall()
        return [
            {
                "id": r[0],
                "user_id": r[1],
                "name": r[2],
                "parent_id": r[3],
                "created_at": r[4]
            } for r in rows
        ]
    finally:
        cur.close()
        conn.close()

def create_transaction(user_id: int, transaction: TransactionCreate) -> dict:
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            """INSERT INTO finance_transactions (
                account_id, category_id, date, amount, description, 
                transaction_type, is_recurring, installment_group_id, 
                installment_number, source_metadata
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
            RETURNING id, created_at""",
            (
                transaction.account_id, transaction.category_id, transaction.date,
                transaction.amount, transaction.description, transaction.transaction_type.value,
                transaction.is_recurring, transaction.installment_group_id,
                transaction.installment_number, json.dumps(transaction.metadata) if transaction.metadata else None
            )
        )
        row = cur.fetchone()
        conn.commit()
        return {
            "id": row[0],
            "account_id": transaction.account_id,
            "category_id": transaction.category_id,
            "date": transaction.date,
            "amount": float(transaction.amount),
            "description": transaction.description,
            "transaction_type": transaction.transaction_type,
            "is_recurring": transaction.is_recurring,
            "installment_group_id": transaction.installment_group_id,
            "installment_number": transaction.installment_number,
            "created_at": row[1]
        }
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def create_installment_group(transaction: InstallmentGroupCreate) -> dict:
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO finance_installment_groups (total_amount, total_installments, description) VALUES (%s, %s, %s) RETURNING id, created_at",
            (transaction.total_amount, transaction.total_installments, transaction.description)
        )
        row = cur.fetchone()
        conn.commit()
        return {
            "id": row[0],
            "total_amount": float(transaction.total_amount),
            "total_installments": transaction.total_installments,
            "description": transaction.description,
            "created_at": row[1]
        }
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def create_installment_transactions(user_id: int, group_id: int, start_date: datetime, account_id: int, category_id: int, amount_per_installment: float, total_installments: int, description: str) -> List[dict]:
    conn = get_db_connection()
    cur = conn.cursor()
    transactions = []
    try:
        for i in range(1, total_installments + 1):
            current_date = start_date + relativedelta(months=i-1)
            desc = f"{description} ({i}/{total_installments})"
            
            cur.execute(
                """INSERT INTO finance_transactions (
                    account_id, category_id, date, amount, description, 
                    transaction_type, is_recurring, installment_group_id, 
                    installment_number
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
                RETURNING id, created_at""",
                (
                    account_id, category_id, current_date, amount_per_installment, 
                    desc, 'expense', False, group_id, i
                )
            )
            row = cur.fetchone()
            transactions.append({
                "id": row[0],
                "date": current_date,
                "amount": amount_per_installment,
                "description": desc,
                "installment_number": i
            })
        conn.commit()
        return transactions
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def get_transactions(user_id: int, account_id: Optional[int] = None) -> List[dict]:
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        query = """
            SELECT t.id, t.account_id, t.category_id, t.date, t.amount, t.description, 
                   t.transaction_type, t.is_recurring, t.installment_group_id, 
                   t.installment_number, t.created_at 
            FROM finance_transactions t
            JOIN finance_accounts a ON t.account_id = a.id
            WHERE a.user_id = %s
        """
        params = [user_id]
        if account_id:
            query += " AND t.account_id = %s"
            params.append(account_id)
        
        cur.execute(query, tuple(params))
        rows = cur.fetchall()
        return [
            {
                "id": r[0],
                "account_id": r[1],
                "category_id": r[2],
                "date": r[3],
                "amount": float(r[4]),
                "description": r[5],
                "transaction_type": r[6],
                "is_recurring": r[7],
                "installment_group_id": r[8],
                "installment_number": r[9],
                "created_at": r[10]
            } for r in rows
        ]
    finally:
        cur.close()
        conn.close()
