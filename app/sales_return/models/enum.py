from enum import Enum

class SalesReturnStatus(str, Enum):
  DRAFT = "DRAFT"
  CONFIRMED = "CONFIRMED"
  CANCELLED = "CANCELLED"
  RECEIVED = "RECEIVED"
  REFUND = "REFUND"