from Google import Create_Service
from Functions.Search import search_emails, search_emails_with_keywords
from Functions.Delete import delete_emails, clean_trash_emails
from config import CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES

def Options(gmail_service, option):
    if option == '1':
        keywords = input("Enter keywords: ")
        email_results = search_emails_with_keywords(gmail_service, keywords)
        print(email_results)
        # Do something with email_results if needed

    elif option == '2':
        sender_email = input("Enter sender email: ")
        SEARCH_QUERY = "from:" + sender_email
        email_results = search_emails(gmail_service, SEARCH_QUERY)
        delete_emails(gmail_service, email_results)

    elif option == '3':
        clean_trash_emails(gmail_service)
        print("Trash cleaned successfully.")

    elif option == '4':
        return False  # Indicate to shut down the program

    else:
        print("Invalid option")
    return True  # Continue running the program

def main():
    gmail_service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    print("Select one to continue")
    while True:
        option = input("1. Fetch emails\n"
                       "2. Delete emails from a sender\n"
                       "3. Clean trash\n"  # Changed option label
                       "4. Shut down program\n")  # Changed option label
        if not Options(gmail_service, option):
            break  # Exit the loop and shut down the program

if __name__ == "__main__":
    main()
