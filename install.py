import pyfiglet
from colorama import Fore, Style
import subprocess

def print_banner(text):
    banner = pyfiglet.figlet_format(text)
    print(banner)

def get_android_version():
    print("Choose Android version:")
    print(f"{Fore.BLUE}1. Android 13{Style.RESET_ALL}")
    print(f"{Fore.GREEN}2. Android 14{Style.RESET_ALL}")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        return "Android 13"
    elif choice == "2":
        return "Android 14"
    else:
        print("Invalid choice. Please select again.")
        return get_android_version()

def main():
    print_banner("Script Essential")
    print("Developer:", Fore.RED + "Sanmeet Pannu" + Style.RESET_ALL)
    
    android_version = get_android_version()
    
    print("Selected Android version:", Fore.YELLOW + android_version + Style.RESET_ALL)
    
    if android_version == "Android 13" or android_version == "Android 14":
        print("Additional options:")
        print(f"{Fore.CYAN}1. KSWeb{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}2. HTTPCanary{Style.RESET_ALL}")
        # Add more options here if needed
        
        option = input("Enter your choice (1/2): ")
        if option == "1":
            install_ksweb_apk()
        elif option == "2":
            # Handle HTTPCanary opt ion
            pass
        else:
            print("Invalid option.")
 
def install_ksweb_apk():
    apk_path = "apks/ksweb.apk" 
    try:
        subprocess.run(["adb", "install", apk_path], check=True)
        print("KSWeb APK installed successfully!")
    except subprocess.CalledProcessError:
        print("Failed to install KSWeb APK.")

if __name__ == "__main__":
    main()
