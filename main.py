from Google import Create_Service
from Functions.Search import search_emails
from Functions.Delete import delete_emails
from config import CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES, SEARCH_QUERY

#main
def main():
    # Create Gmail service
    gmail_service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # Search for emails
    email_results = search_emails(gmail_service, SEARCH_QUERY)

    # Delete the emails
    delete_emails(gmail_service, email_results)

if __name__ == "__main__":
    main()
