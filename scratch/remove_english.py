import re
import os

html_path = r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = [
    ('"System Override" (Ghi đè hệ thống)', '"Ghi đè hệ thống"'),
    ('"State Lock" (Khóa trạng thái)', '"Khóa trạng thái"'),
    ('"Atomic Execution" (Thực thi đơn nhiệm)', '"Thực thi đơn nhiệm"'),
    ('hiện tượng ảo giác (hallucination)', 'hiện tượng ảo giác (bịa đặt thông tin)'),
    ('"Data Forensics" (Giải phẫu dữ liệu)', '"Giải phẫu dữ liệu"'),
    ('"Gap Analysis" (Phân tích khoảng trống)', '"Phân tích khoảng trống"'),
    ('"Timeline Construction" (Dựng trục thời gian)', '"Dựng trục thời gian"'),
    ('"Inter-temporal law" (Luật tại thời điểm)', '"Luật tại thời điểm"'),
    ('"Universal 3-Layer Citation" (Trích dẫn 3 lớp)', '"Trích dẫn 3 lớp"'),
    ('AI "bịa" luật (hallucination)', 'AI "bịa" luật'),
    ('"Mapping Table" (Bảng đối chiếu)', '"Bảng đối chiếu"'),
    ('"Confidence Metric" (Chỉ số tự tin)', '"Chỉ số tự tin"'),
    ('"Multi-layer Filtering" (Lọc nhiều lớp)', '"Lọc nhiều lớp"'),
    ('"Missing Party Scan" (Quét đương sự bị sót)', '"Quét đương sự bị sót"'),
    ('chuỗi câu hỏi tư duy (Chain of thought)', 'chuỗi câu hỏi tư duy'),
    ('"Reverse Thinking" (Tư duy đảo chiều)', '"Tư duy đảo chiều"'),
    ('mô hình Red Team/Blue Team', 'mô hình Đóng vai đối kháng'),
    ('của LLM', 'của Trí tuệ nhân tạo'),
    ('"Case-based Reasoning" (Lập luận dựa trên tình huống)', '"Lập luận dựa trên tình huống"'),
    ('"Final Confidence Score" (Định lượng niềm tin cuối cùng)', '"Định lượng niềm tin cuối cùng"'),
    ('tổng hợp logic chuỗi (Chain-of-logic)', 'tổng hợp logic chuỗi'),
    ('"Deep Dossier Protocol" (Giao thức báo cáo chuyên sâu)', '"Giao thức báo cáo chuyên sâu"'),
    ('"Iterative Generation" (Khởi tạo từng phần)', '"Khởi tạo từng phần"'),
    ('lỗi "ngắt quãng" (cut-off)', 'lỗi ngắt quãng'),
    ('không gian tư duy (context window)', 'không gian xử lý dữ liệu')
]

for old, new in replacements:
    html = html.replace(old, new)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Removed English terms successfully.")
