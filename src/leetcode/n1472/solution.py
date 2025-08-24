class BrowserHistory:

    def __init__(self, homepage: str):
        self.pos = 0
        self.his = [homepage]

    def visit(self, url: str):
        self.pos += 1
        del self.his[self.pos :]
        self.his.append(url)

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos - steps)
        return self.his[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(len(self.his) - 1, self.pos + steps)
        return self.his[self.pos]
