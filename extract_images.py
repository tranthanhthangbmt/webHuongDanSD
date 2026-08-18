import fitz
import os

pdf_path = "TaiLieu/Báo cáo_12.2.2026_v3.pdf"
output_dir = "assets/images"

os.makedirs(output_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    img_count = 0
    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        
        if image_list:
            print(f"Found {len(image_list)} images on page {page_index}")
        
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            img_count += 1
            image_filename = os.path.join(output_dir, f"page_{page_index+1}_img_{image_index}.{image_ext}")
            with open(image_filename, "wb") as f:
                f.write(image_bytes)
            print(f"Saved: {image_filename}")

    print(f"Total extracted images: {img_count}")
except Exception as e:
    print(f"Error: {e}")
