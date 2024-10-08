class PageNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self):
        # Initialize the current node to None
        self.current = None

    # Visit method
    def visit(self, url):
        # Create an instance of the PageNode class and pass the url as an argument
        new_node = PageNode(url)
        if self.current is None:
            self.current = new_node
        else:
            last = self.current
            # Continue the while loop until last.next is falsy or none (find the last node)
            while last.next:
                # In this case, last points to none
                last = last.next
            #     Assign new_node to the last node
            last.next = new_node
            new_node.prev = last
        #     Update the current node with a newly visited page
        self.current = new_node
        # Return the url
        return url

    # Backward method
    def backward(self):
        # Assign the current node to a 'temp' variable
        temp = self.current
        # Check if there is a current node
        if temp is None:
            print("Backward List is empty.")
            return

        # Check if the previous node exists
        if temp.prev:
            # Update temp to the previous node
            temp = self.current.prev
            # Update the current node with the previous node
            self.current = temp
            return temp.url
        print("No previous node.")
        return

    # Forward method
    def forward(self):
        # Assign the current node to a 'temp' variable
        temp = self.current
        # Check if there is a current node
        if temp is None:
            print("Forward List is empty.")
            return

            # Check if the next node exists
        if temp.next:
            temp = self.current.next
            # Update to the next node
            self.current = temp
            return temp.url
        print("No next page.")
        return

    # show_history method
    def show_history(self):
        temp = self.current
        # Continue the while loop as long as 'temp' is truthy
        while temp:
            print(temp.url, end=" <=> ")
            temp = temp.prev
        print("Start")

if __name__ == '__main__':
    # Create an instance of the BrowserHistory() class
    browse = BrowserHistory()
    # Test cases
    print("Visiting:", browse.visit("www.example.com"))
    print("Visiting:", browse.visit("www.google.com"))
    print("Visiting:", browse.visit("www.GitHub.com"))

    print("Back to:", browse.backward())
    print("Back to:", browse.backward())

    print("Forward to:", browse.forward())
    print("Forward to:", browse.forward())
    print("Browsing history (current page first): ")
    # Show browsing history
    browse.show_history()


