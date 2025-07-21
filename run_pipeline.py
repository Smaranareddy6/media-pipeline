import os
from pathlib import Path
from orchestrator.main import process

# Resolve base directory where the script is located
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "inputs"
OUTPUT_DIR = BASE_DIR / "outputs"

def run_all_inputs():
    files = os.listdir(INPUT_DIR)
    print("\n📂 Scanning 'inputs/' folder...\n")

    for filename in files:
        input_path = INPUT_DIR / filename
        print(f"▶️  Processing: {filename}")

        try:
            process(str(input_path))
        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

    print("\n✅ All inputs processed.")
    print("📄 Check the 'outputs/' folder for results.\n")

if __name__ == "__main__":
    run_all_inputs()
