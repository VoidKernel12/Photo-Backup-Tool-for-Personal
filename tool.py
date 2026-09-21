import base64
import getpass
import os
import zipfile

# Try importing pyfiglet for pro terminal banner, with fallback
try:
  import pyfiglet

  HAS_FIGLET = True
except ImportError:
  HAS_FIGLET = False

# Classic & Stylish Termux ANSI Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_ultra_banner():
  os.system("clear" if os.name == "posix" else "cls")
  banner_text = "FILE VAULT"
  if HAS_FIGLET:
    banner = pyfiglet.figlet_format(banner_text, font="slant")
    print(f"{CYAN}{BOLD}{banner}{RESET}")
    print(
        f"{MAGENTA}{BOLD}  [{RED}~{MAGENTA}] TOOL: SECURE FILE STREAM VAULT{RESET}"
    )
    print(f"{MAGENTA}{BOLD}  [{RED}~{MAGENTA}] POWERED BY GEMINI AI{RESET}\n")
  else:
    print(
        f"{RED}{BOLD}======================================================{RESET}"
    )
    print(f"{CYAN}{BOLD}            SECURE FILE STREAM VAULT            {RESET}")
    print(
        f"{RED}{BOLD}======================================================{RESET}"
    )


def get_download_folder():
  sdcard_path = "/storage/emulated/0/Download"
  if os.path.exists(sdcard_path):
    return sdcard_path
  else:
    os.makedirs("downloads", exist_ok=True)
    return "downloads"


