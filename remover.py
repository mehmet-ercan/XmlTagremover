import xml.etree.ElementTree as ET
import glob
import os

folder_path = "./xmlfilespath"

# Tutulacak tag isimleri
keep_tags = {"GUID", "ID"}

# Klasördeki tüm .xml dosyalarını bul
for file_path in glob.glob(os.path.join(folder_path, "*.xml")):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # düğümünü bul
        patient_info = root.find("PatientInfo")
        if patient_info is None:
            print(f"⚠ PatientInfo bulunamadı: {file_path}")
            continue

        # Silinecek tagler
        to_remove = [child for child in patient_info if child.tag not in keep_tags]

        for child in to_remove:
            patient_info.remove(child)

        # (orijinal file name + _utf8.xml)
        base, ext = os.path.splitext(file_path)
        new_file_path = f"{base}_utf8{ext}"

        tree.write(new_file_path, encoding="utf-8", xml_declaration=True)
        print(f"✅ Kaydedildi: {new_file_path}")

    except Exception as e:
        print(f"❌ Hata: {file_path} -> {e}")
