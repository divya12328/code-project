#Yes, by default Django signals run within the same database transaction as the caller if the signal is sent within a transaction context.
from django.db import transaction
from myapp.models import Book, Log

try:
    with transaction.atomic():
        Book.objects.create(title="Signal Test Book")
        raise Exception("Force rollback")
except:
    pass

# Check what's in the DB
print("Books:", Book.objects.all())  # Should be empty
print("Logs:", Log.objects.all())    # Should also be empty if signal is in same transaction

