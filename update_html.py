import os
from bs4 import BeautifulSoup

html_path = "d:/DongAUniversity/Research/Viện kiểm sát/writing papers/webHuongDanSD/index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

explanations = {
    "intro": {
        "mục_đích": "Cung cấp bộ cấu hình lõi (Luật vận hành) nhằm thiết lập tư duy và nguyên tắc làm việc mặc định cho AI.",
        "hướng_dẫn": "Kích hoạt luật vận hành này đầu tiên để AI tuân thủ nghiêm ngặt quy trình tố tụng, không tự ý bỏ bước hay vi phạm quy chế ngành."
    },
    "step1": {
        "mục_đích": "Trích xuất và xác thực hồ sơ từ người dùng để xây dựng nền tảng dữ liệu ban đầu.",
        "hướng_dẫn": "Cung cấp toàn bộ tài liệu, hồ sơ liên quan đến vụ án để hệ thống tự động phân loại, nhận diện thông tin chung và tài sản tranh chấp."
    },
    "step2": {
        "mục_đích": "Xác định chính xác văn bản luật áp dụng theo triết lý 'Luật tại thời điểm'.",
        "hướng_dẫn": "Hệ thống sẽ dựng trục thời gian các sự kiện pháp lý và chiếu xạ để tìm đúng văn bản pháp luật có hiệu lực tương ứng, ngăn chặn lỗi áp dụng sai luật."
    },
    "step3": {
        "mục_đích": "Rà soát sâu các văn bản quy phạm pháp luật để củng cố cơ sở pháp lý.",
        "hướng_dẫn": "AI sẽ truy xuất các văn bản gốc, văn bản sửa đổi bổ sung và áp dụng tiêu chuẩn trích dẫn 3 lớp (Định vị, nguyên văn, từ khóa) để đảm bảo chứng cứ vững chắc."
    },
    "step4": {
        "mục_đích": "Kiểm tra tính hợp pháp của Quyết định hành chính và Hành vi hành chính.",
        "hướng_dẫn": "Đối chiếu dữ liệu thực tế của hồ sơ với yêu cầu của luật pháp để tự động phát hiện các vi phạm thủ tục hoặc nội dung, và cảnh báo lỗi nghiêm trọng."
    },
    "step5a": {
        "mục_đích": "Kiểm tra và đánh giá quy trình ban hành văn bản của cơ quan hành chính nhà nước.",
        "hướng_dẫn": "Hệ thống sẽ quét thẩm quyền, trình tự, thời hạn và hình thức tổng đạt của Quyết định hành chính, đảm bảo không bỏ sót vi phạm nào từ phía cơ quan quản lý."
    },
    "step5b": {
        "mục_đích": "Giám sát toàn bộ hoạt động tố tụng của Tòa án.",
        "hướng_dẫn": "Tự động kiểm tra thời hiệu khởi kiện, đánh giá thẩm quyền thụ lý và rà soát các rủi ro tố tụng như bỏ sót đương sự để đưa ra cảnh báo kịp thời."
    },
    "step6": {
        "mục_đích": "Giả lập môi trường tranh tụng trước phiên tòa để 'thử lửa' lập luận.",
        "hướng_dẫn": "Đóng vai trò Red Team (Luật sư bảo vệ) và Blue Team (Kiểm sát viên) để mô phỏng màn đối đáp, giúp lường trước và bẻ gãy các lập luận của đối phương."
    },
    "step6plus": {
        "mục_đích": "Tìm kiếm và trích dẫn các bản án, án lệ tương tự đã có hiệu lực pháp luật.",
        "hướng_dẫn": "Tham khảo thực tiễn xét xử để củng cố quan điểm giải quyết vụ án, nâng cao tính thuyết phục và giảm thiểu rủi ro bị hủy án, sửa án."
    },
    "step7": {
        "mục_đích": "Đưa ra kết luận cuối cùng và đề xuất đường lối giải quyết vụ án.",
        "hướng_dẫn": "Hội tụ toàn bộ dữ liệu từ các bước trước đó qua 'ma trận logic' để quyết định Chấp nhận hay Bác đơn khởi kiện, kèm theo kiến nghị khắc phục cụ thể."
    },
    "publish": {
        "mục_đích": "Tổng hợp toàn bộ quá trình phân tích thành một Báo cáo chuyên sâu (Deep Dossier) hoàn chỉnh.",
        "hướng_dẫn": "Xuất bản báo cáo chuẩn mực, đáp ứng đầy đủ cấu trúc nghiệp vụ của ngành Kiểm sát, sẵn sàng để in ấn và trình lãnh đạo phê duyệt."
    }
}

for section_id, info in explanations.items():
    section = soup.find("section", id=section_id)
    if not section:
        continue
    
    # 1. Thêm phần giải thích chuyên nghiệp
    step_desc = section.find("div", class_="step-desc")
    
    # Kiểm tra xem đã có step-explanation chưa
    if not section.find("div", class_="step-explanation"):
        explanation_div = soup.new_tag("div", **{"class": "step-explanation"})
        
        p1 = soup.new_tag("p")
        strong1 = soup.new_tag("strong")
        strong1.string = "Mục đích: "
        p1.append(strong1)
        p1.append(info["mục_đích"])
        
        p2 = soup.new_tag("p")
        strong2 = soup.new_tag("strong")
        strong2.string = "Hướng dẫn sử dụng: "
        p2.append(strong2)
        p2.append(info["hướng_dẫn"])
        
        explanation_div.append(p1)
        explanation_div.append(p2)
        
        if step_desc:
            step_desc.insert_after(explanation_div)

    # 2. Bọc các h3 và prompt-container vào trong thẻ <details>
    h3_tags = section.find_all("h3")
    prompt_containers = section.find_all("div", class_="prompt-container")
    
    # Gom tất cả các phần prompt vào một thẻ details
    if h3_tags and prompt_containers and not section.find("details", class_="prompt-details"):
        details = soup.new_tag("details", **{"class": "prompt-details"})
        summary = soup.new_tag("summary")
        summary.string = "Hiển thị Instruction Prompt (Dành cho trường hợp AI quên lệnh)"
        details.append(summary)
        
        # Đưa các thẻ h3 và prompt_container vào trong details
        elements_to_wrap = []
        for h3 in h3_tags:
            elements_to_wrap.append(h3)
        for pc in prompt_containers:
            elements_to_wrap.append(pc)
            
        # Tìm vị trí chèn details (ngay trước thẻ h3 đầu tiên)
        first_h3 = h3_tags[0]
        first_h3.insert_before(details)
        
        # Di chuyển nội dung
        for el in elements_to_wrap:
            el.extract()
            details.append(el)

# Lưu lại file
with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
    
print("Updated HTML successfully.")
