"""
Write class with settings. And a function which can:
 -print all settings
 -has function get_dict() return with dit
Setting parameters:
 -url: str
 -port: int
"""

class Config:

    accepted_schemes = ['http', 'https', 'sftp']
    public_variables = ['url', 'port', 'user', 'password']  # Added user and password to public variables

    def __init__(self, url: str, port: int, user: str = None, password: str = None):
        # Validate port
        if not isinstance(port, int):
            raise TypeError("Port must be an integer")
        if port < 0:
            raise ValueError("Port must be bigger than 0")
        if port > 65535:
            raise ValueError("Port must be smaller than 65535")
        self.port: int = port

        # Validate URL - FIXED: Check if there's NO colon
        if ':' not in url:
            raise ValueError("Invalid URL, must contain scheme and scheme specific parts (e.g., 'http:localhost')")

        url_parts = url.split(":", 1)  # Split only on first colon
        scheme = url_parts[0].lower()
        if scheme not in self.accepted_schemes:
            raise ValueError(f"Invalid URL scheme. Must be one of: {', '.join(self.accepted_schemes)}")

        self.url: str = url
        self.user = user
        self.password = password

    def __str__(self):
        # FIXED: Removed the incorrect {self, self.url}
        return f"Config(url={self.url}, port={self.port}, user={self.user}, password={'***' if self.password else None})"

    def print(self):
        """Print all settings"""
        print(self.__str__())

    def get_dict(self):
        """Return settings as dictionary"""
        variables = vars(self)
        d = {}
        for k in variables:
            if k in self.public_variables:
                d[k] = variables[k]
        return d

if __name__ == "__main__":
    config = Config("http:localhost", 80, user="admin", password="secret")
    config.print()
    d = config.get_dict()
    print(d)