from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from api.models import datos
from api.models import inicio_sesion
from django.db.models import Count
from django.db.models import Sum
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
import paypalrestsdk
def success(request):
    # Aquí puedes realizar acciones adicionales después de una transacción exitosa
    return render(request, 'success.html')  # Puedes crear una plantilla "success.html" con un mensaje de éxito

def cancel(request):
    # Aquí puedes realizar acciones adicionales cuando el usuario cancela la transacción
    return render(request, 'cancel.html')  # Puedes crear una plantilla "cancel.html" con un mensaje de cancelación

# Create your views here.
class Home(APIView):
    template_name="SIGN UP & SIGN IN PAGE.html"
    def get(self, request):
        return render(request, self.template_name)
class Carrito(APIView):
    template_name="book.html"
    def get(self, request):
        return render(request, self.template_name)
class pay(APIView):
    template_name="book copy.html"
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        return render(request, self.template_name)
    
class inicio(APIView):
    template_nam="index.html"
    def get(self, request):
        return render(request, self.template_nam)
    def post(self, request):
        return render(request, self.template_nam)
        
class Catalogo(APIView):
    template_nam="menu.html"
    def get(self, request):
        return render(request, self.template_nam)
    def post(self, request):
        return render(request, self.template_nam)
class Nosotros(APIView):
    template_nam="about.html"
    def get(self, request):
        return render(request, self.template_nam)
    
class Dashboard(APIView):
    template_nam="dashboard.html"
    def get(self, request):
        # Obtén todos los objetos de TuModelo
        objetos = datos.objects.all()
        print(objetos)
        # Pasa los objetos a la plantilla como contexto
        conteo_por_edad = datos.objects.values('edad').annotate(count=Count('edad'))
        conteo_por_api = datos.objects.values('p1').annotate(count=Count('p1'))
        conteo_por_pago = datos.objects.values('p4').annotate(count=Count('p4'))
        conteo_datos = datos.objects.values_list('idUser', flat=True).order_by('-idUser').first()
        dato_mas_comun = datos.objects.values('p7').annotate(count=Count('p7')).order_by('-count').first()
        hora_comun = datos.objects.values('p5').annotate(count=Count('p5')).order_by('-count').first()
        pasos_comun = datos.objects.values('p3').annotate(count=Count('p3'))
        print(conteo_datos)
        print(conteo_por_api)
        context = {
            'objetos': objetos,
            'conteo_por_edad': conteo_por_edad,
            'conteo_por_api': conteo_por_api,
            'conteo_por_pago': conteo_por_pago,
            'conteo_datos' : conteo_datos,
            'dato_mas_comun' : dato_mas_comun,
            'hora_comun' : hora_comun,
            'pasos_comun' : pasos_comun
            
        }
        
        # Renderiza la plantilla con el contexto
        return render(request, self.template_nam, context)
   
def formulario(request):
    if request.method=='POST':
        nombre=request.POST['nombreUsuario']
        email=request.POST['correo']
        pswd=request.POST['passw'] 
        inicio_sesion(username=nombre,name=email,passw=pswd).save()
        messages.success(request,'USUARIO REGISTRADO')
        return render(request,'SIGN UP & SIGN IN PAGE.html')
    else:
        return render(request,'SIGN UP & SIGN IN PAGE.html')
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Utiliza get() para evitar KeyError
        password = request.POST.get('password')

        try:
            if email == ('admin@gmail.com'):
                return redirect('dashboard')  # Redirige a una vista llamada 'index'
            user = inicio_sesion.objects.get(name=email, passw=password)
            request.session['name'] = user.name
            return redirect('index1')  # Redirige a una vista llamada 'index'
        except inicio_sesion.DoesNotExist:
            messages.error(request, '')
        except inicio_sesion.MultipleObjectsReturned:
            messages.error(request, 'No se puede acceder')
        
    return render(request,'SIGN UP & SIGN IN PAGE.html')

def index(request):
    nombre_usuario = request.session.get('name', None)
    return render(request, 'index.html', {'nombre_usuario': nombre_usuario})


