# https://leetcode.com/problems/design-browser-history/

class Browser:
    def __init__(self, url="", prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Browser(homepage)
        self.curr = self.home


    def visit(self, url: str) -> None:
        newTab = Browser(url)
        self.curr.next = newTab
        newTab.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)