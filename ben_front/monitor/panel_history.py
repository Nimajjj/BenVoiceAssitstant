import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PanelHistory(Gtk.ScrolledWindow):
    def __init__(self):
        super().__init__()

        self.chat_list_store = Gtk.ListStore(str)
        self.chat_list_store.append(["Chat 1"])
        self.chat_list_store.append(["Chat 2"])
        self.chat_list_store.append(["Chat 3"])

        chat_list_view = Gtk.TreeView(model=self.chat_list_store)
        chat_column = Gtk.TreeViewColumn("Chats", Gtk.CellRendererText(), text=0)
        chat_list_view.append_column(chat_column)

        self.add(chat_list_view)