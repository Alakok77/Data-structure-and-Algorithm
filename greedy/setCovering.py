import json

def find_stations():
    """เลือกสถานีให้ครอบคลุมทุกเมืองอย่างมีประสิทธิภาพ"""
    target_cities = set(json.loads(input().strip()))  # ใช้ set เพื่อลดความซับซ้อน
    count = int(input().strip())
    stations = [json.loads(input().strip()) for _ in range(count)]

    result = []

    while target_cities:
        # เลือกสถานีที่ครอบคลุม "เมืองที่เหลือ" ได้มากที่สุด
        best_station = max(
            stations,
            key=lambda x: len(set(x["Cities"]) & target_cities),  # จำนวนเมืองที่ครอบคลุม
            default=None
        )

        if not best_station:
            break  # ถ้าไม่มีสถานีที่เหลือให้เลือก ให้หยุด

        result.append(best_station["Name"])
        target_cities -= set(best_station["Cities"])  # ลบเมืองที่ถูกครอบคลุมออก
        stations.remove(best_station)  # เอาสถานีที่เลือกออกจากลิสต์

    print(sorted(result))

find_stations()
