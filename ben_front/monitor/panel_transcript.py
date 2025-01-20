import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import math


class PanelTranscript(Gtk.Box):
    def __init__(self, toggle_callback,  width: int):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        self.width: int = width

        self.message_list_store = Gtk.ListStore(str)
        self.message_list_view = Gtk.TreeView(model=self.message_list_store)
        message_column = Gtk.TreeViewColumn("Messages", Gtk.CellRendererText(), text=0)
        self.message_list_view.append_column(message_column)

        scroll = Gtk.ScrolledWindow()
        scroll.add(self.message_list_view)

        toggle_button = Gtk.Button(label="Toggle Chat Panel")
        toggle_button.connect("clicked", lambda _: toggle_callback())

        self.pack_start(scroll, True, True, 0)
        self.pack_start(toggle_button, False, False, 0)
        self.show_all()


    def new_message(self, text: str) -> None:
        max_length = math.floor(self.width / 5) # Adjust this value based on panel width
        words = text.split()
        current_line = []

        message_chunks = []

        # Add a Separator after the message
        self.message_list_store.prepend([" "])

        for word in words:
            if sum(len(w) + 1 for w in current_line) + len(word) <= max_length:
                current_line.append(word)
            else:
                formatted_message = ' '.join(current_line)
                message_chunks.insert(0, formatted_message)
                current_line = [word]
        if current_line:
            formatted_message = ' '.join(current_line)
            message_chunks.insert(0, formatted_message)

        for chunk in message_chunks:
            self.message_list_store.prepend([chunk])


    def user_message(self, text: str) -> None:
        self.new_message("Me  -  " + text.capitalize())


    def ben_message(self, text: str) -> None:
        self.new_message("Ben  -  " + text)