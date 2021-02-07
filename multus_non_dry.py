import PyPDF2
import os
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.wm_title('Multus')

root.geometry('')

root.iconbitmap(r'images\DG.ico')

# Images

header_img = ImageTk.PhotoImage(Image.open(r'images\DG_banner2.png'))
ccbutton_img = ImageTk.PhotoImage(Image.open(r'images\ccbutton-01.png'))
exitButton_img = ImageTk.PhotoImage(Image.open(r'images\exitbutton.png'))
checkmark_img = ImageTk.PhotoImage(Image.open(r'images\checkmark.png'))
clearbutton_img = ImageTk.PhotoImage(Image.open(r'images\clearbutton.png'))

# Header

cslogo_label = tk.Label(borderwidth=5, image=header_img)
cslogo_label.grid(row=0, column=0, columnspan=7, sticky='nsew')

# Desktop folder entry

multusf_label = tk.Label(
    text='Please enter the desktop folder name:')
multusf_label.grid(row=1, column=0, padx=8,   sticky=tk.W)

multusf_entry = tk.Entry(width=30, bg='white', borderwidth=3)
multusf_entry.grid(row=2, column=0,
                   padx=8, pady=8, sticky=tk.W)
multusf_entry.insert(0, "Multus_Folder")

# Jobs entries

job_label = tk.Label(
    text='Please enter the Job Number and select PDF type:')
job_label.grid(row=3, column=0, columnspan=7,   padx=8, sticky=tk.W)

job_window_1 = tk.Entry(width=30, bg='white',
                        borderwidth=3)
job_window_1.grid(row=4, column=0,
                  padx=8, pady=3, sticky=tk.W)

job_window_2 = tk.Entry(width=30, bg='white',
                        borderwidth=3)
job_window_2.grid(row=6, column=0,
                  padx=8, pady=8, sticky=tk.W)

job_window_3 = tk.Entry(width=30, bg='white',
                        borderwidth=3)
job_window_3.grid(row=8, column=0,
                  padx=8, pady=8, sticky=tk.W)

job_window_4 = tk.Entry(width=30, bg='white',
                        borderwidth=3)
job_window_4.grid(row=10, column=0,
                  padx=8, pady=8, sticky=tk.W)

job_window_5 = tk.Entry(width=30, bg='white',
                        borderwidth=3)
job_window_5.grid(row=12, column=0,
                  padx=8, pady=8, sticky=tk.W)


job_window_6 = tk.Entry(width=30, bg='white',
                        borderwidth=3)
job_window_6.grid(row=14, column=0,
                  padx=8, pady=8, sticky=tk.W)


job_window_7 = tk.Entry(width=30, bg='white',
                        borderwidth=3)
job_window_7.grid(row=16, column=0,
                  padx=8, pady=8, sticky=tk.W)


job_window_8 = tk.Entry(width=30, bg='white',
                        borderwidth=3)
job_window_8.grid(row=18, column=0,
                  padx=8, pady=8, sticky=tk.W)

job_window_9 = tk.Entry(width=30, bg='white',
                        borderwidth=3)
job_window_9.grid(row=20, column=0,
                  padx=8, pady=8, sticky=tk.W)

job_window_10 = tk.Entry(width=30, bg='white',
                         borderwidth=3)
job_window_10.grid(row=22, column=0,
                   padx=8, pady=8, sticky=tk.W)


# PDF types

pdf_type_1 = tk.StringVar(value='LR')
rad_LR_1 = tk.Radiobutton(text='LR', variable=pdf_type_1,
                          value='LR')
rad_LR_1.grid(row=4, column=4, sticky=tk.W)

rad_HR_1 = tk.Radiobutton(text='HR', variable=pdf_type_1,
                          value='HR', tristatevalue="x")
rad_HR_1.grid(row=4, column=5, sticky=tk.W)

rad_RT_1 = tk.Radiobutton(text='RT', variable=pdf_type_1,
                          value='RT', tristatevalue="x")
rad_RT_1.grid(row=4, column=6, sticky=tk.W, padx=(0, 10))


pdf_type_2 = tk.StringVar(value='LR')
rad_LR_2 = tk.Radiobutton(text='LR', variable=pdf_type_2,
                          value='LR')
rad_LR_2.grid(row=6, column=4, sticky=tk.W)

