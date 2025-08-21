#Yes, by default Django signals run in the same thread as the caller.
import threading
from django.core.signals import request_finished
from django.dispatch import receiver

main_thread = threading.current_thread()

@receiver(request_finished)
def signal_handler(sender, **kwargs):
    signal_thread = threading.current_thread()
    print(f"Signal running in thread: {signal_thread.name}")

print(f"Main thread: {main_thread.name}")
request_finished.send(sender=None)
#Since the signal handler runs on the same thread as the sender, this confirms same-thread execution.