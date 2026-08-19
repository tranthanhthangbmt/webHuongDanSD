import os

path = r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ("quy trình tố tụng nghiêm ngặt", "quy trình làm việc nghiêm ngặt"),
    ("Bước 1.", "Bước 1 (liền kề trước đó)."),
    ('là **"Kiểm sát viên"** hoặc **"Đồng chí"**.', 'là **"Kiểm sát viên"** **"Đồng chí"**.'),
    ('Khi nói về UBND/Cơ quan hành chính:', 'Khi nói về UBND/Cơ quan hành chính nhà nước:'),
    ('Dùng từ **"Thủ tục tố tụng"**', 'Dùng từ **"Trình tự, thủ tục tố tụng"**'),
    ('cho hành vi của UBND.', 'cho hành vi của UBND/Cơ quan hành chính nhà nước.'),
    ('Phát hiện vi phạm của Thẩm phán, Thư ký, Người tham gia tố tụng.', 'Phát hiện vi phạm của Thẩm phán, Thư ký, Hội đồng xét xử, Người tham gia tố tụng.'),
    ('pháp luật tố tụng:', 'pháp luật về tố tụng:'),
    ('**Từ khóa đắt giá:**', '**Từ khóa then chốt/cốt lõi:**'),
    ('**Vùng xám (Gray Zone):**', '**Vấn đề cần chú ý / xem xét thêm:**'),
    ('Thưa Kiểm sát viên,', 'Thưa Đồng chí,'),
    ('Bước 1: Giải phẫu dữ liệu', 'Bước 1: Trích xuất dữ liệu'),
    ('1. PHÂN TÍCH DỮ LIỆU', '1. TRÍCH XUẤT DỮ LIỆU'),
    ('1. Phân tích dữ liệu', '1. Trích xuất dữ liệu'),
    ('BƯỚC 1: GIẢI PHẪU DỮ LIỆU (DATA FORENSICS)', 'BƯỚC 1: TRÍCH XUẤT DỮ LIỆU (DATA FORENSICS)'),
    ('Xin Kiểm sát viên', 'Xin Đồng chí'),
    ('Truy vấn điểm mờ (Gap Analysis):', 'Vấn đề cần chú ý / xem xét thêm:'),
    ('MA TRẬN THỜI GIAN & PHÁP LUẬT (TIMELINE & JURISDICTION)', 'SỰ KIỆN PHÁP LÝ VÀ QUY ĐỊNH PHÁP LUẬT TƯƠNG ỨNG'),
    ('2. XÁC ĐỊNH LUẬT ÁP DỤNG THEO SỰ KIỆN PHÁP LÝ', '2. SỰ KIỆN PHÁP LÝ VÀ QUY ĐỊNH PHÁP LUẬT TƯƠNG ỨNG'),
    ('2. Xác định luật áp dụng theo sự kiện pháp lý', '2. Sự kiện pháp lý và quy định pháp luật tương ứng'),
    ('có hiệu lực tại thời điểm đó.', 'có hiệu lực tại thời điểm đó. (Luật, Nghị định, thông tư, … nếu có)'),
    ('Khoanh vùng văn bản địa phương:', 'Khoanh vùng văn bản địa phương (Tỉnh Đắk Lắk, tỉnh Phú yên):'),
    ('| *Luật Đất đai 1987* |', '| *Luật Đất đai 1987/(thêm Nghị định, thông tư liên quan - nếu có)* |'),
    ('tiến hành khai quật văn bản ở Bước 3', 'tiến hành khai thác văn bản ở Bước 3'),
    ('3. RÀ SOÁT VĂN BẢN QUY PHẠM PHÁP LUẬT', '3. RÀ SOÁT QUY ĐỊNH PHÁP LUẬT'),
    ('3. Rà soát văn bản quy phạm pháp luật', '3. Rà soát quy định pháp luật'),
    ('KHAI QUẬT VĂN BẢN', 'RÀ SOÁT QUY ĐỊNH PHÁP LUẬT'),
    ('Tìm chứng cứ pháp lý', 'Tìm căn cứ pháp lý'),
    ('Nghị định sửa đổi,', 'Nghị định/Thông tư sửa đổi,'),
    ('Điều/Khoản ->', 'Điều/Khoản/Điểm ->'),
    ('4. KIỂM TRA TÍNH HỢP PHÁP CỦA QUYẾT ĐỊNH HÀNH CHÍNH, HÀNH VI HÀNH CHÍNH', '4. ĐỐI CHIẾU PHÁP LUẬT'),
    ('4. Kiểm tra tính hợp pháp của QĐHC, HVHC', '4. Đối chiếu pháp luật'),
    ('GIẢI MÃ & ĐỐI CHIẾU', 'ĐỐI CHIẾU PHÁP LUẬT'),
    ('soi lỗi tố tụng', 'kiểm tra lỗi quy trình'),
    ('THANH TRA QUY TRÌNH HÀNH CHÍNH', 'KIỂM TRA QUY TRÌNH HÀNH CHÍNH'),
    ('Phòng Kiểm sát Quyết định hành chính.', 'Phòng Kiểm tra Quyết định hành chính/ Hành vi hành chính.'),
    ('Hành vi hành chính bị kiện', 'Hành vi hành chính (HVHC) bị kiện'),
    ('Sở TNMT).', 'Sở TNMT hoặc cơ quan quản lý hành chính Nhà nước).'),
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
    ('Kiểm sát Tố tụng', 'Kiểm sát việc tuân theo pháp luật về tố tụng'),
    ('bảo vệ quyền lợi cho UBND."*', 'bảo vệ quyền lợi cho UBND/ Người bị kiện."*'),
    ('**02 lập luận sắc bén nhất**', '**02 đến 03 lập luận sắc bén nhất**'),
    ('tình huống nào', 'tình huống tranh tụng nào'),
    ('6+. TÌM KIẾM BẢN ÁN, ÁN LỆ', '6+. TÌM KIẾM TÌNH HUỐNG TƯƠNG TỰ'),
    ('6+. Tìm kiếm bản án, án lệ', '6+. Tìm kiếm tình huống tương tự'),
    ('TÌM KIẾM TIỀN LỆ', 'TÌM KIẾM TÌNH HUỐNG TƯƠNG TỰ'),
    ('So sánh án lệ', 'So sánh Tình huống tương tự'),
    ('Án lệ công bố hoặc Bản án Giám đốc thẩm/Phúc thẩm có tình tiết tương đồng.', 'Án lệ công bố/thông báo rút kinh nghiệm/giải đáp vướng mắc của Tòa án nhân dân tối cao, giải đáp của Viện kiểm sát nhân dân tối cao hoặc Bản án Phúc thẩm/ quyết định Giám đốc thẩm/ quyết định tái thẩm có tình tiết tương đồng.'),
    ('TÌM KIẾM TIỀN LỆ.', 'TÌM KIẾM tình huống pháp lý tương tự.'),
    ('GIAO THỨC XUẤT BẢN: "DEEP DOSSIER"', 'GIAO THỨC XUẤT BẢN:'),
    ('Kết quả kiểm sát Tố tụng:', 'Kết quả Kiểm sát việc tuân theo pháp luật về tố tụng:'),
    ('QĐHC:** (Mổ xẻ chi tiết từng lỗi của UBND', 'QĐHC/HVHC:** (Mổ xẻ chi tiết từng lỗi của người bị kiện'),
    ('**Vùng xám:**', '**Vấn đề cần chú ý / xem xét thêm:**'),
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
new_mui_nhon_1 = """1.  **Mũi nhọn 1: Kiểm tra Thụ lý, Thẩm quyền & Tư cách đương sự mới (Jurisdiction & Party Audit):**
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
        * *Kết luận:* Có còn trong thời hạn 01 năm không?"""
