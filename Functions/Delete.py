def delete_emails(gmail_service, email_results):
    total_emails = len(email_results)
    print(f"Total emails found: {total_emails}")

    if total_emails == 0:
        print("No emails found to delete.")
        return

    confirm = input("Do you want to delete these emails? (yes/no): ").lower()
    if confirm == "yes":
        for index, email_result in enumerate(email_results, start=1):
            print(f"Deleting email {index} of {total_emails}...")
            gmail_service.users().messages().trash(
                userId='me',
                id=email_result['id']
            ).execute()
        print("Emails deleted successfully.")
    else:
        print("Deletion action cancelled.")