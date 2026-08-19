import re
with open(r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\index.html", "r", encoding="utf-8") as f:
    text = f.read()

for sid in ["step5a", "step5b", "step6", "step6plus", "step7", "publish"]:
    match = re.search(f'<section id="{sid}">.*?</section>', text, flags=re.DOTALL)
    if match:
        has_expl = '<div class="step-explanation">' in match.group(0)
        print(f"{sid}: Has explanation? {has_expl}")