def compress_folder_process(mode_name):
  download_dir = get_download_folder()

  try:
    items = os.listdir(download_dir)
    print(f"\n{GREEN}📋 Available Folders in Download:{RESET}")
    for item in items:
      item_path = os.path.join(download_dir, item)
      if os.path.isdir(item_path):
        print(f"  📁 {item}")
  except Exception as e:
    print(f"{RED}❌ Error reading directory: {e}{RESET}")
    return

  folder_name = input(
      f"\n{YELLOW}📌 Enter the exact folder name to pack ({mode_name}):{RESET} "
  ).strip()
  folder_path = os.path.join(download_dir, folder_name)

  if not os.path.isdir(folder_path):
    print(f"{RED}❌ Error: Folder '{folder_name}' not found!{RESET}")
    return

  custom_name = input(
      f"{GREEN}📌 Enter a safe custom name for your data file (e.g.,"
      f" vault_pack):{RESET} "
  ).strip()
  if not custom_name:
    custom_name = "data_vault_pack"

  if not custom_name.endswith(".txt"):
    custom_name += ".txt"

  try:
    print(
        f"{YELLOW}⏳ Processing folder contents securely under"
        f" {mode_name}...{RESET}"
    )

    temp_zip_path = os.path.join(download_dir, f"temp_{folder_name}.zip")

    with zipfile.ZipFile(temp_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
      for root, dirs, files in os.walk(folder_path):
        for file in files:
          file_path = os.path.join(root, file)
          arcname = os.path.relpath(file_path, folder_path)
          zipf.write(file_path, arcname)

    with open(temp_zip_path, "rb") as f:
      encoded_string = base64.b64encode(f.read()).decode("utf-8")

    if os.path.exists(temp_zip_path):
      os.remove(temp_zip_path)

    output_code_path = os.path.join(download_dir, custom_name)
    with open(output_code_path, "w", encoding="utf-8") as code_file:
      code_file.write(encoded_string)

    print(f"\n{GREEN}🎉 SUCCESS! Secure data file generated.{RESET}")
    print(
        f"{GREEN}📁 Saved as:{RESET} {CYAN}{custom_name}{RESET} in Download"
        f" folder."
    )

  except Exception as e:
    print(f"{RED}❌ Error during compression: {e}{RESET}")


def free_option():
  print(f"\n{CYAN}=== 🆓 FREE OPTION (Standard Data Pack) ==={RESET}")
  compress_folder_process("Free Mode")


def vip_option():
  print(f"\n{CYAN}=== 🌟 VIP OPTION (Tier-1 Speed) 🌟 ==={RESET}")
  password = getpass.getpass(f"{YELLOW}🔑 Enter VIP Password:{RESET} ").strip()

  try:
    if (int(password) * 2) + 100 == 1200:
      print(f"{GREEN}✅ Password Verified! Entering VIP Mode...{RESET}")
      compress_folder_process("VIP Mode")
    else:
      print(f"{RED}❌ Incorrect Password! Access Denied.{RESET}")
  except ValueError:
    print(f"{RED}❌ Invalid Format! Access Denied.{RESET}")


def ultra_vip_option():
  print(f"\n{CYAN}=== ⚡ ULTRA VIP OPTION (Tier-2 Max Speed) ⚡ ==={RESET}")
  password = getpass.getpass(f"{YELLOW}🔑 Enter Ultra VIP Password:{RESET} ").strip()

  try:
    if (int(password) * 3) - 702 == 3000:
      print(f"{GREEN}✅ Password Verified! Entering Ultra VIP Mode...{RESET}")
      compress_folder_process("Ultra VIP Mode")
    else:
      print(f"{RED}❌ Incorrect Password! Access Denied.{RESET}")
  except ValueError:
    print(f"{RED}❌ Invalid Format! Access Denied.{RESET}")


def restore_files_option():
  print(f"\n{CYAN}=== 📥 RESTORE FILES (Auto-Detect & Extract) ==={RESET}")
  download_dir = get_download_folder()

  print(f"{YELLOW}🔍 Scanning Download folder for data packs...{RESET}")
  try:
    files = [f for f in os.listdir(download_dir) if f.endswith(".txt")]
    if not files:
      print(f"{RED}❌ No data pack files found in Download folder!{RESET}")
      return

    print(f"{GREEN}📋 Available Data Packs:{RESET}")
    for idx, file in enumerate(files, 1):
      print(f"  📄 {idx}. {file}")

  except Exception as e:
    print(f"{RED}❌ Error scanning files: {e}{RESET}")
    return

  user_input = input(
      f"\n{YELLOW}📌 Enter the data pack file name from above list:{RESET} "
  ).strip()
  possible_file_path = os.path.join(download_dir, user_input)

  if not os.path.exists(possible_file_path):
    print(f"{RED}❌ Error: File not found!{RESET}")
    return

  try:
    print(f"{YELLOW}⏳ Reading data pack file...{RESET}")
    with open(possible_file_path, "r", encoding="utf-8") as f:
      encoded_data = f.read().strip()

    target_folder_name = input(
        f"{GREEN}📌 Enter name for restored folder (e.g., Restored_Data):{RESET}"
        " "
    ).strip()
    if not target_folder_name:
      target_folder_name = "Restored_Files"

    recovered_folder = os.path.join(download_dir, target_folder_name)
    os.makedirs(recovered_folder, exist_ok=True)

    print(
        f"{YELLOW}⏳ Restoring exact folder contents instantly into"
        f" '{target_folder_name}'...{RESET}"
    )
    zip_bytes = base64.b64decode(encoded_data)

    temp_recovered_zip = os.path.join(download_dir, "temp_recovered_vault.zip")
    with open(temp_recovered_zip, "wb") as f:
      f.write(zip_bytes)

    with zipfile.ZipFile(temp_recovered_zip, "r") as zip_ref:
      zip_ref.extractall(recovered_folder)

    if os.path.exists(temp_recovered_zip):
      os.remove(temp_recovered_zip)

    print(
        f"\n{GREEN}🎉 SUCCESS! All folder contents successfully restored!{RESET}"
    )
    print(f"{CYAN}📁 Saved inside folder: {recovered_folder}{RESET}")

  except Exception as e:
    print(f"{RED}❌ Error during recovery: {e}{RESET}")


def main():
  while True:
    print_ultra_banner()
    print(f"{CYAN}------------------------------------------------------{RESET}")
    print(f"{GREEN}1. Free Option (Standard Data Pack){RESET}")
    print(f"{GREEN}2. VIP Option (Tier-1 Speed) [Hidden Pass]{RESET}")
    print(f"{GREEN}3. Ultra VIP Option (Tier-2 Max Speed) [Hidden Pass]{RESET}")
    print(f"{GREEN}4. Restore Files (Extract Data Pack){RESET}")
    print(f"{RED}5. Exit{RESET}")

    choice = input(f"\n{YELLOW}👉 Select an option (1-5):{RESET} ").strip()

    if choice == "1":
      free_option()
      input(f"\n{YELLOW}👉 Press [ENTER] to return to main menu...{RESET}")
    elif choice == "2":
      vip_option()
      input(f"\n{YELLOW}👉 Press [ENTER] to return to main menu...{RESET}")
    elif choice == "3":
      ultra_vip_option()
      input(f"\n{YELLOW}👉 Press [ENTER] to return to main menu...{RESET}")
    elif choice == "4":
      restore_files_option()
      input(f"\n{YELLOW}👉 Press [ENTER] to return to main menu...{RESET}")
    elif choice == "5":
      print(f"{CYAN}👋 Exiting tool. Powered by Gemini AI. Goodbye!{RESET}")
      break
    else:
      print(f"{RED}❌ Invalid option! Please choose between 1-5.{RESET}")
      input(f"\n{YELLOW}👉 Press [ENTER] to continue...{RESET}")


if __name__ == "__main__":
  main()
