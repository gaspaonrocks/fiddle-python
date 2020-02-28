import os

# Set environment variables
os.environ['TWILIO_ACCOUNT_SID']='' # paste in Account SID between single quotes
os.environ['TWILIO_AUTH_TOKEN']='' # paste Auth Token between single quotes

from twilio.rest import Client
from weather_api import City

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()
city = City()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+33695023395'

body_message={
    "sid": "SM17045489d57249ff89e38963b01d799d",
    "date_created": "Tue, 25 Feb 2020 14:24:05 +0000",
    "date_updated": "Tue, 25 Feb 2020 14:24:05 +0000",
    "date_sent": None,
    "account_sid": "ACd63720e657f95caa65c7df90dd28d49a",
    "to": "whatsapp:+33695023395",
    "from": "whatsapp:+14155238886",
    "messaging_service_sid": None,
    "body": "Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/",
    "status": "queued",
    "num_segments": "1",
    "num_media": "0",
    "direction": "outbound-api",
    "api_version": "2010-04-01",
    "price": None,
    "price_unit": None,
    "error_code": None,
    "error_message": None,
    "uri": "/2010-04-01/Accounts/ACd63720e657f95caa65c7df90dd28d49a/Messages/SM17045489d57249ff89e38963b01d799d.json",
    "subresource_uris": {
        "media": "/2010-04-01/Accounts/ACd63720e657f95caa65c7df90dd28d49a/Messages/SM17045489d57249ff89e38963b01d799d/Media.json"
    }
}

weather=city.getWeatherData()
forecast=city.getWeatherForecast()

client.messages.create(body=forecast,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)