from enum import Enum

class GedcomError:

    def __init__(self, errorType, storyId, errorObject, errorMessage):
        self.errorType = errorType
        self.storyId = storyId
        self.errorObject = errorObject
        self.errorMessage = errorMessage

    def __str__(self):
        typeString = type(self.errorObject).__name__.upper()
        return f'{self.errorType.name.upper()}, {typeString}, {self.storyId}, {self.errorObject}: {self.errorMessage}'

class ErrorType(Enum):
    error = 1
    anomaly = 2