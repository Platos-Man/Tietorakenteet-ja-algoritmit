class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        if len(self.collection) % self.items_per_page == 0:
            return len(self.collection) // self.items_per_page
        return len(self.collection) // self.items_per_page + 1

    def page_item_count(self, page_index):
        if page_index * self.items_per_page >= len(self.collection) or page_index < 0:
            return -1
        return len(
            self.collection[
                page_index
                * self.items_per_page : (page_index + 1)
                * self.items_per_page
            ]
        )

    def page_index(self, item_index):
        if item_index >= len(self.collection) or item_index < 0:
            return -1
        i = 0
        while True:
            if item_index < self.items_per_page * (i + 1):
                return i
            i += 1


helper = PaginationHelper(["a", "b", "c", "d", "e", "f"], 4)
print(helper.page_count())  # should == 2
print(helper.item_count())  # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1))  # last page - should == 2
print(helper.page_item_count(2))  # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(0))  # should == -1
print(helper.page_index(5))  # should == 1 (zero based index)
print(helper.page_index(2))  # should == 0
print(helper.page_index(20))  # should == -1
print(helper.page_index(-10))  # should == -1 because negative indexes are invalid
