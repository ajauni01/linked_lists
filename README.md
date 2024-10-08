Let's revisit our browser  history program where we had to maintain two stacks to manage our forward and backward browser history.  In this script you will use a DLL (doubly linked list) to support an efficient navigation in both directions.  This will also provide efficient, quick inserts and deletion from both ends and flexible data management.

Once again, in a web browser, users can navigate backward and forward through their browsing history - fits nicely with the principles of doubly linked list.

Each visited web pages is stored in your browser history.  The current page is always linked to the previous page and the next page (when available).  Use a DLL to manage the move both forward and backward through the users history.  Using the principles from our lecture code create:

a class called PageNode with attributes url, next, prev
a class called BrowserHistory with a constructor that initializes our current node to None (pointer to current page)
create methods called visit (adds a new page to the history), back (go back to previous page), forward (go forward to next page), show_history (prints the entire browsing history (visualization), and a main function that tests this code.
main should create a BrowserHistory object, add some web pages, test go back, test go forward and test show history 
