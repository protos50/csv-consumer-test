import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GUI:
    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_title("COVID-19 Vaccine Analysis")
        self.window.set_default_size(800, 600)
        self.window.connect("destroy", Gtk.main_quit)

        self.vbox = Gtk.VBox()
        self.window.add(self.vbox)

        self.label = Gtk.Label(label="Welcome to the COVID-19 Vaccine Analysis App!")
        self.vbox.pack_start(self.label, True, True, 0)

        self.button = Gtk.Button(label="Start Analysis")
        self.button.connect("clicked", self.start_analysis)
        self.vbox.pack_start(self.button, True, True, 0)

        self.window.show_all()

    def start_analysis(self, widget):
        # print a sum in the gui
        print("Starting analysis...")
        result = 5 + 10
        self.label.set_text("The sum of 5 and 10 is: " + str(result))

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    gui = GUI()
    gui.run()
