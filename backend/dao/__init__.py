"""
DAO Package
Issue #16: Creazione DAO per gestione dati
"""

from .base_dao import BaseDAO
from .post_dao import PostDAO

__all__ = [
    "BaseDAO",
    "PostDAO"
]
