class MicrosoftTeamsRequestException(Exception):
    def __init__(self, msg, code=None):
        self.code = code


class MissingConnectorConfigKeyException(Exception):
    pass


class MissingTemplatePathException(Exception):
    pass
