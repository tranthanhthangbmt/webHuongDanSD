import re
import html as html_lib
import os

txt_path = r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\TaiLieu\instruction v17B_19.8.2026.txt"
with open(txt_path, "r", encoding="utf-8") as f:
    txt = f.read()

def get_section(text, start_marker, end_marker):
    start = text.find(start_marker)
    if start == -1: return ""
    if end_marker:
        end = text.find(end_marker, start)
        if end == -1: return ""
        section = text[start:end].strip()
    else:
        section = text[start:].strip()
    if section.endswith("---"):
        section = section[:-3].strip()
    return section

sections = {}
markers = {
    "prompt-intro": ("# 0. LUẬT VẬN HÀNH BẤT BIẾN", "### 🏛️ BƯỚC 1:"),
    "prompt-step1": ("### 🏛️ BƯỚC 1:", "### 🏛️ BƯỚC 2:"),
    "prompt-step2": ("### 🏛️ BƯỚC 2:", "### 🏛️ BƯỚC 3:"),
    "prompt-step3": ("### 🏛️ BƯỚC 3:", "### 🏛️ BƯỚC 4:"),
    "prompt-step4": ("### 🏛️ BƯỚC 4:", "### 🏛️ BƯỚC 5A:"),
    "prompt-step5a": ("### 🏛️ BƯỚC 5A:", "### 🏛️ BƯỚC 5B:"),
    "prompt-step5b": ("### 🏛️ BƯỚC 5B:", "### 🏛️ BƯỚC 6:"),
    "prompt-step6": ("### 🏛️ BƯỚC 6:", "### 🏛️ BƯỚC 6+:"),
    "prompt-step6plus": ("### 🏛️ BƯỚC 6+:", "### 🏛️ BƯỚC 7:"),
    "prompt-step7": ("### 🏛️ BƯỚC 7:", "### 📠 GIAO THỨC XUẤT BẢN:"),
    "prompt-pub1": ("### 📠 GIAO THỨC XUẤT BẢN:", "**PHẦN 2:"),
    "prompt-pub2": ("**PHẦN 2:", "**PHẦN 3:"),
    "prompt-pub3": ("**PHẦN 3:", "## 4. CÀI ĐẶT GIAO TIẾP"),
    "section4": ("## 4. CÀI ĐẶT GIAO TIẾP", None)
}

for k, (s, e) in markers.items():
    sections[k] = get_section(txt, s, e)

sections["prompt-intro"] += "\n\n---\n\n" + sections["section4"]

html_path = r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

for prompt_id in markers.keys():
    if prompt_id == "section4": continue
    content_encoded = html_lib.escape(sections[prompt_id], quote=False)
    pattern = r'(<div class="prompt-content" id="' + prompt_id + r'">).*?(</div>)'
    def repl(m):
        return m.group(1) + content_encoded + m.group(2)
    html = re.sub(pattern, repl, html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html prompts successfully.")
