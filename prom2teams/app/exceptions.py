from typing import Optional


class MicrosoftTeamsRequestException(Exception):
    def __init__(self, message: str, code: Optional[int] = None):
        self.code = code
        super().__init__(message)


class MissingConnectorConfigKeyException(Exception):
    pass


class MissingTemplatePathException(Exception):
    pass
