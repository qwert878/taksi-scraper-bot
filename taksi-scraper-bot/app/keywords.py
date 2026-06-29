KEYWORDS = [
    "taksi", "taxi", "mashina kerak", "avto kerak",
    "zayafka", "zakaz", "buyurtma",
    "olib ket", "olib boring", "borish kerak",
    "ketish kerak", "yetkazib ber",
    "такси", "машина нужна", "нужна машина",
    "заказ", "заявка", "отвезите",
    "аэропорт", "вокзал",
    "need car", "need taxi",
]

def is_taxi_request(text: str) -> bool:
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in KEYWORDS)
