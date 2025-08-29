from django.db import models
# Create your models here.
import uuid
from django.core.mail import send_mail
from django.conf import settings

class Package(models.Model):
    
    STATUS_CHOICES =[
        ('processing', 'Processing'),
        ('shipped','Shipped'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery','Out for delivery'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled')
        
    ]
    
    
    sender_name=models.CharField(max_length=100)
    reciever_name=models.CharField(max_length=100)
    reciever_email=models.EmailField()
    location=models.CharField(max_length=50, default='unknown2')
    tracking_id=models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES, default='processing')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.tracking_id} - {self.reciever_name} - {self.status}'
    
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None  # check if package is new
        super().save(*args, **kwargs)

        # Send email only for new packages
        if is_new:
            subject = f"Your Package Tracking ID: {self.tracking_id}"
            message = f"""
            Hello {self.reciever_name},

           Your package has been created successfully.

           Tracking ID: {self.tracking_id}
           Status: {self.get_status_display()}

           Thank you for choosing our service.
           """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,  # from email, will use DEFAULT_FROM_EMAIL
                [self.reciever_email],
                fail_silently=False,
            )


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message=models.TextField(max_length=300)
    
    def __str__(self):
        return self.email