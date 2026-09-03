class Notifier:
    """Base Notifier class handling core broadcast logic."""
    def __init__(self, sender_id: str, **kwargs):
        # Cooperatively pass remaining arguments up the MRO chain
        super().__init__(**kwargs)
        self.sender_id = sender_id

    def send(self, message: str) -> list:
        """Returns the base general broadcast log."""
        return [f"[Notifier {self.sender_id}] general broadcast: {message}"]


class EmailNotifier(Notifier):
    """Subclass handling email-based notifications cooperatively."""
    def __init__(self, email_server: str, **kwargs):
        super().__init__(**kwargs)
        self.email_server = email_server

    def send(self, message: str) -> list:
        # Call super().send() to fetch logs from the next class in MRO
        logs = super().send(message)
        logs.insert(0, f"[Email via {self.email_server}] sending: {message}")
        return logs


class SMSNotifier(Notifier):
    """Subclass handling SMS-based notifications cooperatively."""
    def __init__(self, sms_gateway: str, **kwargs):
        super().__init__(**kwargs)
        self.sms_gateway = sms_gateway

    def send(self, message: str) -> list:
        # Call super().send() to continue down the MRO path
        logs = super().send(message)
        logs.insert(0, f"[SMS via {self.sms_gateway}] sending: {message}")
        return logs


class HybridAlertChannel(EmailNotifier, SMSNotifier):
    """Hybrid notification channel combining both Email and SMS via multiple inheritance."""
    def __init__(self, sender_id: str, email_server: str, sms_gateway: str):
        # Pass all initialization parameters cooperatively using keyword arguments
        super().__init__(sender_id=sender_id, email_server=email_server, sms_gateway=sms_gateway)

    def send(self, message: str) -> list:
        # Retrieve logs accumulated from the cooperative MRO chain
        logs = super().send(message)
        logs.insert(0, "[HYBRID ALERT] Initiating dual channels...")
        return logs

# Verification of Method Resolution Order (MRO)
print("Method Resolution Order (MRO):")
for cls in HybridAlertChannel.mro():
    print(cls.__name__)

print("="*80)

alert = HybridAlertChannel(sender_id="SYS-ADMIN", email_server="smtp.cdac.in", sms_gateway="gw.acts.com")
logs = alert.send("Disk space 95%")
for log in logs:
    print(log)

