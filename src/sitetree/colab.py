from .core import generate_pdf

def run():
    from google.colab import files  # فقط در Colab

    print("📤 Please upload your Excel file (.xlsx)...")
    uploaded = files.upload()
    if not uploaded:
        raise SystemExit("No file uploaded.")

    excel_path = list(uploaded.keys())[0]
    output_pdf = "site_tree.pdf"

    generate_pdf(excel_path, output_pdf, show=False)
    files.download(output_pdf)

    print(f"✅ Done: {output_pdf}")