from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
def formulario_verificacion(request):
    if request.method == 'POST':
        nombre = request.POST['nombreUsuario']
        email = request.POST['correo']
        pswd = request.POST['passw'] 

        try:
            # Verificar si el correo ya existe en la base de datos
            if inicio_sesion.objects.filter(name=email).exists():
                raise ValidationError("Este correo electrónico ya está registrado.")

            # Guardar el usuario en la base de datos
            usuario = inicio_sesion(username=nombre, name=email, passw=pswd)
            usuario.full_clean()  # Esto verifica las restricciones del modelo
            usuario.save()

            # Enviar correo de verificación
            subject = 'Verificación de registro!'
            message = f'¡Gracias por registrarte en nuestro sitio! Los datos de tu cuenta son Nombre de usuario {email} y tu contraseña es {pswd}{get_random_string()}'
            from_email = 'marco.vallejo2000@gmail.com'  # Debe ser una dirección de correo configurada en tu servidor de correo

            send_mail(subject, message, from_email, [email])

            messages.success(request, 'USUARIO REGISTRADO. Por favor, verifica tu correo.')
            return render(request, 'SIGN UP & SIGN IN PAGE.html')

        except ValidationError as e:
            messages.error(request, str(e))
            return render(request, 'SIGN UP & SIGN IN PAGE.html')

    else:
        return render(request, 'SIGN UP & SIGN IN PAGE.html')
    

@csrf_exempt
# def create_payment(request):
#     paypal_config.payment({
#         "intent": "sale",
#         "payer": {
#             "payment_method": "paypal"
#         },
#         "redirect_urls": {
#             "return_url": "http://127.0.0.1:8000/success/",
#             "cancel_url": "http://127.0.0.1:8000/cancel/"
#         },
#         "transactions": [{
#             "item_list": {
#                 "items": [{
#                     "name": "Item de prueba",
#                     "sku": "item",
#                     "price": "10.00",
#                     "currency": "USD",
#                     "quantity": 1
#                 }]
#             },
#             "amount": {
#                 "total": "10.00",
#                 "currency": "USD"
#             },
#             "description": "Compra de prueba"
#         }]
#     })
  
#     if Payment.create(request):
#         for link in Payment.links:
#             if link.method == "REDIRECT":
#                 redirect_url = link.href
#                 return HttpResponseRedirect(redirect_url)
#     else:  
#         print(Payment.error)


#     return render(request, 'payment.html')


def create_payment(request):
    paypalrestsdk.configure({
        "mode": "sandbox",  # sandbox or live
        'client_id': "AcSvt8ORvhMoD2E2XNUo33-L5BZGj8W5csa7TEZ_x1kSz5E-e_9XMrb3oWYNx7QeN03Sx6LV_8fRjSMp",  # Reemplaza con tu ID de cliente de PayPal
        'client_secret': "EPPCASPCg53q6wpwWsejpa7BK55JppwLTpbB0sV_RBQ4zGm2UFyFC3MKyuXGCoj9BaDtqUTM2C2Rt2C8",  # Reemplaza con tu secreto de cliente de PayPal
    })

    payment = paypalrestsdk.configure({
        "intent": "sale",
        "payer": {
            "payment_method": "credit_card",
            "funding_instruments": [
                {
                    "credit_card": {
                        "number": "4111111111111111",  # Número de tarjeta de prueba
                        "type": "visa",
                        "expire_month": 12,
                        "expire_year": 2022,
                        "cvv2": "123",
                        "first_name": "John",
                        "last_name": "Doe"
                    }
                }
            ]
        },
        "transactions": [
            {
                "amount": {
                    "total": "6.70",
                    "currency": "USD"
                },
                "description": "Payment by credit card."
            }
        ]
    })

    if payment.create():
        print(payment.id)
        print("Payment created successfully")
    else:
        print(payment.error)
from django.shortcuts import render

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

def CheckOut(request):

    

    host = request.get_host()
    total = request.session.get('total', 0)
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(total),
        'item_name': 'Salsa Macha',
        'invoice': uuid.uuid4(),
        'currency_code': 'MXN',
        'return_url': "http://127.0.0.1:8000/payment/",
        'return_url': "http://127.0.0.1:8000/success/",
        'cancel_url': "http://127.0.0.1:8000/cancel/"
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'product': '1',
        'paypal': paypal_payment
    }

    return render(request,'payment.html', context)

