import re
with open(r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\index.html", "r", encoding="utf-8") as f:
    text = f.read()
matches = re.finditer(r'<div class="step-explanation">(.*?)</div>', text, flags=re.DOTALL)
for i, m in enumerate(matches):
    print(f"Match {i}:")
    print(m.group(0))
    print("-" * 50)
