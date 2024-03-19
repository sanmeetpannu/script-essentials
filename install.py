import pyfiglet

def print_banner(text):
    banner = pyfiglet.figlet_format(text)
    print(banner)

def main():
    repo_name = "Script Essential"
    dev_name = "Sanmeet Pannu"

    print_banner(repo_name)
    print(f"Developer: {dev_name}")

if __name__ == "__main__":
    main()