if old_mui_nhon_1 in content:
    content = content.replace(old_mui_nhon_1, new_mui_nhon_1)
else:
    print("WARNING: Mũi nhọn 1 not found")

# 3. Add Ngân hàng & Chủ tịch UBND
if "* *Ngân hàng:* Đất có đang thế chấp không?" in content and "Chủ tịch UBND cấp Xã:" not in content:
    content = content.replace(
        "* *Ngân hàng:* Đất có đang thế chấp không?",
        "* *Ngân hàng:* Đất có đang thế chấp không?\n        * **[CẬP NHẬT 2025] *Chủ tịch UBND cấp Xã:* Đã được đưa vào tham gia tố tụng với tư cách người kế thừa/đương sự đối với yêu cầu hủy GCNQSDĐ (theo CV 285/TANDTC-PC) chưa?**"
    )

# 4. Add table row
if "| **TỐ TỤNG (TÒA ÁN)** | *VD: Bỏ sót vợ người khởi kiện* | *Nghiêm trọng (Ảnh hưởng quyền lợi)* |" in content and "Xác định sai đương sự" not in content:
    content = content.replace(
        "| **TỐ TỤNG (TÒA ÁN)** | *VD: Bỏ sót vợ người khởi kiện* | *Nghiêm trọng (Ảnh hưởng quyền lợi)* |",
        "| **TỐ TỤNG (TÒA ÁN)** | *VD: Xác định sai đương sự (Không đưa Chủ tịch UBND xã vào tham gia tố tụng theo CV 285)* | *Nghiêm trọng (Vi phạm tư cách đương sự)* |\n| **TỐ TỤNG (TÒA ÁN)** | *VD: Bỏ sót vợ người khởi kiện* | *Nghiêm trọng (Ảnh hưởng quyền lợi)* |"
    )

# 5. Add section 4
new_section = """
---

## 4. CÀI ĐẶT GIAO TIẾP & NGÔN NGỮ (PROCURACY STANDARD)
- **Giọng văn:** Nghiêm túc, Chính trị, tư pháp, Chuẩn mực hành chính công vụ.
- **Quy tắc dùng từ:**
* KHÔNG dùng: "Soi lỗi", "Bắt lỗi", "Cãi nhau", "Phán quyết".
* PHẢI dùng: "Phát hiện vi phạm", "Kiểm sát tra tính hợp pháp", "Tranh tụng/Đối đáp", "Đề xuất quan điểm/Đường lối".
- **Yêu cầu đặc biệt:**
* Tuyệt đối không tự ý kết luận khi thiếu căn cứ. Phải dùng cụm từ *"Có dấu hiệu vi phạm"* thay vì khẳng định *"Đã vi phạm"* khi hồ sơ chưa đủ.
* Nếu không tìm thấy văn bản trong PDF, phải báo cáo: *"Dữ liệu hồ sơ hiện tại chưa thể hiện nội dung này. Đề nghị đồng chí cung cấp thêm."*"""

if "## 4. CÀI ĐẶT GIAO TIẾP" not in content:
    # Insert it right before "</div>\n</div></details>\n\n</div>\n</section>\n<!-- Step 1 -->"
    insert_pos = content.find('Chúng ta hãy bắt đầu với **Bước 1: Trích xuất dữ liệu**."*</div>')
    if insert_pos != -1:
        insert_text = 'Chúng ta hãy bắt đầu với **Bước 1: Trích xuất dữ liệu**."*\n' + new_section + '\n</div>'
        content = content.replace('Chúng ta hãy bắt đầu với **Bước 1: Trích xuất dữ liệu**."*</div>', insert_text)
    else:
        print("WARNING: Could not find insert position for section 4")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated index.html successfully.")
