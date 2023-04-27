from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking
from os.path import join

class IntruderAlertSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('intruder.alert.intent')
    def handle_intruder_alert(self, message):
        # Set the volume to 100%
        self.enclosure.mouth_text("Increasing volume to 100 percent")
        self.audioservice.set_volume(100)

        # Play the MP3 file from the desktop
        self.enclosure.mouth_text("Playing intruder alert sound")
        mp3_path = '/home/pi/Desktop/intruder_alert.mp3'
        self.audioservice.play(mp3_path)

        # Wait for the audio to finish playing
        wait_while_speaking()

def create_skill():
    return IntruderAlertSkill()

