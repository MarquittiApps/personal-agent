import sys
import os
from datetime import datetime

# Set PYTHONPATH to root
sys.path.append(os.getcwd())

from app.crud import finance as crud
from app.models.finance import InstallmentGroupCreate, TransactionCreate, TransactionType

def test_installments():
    user_id = 1
    # Assume account 1 and category 1 exist from S1
    
    print("Testing Installment Group Creation...")
    ig_data = InstallmentGroupCreate(total_amount=3000.0, total_installments=3, description="Notebook")
    ig = crud.create_installment_group(ig_data)
    print(f"Created Group: {ig}")
    
    print("\nTesting Bulk Installment Transactions...")
    start_date = datetime(2024, 1, 15)
    transactions = crud.create_installment_transactions(
        user_id=user_id,
        group_id=ig['id'],
        start_date=start_date,
        account_id=1,
        category_id=1,
        amount_per_installment=1000.0,
        total_installments=3,
        description="Notebook"
    )
    for t in transactions:
        print(f"Created Installment: {t['description']} - Date: {t['date']}")

if __name__ == "__main__":
    try:
        test_installments()
        print("\nVerification SUCCESSFUL!")
    except Exception as e:
        print(f"\nVerification FAILED: {e}")
        sys.exit(1)
