import re

html_path = r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

explanations_to_append = {
    "intro": r'<p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Sử dụng kỹ thuật "System Override" (Ghi đè hệ thống) và "State Lock" (Khóa trạng thái) để buộc AI phải thoát khỏi vai trò trợ lý thông thường, nhập vai tuyệt đối vào một "Kiểm sát viên". Kỹ thuật "Atomic Execution" (Thực thi đơn nhiệm) ngăn chặn hiện tượng ảo giác (hallucination) do xử lý quá nhiều thông tin cùng lúc, đảm bảo AI tuân thủ nguyên tắc thận trọng, đi từng bước vững chắc của ngành Kiểm sát.</p>',
    "step1": r'<p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Kỹ thuật "Data Forensics" (Giải phẫu dữ liệu) kết hợp "Gap Analysis" (Phân tích khoảng trống) giúp AI không chỉ thụ động tiếp nhận văn bản mà còn chủ động cấu trúc hóa các sự kiện lộn xộn. Đặc biệt, yêu cầu trích dẫn nguyên văn giúp bám sát chứng cứ gốc, đồng thời chủ động truy vấn các "điểm mờ" (thiếu thông tin) giống như tư duy phản biện của một Kiểm sát viên dày dặn kinh nghiệm.</p>',
    "step2": r'<p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Ứng dụng kỹ thuật "Timeline Construction" (Dựng trục thời gian) và "Inter-temporal law" (Luật tại thời điểm). Prompt buộc AI không được tìm kiếm luật chung chung mà phải "neo" (anchor) từng hành vi hành chính vào đúng mốc thời gian lịch sử. Điều này khắc phục điểm yếu chí mạng của LLM là hay "râu ông nọ cắm cằm bà kia", đảm bảo tính chính xác tuyệt đối trong việc xác định văn bản pháp luật áp dụng.</p>',
    "step3": r'<p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Kỹ thuật "Universal 3-Layer Citation" (Trích dẫn 3 lớp) buộc AI phải cung cấp thông tin theo cấu trúc: Vị trí - Nguyên văn - Từ khóa. Điều này giúp loại bỏ hoàn toàn tình trạng AI "bịa" luật (hallucination). Đồng thời, prompt ép AI phải tìm kiếm các văn bản hướng dẫn (Nghị định, Thông tư sửa đổi) thay vì chỉ dừng lại ở Luật gốc, thể hiện tư duy pháp lý toàn diện của người hành nghề luật.</p>',
    "step4": r'<p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Sử dụng kỹ thuật "Mapping Table" (Bảng đối chiếu) kết hợp "Confidence Metric" (Chỉ số tự tin). Bảng đối chiếu ép AI đưa ra logic suy luận minh bạch: Luật yêu cầu A, Thực tế là B -&gt; Kết luận Khớp/Lệch. Đặc biệt, "Chỉ số tự tin" và yêu cầu chỉ ra "Vấn đề cần chú ý" ép AI phải đánh giá giới hạn lập luận của chính mình, không được kết luận bừa khi chứng cứ yếu, thể hiện sự thận trọng tối đa của nghiệp vụ kiểm sát.</p>',
    "step5a": r'<p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Kỹ thuật "Multi-layer Filtering" (Lọc nhiều lớp) chia bài toán phức tạp thành các mũi nhọn độc lập: Thẩm quyền, Trình tự thời gian và Hình thức tống đạt. Thay vì đánh giá chung chung, prompt cung cấp sẵn các "thước đo" (ví dụ: công thức trừ lùi 20 ngày niêm yết) để AI làm toán và đối chiếu, biến AI thành một cỗ máy soi lỗi quy trình chính xác và không bỏ lọt vi phạm.</p>',
    "step6": r'<p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Áp dụng kỹ thuật "Reverse Thinking" (Tư duy đảo chiều) thông qua mô hình Red Team/Blue Team. Việc buộc AI phải tạm quên vai trò Kiểm sát viên để đóng vai Luật sư đối phương giúp khơi dậy khả năng tranh biện đa chiều của LLM. Nhờ đó, AI có thể tự tìm ra lỗ hổng trong lập luận của mình và chuẩn bị "vũ khí" pháp lý sắc bén nhất để phản bác, chống lại sự chủ quan phiến diện.</p>',
    "step7": r'<p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Sử dụng kỹ thuật "Final Confidence Score" (Định lượng niềm tin cuối cùng) kết hợp tổng hợp logic chuỗi (Chain-of-logic). Kỹ thuật này ngăn AI đưa ra kết luận cảm tính, bắt buộc mọi đề xuất (Chấp nhận/Bác đơn) đều phải là hệ quả tất yếu từ các bằng chứng và lỗi vi phạm đã được chốt ở 6 bước trước đó, đảm bảo tính khách quan và vững chắc của quan điểm giải quyết án.</p>',
}