rad_HR_2 = tk.Radiobutton(text='HR', variable=pdf_type_2,
                          value='HR', tristatevalue="x")
rad_HR_2.grid(row=6, column=5, sticky=tk.W)

rad_RT_2 = tk.Radiobutton(text='RT', variable=pdf_type_2,
                          value='RT', tristatevalue="x")
rad_RT_2.grid(row=6, column=6, sticky=tk.W)


pdf_type_3 = tk.StringVar(value='LR')
rad_LR_3 = tk.Radiobutton(text='LR', variable=pdf_type_3,
                          value='LR')
rad_LR_3.grid(row=8, column=4, sticky=tk.W)

rad_HR_3 = tk.Radiobutton(text='HR', variable=pdf_type_3,
                          value='HR', tristatevalue="x")
rad_HR_3.grid(row=8, column=5, sticky=tk.W)

rad_RT_3 = tk.Radiobutton(text='RT', variable=pdf_type_3,
                          value='RT', tristatevalue="x")
rad_RT_3.grid(row=8, column=6, sticky=tk.W)


pdf_type_4 = tk.StringVar(value='LR')
rad_LR_4 = tk.Radiobutton(text='LR', variable=pdf_type_4,
                          value='LR')
rad_LR_4.grid(row=10, column=4, sticky=tk.W)

rad_HR_4 = tk.Radiobutton(text='HR', variable=pdf_type_4,
                          value='HR', tristatevalue="x")
rad_HR_4.grid(row=10, column=5, sticky=tk.W)

rad_RT_4 = tk.Radiobutton(text='RT', variable=pdf_type_4,
                          value='RT', tristatevalue="x")
rad_RT_4.grid(row=10, column=6, sticky=tk.W)


pdf_type_5 = tk.StringVar(value='LR')
rad_LR_5 = tk.Radiobutton(text='LR', variable=pdf_type_5,
                          value='LR')
rad_LR_5.grid(row=12, column=4, sticky=tk.W)

rad_HR_5 = tk.Radiobutton(text='HR', variable=pdf_type_5,
                          value='HR', tristatevalue="x")
rad_HR_5.grid(row=12, column=5, sticky=tk.W)

rad_RT_5 = tk.Radiobutton(text='RT', variable=pdf_type_5,
                          value='RT', tristatevalue="x")
rad_RT_5.grid(row=12, column=6, sticky=tk.W)


pdf_type_6 = tk.StringVar(value='LR')
rad_LR_6 = tk.Radiobutton(text='LR', variable=pdf_type_6,
                          value='LR')
rad_LR_6.grid(row=14, column=4, sticky=tk.W)

rad_HR_6 = tk.Radiobutton(text='HR', variable=pdf_type_6,
                          value='HR', tristatevalue="x")
rad_HR_6.grid(row=14, column=5, sticky=tk.W)

rad_RT_6 = tk.Radiobutton(text='RT', variable=pdf_type_6,
                          value='RT', tristatevalue="x")
rad_RT_6.grid(row=14, column=6, sticky=tk.W)


pdf_type_7 = tk.StringVar(value='LR')
rad_LR_7 = tk.Radiobutton(text='LR', variable=pdf_type_7,
                          value='LR')
rad_LR_7.grid(row=16, column=4, sticky=tk.W)

rad_HR_7 = tk.Radiobutton(text='HR', variable=pdf_type_7,
                          value='HR', tristatevalue="x")
rad_HR_7.grid(row=16, column=5, sticky=tk.W)

rad_RT_7 = tk.Radiobutton(text='RT', variable=pdf_type_7,
                          value='RT', tristatevalue="x")
rad_RT_7.grid(row=16, column=6, sticky=tk.W)

pdf_type_8 = tk.StringVar(value='LR')
rad_LR_8 = tk.Radiobutton(text='LR', variable=pdf_type_8,
                          value='LR')
rad_LR_8.grid(row=18, column=4, sticky=tk.W)

rad_HR_8 = tk.Radiobutton(text='HR', variable=pdf_type_8,
                          value='HR', tristatevalue="x")
rad_HR_8.grid(row=18, column=5, sticky=tk.W)

rad_RT_8 = tk.Radiobutton(text='RT', variable=pdf_type_8,
                          value='RT', tristatevalue="x")
rad_RT_8.grid(row=18, column=6, sticky=tk.W)


