"""
Database package
Issue #17: Backend collegamento DB
"""

from .connection import (
    connect_to_mongodb,
    close_mongodb_connection,
    get_database,
    verify_connection,
    get_database_sync
)

__all__ = [
    "connect_to_mongodb",
    "close_mongodb_connection",
    "get_database",
    "verify_connection",
    "get_database_sync"
]
