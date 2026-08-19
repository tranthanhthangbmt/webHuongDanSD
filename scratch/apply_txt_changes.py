import os

source_path = r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\TaiLieu\instruction v17A_31.7.2026_.txt"
dest_path = r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\TaiLieu\instruction v17B_19.8.2026.txt"

with open(source_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ("quy trình tố tụng nghiêm ngặt", "quy trình làm việc nghiêm ngặt"),
    ("Bước 1.", "Bước 1 (liền kề trước đó)."),
    ('**"Kiểm sát viên"** hoặc **"Đồng chí"**.', '**"Kiểm sát viên"** **"Đồng chí"**.'),
    ('Khi nói về UBND/Cơ quan hành chính:', 'Khi nói về UBND/Cơ quan hành chính nhà nước:'),
    ('**"Thủ tục tố tụng"**', '**"Trình tự, thủ tục tố tụng"**'),
    ('cho hành vi của UBND.', 'cho hành vi của UBND/Cơ quan hành chính nhà nước.'),
    ('Phát hiện vi phạm của Thẩm phán, Thư ký, Người tham gia tố tụng.', 'Phát hiện vi phạm của Thẩm phán, Thư ký, Hội đồng xét xử, Người tham gia tố tụng.'),
    ('pháp luật tố tụng:', 'pháp luật về tố tụng:'),
    ('**Từ khóa đắt giá:**', '**Từ khóa then chốt/cốt lõi:**'),
    ('**Vùng xám (Gray Zone):**', '**Vấn đề cần chú ý / xem xét thêm:**'),
    ('**Vùng xám:**', '**Vấn đề cần chú ý / xem xét thêm:**'),
    ('Thưa Kiểm sát viên,', 'Thưa Đồng chí,'),
    ('Giải phẫu dữ liệu', 'Trích xuất dữ liệu'),
    ('GIẢI PHẪU DỮ LIỆU', 'TRÍCH XUẤT DỮ LIỆU'),
    ('Xin Kiểm sát viên', 'Xin Đồng chí'),
    ('Truy vấn điểm mờ (Gap Analysis):', 'Vấn đề cần chú ý / xem xét thêm:'),
    ('MA TRẬN THỜI GIAN & PHÁP LUẬT (TIMELINE & JURISDICTION)', 'SỰ KIỆN PHÁP LÝ VÀ QUY ĐỊNH PHÁP LUẬT TƯƠNG ỨNG'),
    ('có hiệu lực tại thời điểm đó.', 'có hiệu lực tại thời điểm đó. (Luật, Nghị định, thông tư, … nếu có)'),
    ('Khoanh vùng văn bản địa phương:', 'Khoanh vùng văn bản địa phương (Tỉnh Đắk Lắk, tỉnh Phú yên):'),
    ('| *Luật Đất đai 1987* |', '| *Luật Đất đai 1987/(thêm Nghị định, thông tư liên quan - nếu có)* |'),
    ('khai quật văn bản ở Bước 3', 'khai thác văn bản ở Bước 3'),
    ('KHAI QUẬT VĂN BẢN', 'RÀ SOÁT QUY ĐỊNH PHÁP LUẬT'),
    ('Tìm chứng cứ pháp lý', 'Tìm căn cứ pháp lý'),
    ('Nghị định sửa đổi,', 'Nghị định/Thông tư sửa đổi,'),
    ('Điều/Khoản ->', 'Điều/Khoản/Điểm ->'),
    ('GIẢI MÃ & ĐỐI CHIẾU', 'ĐỐI CHIẾU PHÁP LUẬT'),
    ('soi lỗi tố tụng', 'kiểm tra lỗi quy trình'),
    ('THANH TRA QUY TRÌNH HÀNH CHÍNH', 'KIỂM TRA QUY TRÌNH HÀNH CHÍNH'),
    ('Phòng Kiểm sát Quyết định hành chính.', 'Phòng Kiểm tra Quyết định hành chính/ Hành vi hành chính.'),
    ('Hành vi hành chính bị kiện (Của UBND hoặc Sở TNMT).', 'Hành vi hành chính (HVHC) bị kiện (Của UBND hoặc Sở TNMT hoặc cơ quan quản lý hành chính Nhà nước).'),
    ('địa phương).', 'địa phương, chú ý Luật sửa đổi, bổ sung).'),
    ('thanh tra quy trình hành chính của UBND', 'kiểm tra quy trình hành chính của cơ quan quản lý hành chính nhà nước'),
    ('Kiểm sát Tố tụng Tòa án', 'Kiểm sát trình tự Tố tụng của Tòa án'),
    ('Hành vi tố tụng', 'Hoạt động tố tụng'),
    ('Thư ký Tòa án và', 'Thư ký Tòa án, Hội đồng xét xử và'),
    ('| *Nghiêm trọng (Vi phạm trình tự thu hồi)* |', '| *Vi phạm (Vi phạm trình tự thu hồi)* |'),
    ('| *Rất nghiêm trọng (Vi phạm thẩm quyền)* |', '| *Nghiêm trọng (Vi phạm thẩm quyền theo cấp lãnh thổ)* |'),
    ('| *Rất nghiêm trọng (Ảnh hưởng quyền lợi)* |', '| *Nghiêm trọng (Ảnh hưởng quyền lợi)* |'),
    ('Thụ lý sai thẩm quyền (Tòa huyện thụ lý)', 'Thụ lý sai thẩm quyền (Tòa khu vực 1 thụ lý án kiện UBND cấp xã không thuộc phạm vi địa giới hành chính của Tòa khu vực 1)'),
    ('Thanh tra Hành chính', 'Kiểm tra trình tự, thủ tục Hành chính'),
    ('Kiểm sát Tố tụng (Bước 5B)', 'Kiểm sát việc tuân theo pháp luật về tố tụng (Bước 5B)'),
    ('Kiểm sát Tố tụng', 'Kiểm sát việc tuân theo pháp luật về tố tụng'),
    ('bảo vệ quyền lợi cho UBND."', 'bảo vệ quyền lợi cho UBND/ Người bị kiện."'),
    ('**02 lập luận sắc bén nhất**', '**02 đến 03 lập luận sắc bén nhất**'),
    ('tình huống nào khác', 'tình huống tranh tụng nào khác'),
    ('TÌM KIẾM TIỀN LỆ', 'TÌM KIẾM TÌNH HUỐNG TƯƠNG TỰ'),
    ('So sánh án lệ', 'So sánh Tình huống tương tự'),
    ('Án lệ công bố hoặc Bản án Giám đốc thẩm/Phúc thẩm', 'Án lệ công bố/thông báo rút kinh nghiệm/giải đáp vướng mắc của Tòa án nhân dân tối cao, giải đáp của Viện kiểm sát nhân dân tối cao hoặc Bản án Phúc thẩm/ quyết định Giám đốc thẩm/ quyết định tái thẩm'),
    ('TÌM KIẾM TIỀN LỆ.', 'TÌM KIẾM tình huống pháp lý tương tự.'),
    ('"DEEP DOSSIER" (BÁO CÁO CHUYÊN SÂU)', '(BÁO CÁO CHUYÊN SÂU)'),
    ('Kết quả kiểm sát Tố tụng:', 'Kết quả Kiểm sát việc tuân theo pháp luật về tố tụng:'),
    ('QĐHC:** (Mổ xẻ chi tiết từng lỗi của UBND', 'QĐHC/HVHC:** (Mổ xẻ chi tiết từng lỗi của người bị kiện'),
    ('Nghiêm túc, Chính trị, Chuẩn mực', 'Nghiêm túc, Chính trị, tư pháp, Chuẩn mực'),
    ('Kiểm sát tính hợp pháp', 'Kiểm sát tra tính hợp pháp'),
    ('Kiểm sát viên cung cấp thêm', 'đồng chí cung cấp thêm')
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
    else:
        print(f"WARNING: String not found: {old}")

# Handle multiline additions
# 1. Add "Người có quyền lợi nghĩa vụ liên quan"
if "* Người bị kiện: [...]" in content and "* Người có quyền lợi nghĩa vụ liên quan:" not in content:
    content = content.replace(
        "* Người bị kiện: [...]",
        "* Người bị kiện: [...]\n    * Người có quyền lợi nghĩa vụ liên quan: [...]\n    * Người làm chứng: [...]"
    )

# 2. Update Mũi nhọn 1
old_mui_nhon_1 = """1.  **Mũi nhọn 1: Kiểm tra Thụ lý & Thẩm quyền (Jurisdiction Audit):**
    * **Thẩm quyền theo cấp:** Đối chiếu **Điều 30, 31, 32 Luật Tố tụng hành chính 2015**.
        * *Quy tắc:* Nếu kiện Quyết định của UBND cấp Huyện/Chủ tịch UBND cấp Huyện -> Thẩm quyền sơ thẩm thuộc **Tòa án cấp Tỉnh** (để đảm bảo khách quan). Nếu Tòa Huyện thụ lý là SAI.
    * **Thời hiệu khởi kiện:** Đối chiếu **Điều 116 LTTHC**.
        * *Công thức:* `[Ngày nộp đơn khởi kiện]` - `[Ngày nhận được/biết được Quyết định hành chính]`.
        * *Kết luận:* Có còn trong thời hạn 01 năm không?"""

# In the txt file, the indentation might use unusual spacing (e.g. non-breaking spaces or different indent size). 
# Let's find it exactly by searching a substring and replacing.
if "1.  **Mũi nhọn 1: Kiểm tra Thụ lý & Thẩm quyền (Jurisdiction Audit):**" in content:
    # Need to extract the exact old string to replace.
    start_idx = content.find("1.  **Mũi nhọn 1: Kiểm tra Thụ lý & Thẩm quyền (Jurisdiction Audit):**")
    end_idx = content.find("2.  **Mũi nhọn 2:", start_idx)
    if start_idx != -1 and end_idx != -1:
        exact_old = content[start_idx:end_idx]
        new_mui_nhon_1 = """1.  **Mũi nhọn 1: Kiểm tra Thụ lý, Thẩm quyền & Tư cách đương sự mới (Jurisdiction & Party Audit):**
    * **[CẬP NHẬT 2025] Thẩm quyền theo cấp & Tổ chức Tòa án mới:** Đối chiếu Luật Tố tụng hành chính (sửa đổi, bổ sung năm 2025 theo Luật 85/2025/QH15) và Nghị quyết 05/2025/NQ-HĐTP.
        * *Quy tắc phân định Sơ thẩm:* **Tòa án nhân dân khu vực** (thay thế Tòa cấp huyện cũ) từ 01/7/2025, thụ lý sơ thẩm các khiếu kiện theo Điều 31. Tuy nhiên, nếu kiện Quyết định của UBND cấp Huyện/Chủ tịch UBND cấp Huyện -> sau ngày 01/7/2025, Thẩm quyền sơ thẩm thuộc **Tòa án cấp Tỉnh Khu vực**.
    * **[CẬP NHẬT 2025] Thẩm quyền trong giai đoạn chuyển giao:** Đối chiếu Nghị quyết 01/2025/NQ-HĐTP và Công văn 285/TANDTC-PC.
        * *Quy tắc chuyển tiếp Phúc thẩm:* Đối với các vụ án đã được TAND Cấp cao thụ lý phúc thẩm TRƯỚC ngày 01/7/2025 nhưng chưa giải quyết xong -> Thẩm quyền giải quyết tiếp theo bắt buộc thuộc về **Tòa Phúc thẩm Tòa án nhân dân tối cao**.
    * **[CẬP NHẬT 2025] Rà soát "Người kế thừa quyền và nghĩa vụ tố tụng":** Đối chiếu Luật Tổ chức Chính quyền địa phương sửa đổi 2025, Nghị quyết 01/2025/NQ-HĐTP và Công văn 285/TANDTC-PC (áp dụng từ 01/7/2025).
        * *Quy tắc đột phá (Đặc biệt chú ý án liên quan GCNQSDĐ):* Trong các vụ án có yêu cầu hủy Giấy chứng nhận quyền sử dụng đất (GCNQSDĐ) do UBND cấp Huyện cấp:
        * *Nếu Tòa thụ lý TRƯỚC 01/7/2025:* Tòa án có xác định đúng **Chủ tịch UBND cấp xã** (nơi cư trú của cá nhân có thẩm quyền) là *người kế thừa quyền và nghĩa vụ tố tụng* của UBND cấp huyện không?
        * *Nếu Tòa thụ lý Từ 01/7/2025:* Tòa án có đưa thẳng **Chủ tịch UBND cấp xã** vào tham gia tố tụng ngay từ đầu với tư cách đương sự (Người bị kiện/Người có quyền lợi, nghĩa vụ liên quan) không?
        * *Kết luận:* Nếu Tòa án bỏ qua sự chuyển giao thẩm quyền này và vẫn tiếp tục để UBND cấp Huyện làm đương sự duy nhất -> **Vi phạm nghiêm trọng việc xác định tư cách đương sự.**
    * **Thời hiệu khởi kiện:** Đối chiếu **Điều 116 LTTHC**.
        * *Công thức:* `[Ngày nộp đơn khởi kiện]` - `[Ngày nhận được/biết được Quyết định hành chính]`.
        * *Kết luận:* Có còn trong thời hạn 01 năm không?

"""
        content = content.replace(exact_old, new_mui_nhon_1)
else:
    print("WARNING: Mũi nhọn 1 not found via exact match start")

# 3. Add Ngân hàng & Chủ tịch UBND
if "* *Ngân hàng:* Đất có đang thế chấp không?" in content and "Chủ tịch UBND cấp Xã:" not in content:
    content = content.replace(
        "* *Ngân hàng:* Đất có đang thế chấp không?",
        "* *Ngân hàng:* Đất có đang thế chấp không?\n        * **[CẬP NHẬT 2025] *Chủ tịch UBND cấp Xã:* Đã được đưa vào tham gia tố tụng với tư cách người kế thừa/đương sự đối với yêu cầu hủy GCNQSDĐ (theo CV 285/TANDTC-PC) chưa?**"
    )

# 4. Add table row
if "| **TỐ TỤNG (TÒA ÁN)** | *VD: Bỏ sót vợ người khởi kiện* | *Nghiêm trọng (Ảnh hưởng quyền lợi)* |" in content and "Xác định sai đương sự" not in content:
    content = content.replace(
        "| **TỐ TỤNG (TÒA ÁN)** | *VD: Bỏ sót vợ người khởi kiện* | *Nghiêm trọng (Ảnh hưởng quyền lợi)* |",
        "| **TỐ TỤNG (TÒA ÁN)** | *VD: Xác định sai đương sự (Không đưa Chủ tịch UBND xã vào tham gia tố tụng theo CV 285)* | *Nghiêm trọng (Vi phạm tư cách đương sự)* |\n| **TỐ TỤNG (TÒA ÁN)** | *VD: Bỏ sót vợ người khởi kiện* | *Nghiêm trọng (Ảnh hưởng quyền lợi)* |"
    )

with open(dest_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated text file successfully.")
