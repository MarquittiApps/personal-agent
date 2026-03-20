from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class AccountType(str, Enum):
    CHECKING = "checking"
    SAVINGS = "savings"
    CREDIT_CARD = "credit_card"

class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class AccountBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    account_type: AccountType
    balance: float = 0.0

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    parent_id: Optional[int] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class InstallmentGroupBase(BaseModel):
    total_amount: float
    total_installments: int
    description: Optional[str] = None

class InstallmentGroupCreate(InstallmentGroupBase):
    pass

class InstallmentGroup(InstallmentGroupBase):
    id: int
    created_at: datetime

class TransactionBase(BaseModel):
    account_id: int
    category_id: int
    date: datetime
    amount: float
    description: str
    transaction_type: TransactionType
    is_recurring: bool = False
    installment_group_id: Optional[int] = None
    installment_number: Optional[int] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
