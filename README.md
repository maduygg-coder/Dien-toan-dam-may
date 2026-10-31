
Duy,Công,Lâm,Bình,Minh
# CloudTask – Quản lý lịch học cá nhân

Dự án môn Điện toán đám mây, hỗ trợ sinh viên quản lý lịch học cá nhân.

## Chức năng đã thực hiện

- Xem danh sách lịch học.
- Thêm lịch học.
- Chỉnh sửa lịch học.
- Xóa lịch học có xác nhận.
- Kiểm tra thông tin bắt buộc và giờ kết thúc sau giờ bắt đầu.
- Lưu dữ liệu bằng SQLite.

## Công nghệ hiện tại

- Python và Flask: xử lý phía máy chủ.
- HTML, CSS, Jinja: giao diện.
- SQLite: lưu dữ liệu trên máy.
- GitHub: quản lý mã nguồn và phối hợp nhóm.

## Cách chạy trên Windows

Mở Terminal tại thư mục dự án, chạy:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Mở trình duyệt tại: http://127.0.0.1:5000

Giữ Terminal chạy trong khi sử dụng.
Nhấn Ctrl + C trong Terminal để dừng ứng dụng.

## Dữ liệu

File cloudtask.db được tự động tạo khi chạy ứng dụng.
File này chứa lịch học trên từng máy và không được đưa lên GitHub.
Máy mới chạy ứng dụng sẽ có danh sách lịch học trống.

## Tiến độ

Đã hoàn thành bản chạy local với chức năng thêm, xem, sửa, xóa lịch học.

Chưa triển khai lên cloud. Chưa có đăng nhập và phân tách dữ liệu
theo người dùng.

## Kế hoạch tiếp theo

- Lựa chọn và triển khai dịch vụ cloud.
- Cấu hình lưu trữ dữ liệu phù hợp khi triển khai.
- Kiểm thử và chuẩn bị minh chứng demo.