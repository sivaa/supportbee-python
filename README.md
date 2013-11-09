supportbee-python
=================
Python Library for SupportBee APIs

- Install

`pip install https://github.com/sivaa/supportbee-python/archive/master.zip`

- Quick Start

```

	from supportbee import SupportBee
	sb = SupportBee("<ACCOUNT NAME>", "<AUTH_TOKEN>")

    # Fetch Tickets
    sb.fetch_tickets()
        
    # Ticket Create
    data = {"ticket": {"subject" : "Ticket 01", "requester_name": "Siva Arun", "requester_email": "siva@sivaa.in", "cc": ["Krace <me@kracekumar.com>",], 
                       "content":{"html":" <h1>Content of Ticket 01 </h1>", }}
            }
    ticket_data = sb.create_ticket(data)
    sample_ticket_id1 = ticket_data['ticket']['id']  

    data = {"ticket": {"subject" : "Ticket 02", "requester_name": "Siva Arun", "requester_email": "siva@sivaa.in", "cc": ["Krace <me@kracekumar.com>",], 
                       "content":{"html":" <h1>Content of Ticket 02 </h1>", }}
            }  
    ticket_data = sb.create_ticket(data)
    sample_ticket_id2 = ticket_data['ticket']['id']  
    
    # Fetch Tickets
    sb.fetch_tickets()

    # Show a Ticket    
    sb.show_ticket(sample_ticket_id1)

    # Assign to the User 
    data = { "assignment" : { "user_id" : <USER_ID> } }
    sb.assign_ticket(sample_ticket_id1, data)

    # Assign to the Group
    data = { "assignment" : {"group_id" : <GROUP_ID>} }
    sb.assign_ticket(sample_ticket_id2, data)
    
    # Fetch Replies
    sb.fetch_replies(sample_ticket_id1)
    
    # Create Reply
    data =  {"reply":{"content":{ "html":" <u> Demo reply 01 </u>  Do you have the milestone 01?", "attachment_ids":[] } } }
    reply_data = sb.create_reply(sample_ticket_id1, data)
    samply_reply_id1 = reply_data['reply']['id'] 
    
    data =  {"reply":{"content":{ "html":" <u> Demo reply 02 </u>  Do you have the milestone 02?", "attachment_ids":[] } } }
    reply_data = sb.create_reply(sample_ticket_id1, data)
    samply_reply_id2 = reply_data['reply']['id'] 
    
    # Fetch Replies
    sb.fetch_replies(sample_ticket_id1)
    
    # Show A  Reply
    sb.show_reply(sample_ticket_id1, samply_reply_id1)
    
    # Star Ticket
    sb.star_ticket(sample_ticket_id1)
    
    # UnStar Ticket
    sb.unstar_ticket(sample_ticket_id1)

    # Archive Ticket   
    sb.archive_ticket(sample_ticket_id1)

    # Un-Archive Ticket    
    sb.unarchive_ticket(sample_ticket_id1)
    
    # Spam Ticket
    sb.spam_ticket(sample_ticket_id1)
    
    # Unspam Ticket
    sb.unspam_ticket(sample_ticket_id1)
    
    # Trash Ticket
    sb.trash_ticket(sample_ticket_id1)
    
    # Untrash Ticket
    sb.untrash_ticket(sample_ticket_id1)
	
```

# TODO
* Release on PyPi
* Add tests
* Implement remaining APIs (User/Agent/Group, Label, Attachment, Snippet, Webhooks & Reports)