pdf_type_9 = tk.StringVar(value='LR')
rad_LR_9 = tk.Radiobutton(text='LR', variable=pdf_type_9,
                          value='LR')
rad_LR_9.grid(row=20, column=4, sticky=tk.W)

rad_HR_9 = tk.Radiobutton(text='HR', variable=pdf_type_9,
                          value='HR', tristatevalue="x")
rad_HR_9.grid(row=20, column=5, sticky=tk.W)

rad_RT_9 = tk.Radiobutton(text='RT', variable=pdf_type_9,
                          value='RT', tristatevalue="x")
rad_RT_9.grid(row=20, column=6, sticky=tk.W)


pdf_type_10 = tk.StringVar(value='LR')
rad_LR_10 = tk.Radiobutton(text='LR', variable=pdf_type_10,
                           value='LR')
rad_LR_10.grid(row=22, column=4, sticky=tk.W)

rad_HR_10 = tk.Radiobutton(text='HR', variable=pdf_type_10,
                           value='HR', tristatevalue="x")
rad_HR_10.grid(row=22, column=5, sticky=tk.W)

rad_RT_10 = tk.Radiobutton(text='RT', variable=pdf_type_10,
                           value='RT', tristatevalue="x")
rad_RT_10.grid(row=22, column=6, sticky=tk.W)


# User info

user = os.getlogin()

# Job labels
job_lbl1 = tk.Label(text=' ')
job_lbl2 = tk.Label(text=' ')
job_lbl3 = tk.Label(text=' ')
job_lbl4 = tk.Label(text=' ')
job_lbl5 = tk.Label(text=' ')
job_lbl6 = tk.Label(text=' ')
job_lbl7 = tk.Label(text=' ')
job_lbl8 = tk.Label(text=' ')
job_lbl9 = tk.Label(text=' ')
job_lbl10 = tk.Label(text=' ')

# PDF labels
pdf_lbl1 = tk.Label(text=' ')
pdf_lbl2 = tk.Label(text=' ')
pdf_lbl3 = tk.Label(text=' ')
pdf_lbl4 = tk.Label(text=' ')
pdf_lbl5 = tk.Label(text=' ')
pdf_lbl6 = tk.Label(text=' ')
pdf_lbl7 = tk.Label(text=' ')
pdf_lbl8 = tk.Label(text=' ')
pdf_lbl9 = tk.Label(text=' ')
pdf_lbl10 = tk.Label(text=' ')


# Multus Function


