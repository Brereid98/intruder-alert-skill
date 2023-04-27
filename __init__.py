from mycroft import MycroftSkill, intent_file_handler


class IntruderAlert(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('alert.intruder.intent')
    def handle_alert_intruder(self, message):
        self.speak_dialog('alert.intruder')


def create_skill():
    return IntruderAlert()

