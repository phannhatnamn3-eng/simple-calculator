# calculator.py

def add(a, b):
    """Hàm này thực hiện phép cộng hai số."""
    return a + b

def subtract(a, b):
    """Hàm này thực hiện phép trừ hai số."""
    return a - b

# Điểm khởi chạy chính của chương trình
if __name__ == "__main__":
    print("Chào mừng đến với máy tính đơn giản!")
    add_result = add(5, 3)
    print(f"Kết quả của 5 + 3 là: {add_result}")

    subtract_result = subtract(10, 4)
    print(f"Kết quả của 10 - 4 là: {subtract_result}")
