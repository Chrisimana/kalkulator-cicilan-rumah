import sys
import os

# Tambahkan path ke sys.path agar modules dapat diimport
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from gui_app import CicilanRumahApp

def main():
    """Fungsi utama untuk menjalankan aplikasi"""
    try:
        print("🚀 Menjalankan Kalkulator Cicilan Rumah...")
        print("📁 Memuat database...")
        print("🎨 Menyiapkan interface...")
        
        app = CicilanRumahApp()
        print("✅ Aplikasi siap!")
        app.run()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Tekan Enter untuk keluar...")

if __name__ == "__main__":
    main()