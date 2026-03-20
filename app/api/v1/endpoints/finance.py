from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.finance import (
    Account, AccountCreate, Transaction, TransactionCreate,
    Category, CategoryCreate
)
from app.crud import finance as crud

router = APIRouter(tags=["Finance"])

DEFAULT_USER_ID = 1

@router.get("/accounts", response_model=List[Account])
async def get_accounts():
    """Listar todas as contas vinculadas ao usuário."""
    return crud.get_accounts(user_id=DEFAULT_USER_ID)

@router.post("/accounts", response_model=Account)
async def create_account(account: AccountCreate):
    """Criar uma nova conta ou cartão."""
    try:
        return crud.create_account(user_id=DEFAULT_USER_ID, account=account)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/categories", response_model=List[Category])
def list_categories():
    """Listar categorias (estrutura de árvore)."""
    return crud.get_categories(DEFAULT_USER_ID)

@router.get("/transactions", response_model=List[Transaction])
def list_transactions(account_id: Optional[int] = None):
    return crud.get_transactions(DEFAULT_USER_ID, account_id)

@router.get("/dashboard")
def get_finance_dashboard():
    accounts = crud.get_accounts(DEFAULT_USER_ID)
    transactions = crud.get_transactions(DEFAULT_USER_ID)
    
    # Simple aggregation for dashboard
    total_balance = sum(acc.balance for acc in accounts) # Assuming 'balance' is an attribute of Account model
    recent = transactions[:10]
    
    return {
        "total_balance": total_balance,
        "accounts": accounts,
        "recent_transactions": recent
    }

@router.post("/categories", response_model=Category)
async def create_category(category: CategoryCreate):
    """Criar uma nova categoria."""
    try:
        return crud.create_category(user_id=DEFAULT_USER_ID, category=category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
