class DomainError(Exception):
    """Excepción base para errores de negocio (independiente de HTTP)."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class NotFoundError(DomainError):
    """Se lanza cuando un recurso solicitado no existe."""


class ValidationError(DomainError):
    """Se lanza cuando una regla de negocio de entrada no se cumple."""
