def search_emails(gmail_service, query, labels=None):
    next_page_token = None
    email_messages = []

    while True:
        message_response = gmail_service.users().messages().list(
            userId='me',
            labelIds=labels,
            q=query,
            maxResults=500,
            pageToken=next_page_token
        ).execute()
        messages = message_response.get('messages', [])
        email_messages.extend(messages)

        next_page_token = message_response.get('nextPageToken')
        if not next_page_token:
            break

    return email_messages