import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title(" Frame Recorder")
root.geometry("600x300")
root.configure(bg='lightpink')  # Màu nền tùy chỉnh

# Thêm nhãn tiêu đề lớn ở giữa
title_label = tk.Label(root, text="Frame Recorder", font=("Arial", 24), bg='lightpink')
title_label.pack(pady=20)

# Tạo một khung để chứa đầu vào FPS và nhãn
fps_frame = tk.Frame(root, bg='lightpink')
fps_frame.pack(pady=10)

# Thêm nhãn và trường đầu vào cho FPS
fps_label = tk.Label(fps_frame, text="FPS (khung hình/giây):", font=("Arial", 14), bg='lightpink')
fps_label.pack(side=tk.LEFT, padx=5)

fps_entry = tk.Entry(fps_frame, font=("Arial", 14))
fps_entry.pack(side=tk.LEFT, padx=5)

# Tạo một khung để chứa các nút
button_frame = tk.Frame(root, bg='lightpink')
button_frame.pack(pady=20)

# Thêm các nút "Tạm dừng", "Bắt đầu" và "Kết thúc"
pause_button = tk.Button(button_frame, text="Tạm dừng", font=("Arial", 14))
pause_button.pack(side=tk.LEFT, padx=5)

start_button = tk.Button(button_frame, text="Bắt đầu", font=("Arial", 14))
start_button.pack(side=tk.LEFT, padx=5)

end_button = tk.Button(button_frame, text="Kết thúc", font=("Arial", 14))
end_button.pack(side=tk.LEFT, padx=5)

# Thêm nhãn trạng thái để hiển thị trạng thái ghi hiện tại
status_label = tk.Label(root, text="Trạng thái: Đang chờ", font=("Arial", 14), bg='lightpink')
status_label.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
