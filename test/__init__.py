# -*- coding: utf-8 -*-
from supportbee import SupportBee
from pprint import pprint
from time import sleep

MY_USER_ID = '531274'
SALES_GROUP_ID = '1970'

if __name__ == '__main__':
    sb = SupportBee('supportbee-python', 'R8RfBRuKqGctyJeVx9xe')

    # Delete all the tickets
    print "\n\n Cleaning up the Mailbox \n" + 75 * "="
    [sb.trash_ticket(ticket['id']) for ticket in sb.fetch_tickets()['tickets']]

    # Fetch Tickets
    print "\n\n Current Tickets \n" + 75 * "="
    pprint(sb.fetch_tickets())
    sleep(4)
    
    # Ticket Create
    print "\n\n Creating the First Ticket \n" + 75 * "="
    data = {"ticket": {"subject" : "Ticket 01", "requester_name": "Siva Arun", "requester_email": "siva@sivaa.in", "cc": ["Krace <me@kracekumar.com>",], 
                       "content":{"html":" <h1>Content of Ticket 01 </h1>", }}
            }
    ticket_data = sb.create_ticket(data)
    sample_ticket_id1 = ticket_data['ticket']['id']  
    pprint(ticket_data)
    sleep(4)

    print "\n\n Creating the Second Ticket \n" + 75 * "="
    data = {"ticket": {"subject" : "Ticket 02", "requester_name": "Siva Arun", "requester_email": "siva@sivaa.in", "cc": ["Krace <me@kracekumar.com>",], 
                       "content":{"html":" <h1>Content of Ticket 02 </h1>", }}
            }  
    ticket_data = sb.create_ticket(data)
    sample_ticket_id2 = ticket_data['ticket']['id']  
    pprint(ticket_data)
    sleep(4)

    # Fetch Tickets
    print "\n\n Current Tickets \n" + 75 * "="
    pprint(sb.fetch_tickets())
    sleep(4)

    # Show Ticket    
    print "\n\n Show the First Ticket \n" + 75 * "="
    pprint(sb.show_ticket(sample_ticket_id1))

    # Assign to the User 
    print "\n\n Assign the First Ticket to SIVA \n" + 75 * "="
    data = { "assignment" : { "user_id" : MY_USER_ID } }
    pprint(sb.assign_ticket(sample_ticket_id1, data))
    sleep(10)

    # Assign to the Group
    print "\n\n Assign the Second Ticket to SALES Group \n" + 75 * "="
    data = { "assignment" : {"group_id" : SALES_GROUP_ID} }
    pprint(sb.assign_ticket(sample_ticket_id2, data))
    sleep(10)
    
    # Fetch Replies
    print "\n\n Current Replies \n" + 75 * "="
    pprint(sb.fetch_replies(sample_ticket_id1)) 
    sleep(4)
    
    # Create Reply
    print "\n\n Creating First Reply for First Ticket \n" + 75 * "="
    data =  {"reply":{"content":{ "html":" <u> Demo reply 01 </u>  Do you have the milestone 01?", "attachment_ids":[] } } }
    reply_data = sb.create_reply(sample_ticket_id1, data)
    samply_reply_id1 = reply_data['reply']['id'] 
    pprint(reply_data)
    sleep(10)
    
    print "\n\n Creating Second Reply for First Ticket \n" + 75 * "="
    data =  {"reply":{"content":{ "html":" <u> Demo reply 02 </u>  Do you have the milestone 02?", "attachment_ids":[] } } }
    reply_data = sb.create_reply(sample_ticket_id1, data)
    samply_reply_id2 = reply_data['reply']['id'] 
    pprint(reply_data)
    sleep(4)
    
    # Fetch Replies
    print "\n\n Current Replies \n" + 75 * "="
    pprint(sb.fetch_replies(sample_ticket_id1)) 
    sleep(4)
    
    # Show Replies
    print "\n\n Show the First Reply for First Ticket \n" + 75 * "="
    pprint(sb.show_reply(sample_ticket_id1, samply_reply_id1)) 
    sleep(4)
    
    # Star Ticket
    print "\n\n Action - STAR  the first ticket \n"
    sb.star_ticket(sample_ticket_id1)
    sleep(8)
    
    # UnStar Ticket
    print "\n\n Action - UN-STAR   the first ticket \n" 
    sb.unstar_ticket(sample_ticket_id1)
    sleep(8)

    # Archive Ticket   
    print "\n\n Action - ARCHIVE  the first ticket \n"
    sb.archive_ticket(sample_ticket_id1)
    sleep(8)

    # Un-Archive Ticket    
    print "\n\n Action - UN-ARCHIVE  the first ticket \n" 
    sb.unarchive_ticket(sample_ticket_id1)
    sleep(8)
    
    # Spam Ticket
    print "\n\n Action - SPAM  the first ticket \n" 
    sb.spam_ticket(sample_ticket_id1)
    sleep(8)
    
    # Unspam Ticket
    print "\n\n Action - UN-SPAM the first ticket \n" 
    sb.unspam_ticket(sample_ticket_id1)
    sleep(8)
    
    # Trash Ticket
    print "\n\n Action - TRASH the first ticket \n" 
    sb.trash_ticket(sample_ticket_id1)
    sleep(8)
    
    # Untrash Ticket
    print "\n\n Action - UN-TRASH the first ticket \n" 
    sb.untrash_ticket(sample_ticket_id1)
