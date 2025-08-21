from django.core.signals import request_finished
from django.dispatch import receiver
import time
#By default, Django signals are executed synchronously. This means when a signal is sent, the connected receivers are called one-by-one in the same thread before the sending function continues.


@receiver(request_finished)
def signal_handler(sender, **kwargs):
    print("Signal start")
    time.sleep(2)  # simulate slow processing
    print("Signal end")

print("Before sending signal")
request_finished.send(sender=None)
print("After sending signal")
#This shows the sender blocks until the signal handler finishes, proving synchronous execution.