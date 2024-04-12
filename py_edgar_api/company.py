class Company:
    def __init__(self, cik: str, name: str) -> None:
        self.cik = cik
        self.name = name

    def __repr__(self) -> str:
        return f"{self.cik} - {self.name}"