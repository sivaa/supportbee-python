# -*- coding: utf-8 -*-
from supportbee import SupportBee
from pprint import pprint

if __name__ == '__main__':
    sb = SupportBee('supportbee-python', 'R8RfBRuKqGctyJeVx9xe')
 
    pprint(sb.archive_ticket('1661336'))
 
 
    

# Show Ticket    
    
#    pprint(sb.show_ticket('1661336'))
    
    
#    Ticket Create
#    data = {
#            "ticket": {
#                        "subject" : "Release on PyPi",
#                        "requester_name": "Siva Arun",
#                        "requester_email": "siva@sivaa.in",
#                            "cc": [
#                                   "Krace <me@kracekumar.com>",
#                                   ],
#                        "content":{
#                          "html":" <h1>Release suportbee-python in PyPi </h1>",
#                                }
#                      }
#            }  
#    
#    pprint(sb.create_ticket(data))





# #    try:
#    pprint(sb.fetch_tickets(starred="false"))
# #    except Exception, e:
# #        print e
# #        print e.__dict__

