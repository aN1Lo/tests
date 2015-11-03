import os

__all__ = [unit[:unit.find('.')] for unit in os.listdir(__name__) if unit.endswith('.py') and "__init__" not in unit]
print(__all__)
