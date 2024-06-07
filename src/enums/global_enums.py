from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected."
    WRONG_STATUS_KEY = "Received key is not equal to expected."
    WRONG_STATUS_VALUE = "Received key value is not equal to expected."
    WRONG_RESPONSE_TEXT = "Received response text is not equal to expected."
