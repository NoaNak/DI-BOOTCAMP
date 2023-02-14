from math import ceil

class Pagination:

    def __init__(self, items: list = [], page_size: int = 10):
        self.items = items
        self.page_size = page_size
        self.visible = items[:page_size]
        self.current_page = 0

    def get_visible(self) -> list:
        return self.visible

    def get_to_page(self, page_num: int) -> list:
        self.current_page = page_num
        pages = ceil(len(self.items) / self.page_size) # 26 // 4 => 6 . ceil(26 / 4 ) => 7
        pages_items = {} 
        i = 0
        for page in range(pages):
            pages_items[page] = self.items[i: i + self.page_size] # {0: [a, b, c, d]}
            i += self.page_size

        return pages_items[page_num]
            
    def firstPage(self) -> list:
        return self.get_to_page(0)
    
    def lastPage(self) -> list:
        pages = ceil(len(self.items) / self.page_size) # 6
        return self.get_to_page(pages - 1)

    def nextPage(self) -> list:
        return self.get_to_page(self.current_page + 1)
    
    def previousPage(self) -> list:
        return self.get_to_page(self.current_page - 1)

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.firstPage())
print(p.nextPage())
print(p.nextPage())
print(p.previousPage())
print(p.lastPage())