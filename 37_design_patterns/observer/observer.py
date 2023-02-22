import abc
import typing as t


class Subscriber(abc.ABC):
    @abc.abstractmethod
    def update(self, message: str) -> None:
        pass


class EmailSubscriber(Subscriber):
    def update(self, message: str) -> None:
        print(f'Sending message {message} via email')


class SmsSubscriber(Subscriber):
    def update(self, message: str) -> None:
        print(f'Sending message {message} via SMS')


class AlertManager:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, event_type, message):
        for subscriber in self.subscribers:
            if isinstance(subscriber, event_type):
                subscriber.update(message)

    def notify_all(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


class Application:
    def __init__(self, alert_manager) -> None:
        self.alert_manager = alert_manager

    def actualizare_preturi(self):
        print('Ceva job de actualizare preturi...')
        self.alert_manager.notify_subscribers(
            SmsSubscriber, 'Preturi actualizate, intra pe aplicatie')
        self.alert_manager.notify_subscribers(
            EmailSubscriber, 'Preturi actualizate, intra pe aplicatie')

    def actualizare_termeni(self):
        print('Ceva job de actualizare termeni si conditii...')
        self.alert_manager.notify_subscribers(
            EmailSubscriber, 'Au fost actualizate termenii si conditiile')


if __name__ == '__main__':
    email_subs = EmailSubscriber()
    sms_subs = SmsSubscriber()

    alert_manager = AlertManager()
    alert_manager.subscribe(email_subs)
    alert_manager.subscribe(sms_subs)

    app = Application(alert_manager)

    app.actualizare_preturi()
    print('----')
    app.actualizare_termeni()
    print('----')

    alert_manager.unsubscribe(email_subs)

    app.actualizare_preturi()
