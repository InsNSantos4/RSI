class Host:
    def __init__(self, id: int, ip: str, name: str, permission_level: int):
        self.id = id
        self.ip = ip
        self.name = name
        self.permission_level = permission_level

        def __str__(self):
            return f"{self.id} {self.ip} {self.name} {self.permission_level}"       