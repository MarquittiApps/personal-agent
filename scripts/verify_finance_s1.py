import sys
import os
from datetime import datetime

# Set PYTHONPATH to root
sys.path.append(os.getcwd())

from app.crud import finance as crud
from app.models.finance import AccountCreate, AccountType, CategoryCreate

def test_crud():
    user_id = 1
    
    print("Testing Account Creation...")
    acc_data = AccountCreate(name="Carteira Principal", account_type=AccountType.CHECKING, balance=100.0)
    account = crud.create_account(user_id, acc_data)
    print(f"Created Account: {account}")
    
    print("\nTesting Category Creation...")
    cat_data = CategoryCreate(name="Alimentação")
    category = crud.create_category(user_id, cat_data)
    print(f"Created Category: {category}")
    
    print("\nTesting Retrieval...")
    accounts = crud.get_accounts(user_id)
    categories = crud.get_categories(user_id)
    print(f"Accounts: {len(accounts)}")
    print(f"Categories: {len(categories)}")

if __name__ == "__main__":
    try:
        test_crud()
        print("\nVerification SUCCESSFUL!")
    except Exception as e:
        print(f"\nVerification FAILED: {e}")
        sys.exit(1)