new_explanations = {
    "step5b": r'<div class="step-explanation"><p><strong>Mục đích: </strong>Kiểm sát việc tuân theo pháp luật tố tụng của Tòa án.</p><p><strong>Hướng dẫn sử dụng: </strong>Hệ thống tự động rà soát thẩm quyền, thời hạn xét xử, tống đạt và đặc biệt là chống bỏ sót tư cách đương sự để đảm bảo bản án không bị hủy.</p><p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Kỹ thuật "Missing Party Scan" (Quét đương sự bị sót) cung cấp cho AI chuỗi câu hỏi tư duy (Chain of thought) sắc bén như: "Ngoài người đứng tên bìa đỏ, trên mảnh đất còn ai không?". Thay vì để AI tự do phân tích, prompt định hướng AI nhìn sâu vào các "điểm mù" tố tụng (vợ chồng, ngân hàng, Chủ tịch xã), giúp phòng ngừa triệt để các vi phạm tố tụng có khả năng dẫn đến hủy án.</p></div>',
    "step6plus": r'<div class="step-explanation"><p><strong>Mục đích: </strong>Tìm kiếm tình huống pháp lý tương tự để đối chiếu.</p><p><strong>Hướng dẫn sử dụng: </strong>Hệ thống rà soát án lệ, quyết định giám đốc thẩm hoặc bản án tương tự để tìm cách giải quyết thống nhất, củng cố quan điểm giải quyết án.</p><p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Áp dụng "Case-based Reasoning" (Lập luận dựa trên tình huống). Prompt buộc AI so sánh tình tiết vụ án hiện tại với vụ án mẫu theo một ma trận tương quan khắt khe, giúp AI đưa ra đề xuất không chỉ dựa trên văn bản luật mà còn bám sát đường lối xét xử của các cấp Tòa án, đảm bảo tính thực tiễn và thuyết phục cao.</p></div>',
    "publish": r'<div class="step-explanation"><p><strong>Mục đích: </strong>Tự động soạn thảo Báo cáo chuyên sâu dựa trên toàn bộ kết quả phân tích.</p><p><strong>Hướng dẫn sử dụng: </strong>Ra lệnh theo 3 phần (Tố tụng, Phân tích, Kết luận) để AI xuất ra dự thảo văn bản hoàn chỉnh dùng cho Kiểm sát viên.</p><p><strong>Tính ưu việt của kỹ thuật Prompt: </strong>Kỹ thuật "Deep Dossier Protocol" (Giao thức báo cáo chuyên sâu) và "Iterative Generation" (Khởi tạo từng phần). Thay vì bắt AI viết một báo cáo dài ngay lập tức dễ sinh ra lỗi "ngắt quãng" (cut-off) hoặc nói chung chung, prompt ép AI viết từng phần riêng biệt thông qua các chốt chặn xác nhận. Điều này đảm bảo AI có đủ không gian tư duy (context window) để đi sâu vào chi tiết, trích xuất đúng các vi phạm đã ghi nhận và tổng hợp lại thành văn bản có chất lượng nghiệp vụ cao nhất.</p></div>'
}

# For sections that already have step-explanation
for section_id, append_txt in explanations_to_append.items():
    # Regex to find <section id="section_id"> ... <div class="step-explanation"> ... </div>
    pattern = r'(<section id="' + section_id + r'">.*?<div class="step-explanation">.*?)(</div>\s*(?:<details|<div class="prompt))'
    
    def repl(m):
        return m.group(1) + append_txt + m.group(2)
        
    html = re.sub(pattern, repl, html, flags=re.DOTALL)

# For sections that DO NOT have step-explanation
for section_id, new_div in new_explanations.items():
    # insert after <div class="step-card">
    pattern = r'(<section id="' + section_id + r'">.*?<div class="step-card">)'
    def repl_new(m):
        return m.group(1) + '\n' + new_div
    html = re.sub(pattern, repl_new, html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Added explanations successfully.")
