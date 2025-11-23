class APIError(Exception):
    """Raised when an api error occurs."""
    def __init__(self, message:str, status_code=500):
        self.status_code = status_code
        super().__init__(message)

class DatabaseError(APIError):
    """Raised when a db error occurs."""
    def __init__(self, message:str, status_code=500):
        super().__init__(message, status_code)

class DBQueryError(DatabaseError):
    """Raised when a db query error occurs."""
    def __init__(self, message:str, status_code=400):
        super().__init__(message, status_code)

class NotFoundError(DBQueryError):
    """Raised when an item cannot be found."""
    def __init__(self, not_found_item:str='Item'):
        message = f"{not_found_item} could not be found."
        super().__init__(message, 404)

class BadRequestError(DBQueryError):
    """Raised when the request body is invalid (400)."""
    def __init__(self, message: str = "Bad Request"):
        super().__init__(message, status_code=400)