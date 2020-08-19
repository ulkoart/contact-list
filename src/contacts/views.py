from rest_framework import generics

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
