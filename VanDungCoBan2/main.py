from abc import ABC, abstractmethod
# Lớp cha: Khuôn mẫu Tướng (Nhưng không dùng thư viện ABC)
class Hero(ABC):
    @abstractmethod
    def use_ultimate(self):
       pass

# Lớp con 1: Pháp Sư (Code đúng)
class Mage(Hero):
    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")

# Lớp con 2: Sát Thủ (Lỗi thiết kế)
class Assassin(Hero):
    # Lập trình viên quên ghi đè use_ultimate(), tự chế ra hàm mới
    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")

# --- KỊCH BẢN LỖI RUNTIME ---
print("--- LOADING TRẬN ĐẤU ---")
# Việc khởi tạo Sát Thủ diễn ra trót lọt, không hề có cảnh báo nào!
team_heroes = [Mage(), Assassin()] 
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
# Vòng lặp Đa hình (Polymorphism)
for hero in team_heroes:
    hero.use_ultimate()
    
"""
Vòng lặp for hero in team_heroes: hero.use_ultimate() thể hiện tính chất Đa hình (Polymorphism) trong Python như thế nào?
=>
Với đoạn code cũ (không dùng thư viện abc), đối tượng Assassin vẫn được tạo ra thành công và đưa vào mảng trận đấu.
Game chỉ văng lỗi NotImplementedError vào đúng khoảnh khắc nào? Tại sao việc báo lỗi muộn như vậy lại là thảm họa đối với trải nghiệm người chơi?
=> Báo lỗi ở dòng thứ 5 sau khi chạy hết code. Việc đó khiến cho code bị lỗi đáng kể
Khi bạn import và sử dụng module abc (Abstract Base Classes) kèm decorator @abstractmethod cho lớp Hero,
nếu lớp Assassin vẫn ngoan cố không ghi đè hàm use_ultimate(), thì lỗi sẽ văng ra vào thời điểm nào? (Lúc loading ván đấu hay lúc giao tranh?).
=> Lúc loading ván đấu
Nguyên lý Fail Fast (Thất bại nhanh/Báo lỗi sớm) được thể hiện như thế nào khi chúng ta áp dụng Abstract Base Classes vào kiến trúc Game?
=> Việc áp dụng đó khiến ta phát hiện rõ code bị gặp lỗi ở đúng chính xác thời điểm code dừng để ta có thể sửa code dễ dàng hơn.
"""