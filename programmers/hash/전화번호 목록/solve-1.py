def solution(phone_book):
    phone_book = sorted(phone_book)

    # 2칸씩 이동할 때 용이
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


phone_book = ["12", "123", "1235", "567", "88", "9123"]
solution(phone_book)
