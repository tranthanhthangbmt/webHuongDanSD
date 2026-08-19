import re
with open(r"d:\DongAUniversity\Research\Viện kiểm sát\writing papers\webHuongDanSD\index.html", "r", encoding="utf-8") as f:
    text = f.read()

print("Checking 5B:")
match_5b = re.search(r'<section id="step5b">.*?</section>', text, flags=re.DOTALL)
if match_5b: print("Found 5B")
else: print("5B not found")

print("Checking 6+:")
match_6p = re.search(r'<section id="step6plus">.*?</section>', text, flags=re.DOTALL)
if match_6p: print("Found 6+")
else: print("6+ not found")

print("Checking 8:")
match_8 = re.search(r'<section id="publish">.*?</section>', text, flags=re.DOTALL)
if match_8: print("Found 8")
else: print("8 not found")
