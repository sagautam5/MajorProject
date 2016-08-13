#!/usr/bin/env python3

import math
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from DementiaDetector import on_fileOpen

fileLocation = "/home/abinash/Project/_Project/Dementia/Resource/Layers/layer"

class FileChooserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.openFlag = False
        self.filepath = ''
        self.on_file_clicked(self)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.filepath = self.filepath + dialog.get_filename()
            self.openFlag = True
            print("File selected: " + self.filepath)

        elif response == Gtk.ResponseType.CANCEL:
            self.openFlag = False
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):

        filter_any = Gtk.FileFilter()
        filter_any.set_name("img files")
        filter_any.add_pattern("*.img")
        dialog.add_filter(filter_any)


class handler:

    def __init__(self):
        self.filePath=''

    def on_fileOpen_activate(self, widget):
        print("open")
        win = FileChooserWindow()

        if (win.openFlag == True):
            self.filePath = win.filepath
            print ("calling functin on_fileOpen")
            on_fileOpen(win.filepath)

#           self.parent.parent.hide()

            window2=Window2()
            window2.set_default_size(600,338)
            window2.set_resizable(False)
            window2.show_all()


    def on_helpAbout_activate(self, widget):
        #do something
        print("about")

    def on_fileQuit_activate(self, widget):
        print("filequit")
        Gtk.main_quit


class handler1(handler):

    def on_window1_destroy(self, widget):
        print("win1des")
        Gtk.main_quit


class Main:
    def __init__(self):
        handler11 = handler1()
        builder1 = Gtk.Builder()
        builder1.add_from_file("dementia.glade")
        builder1.connect_signals(handler11)

        window1 = builder1.get_object("window1")
        window1.set_default_size(600,338)
        window1.set_resizable(False)
        window1.show_all()


class Window2(Gtk.Window):
    def __init__(self):

        self.adjustment= Gtk.Adjustment(88, 1, 176, 0, 1, 0)
        self.buttonCheck = Gtk.Button(label="Check")
        self.buttonSave = Gtk.Button(label="Save Image")
        self.displayArea = Gtk.TextView()
        self.imageSlider = Gtk.VScale(adjustment=self.adjustment)
        self.imageArea = Gtk.Image()

        Gtk.Window.__init__(self, title= "Dementia Detector")

        grid = Gtk.Grid()
        self.add(grid)

        #imageArea.set_size_request(10,10)

        grid.attach(self.imageArea, 0, 0, 10, 10)
        grid.attach_next_to(self.imageSlider, self.imageArea, Gtk.PositionType.RIGHT, 1, 10)
        grid.attach_next_to(self.buttonCheck, self.imageArea, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(self.displayArea, self.buttonCheck, Gtk.PositionType.RIGHT, 7, 1)
        grid.attach_next_to(self.buttonSave, self.displayArea, Gtk.PositionType.RIGHT, 1, 1)

        self.imageSlider.set_digits(0)
        self.imageSlider.set_draw_value(False)
        self.imageSlider.set_digits(0)

        self.imageArea.set_from_file(fileLocation+"88.jpg")

        self.displayArea.set_editable(False)

        self.buttonCheck.connect("clicked", self.on_buttonCheck_clicked)
        self.buttonSave.connect("clicked", self.on_buttonSave_clicked)
        self.imageSlider.connect("value-changed", self.on_imageSlider_moved)
        self.connect("destroy", self.on_window2_destroy)
        self.set_default_size(600,338)

    def on_window2_destroy(self, widget):
        Gtk.main_quit
        print("win2des win2des")

    def on_buttonCheck_clicked(self, widget):

        print("check check")
        text = ''
        from DementiaDetector import newLabel, predictionResult
        print(newLabel)
        print(predictionResult)
        if (newLabel == 0):
            text += 'KNN Model : Dementia Positive'
        else:
            text += 'KNN Model : Dementia Negative'
        if (predictionResult == 0):
            text += '\nANN Model : Dementia Positive'
        else:
            text += '\nANN Model : Dementia Negative'

        textBuf = Gtk.TextBuffer()
        textBuf.set_text(text)

        self.displayArea.set_buffer(textBuf)

    def on_buttonSave_clicked(self, widget):
        print("save save")

    def on_imageSlider_moved(self, get):
        print("moved moved")
        pos = self.imageSlider.get_value()
        pos =str(int(pos))
        print(pos)
        self.imageArea.set_from_file(fileLocation+pos+".jpg")

MainInstance = Main()
Gtk.main()
