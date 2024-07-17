import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("AtarBals Modem Antivius")
root.geometry("800x500")
root.configure(bg='lightblue')  # Màu nền tùy chỉnh

# Tạo khung chính chia thành thanh bên và khu vực nội dung chính
main_frame = tk.Frame(root, bg='Blue')
main_frame.pack(fill=tk.BOTH, expand=True)

# Thanh bên
sidebar = tk.Frame(main_frame, width=200, bg='Blue')
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Khu vực nội dung chính
content_area = tk.Frame(main_frame, bg='white')
content_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Các phần trong thanh bên
status_label = tk.Label(sidebar, text="Status", font=("Arial", 14), bg='Blue', fg='white')
status_label.pack(pady=10, padx=10, anchor='w')

update_label = tk.Label(sidebar, text="Updates", font=("Arial", 14), bg='Blue', fg='white')
update_label.pack(pady=10, padx=10, anchor='w')

settings_label = tk.Label(sidebar, text="Settings", font=("Arial", 14), bg='Blue', fg='white')
settings_label.pack(pady=10, padx=10, anchor='w')

ShareFeedback_label = tk.Label(sidebar, text="Share Feedback ", font=("Arial", 14), bg='Blue', fg='white')
ShareFeedback_label.pack(pady=10, padx=10, anchor='w')

BuyPremium_label = tk.Label(sidebar, text="Buy Premium ", font=("Arial", 14), bg='Blue', fg='white')
BuyPremium_label.pack(pady=10, padx=10, anchor='w')

Help_label = tk.Label(sidebar, text="Help ", font=("Arial", 14), bg='Blue', fg='white')
Help_label.pack(pady=10, padx=10, anchor='w')
# Nút "Quét ngay"
scan_button = tk.Button(sidebar, text="Scan Now", font=("Arial", 14), bg='Green1', fg='white')
scan_button.pack(pady=20, padx=10, fill=tk.X)

# Các thành phần trong khu vực nội dung chính
title_label = tk.Label(content_area, text="Scan", font=("Arial", 24), bg='white')
title_label.pack(pady=20)

subtitle_label = tk.Label(content_area, text="Premium will be free forever.You just need to click button.", font=("Arial", 18), bg='white')
subtitle_label.pack(pady=10)

# Tạo khung để chứa các nút chức năng
button_frame = tk.Frame(content_area, bg='white')
button_frame.pack(pady=20)

# Thêm các nút chức năng
quick_scan_button = tk.Button(button_frame, text="Quick Scan", font=("Arial", 14), bg='magenta', fg='black')
quick_scan_button.pack(side=tk.LEFT, padx=10)
def on_scan_button_click():
    current_status_label.config(text="Quick Scan")
web_protection_button = tk.Button(button_frame, text="Web Protection", font=("Arial", 14), bg='magenta', fg='black')
web_protection_button.pack(side=tk.LEFT, padx=10)

Quarantine_button = tk.Button(button_frame, text="Quarantine", font=("Arial", 14), bg='magenta', fg='black')
Quarantine_button.pack(side=tk.LEFT, padx=10)

Full_Scan_button = tk.Button(button_frame, text="Full Scan", font=("Arial", 14), bg='magenta', fg='black')
Full_Scan_button.pack(side=tk.LEFT, padx=10)

Simple_Update_button = tk.Button(button_frame, text="Simple Update", font=("Arial", 14), bg='magenta', fg='black')
Simple_Update_button.pack(side=tk.LEFT, padx=10)
# Nhãn trạng thái hiển thị hành động/trạng thái hiện tại
current_status_label = tk.Label(content_area, text="Trạng thái hiện tại: Đang chờ", font=("Arial", 14), bg='white')
current_status_label.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
