#!/usr/bin/env python3

import os
import math
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk, Pango
from DementiaDetector import on_fileOpen,startjvm


#fileLoc = "/home/abinash/Project/_Project/Dementia/"
fileLocation = '/Resource/Layers/layer'

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

class FileSaveWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.filepath = ''
        self.saveFlag = False
        self.on_save_clicked(self)

    def on_save_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Choose save location", self,
            Gtk.FileChooserAction.SAVE,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.filepath = self.filepath + dialog.get_filename()
            self.saveFlag = True
            print("File save: " + self.filepath)

        elif response == Gtk.ResponseType.CANCEL:
            self.saveFlag = False
            print("Cancel clicked")

        dialog.destroy()



class Main:
    def __init__(self):
        self.filepath = ''
        startjvm()
        builder1 = Gtk.Builder()
        builder1.add_from_file(os.getcwd()+"/Resource/dementia.glade")
        builder1.connect_signals(self)

        self.window1 = builder1.get_object("window1")
        self.window1.set_default_size(600,338)
        self.window1.set_position(Gtk.WindowPosition.CENTER)
        self.window1.set_resizable(False)
        self.window1.show_all()

    def on_fileOpen_activate(self, widget):
        print("open")
        win = FileChooserWindow()

        if (win.openFlag == True):
            self.filePath = win.filepath
            print ("calling functin on_fileOpen")
            on_fileOpen(win.filepath)

            self.window1.hide()

            window2=Window2(self.window1)
#            window2.set_resizable(True)
            window2.set_position(Gtk.WindowPosition.CENTER)
#            window2.resize(600,338)
            window2.set_resizable(False)
            window2.show_all()


    def on_helpAbout_activate(self, widget):
        print("about")
        self.window1.hide()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(os.getcwd()+'/Resource/Logo.png')
        builder = Gtk.Builder()
        builder.add_from_file(os.getcwd()+"/Resource/dementia.glade")
        about = builder.get_object("aboutDementia")
        about.set_program_name("Dementa Detector")
        about.set_version("1.0.0.1")
        about.set_logo(pixbuf)
        authorList = ['Sagar Gautam', 'Abinash Manandhar','Sujan Sauden',
                        'Dharma K. Shrestha']
        about.set_authors(authorList)
        about.set_comments("Main purpose of the project is to identify "+
                            "dementia in MRI scan using machine learning"+
                            "algorithm. Training images are preprocessed"+
                            " to determine features and based on these "+
                            "features Neural Network and K Nearest "+
                            "Neighbour model has been developed which"+
                            "predicts dementia in MRI scans.")
        about.set_license_type(Gtk.License.GPL_3_0)

        about.run()
        about.destroy()
        self.window1.show()

    def on_fileQuit_activate(self, widget):
        print("filequit")
        self.window1.destroy()
        Gtk.main_quit()

    def on_window1_destroy(self, widget):
        print("win1des")
        self.window1.destroy()
        Gtk.main_quit()


class Window2(Gtk.Window):
    def __init__(self, window1):

        self.fileloc = ''
        self.text1 = ''
        self.text2 = ''
        self.window1 = window1
        self.adjustment= Gtk.Adjustment(88, 1, 176, 0, 1, 0)
        self.buttonCheck = Gtk.Button(label="Check")
        self.buttonSave = Gtk.Button(label="Save Image")
        self.imageSlider = Gtk.VScale(adjustment = self.adjustment)
        self.imageArea = Gtk.Image()
        self.displayResult = Gtk.TextView()
        self.displayTitle = Gtk.TextView()
        color = Gdk.RGBA()
        color.parse('#f2f1ef')
        color.to_string()
        self.displayResult.override_background_color(Gtk.StateType.NORMAL, color)
        self.displayTitle.override_background_color(Gtk.StateType.NORMAL, color)
        self.textBuf1 = self.displayTitle.get_buffer()
        self.textBuf2 = self.displayResult.get_buffer()
        self.tag_bold = self.textBuf1.create_tag("bold",
                            weight=Pango.Weight.BOLD)
        self.tag_italic = self.textBuf2.create_tag("italic",
                            style=Pango.Style.ITALIC)
        self.tag_underline = self.textBuf1.create_tag("underline",
                            underline=Pango.Underline.SINGLE)


        Gtk.Window.__init__(self, title= "Dementia Detector")

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        grid.attach(self.imageArea, 3, 333, 10, 10)
        grid.attach_next_to(self.imageSlider, self.imageArea,
                                Gtk.PositionType.RIGHT, 1, 10)
        grid.attach_next_to(self.buttonCheck, self.imageArea,
                                Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(self.buttonSave, self.buttonCheck,
                                Gtk.PositionType.RIGHT, 7, 1)
        grid.attach_next_to(self.displayTitle, self.imageSlider,
                                Gtk.PositionType.RIGHT, 20, 2)
        grid.attach_next_to(self.displayResult, self.displayTitle,
                                Gtk.PositionType.BOTTOM, 20, 10)

        self.imageSlider.set_digits(0)
        self.imageSlider.set_draw_value(False)
        self.imageSlider.set_digits(0)

        self.fileloc = fileLocation+"88.jpg"
        self.imageArea.set_from_file(os.getcwd()+self.fileloc)

        self.displayTitle.set_editable(False)
        self.displayResult.set_editable(False)

        self.text1 = '      Results from ANN and KNN:       '
        self.textBuf1.set_text(self.text1)
        start, end = self.textBuf1.get_bounds()
        self.textBuf1.apply_tag(self.tag_underline, start, end)
        self.displayTitle.set_buffer(self.textBuf1)

        self.buttonCheck.connect("clicked", self.on_buttonCheck_clicked)
        self.buttonSave.connect("clicked", self.on_buttonSave_clicked)
        self.imageSlider.connect("value-changed", self.on_imageSlider_moved)
        self.connect("destroy", self.on_window2_destroy)

    def on_window2_destroy(self, widget):
        self.window1.show()
        print("win2des win2des")

    def on_buttonCheck_clicked(self, widget):

        print("check check")
        from DementiaDetector import newLabel, predictionResult
        print(newLabel)
        print(predictionResult)
        if (newLabel == 0):
            self.text2 += '\n\n\nKNN Model : Dementia Positive'
        else:
            self.text2 += '\n\n\nKNN Model : Dementia Negative'
        if (predictionResult == 0):
            self.text2 += '\n\nANN Model : Dementia Positive'
        else:
            self.text2 += '\n\nANN Model : Dementia Negative'

        self.textBuf2.set_text(self.text2)
        start, end = self.textBuf2.get_bounds()
        self.displayResult.set_buffer(self.textBuf2)

    def on_buttonSave_clicked(self, widget):
        print("save save")
        win = FileSaveWindow()

        if (win.saveFlag == True):
            print(win.filepath)
            print(self.fileloc)
            os.rename(os.getcwd()+self.fileloc,win.filepath)

    def on_imageSlider_moved(self, get):
        print("moved moved")
        pos = self.imageSlider.get_value()
        pos =str(int(pos))
        print(pos)
        self.fileloc = fileLocation+pos+".jpg"
        self.imageArea.set_from_file(os.getcwd()+self.fileloc)

MainInstance = Main()
Gtk.main()
