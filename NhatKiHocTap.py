
# NHAT KY HOC TAP 
diary = []

def danh_gia(gio, muc_do):
    if gio >= 2 and muc_do >= 4:
        return "Học tập rất hiệu quả"
    elif gio >= 1:
        return "Học tập ổn"
    else:
        return "Cần cố gắng hơn"

def them_nhat_ky():
    mon = input("Nhập môn học: ")
    gio = float(input("Nhập số giờ học: "))
    muc_do = int(input("Mức độ hiểu bài (1-5): "))

    ket_qua = danh_gia(gio, muc_do)

    ngay_hoc = {
        "mon": mon,
        "gio": gio,
        "muc_do": muc_do,
        "danh_gia": ket_qua
    }

    diary.append(ngay_hoc)
    print("Đã lưu nhật ký!\n")

def xem_nhat_ky():
    if len(diary) == 0:
        print("Chưa có nhật ký nào!\n")
        return

    print("\nNHẬT KÝ HỌC TẬP")
    for i, d in enumerate(diary, start=1):
        print(f"{i}. {d['mon']} | {d['gio']} giờ | Hiểu: {d['muc_do']}/5")
        print(d["danh_gia"])
    print()

while True:
    print("===== MENU =====")
    print("1. Thêm nhật ký học tập")
    print("2. Xem nhật ký")
    print("3. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == "1":
        them_nhat_ky()
    elif chon == "2":
        xem_nhat_ky()
    elif chon == "3":
        print("Kết thúc chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!\n")
