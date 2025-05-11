class WebsiteTree:
    def __init__(self,data):
        self.data=data
        self.children=[]
    def add_websites(self,website_node):
        self.children.append(website_node)
    def display(self,level=0):
        print(" "*level*4 +f"- {self.data}")
        for child in self.children:
            child.display(level+1)
def search(website_node,target):
    if website_node.data == target:
        return website_node
    for child in website_node.children:
        result=search(child,target)
        if result:
            return result
    return None
def count_websites(website_node):
    count=1
    for child in website_node.children:
        count+=count_websites(child)
    return count

# Create root of the website
root = WebsiteTree("Home")

# Level 1 sections
about = WebsiteTree("About")
services = WebsiteTree("Services")
contact = WebsiteTree("Contact")

# Level 2 subsections
team = WebsiteTree("Team")
web_dev = WebsiteTree("Web Development")
ai = WebsiteTree("AI Solutions")

# Build the tree
about.add_websites(team)
services.add_websites(web_dev)
services.add_websites(ai)

root.add_websites(about)
root.add_websites(services)
root.add_websites(contact)

# Display the website menu
print("Website Navigation Menu:")
root.display()

# Search for a page
target = "AI Solutions"
found = search(root, target)
if found:
    print(f"\n'{target}' found in the website menu!")
else:
    print(f"\n'{target}' not found.")

# Count total sections/pages
print("\nTotal number of pages in the website:", count_websites(root))
