#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Aug 07, 2018 03:00:18 PM

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
# import sys
import os
import Imreg.Resources as Res
import Imreg.RegistrationMethods as Reg
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter import messagebox
import time
import random

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


# -----------------------------------------------------------------------------
# START METHODS
# -----------------------------------------------------------------------------
def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    top = Regim(root)
    root.mainloop()


w = None


def create_regim(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Regim(w)
    return w, top


def destroy_regim():
    global w
    w.destroy()
    w = None


def exit_btn():
    """Close program"""
    root.quit()
    root.destroy()
    exit()


# -----------------------------------------------------------------------------
# GLOBAL VARIABLES
# -----------------------------------------------------------------------------
"""When building .exe file, remember to change images/*. to *. """
MY_ICON = 'images/icon.ico'
MY_SAVE_BTN_PATH = 'images/save_btn.png'
MY_DELETE_BTN_PATH = 'images/delete_btn.png'
MY_EMPTY_IMAGE_PATH = 'images/empty.jpg'
MY_PNG_DEST_1 = 'input_1.png'
MY_PNG_DEST_2 = 'input_2.png'
MY_OUT_DEST = 'output.png'
MY_IMREF_PATH = ''
MY_IMINPUT_PATH = ''
BASIC_COLOR = '#2857a9'

IN_SIZE = 200, 200
OUT_SIZE = 400, 400

# -----------------------------------------------------------------------------
# MAIN CLASS
# -----------------------------------------------------------------------------


class Regim:

    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
                top is the toplevel containing window."""

        from PIL import ImageTk, Image

        # Loading required images and paths
        self.icon_path = Res.resource_path(MY_ICON)
        self.save_btn_path = Res.resource_path(MY_SAVE_BTN_PATH)
        self.delete_btn_path = Res.resource_path(MY_DELETE_BTN_PATH)
        self.empty_image_path = Res.resource_path(MY_EMPTY_IMAGE_PATH)
        self.png_dest_1 = MY_PNG_DEST_1
        self.png_dest_2 = MY_PNG_DEST_2
        self.im_fixed_path = None
        self.im_moving_path = None

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font9 = "-family Verdana -size 9 -weight normal -slant roman" \
                 " -underline 0 -overstrike 0"
        font11 = "-family Verdana -size 11 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font13 = "-family Verdana -size 13 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        # Opening and resizing images
        self.empty_image = Image.open(self.empty_image_path)
        self.empty_image.thumbnail(IN_SIZE, Image.ANTIALIAS)
        self.empty_image = ImageTk.PhotoImage(self.empty_image)

        self.empty_image2 = Image.open(self.empty_image_path)
        self.empty_image2.thumbnail(OUT_SIZE, Image.ANTIALIAS)
        self.empty_image2 = ImageTk.PhotoImage(self.empty_image2)

        # Creating all the GUI
        top.geometry("1200x650+127+8")
        top.title("Regim")
        top.iconbitmap(self.icon_path)
        top.resizable(False, False)
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#ffffff")
        top.configure(highlightcolor="black")

        # Menu bar configuration
        self.menubar = Menu(top, font="TkMenuFont")
        top.configure(menu=self.menubar)

        self.file = Menu(top, tearoff=0)
        self.menubar.add_cascade(
            menu=self.file,
            font="TkMenuFont",
            label="File"
        )
        self.file.add_command(
            font="TkMenuFont",
            command="",
            label="Load"
        )
        self.file.add_command(
            font="TkMenuFont",
            label="Exit",
            command=exit_btn
        )

        self.help = Menu(top, tearoff=0)

        self.menubar.add_cascade(
            menu=self.help,
            activebackground="#d9d9d9",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Help"
        )
        self.help.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="About"
        )

        # Frames configuration
        self.frame_side = Frame(top)
        self.frame_side.place(relx=-0.02, rely=-0.02, relheight=1.01, relwidth=0.16)
        self.frame_side.configure(relief=SUNKEN)
        self.frame_side.configure(borderwidth="1")
        self.frame_side.configure(relief=SUNKEN)
        self.frame_side.configure(background="#202020")  # color #383838
        self.frame_side.configure(highlightbackground="#ffffff")
        self.frame_side.configure(highlightcolor="black")
        self.frame_side.configure(width=215)

        # Registration button
        self.reg_button = Button(self.frame_side)
        self.reg_button.place(relx=0.16, rely=0.87, height=34, width=150)
        self.reg_button.configure(activebackground="#0f306a")
        self.reg_button.configure(activeforeground="white")
        self.reg_button.configure(activeforeground="#ffffff")
        self.reg_button.configure(background=BASIC_COLOR)
        self.reg_button.configure(borderwidth="0")
        self.reg_button.configure(disabledforeground="#a3a3a3")
        self.reg_button.configure(font=font13)
        self.reg_button.configure(foreground="#ffffff")
        self.reg_button.configure(highlightbackground="#d9d9d9")
        self.reg_button.configure(highlightcolor="black")
        self.reg_button.configure(overrelief="sunken")
        self.reg_button.configure(pady="0")
        self.reg_button.configure(relief=FLAT)
        self.reg_button.configure(text='Registration')
        self.reg_button.configure(command=self.do_registration)

        # Side menu
        self.label_side = LabelFrame(self.frame_side)
        self.label_side.place(relx=0.16, rely=0.085, relheight=0.755, relwidth=0.8)
        self.label_side.configure(borderwidth="1")
        self.label_side.configure(foreground="black")
        self.label_side.configure(relief=FLAT)
        self.label_side.configure(background="#393939")  # color #585858
        self.label_side.configure(width=150)

        # Frame inputs and output
        self.frame_process = Frame(top)
        self.frame_process.place(relx=0.137, rely=0.02, relheight=1.02, relwidth=0.883)
        self.frame_process.configure(borderwidth="1")
        self.frame_process.configure(background="#5d5f60")
        self.frame_process.configure(highlightbackground="#000000")
        self.frame_process.configure(highlightcolor="#ffffff")
        self.frame_process.configure(width=805)

        # Frame DICOM info 1
        self.frame_dicom_info_1 = Frame(self.frame_process)
        self.frame_dicom_info_1.place(relx=0.28, rely=0.08, height=200, width=140)
        self.frame_dicom_info_1.configure(borderwidth="0")
        self.frame_dicom_info_1.configure(background="#ccc")
        self.frame_dicom_info_1.configure(highlightbackground="#000000")
        self.frame_dicom_info_1.configure(highlightcolor="#ffffff")

        # Frame DICOM info 2
        self.frame_dicom_info_2 = Frame(self.frame_process)
        self.frame_dicom_info_2.place(relx=0.28, rely=0.51, height=200, width=140)
        self.frame_dicom_info_2.configure(borderwidth="0")
        self.frame_dicom_info_2.configure(background="#ccc")
        self.frame_dicom_info_2.configure(highlightbackground="#000000")
        self.frame_dicom_info_2.configure(highlightcolor="#ffffff")

        # Frame Outputs
        self.frame_outputs = Frame(self.frame_process)
        self.frame_outputs.place(relx=0.47, rely=0, relheight=1.02)
        self.frame_outputs.configure(borderwidth="0")
        self.frame_outputs.configure(background="#444749")
        self.frame_outputs.configure(highlightbackground="#000000")
        self.frame_outputs.configure(highlightcolor="#ffffff")
        self.frame_outputs.configure(width=564)

        # Registered image frame
        self.frame_registered = Frame(self.frame_outputs)
        self.frame_registered.place(relx=0.11, rely=0.08, height=202, width=202)
        self.frame_registered.configure(borderwidth="0")
        self.frame_registered.configure(background="#ccc")
        self.frame_registered.configure(highlightbackground="#000000")
        self.frame_registered.configure(highlightcolor="#ffffff")

        # Data frame
        self.frame_data = Frame(self.frame_outputs)
        self.frame_data.place(relx=0.59, rely=0.08, height=202, width=122)
        self.frame_data.configure(borderwidth="0")
        self.frame_data.configure(background="#ccc")
        self.frame_data.configure(highlightbackground="#000000")
        self.frame_data.configure(highlightcolor="#ffffff")

        # Right frame
        self.frame_right = Frame(self.frame_process)
        self.frame_right.place(relx=0.946, rely=0, relheight=1.02)
        self.frame_right.configure(borderwidth="0")
        self.frame_right.configure(background="#1d1f21")
        self.frame_right.configure(highlightbackground="#000000")
        self.frame_right.configure(highlightcolor="#ffffff")
        self.frame_right.configure(width=40)

        # Label fixed image
        self.label_fixed = Label(self.frame_process)
        self.label_fixed.place(relx=0.05, rely=0.08, height=200, width=200)
        self.label_fixed.configure(background="#5d5f60")
        self.label_fixed.configure(disabledforeground="#a3a3a3")
        self.label_fixed.configure(font=font11)
        self.label_fixed.configure(foreground="#000000")
        self.label_fixed.configure(text='''Fixed image''')
        self.label_fixed.configure(width=200)
        self.label_fixed.configure(image=self.empty_image)
        self.label_fixed.image = self.empty_image

        # Label moving image
        self.label_moving = Label(self.frame_process)
        self.label_moving.place(relx=0.05, rely=0.51, height=200, width=200)
        self.label_moving.configure(activebackground="#f9f9f9")
        self.label_moving.configure(activeforeground="black")
        self.label_moving.configure(background="#5d5f60")
        self.label_moving.configure(cursor="")
        self.label_moving.configure(disabledforeground="#a3a3a3")
        self.label_moving.configure(font=font11)
        self.label_moving.configure(foreground="#000000")
        self.label_moving.configure(highlightbackground="#d9d9d9")
        self.label_moving.configure(highlightcolor="black")
        self.label_moving.configure(text='''Moving image''')
        self.label_moving.configure(image=self.empty_image)
        self.label_moving.image = self.empty_image

        # Label registered image
        self.label_reg = Label(self.frame_registered)
        self.label_reg.place(relx=0.003, rely=0.003, height=200, width=200)
        self.label_reg.configure(activebackground="#f9f9f9")
        self.label_reg.configure(activeforeground="black")
        self.label_reg.configure(background="#444749")
        self.label_reg.configure(cursor="")
        self.label_reg.configure(disabledforeground="#a3a3a3")
        self.label_reg.configure(font=font11)
        self.label_reg.configure(foreground="#ccc")
        self.label_reg.configure(highlightbackground="#d9d9d9")
        self.label_reg.configure(highlightcolor="black")
        self.label_reg.configure(text='''Registered image''')

        # Data label
        self.label_data = Label(self.frame_data)
        self.label_data.place(relx=0.005, rely=0.003, height=30, width=120)
        self.label_data.configure(background="#444749")
        self.label_data.configure(cursor="")
        self.label_data.configure(font=font9)
        self.label_data.configure(foreground="#ccc")
        self.label_data.configure(text='Data')

        # Info label
        self.label_info = Label(self.frame_data)
        self.label_info.place(relx=0.005, rely=0.155, height=170, width=120)
        self.label_info.configure(background="#444749")
        self.label_info.configure(cursor="")
        self.label_info.configure(font=font9)
        self.label_info.configure(foreground="#ccc")
        self.label_info.configure(wraplength=100)

        # Title DICOM info 1
        self.label_title_1 = Label(self.frame_dicom_info_1)
        self.label_title_1.place(relx=0.005, rely=0.003, height=30, width=138)
        self.label_title_1.configure(background="#5d5f60")
        self.label_title_1.configure(cursor="")
        self.label_title_1.configure(font=font9)
        self.label_title_1.configure(foreground="#ccc")
        self.label_title_1.configure(text='DICOM info')

        # Label DICOM data 1
        self.label_dicom_data_1 = Label(self.frame_dicom_info_1)
        self.label_dicom_data_1.place(relx=0.005, rely=0.145, height=170, width=138)
        self.label_dicom_data_1.configure(background="#5d5f60")
        self.label_dicom_data_1.configure(cursor="")
        self.label_dicom_data_1.configure(font=font9)
        self.label_dicom_data_1.configure(foreground="#ccc")
        self.label_dicom_data_1.configure(text='')

        # Title DICOM info 2
        self.label_title_2 = Label(self.frame_dicom_info_2)
        self.label_title_2.place(relx=0.005, rely=0.003, height=30, width=138)
        self.label_title_2.configure(background="#5d5f60")
        self.label_title_2.configure(cursor="")
        self.label_title_2.configure(font=font9)
        self.label_title_2.configure(foreground="#ccc")
        self.label_title_2.configure(text='DICOM info')

        # Label DICOM data 2
        self.label_dicom_data_2 = Label(self.frame_dicom_info_2)
        self.label_dicom_data_2.place(relx=0.005, rely=0.145, height=170, width=138)
        self.label_dicom_data_2.configure(background="#5d5f60")
        self.label_dicom_data_2.configure(cursor="")
        self.label_dicom_data_2.configure(font=font9)
        self.label_dicom_data_2.configure(foreground="#ccc")
        self.label_dicom_data_2.configure(text='')

        # Frame foot
        self.frame_foot = Frame(top)
        self.frame_foot.place(relx=-0.01, rely=0.94, relheight=0.07, relwidth=1.02)
        self.frame_foot.configure(relief=SUNKEN)
        self.frame_foot.configure(borderwidth="1")
        self.frame_foot.configure(relief=SUNKEN)
        self.frame_foot.configure(background="#202020")  # color #383838
        self.frame_foot.configure(highlightbackground="#d9d9d9")
        self.frame_foot.configure(highlightcolor="#ffffff")
        self.frame_foot.configure(width=995)

        # Top frame
        self.frame_top = Frame(top)
        self.frame_top.place(relx=-0.01, rely=-0.1, relheight=0.14, relwidth=1.03)
        self.frame_top.configure(relief=RIDGE)
        self.frame_top.configure(borderwidth="1")
        self.frame_top.configure(relief=RIDGE)
        self.frame_top.configure(background="#202020")
        self.frame_top.configure(highlightbackground="#d9d9d9")
        self.frame_top.configure(highlightcolor="#ffffff")
        self.frame_top.configure(width=1005)

        # SAVE AS button
        self.save_button = Button(self.frame_right)
        self.save_button.place(relx=0.05, rely=0.73, height=30, width=30)
        self.save_button.configure(activebackground="#fff")
        self.save_button.configure(background="#d9d9d9")
        self.save_button.configure(borderwidth="0")
        self._save_img = PhotoImage(file=self.save_btn_path)
        self.save_button.configure(image=self._save_img)
        self.save_button.configure(command=self.save_file)

        # DELETE button
        self.delete_button = Button(self.frame_right)
        self.delete_button.place(relx=0.05, rely=0.82, height=30, width=30)
        self.delete_button.configure(activebackground="#fff")
        self.delete_button.configure(background="#d9d9d9")
        self.delete_button.configure(borderwidth="0")
        self._del_img = PhotoImage(file=self.delete_btn_path)
        self.delete_button.configure(image=self._del_img)
        self.delete_button.configure(command=self.delete_files)

        # Left menu labels
        self.select_input_label = Label(self.label_side)
        self.select_input_label.place(relx=0, rely=0, height=30, width=150)
        self.select_input_label.configure(background=BASIC_COLOR)
        self.select_input_label.configure(disabledforeground="#a3a3a3")
        self.select_input_label.configure(foreground="#fff")
        self.select_input_label.configure(font=font11)
        self.select_input_label.configure(text="Select inputs")
        self.select_input_label.configure(width=400)
        # Select fixed image button
        self.select_fixed_btn = Button(self.label_side)
        self.select_fixed_btn.place(relx=0, rely=0.08, height=26, width=150)
        self.select_fixed_btn.configure(background="#393939")
        self.select_fixed_btn.configure(activebackground="#474747")
        self.select_fixed_btn.configure(activeforeground="#cccccc")
        self.select_fixed_btn.configure(disabledforeground="#a3a3a3")
        self.select_fixed_btn.configure(foreground="#ccc")
        self.select_fixed_btn.configure(font=font11)
        self.select_fixed_btn.configure(text="Fixed image")
        self.select_fixed_btn.configure(width=400)
        self.select_fixed_btn.configure(borderwidth="0")
        self.select_fixed_btn.configure(command=self.add_fixed_image)
        # Select moving image button
        self.select_moving_btn = Button(self.label_side)
        self.select_moving_btn.place(relx=0, rely=0.15, height=26, width=150)
        self.select_moving_btn.configure(background="#393939")
        self.select_moving_btn.configure(activebackground="#474747")
        self.select_moving_btn.configure(activeforeground="#cccccc")
        self.select_moving_btn.configure(disabledforeground="#a3a3a3")
        self.select_moving_btn.configure(foreground="#ccc")
        self.select_moving_btn.configure(font=font11)
        self.select_moving_btn.configure(text="Moving image")
        self.select_moving_btn.configure(width=400)
        self.select_moving_btn.configure(borderwidth="0")
        self.select_moving_btn.configure(command=self.add_moving_image)
        # Left method label
        self.select_method_label = Label(self.label_side)
        self.select_method_label.place(relx=0, rely=0.23, height=30, width=150)
        self.select_method_label.configure(background=BASIC_COLOR)
        self.select_method_label.configure(disabledforeground="#a3a3a3")
        self.select_method_label.configure(foreground="#fff")
        self.select_method_label.configure(font=font11)
        self.select_method_label.configure(text="Regim methods")
        self.select_method_label.configure(width=400)
        # Select default method button
        self.select_default_btn = Button(self.label_side)
        self.select_default_btn.place(relx=0, rely=0.31, height=26, width=150)
        self.select_default_btn.configure(background="#393939")
        self.select_default_btn.configure(disabledforeground="#a3a3a3")
        self.select_default_btn.configure(foreground="#ccc")
        self.select_default_btn.configure(activebackground="#474747")
        self.select_default_btn.configure(activeforeground="#cccccc")
        self.select_default_btn.configure(font=font11)
        self.select_default_btn.configure(text="Default")
        self.select_default_btn.configure(width=400)
        self.select_default_btn.configure(borderwidth="0")
        self.select_default_btn.configure(command="")
        # Select exhaustive method button
        self.select_exhaustive_btn = Button(self.label_side)
        self.select_exhaustive_btn.place(relx=0, rely=0.38, height=26, width=150)
        self.select_exhaustive_btn.configure(background="#393939")
        self.select_exhaustive_btn.configure(disabledforeground="#a3a3a3")
        self.select_exhaustive_btn.configure(foreground="#ccc")
        self.select_exhaustive_btn.configure(activebackground="#474747")
        self.select_exhaustive_btn.configure(activeforeground="#cccccc")
        self.select_exhaustive_btn.configure(font=font11)
        self.select_exhaustive_btn.configure(text="Exhaustive")
        self.select_exhaustive_btn.configure(width=400)
        self.select_exhaustive_btn.configure(borderwidth="0")
        self.select_exhaustive_btn.configure(command="")
        # Left parameters label
        self.select_parameters_label = Label(self.label_side)
        self.select_parameters_label.place(relx=0, rely=0.46, height=30, width=150)
        self.select_parameters_label.configure(background=BASIC_COLOR)
        self.select_parameters_label.configure(disabledforeground="#a3a3a3")
        self.select_parameters_label.configure(foreground="#fff")
        self.select_parameters_label.configure(font=font11)
        self.select_parameters_label.configure(text="Parameters")
        self.select_parameters_label.configure(width=400)
        # Iterations input
        self.iterations_input = Button(self.label_side)
        self.iterations_input.place(relx=0, rely=0.54, height=26, width=150)
        self.iterations_input.configure(background="#393939")
        self.iterations_input.configure(disabledforeground="#a3a3a3")
        self.iterations_input.configure(foreground="#ccc")
        self.iterations_input.configure(activebackground="#474747")
        self.iterations_input.configure(activeforeground="#cccccc")
        self.iterations_input.configure(font=font11)
        self.iterations_input.configure(text="Iterations")
        self.iterations_input.configure(width=400)
        self.iterations_input.configure(borderwidth="0")
        self.iterations_input.configure(command="")
        # Min step input
        self.minstep_input = Button(self.label_side)
        self.minstep_input.place(relx=0, rely=0.61, height=26, width=150)
        self.minstep_input.configure(background="#393939")
        self.minstep_input.configure(disabledforeground="#a3a3a3")
        self.minstep_input.configure(foreground="#ccc")
        self.minstep_input.configure(activebackground="#474747")
        self.minstep_input.configure(activeforeground="#cccccc")
        self.minstep_input.configure(font=font11)
        self.minstep_input.configure(text="Min step")
        self.minstep_input.configure(width=400)
        self.minstep_input.configure(borderwidth="0")
        self.minstep_input.configure(command="")

        # Progress bar
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", troughcolor='#202020', background=BASIC_COLOR)
        self.progress_bar = ttk.Progressbar(self.frame_foot,
                                            style="red.Horizontal.TProgressbar",
                                            orient='horizontal',
                                            mode='determinate')
        self.progress_bar.place(relx=0, rely=0, height=40, width=1215)
        self.mask = Label(self.frame_foot)
        self.mask.place(relx=0, rely=0, height=31, width=1215)
        self.mask.configure(background='#202020')

    def add_fixed_image(self):
        """Open an image file and show it in the GUI"""
        from PIL import ImageTk, Image
        self.png_dest_1 = MY_PNG_DEST_1
        # Searching file
        try:
            self.im_fixed_path = askopenfilename(
                        initialdir=".",
                        filetypes=(
                            ("Dicom (*.DCM)", "*.dcm"),
                            ("JPEG (*.JPG)", "*.jpg*"),
                            ("PNG (*.PNG)", "*.png*")
                        ),
                        title="Choose image 1."
                       )
            # Converting .dcm file to .png for manipulation
            if self.im_fixed_path[-3:] == 'dcm':
                Res.dicom_to_png(self.im_fixed_path, self.png_dest_1)
            else:
                self.png_dest_1 = self.im_fixed_path

            # Place it in the GUI label
            png_file = Image.open(self.png_dest_1)
            png_file.thumbnail(IN_SIZE, Image.ANTIALIAS)
            png_image = ImageTk.PhotoImage(png_file)
            self.label_fixed.configure(image=png_image)
            self.label_fixed.image = png_image

            self.im_fixed_path = self.png_dest_1

        except:
            pass

    def add_moving_image(self):
        """Open an image file and show it in the GUI"""
        from PIL import ImageTk, Image
        self.png_dest_2 = MY_PNG_DEST_2
        try:
            # Searching file
            self.im_moving_path = askopenfilename(
                            initialdir=".",
                            filetypes=(
                                ("Dicom (*.DCM)", "*.dcm"),
                                ("JPEG (*.JPG)", "*.jpg*"),
                                ("PNG (*.PNG)", "*.png*")
                            ),
                            title="Choose image 2."
                            )
            # Converting .dcm file to .png for manipulation
            if self.im_moving_path[-3:] == 'dcm':
                Res.dicom_to_png(self.im_moving_path, self.png_dest_2)
            else:
                self.png_dest_2 = self.im_moving_path

            # Place it in the GUI label
            png_file = Image.open(self.png_dest_2)
            png_file.thumbnail(IN_SIZE, Image.ANTIALIAS)
            png_image = ImageTk.PhotoImage(png_file)
            self.label_moving.configure(image=png_image)
            self.label_moving.image = png_image

            self.im_moving_path = self.png_dest_2

        except:
            pass

    def do_registration(self):
        """Do the registration for the fixed and moving image"""
        from PIL import Image, ImageTk
        try:
            self.progress_bar['maximum'] = 100
            self.run_progress_bar(1, random.randint(30, 60))

            my_imreg = Reg.Imreg(self.png_dest_1, self.png_dest_2)
            registered_image = my_imreg.image_registration_method_displacement()
            self.output_image = registered_image

            self.progress_bar['value'] = random.randint(70, 90)
            self.progress_bar.update()
            time.sleep(0.1)

            # registered_image = Image.fromarray(self.registered_image)
            registered_image.thumbnail(IN_SIZE, Image.ANTIALIAS)
            registered_image.save(MY_OUT_DEST)
            registered_image = ImageTk.PhotoImage(registered_image)

            self.progress_bar['value'] = 100
            self.progress_bar.update()
            time.sleep(0.2)

            self.label_reg.configure(image=registered_image)
            self.label_reg.image = registered_image

            self.label_info.configure(text=my_imreg.info_data)

            self.progress_bar['value'] = 0
        except:
            pass

    def run_progress_bar(self, start, stop):
        """Run the progress bar"""
        # self.progress_bar['maximum'] = 100
        for i in range(start, stop):
            time.sleep(0.015)
            self.progress_bar['value'] = i
            self.progress_bar.update()

        # self.progress_bar['value'] = 0

    def save_file(self):
        """Save registered image"""
        f = asksaveasfile(mode='w', defaultextension=".png")
        if f is None:  # asksaveasfile return 'None' if dialog closed with "cancel".
            return
        saving_path = f.name
        self.output_image.save(saving_path)
        f.close()

    def delete_files(self):
        title = "Delete files"
        message = "Are you sure you want to permanently delete the images files?"
        answer = messagebox.askquestion(title, message, icon='warning')
        if answer == "yes":
            if os.path.exists(MY_PNG_DEST_1):
                os.remove(MY_PNG_DEST_1)
            if os.path.exists(MY_PNG_DEST_2):
                os.remove(MY_PNG_DEST_2)
            if os.path.exists(MY_OUT_DEST):
                os.remove(MY_OUT_DEST)
        else:
            pass


if __name__ == '__main__':
    vp_start_gui()