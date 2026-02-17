# 쇼핑 카트 프로그램 - 딕셔너리 활용

# 쇼핑 카트: {상품명: [수량, 개당 가격]}
cart = {
    "사과": [2, 1000],
    "바나나": [3, 800],
    "오렌지": [1, 1500]
}

print("쇼핑 카트:")
total = 0
for item, (qty, price) in cart.items():
    subtotal = qty * price
    total += subtotal
    print(f"{item}: {qty}개 (개당 {price}원) = {subtotal}원")

print(f"총 가격: {total}원")
