import gi # type: ignore
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk # type : ignore

from monitor.panel_history import PanelHistory
from monitor.panel_transcript import PanelTranscript


class Monitor(Gtk.Window):
    def __init__(self):
        super().__init__(title="Ben VoiceAssistant")
        self.w = 256
        self.h = 512
        self.set_default_size(self.w, self.h)

        # Create the vertical Paned container
        self.vpaned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        self.add(self.vpaned)

        # Left panel: Chat list (hidden by default)
        self.panel_history = PanelHistory()
        self.vpaned.add1(self.panel_history)
        self.vpaned.child_set_property(self.panel_history, "shrink", False)
        self.panel_history.hide()

        # Right panel: Message list with toggle button
        self.panel_transcript = PanelTranscript(toggle_callback=self.toggle_left_panel, width=self.w)
        self.vpaned.add2(self.panel_transcript)


    def toggle_left_panel(self):
        if self.panel_history.is_visible():
            self.panel_history.hide()
        else:
            self.panel_history.show()

    
    def start(self, transcript: str) -> None:
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        self.toggle_left_panel()
        self.panel_transcript.user_message(transcript)
        self.set_keep_above(True)
        self.present()
        Gtk.main()

