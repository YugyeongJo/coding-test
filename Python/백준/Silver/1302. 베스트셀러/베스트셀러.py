import sys
input = sys.stdin.readline

from collections import defaultdict

N = int(input())
book_info = defaultdict(int)

for _ in range(N):
    book_name = input().rstrip()
    
    book_info[book_name] += 1

max_book_sales = max(book_info.values())

max_book_count = min([book for book, count in book_info.items() if count == max_book_sales])
print(max_book_count)