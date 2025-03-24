class BrowserHistory:
    def __init__(self):
        self.back_stack=[]
        self.forward_stack=[]
    def visit_Page(self,url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print(f"Visited: {url}")
    def go_back(self):
        if len(self.back_stack) <=1:
            print("No page to go back to")
            return
        last_page=self.back_stack.pop()
        self.forward_stack.append(last_page)
        print(f"Went back to: {self.back_stack [-1]}")
    def go_forward(self):
        if not self.forward_stack:
            print("No page to go forward.")
            return
        next_page=self.forward_stack.pop()
        self.back_stack.append(next_page)
        print(f"Went Forward to {next_page}")
    def show_History(self):
        print("BackWard Page: ",self.back_stack)
        print("Forward Page: ",self.forward_stack)
browser = BrowserHistory()
browser.visit_Page("google.com")
browser.visit_Page("youtube.com")
browser.visit_Page("github.com")
print()
browser.go_back()
browser.go_back()
print()
browser.go_forward()
print()
browser.show_History() 

