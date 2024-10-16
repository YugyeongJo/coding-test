from collections import Counter

N = int(input())
book_info = [input().rstrip() for _ in range(N)]
book_info = Counter(book_info)

max_book_sales = max(book_info.values())

max_book_count = min([book for book, count in book_info.items() if count == max_book_sales])
print(max_book_count)