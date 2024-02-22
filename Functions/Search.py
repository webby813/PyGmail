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

def search_emails_with_keywords(gmail_service, keywords, labels=None):
    next_page_token = None
    email_messages = []

    # Construct the query string to search for emails containing any of the specified keywords
    query = ' OR '.join(f'"{keyword}"' for keyword in keywords)

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
