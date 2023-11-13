from django.http import HttpResponse
import paypalrestsdk
from paypalrestsdk import CreditCard


def payment(request):
    paypalrestsdk.configure({
        "mode": "sandbox",  # Cambia a "live" para producción
        "client_id": "AcSvt8ORvhMoD2E2XNUo33-L5BZGj8W5csa7TEZ_x1kSz5E-e_9XMrb3oWYNx7QeN03Sx6LV_8fRjSMp",
        "client_secret": "EPPCASPCg53q6wpwWsejpa7BK55JppwLTpbB0sV_RBQ4zGm2UFyFC3MKyuXGCoj9BaDtqUTM2C2Rt2C8"
    })

    # credit_card = CreditCard({
    #         "type": "visa",
    #         "number": "4024007185826731",
    #         "expire_month": "12",
    #         "expire_year": "2022",
    #         "cvv2": "874",
    #         "first_name": "Joe",
    #         "last_name": "Shopper",
    #     })

    # if credit_card.create():
    #         print("CreditCard[%s] created successfully" % (credit_card.id ))
    #         return HttpResponse('good')
    # else:
    #         print("Error while creating CreditCard:")
    #         print(credit_card.error)