def multus():

    # Directory leading to jobs folder, will have to be modified

    parent_dir = r'C:\Users\{}\Desktop'.format(user)

    # Save paths for the PDFs

    hr_save_path_1 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_1.get() + '.pdf')
    lr_save_path_1 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_1.get() + '-LR.pdf')
    rt_save_path_1 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_1.get() + '-RT.pdf')

    hr_save_path_2 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_2.get() + '.pdf')
    lr_save_path_2 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_2.get() + '-LR.pdf')
    rt_save_path_2 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_2.get() + '-RT.pdf')

    hr_save_path_3 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_3.get() + '.pdf')
    lr_save_path_3 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_3.get() + '-LR.pdf')
    rt_save_path_3 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_3.get() + '-RT.pdf')

    hr_save_path_4 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_4.get() + '.pdf')
    lr_save_path_4 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_4.get() + '-LR.pdf')
    rt_save_path_4 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_4.get() + '-RT.pdf')

    hr_save_path_5 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_5.get() + '.pdf')
    lr_save_path_5 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_5.get() + '-LR.pdf')
    rt_save_path_5 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_5.get() + '-RT.pdf')

    hr_save_path_6 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_6.get() + '.pdf')
    lr_save_path_6 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_6.get() + '-LR.pdf')
    rt_save_path_6 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_6.get() + '-RT.pdf')

    hr_save_path_7 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_7.get() + '.pdf')
    lr_save_path_7 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_7.get() + '-LR.pdf')
    rt_save_path_7 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_7.get() + '-RT.pdf')

    hr_save_path_8 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_8.get() + '.pdf')
    lr_save_path_8 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_8.get() + '-LR.pdf')
    rt_save_path_8 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_8.get() + '-RT.pdf')

    hr_save_path_9 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_9.get() + '.pdf')
    lr_save_path_9 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_9.get() + '-LR.pdf')
    rt_save_path_9 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_9.get() + '-RT.pdf')

    hr_save_path_10 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_10.get() + '.pdf')
    lr_save_path_10 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_10.get() + '-LR.pdf')
    rt_save_path_10 = os.path.join(
        parent_dir, multusf_entry.get(), job_window_10.get() + '-RT.pdf')

    # Job directory, will have to be modified

    job_dir_1 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_1.get()))

    job_dir_2 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_2.get()))

    job_dir_3 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_3.get()))

    job_dir_4 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_4.get()))

    job_dir_5 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_5.get()))

    job_dir_6 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_6.get()))

    job_dir_7 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_7.get()))

    job_dir_8 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_8.get()))

    job_dir_9 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_9.get()))

    job_dir_10 = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window_10.get()))

    # Path to HR, LR, RT PDF types

    hr_job_path_1 = os.path.abspath(
        job_window_1.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_1.get() + '.pdf')

    lr_job_path_1 = os.path.abspath(
        job_window_1.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_1.get() + '-LR.pdf')

    rt_job_path_1 = os.path.abspath(
        job_window_1.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_1.get() + '-RT.pdf')

    hr_job_path_2 = os.path.abspath(
        job_window_2.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_2.get() + '.pdf')

    lr_job_path_2 = os.path.abspath(
        job_window_2.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_2.get() + '-LR.pdf')

    rt_job_path_2 = os.path.abspath(
        job_window_2.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_2.get() + '-RT.pdf')

    hr_job_path_3 = os.path.abspath(
        job_window_3.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_3.get() + '.pdf')

    lr_job_path_3 = os.path.abspath(
        job_window_3.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_3.get() + '-LR.pdf')

    rt_job_path_3 = os.path.abspath(
        job_window_3.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_3.get() + '-RT.pdf')

    hr_job_path_4 = os.path.abspath(
        job_window_4.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_4.get() + '.pdf')

    lr_job_path_4 = os.path.abspath(
        job_window_4.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_4.get() + '-LR.pdf')

    rt_job_path_4 = os.path.abspath(
        job_window_4.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_4.get() + '-RT.pdf')

    hr_job_path_5 = os.path.abspath(
        job_window_5.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_5.get() + '.pdf')

    lr_job_path_5 = os.path.abspath(
        job_window_5.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_5.get() + '-LR.pdf')

    rt_job_path_5 = os.path.abspath(
        job_window_5.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_5.get() + '-RT.pdf')

    hr_job_path_6 = os.path.abspath(
        job_window_6.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_6.get() + '.pdf')

    lr_job_path_6 = os.path.abspath(
        job_window_6.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_6.get() + '-LR.pdf')

    rt_job_path_6 = os.path.abspath(
        job_window_6.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_6.get() + '-RT.pdf')

    hr_job_path_7 = os.path.abspath(
        job_window_7.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_7.get() + '.pdf')

    lr_job_path_7 = os.path.abspath(
        job_window_7.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_7.get() + '-LR.pdf')

    rt_job_path_7 = os.path.abspath(
        job_window_7.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_7.get() + '-RT.pdf')

    hr_job_path_8 = os.path.abspath(
        job_window_8.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_8.get() + '.pdf')

    lr_job_path_8 = os.path.abspath(
        job_window_8.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_8.get() + '-LR.pdf')

    rt_job_path_8 = os.path.abspath(
        job_window_8.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_8.get() + '-RT.pdf')

    hr_job_path_9 = os.path.abspath(
        job_window_9.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_9.get() + '.pdf')

    lr_job_path_9 = os.path.abspath(
        job_window_9.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_9.get() + '-LR.pdf')

    rt_job_path_9 = os.path.abspath(
        job_window_9.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_9.get() + '-RT.pdf')

    hr_job_path_10 = os.path.abspath(
        job_window_10.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window_10.get() + '.pdf')

    lr_job_path_10 = os.path.abspath(
        job_window_10.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window_10.get() + '-LR.pdf')

    rt_job_path_10 = os.path.abspath(
        job_window_10.get() + '/Nexus_Files/Raster_PDF' + '/' + job_window_10.get() + '-RT.pdf')

    # Will create Multus Folder

    if not os.path.exists(os.path.join(parent_dir, multusf_entry.get())):
        print('The new folder {} has been created!'.format(multusf_entry.get()))
        os.makedirs(os.path.join(parent_dir, multusf_entry.get()))
    else:
        print('{} Folder already exist. Will continue on.'.format(
            multusf_entry.get()))

    # Checks user entires for job folder

    if job_dir_1:
        if len(job_window_1.get()) == 7:
            if pdf_type_1.get() == 'HR':
                with open(hr_job_path_1, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_1, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl1.config(image=checkmark_img)
                        pdf_lbl1.grid(row=5, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_1.get() == 'LR':
                with open(lr_job_path_1, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_1, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl1.config(image=checkmark_img)
                        pdf_lbl1.grid(row=5, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_1.get() == 'RT':
                with open(rt_job_path_1, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                    with open(rt_save_path_1, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Raster PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl1.config(image=checkmark_img)
                        pdf_lbl1.grid(row=5, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)
        else:
            job_lbl1.config(
                text='(No user input)', fg='#000000')
            job_lbl1.grid(row=5, column=0, columnspan=7,
                          padx=8, sticky=tk.W)
    else:
        job_lbl1.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl1.grid(row=5, column=0, columnspan=7,
                      padx=8, sticky=tk.W)

    if job_dir_2:
        if len(job_window_2.get()) == 7:
            if pdf_type_2.get() == 'HR':
                with open(hr_job_path_2, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_2, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl2.config(image=checkmark_img)
                        pdf_lbl2.grid(row=7, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_2.get() == 'LR':
                with open(lr_job_path_2, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_2, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl2.config(image=checkmark_img)
                        pdf_lbl2.grid(row=7, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_2.get() == 'RT':
                with open(rt_job_path_2, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                    with open(rt_save_path_2, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Raster PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl2.config(image=checkmark_img)
                        pdf_lbl2.grid(row=7, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)
        else:
            job_lbl2.config(
                text='(No user input)', fg='#000000')
            job_lbl2.grid(row=7, column=0, columnspan=7,
                          padx=8, sticky=tk.W)
    else:
        job_lbl2.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl2.grid(row=7, column=0, columnspan=7,
                      padx=8, sticky=tk.W)

    if job_dir_3:
        if len(job_window_3.get()) == 7:
            if pdf_type_3.get() == 'HR':
                with open(hr_job_path_3, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_3, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl3.config(image=checkmark_img)
                        pdf_lbl3.grid(row=9, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_3.get() == 'LR':
                with open(lr_job_path_3, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_3, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl3.config(image=checkmark_img)
                        pdf_lbl3.grid(row=9, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_3.get() == 'RT':
                with open(rt_job_path_3, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                with open(rt_save_path_3, 'wb') as outputfile:

                    copier.write(outputfile)
                    print('Raster PDFs have been copied and saved to {}'.format(
                        multusf_entry.get()))
                    pdf_lbl3.config(image=checkmark_img)
                    pdf_lbl3.grid(row=9, column=0, columnspan=7,
                                  padx=8, sticky=tk.W)
        else:
            job_lbl3.config(
                text='(No user input)', fg='#000000')
            job_lbl3.grid(row=9, column=0, columnspan=7,
                          padx=8, sticky=tk.W)
    else:
        job_lbl3.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl3.grid(row=9, column=0, columnspan=7,
                      padx=8, sticky=tk.W)

    if job_dir_4:
        if len(job_window_4.get()) == 7:
            if pdf_type_4.get() == 'HR':
                with open(hr_job_path_4, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_4, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl4.config(image=checkmark_img)
                        pdf_lbl4.grid(row=11, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_4.get() == 'LR':
                with open(lr_job_path_4, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_4, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl4.config(image=checkmark_img)
                        pdf_lbl4.grid(row=11, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_4.get() == 'RT':
                with open(rt_job_path_4, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                    with open(rt_save_path_4, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Raster PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl4.config(image=checkmark_img)
                        pdf_lbl4.grid(row=11, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)
        else:
            job_lbl4.config(
                text='(No user input)', fg='#000000')
            job_lbl4.grid(row=11, column=0, columnspan=7,
                          padx=8, sticky=tk.W)

    else:
        job_lbl4.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl4.grid(row=11, column=0, columnspan=7,
                      padx=8, sticky=tk.W)

    if job_dir_5:
        if len(job_window_5.get()) == 7:

            if pdf_type_5.get() == 'HR':
                with open(hr_job_path_5, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_5, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl5.config(image=checkmark_img)
                        pdf_lbl5.grid(row=13, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_5.get() == 'LR':
                with open(lr_job_path_5, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_5, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl5.config(image=checkmark_img)
                        pdf_lbl5.grid(row=13, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_5.get() == 'RT':
                with open(rt_job_path_5, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                    with open(rt_save_path_5, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Raster PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl5.config(image=checkmark_img)
                        pdf_lbl5.grid(row=13, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)
        else:
            job_lbl5.config(
                text='(No user input)', fg='#000000')
            job_lbl5.grid(row=13, column=0, columnspan=7,
                          padx=8, sticky=tk.W)
    else:
        job_lbl5.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl5.grid(row=13, column=0, columnspan=7,
                      padx=8, sticky=tk.W)

    if job_dir_6:
        if len(job_window_6.get()) == 7:
            if pdf_type_6.get() == 'HR':
                with open(hr_job_path_6, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_6, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl6.config(image=checkmark_img)
                        pdf_lbl6.grid(row=15, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_6.get() == 'LR':
                with open(lr_job_path_6, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_6, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl6.config(image=checkmark_img)
                        pdf_lbl6.grid(row=15, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_6.get() == 'RT':
                with open(rt_job_path_6, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                    with open(rt_save_path_6, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Raster PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl6.config(image=checkmark_img)
                        pdf_lbl6.grid(row=15, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)
        else:
            job_lbl6.config(
                text='(No user input)', fg='#000000')
            job_lbl6.grid(row=15, column=0, columnspan=7,
                          padx=8, sticky=tk.W)
    else:
        job_lbl6.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl6.grid(row=15, column=0, columnspan=7,
                      padx=8, sticky=tk.W)

    if job_dir_7:
        if len(job_window_7.get()) == 7:
            if pdf_type_7.get() == 'HR':
                with open(hr_job_path_7, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_7, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl7.config(image=checkmark_img)
                        pdf_lbl7.grid(row=17, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_7.get() == 'LR':
                with open(lr_job_path_7, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_7, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl7.config(image=checkmark_img)
                        pdf_lbl7.grid(row=17, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_7.get() == 'RT':
                with open(rt_job_path_7, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                    with open(rt_save_path_7, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Raster PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl7.config(image=checkmark_img)
                        pdf_lbl7.grid(row=17, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)
        else:
            job_lbl7.config(
                text='(No user input)', fg='#000000')
            job_lbl7.grid(row=17, column=0, columnspan=7,
                          padx=8, sticky=tk.W)

    else:
        job_lbl7.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl7.grid(row=17, column=0, columnspan=7,
                      padx=8, sticky=tk.W)

    if job_dir_8:
        if len(job_window_8.get()) == 7:
            if pdf_type_8.get() == 'HR':
                with open(hr_job_path_8, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_8, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl8.config(image=checkmark_img)
                        pdf_lbl8.grid(row=19, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_8.get() == 'LR':
                with open(lr_job_path_8, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_8, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl8.config(image=checkmark_img)
                        pdf_lbl8.grid(row=19, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_8.get() == 'RT':
                with open(rt_job_path_8, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                    with open(rt_save_path_8, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Raster PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl8.config(image=checkmark_img)
                        pdf_lbl8.grid(row=19, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)
        else:
            job_lbl8.config(
                text='(No user input)', fg='#000000')
            job_lbl8.grid(row=19, column=0, columnspan=7,
                          padx=8, sticky=tk.W)

    else:
        job_lbl8.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl8.grid(row=19, column=0, columnspan=7,
                      padx=8, sticky=tk.W)

    if job_dir_9:
        if len(job_window_9.get()) == 7:
            if pdf_type_9.get() == 'HR':
                with open(hr_job_path_9, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_9, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl9.config(image=checkmark_img)
                        pdf_lbl9.grid(row=21, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_9.get() == 'LR':
                with open(lr_job_path_9, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_9, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl9.config(image=checkmark_img)
                        pdf_lbl9.grid(row=21, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)

            elif pdf_type_9.get() == 'RT':
                with open(rt_job_path_9, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                    with open(rt_save_path_9, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Raster PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl9.config(image=checkmark_img)
                        pdf_lbl9.grid(row=21, column=0, columnspan=7,
                                      padx=8, sticky=tk.W)
        else:
            job_lbl9.config(
                text='(No user input)', fg='#000000')
            job_lbl9.grid(row=21, column=0, columnspan=7,
                          padx=8, sticky=tk.W)
    else:
        job_lbl9.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl9.grid(row=21, column=0, columnspan=7,
                      padx=8, sticky=tk.W)

    if job_dir_10:
        if len(job_window_10.get()) == 7:
            if pdf_type_10.get() == 'HR':
                with open(hr_job_path_10, 'rb') as new_hr:
                    hirez = PyPDF2.PdfFileReader(new_hr)
                    hr_copy = hirez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(hr_copy)

                    with open(hr_save_path_10, 'wb') as outputfile:
                        copier.write(outputfile)
                        print('High Res has been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl10.config(image=checkmark_img)
                        pdf_lbl10.grid(row=23, column=0, columnspan=7,
                                       padx=8, sticky=tk.W)

            elif pdf_type_10.get() == 'LR':
                with open(lr_job_path_10, 'rb') as new_lr:
                    lorez = PyPDF2.PdfFileReader(new_lr)
                    lr_copy = lorez.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(lr_copy)

                    with open(lr_save_path_10, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Low-Res PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl10.config(image=checkmark_img)
                        pdf_lbl10.grid(row=23, column=0, columnspan=7,
                                       padx=8, sticky=tk.W)

            elif pdf_type_10.get() == 'RT':
                with open(rt_job_path_10, 'rb') as new_rt:
                    raster = PyPDF2.PdfFileReader(new_rt)
                    rt_copy = raster.getPage(0)
                    copier = PyPDF2.PdfFileWriter()
                    copier.addPage(rt_copy)

                    with open(rt_save_path_10, 'wb') as outputfile:

                        copier.write(outputfile)
                        print('Raster PDFs have been copied and saved to {}'.format(
                            multusf_entry.get()))
                        pdf_lbl10.config(image=checkmark_img)
                        pdf_lbl10.grid(row=23, column=0, columnspan=7,
                                       padx=8, sticky=tk.W)
        else:
            job_lbl10.config(
                text='(No user input)', fg='#000000')
            job_lbl10.grid(row=23, column=0, columnspan=7,
                           padx=8, sticky=tk.W)
    else:
        job_lbl10.config(
            text='Job not found. Please recheck your entry.', fg='#FF0000')
        job_lbl10.grid(row=23, column=0, columnspan=7,
                       padx=8, sticky=tk.W)

# Clears all user entries


def clear():

    job_window_1.delete(0, tk.END)
    job_window_2.delete(0, tk.END)
    job_window_3.delete(0, tk.END)
    job_window_4.delete(0, tk.END)
    job_window_5.delete(0, tk.END)
    job_window_6.delete(0, tk.END)
    job_window_7.delete(0, tk.END)
    job_window_8.delete(0, tk.END)
    job_window_9.delete(0, tk.END)
    job_window_10.delete(0, tk.END)

    job_lbl1.config(text=' ', image='')
    job_lbl2.config(text=' ', image='')
    job_lbl3.config(text=' ', image='')
    job_lbl4.config(text=' ', image='')
    job_lbl5.config(text=' ', image='')
    job_lbl6.config(text=' ', image='')
    job_lbl7.config(text=' ', image='')
    job_lbl8.config(text=' ', image='')
    job_lbl9.config(text=' ', image='')
    job_lbl10.config(text=' ', image='')

    pdf_lbl1.config(text=' ', image='')
    pdf_lbl2.config(text=' ', image='')
    pdf_lbl3.config(text=' ', image='')
    pdf_lbl4.config(text=' ', image='')
    pdf_lbl5.config(text=' ', image='')
    pdf_lbl6.config(text=' ', image='')
    pdf_lbl7.config(text=' ', image='')
    pdf_lbl8.config(text=' ', image='')
    pdf_lbl9.config(text=' ', image='')
    pdf_lbl10.config(text=' ', image='')


# Multus function button
multus_button = tk.Button(command=multus, image=ccbutton_img, borderwidth=0)
multus_button.grid(row=24, column=0,   sticky=tk.W, padx=10, pady=8)

# Clear function button
clear_button = tk.Button(command=clear, borderwidth=0, image=clearbutton_img)
clear_button.grid(row=24, column=1, columnspan=7, sticky=tk.W, pady=10, padx=8)

root.mainloop()

# CL3188
