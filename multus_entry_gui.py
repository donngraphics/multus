import PyPDF2
import os
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.wm_title('Multus')

root.geometry('350x300')

root.iconbitmap(r'images\DG.ico')

header_img = ImageTk.PhotoImage(Image.open(r'images\DG_banner2.png'))


cslogo_label = tk.Label(borderwidth=5, image=header_img)
cslogo_label.grid(row=0, column=0, columnspan=4)

multusf_label = tk.Label(
    text='Please enter the desktop folder name:')
multusf_label.grid(row=1, column=0, padx=8, sticky=tk.W)

multusf_entry = tk.Entry(width=30, bg='white', borderwidth=3)
multusf_entry.grid(row=2, column=0, padx=8, pady=8, sticky=tk.W)
multusf_entry.insert(0, "Multus_Folder")

job_label = tk.Label(
    text='Please enter the Job Number below, then select the PDF type:')
job_label.grid(row=3, column=0, columnspan=4, padx=8, sticky=tk.W)


job_window = tk.Entry(width=30, bg='white',
                      borderwidth=3)
job_window.grid(row=4, column=0, padx=8, pady=8, sticky=tk.W)


pdf_type = tk.StringVar(value='LR')
rad_LR = tk.Radiobutton(text='LR', variable=pdf_type,
                        value='LR')
rad_LR.grid(row=4, column=1, sticky=tk.W)

rad_HR = tk.Radiobutton(text='HR', variable=pdf_type,
                        value='HR', tristatevalue="x")
rad_HR.grid(row=4, column=2, sticky=tk.W)

rad_HT = tk.Radiobutton(text='RT', variable=pdf_type,
                        value='RT', tristatevalue="x")
rad_HT.grid(row=4, column=3, sticky=tk.W)

job_lbl1 = tk.Label(text=' ')
pdf_lbl1 = tk.Label(text=' ')

user = os.getlogin()


def multus():

    parent_dir = r'C:\Users\{}\Desktop'.format(user)

    # multus_dir = os.path.isdir(os.path.join(parent_dir, multusf_entry.get()))

    hr_save_path = os.path.join(
        parent_dir, multusf_entry.get(), job_window.get() + '.pdf')
    lr_save_path = os.path.join(
        parent_dir, multusf_entry.get(), job_window.get() + '-LR.pdf')
    rt_save_path = os.path.join(
        parent_dir, multusf_entry.get(), job_window.get() + '-RT.pdf')

    job_dir = os.path.isdir(os.path.join(
        parent_dir, 'Multus', job_window.get()))

    hr_job_path = os.path.abspath(
        job_window.get() + '/Nexus_Files/HiRes_PDF' + '/' + job_window.get() + '.pdf')

    lr_job_path = os.path.abspath(
        job_window.get() + '/Nexus_Files/Softproof_PDF' + '/' + job_window.get() + '-LR.pdf')

    rt_job_path = os.path.abspath(job_window.get(
    ) + '/Nexus_Files/Raster_PDF' + '/' + job_window.get() + '-RT.pdf')

    if not os.path.exists(os.path.join(parent_dir, multusf_entry.get())):
        print('The new folder {} has been created!'.format(multusf_entry.get()))
        os.makedirs(os.path.join(parent_dir, multusf_entry.get()))
    else:
        print('{} Folder already exist. Will continue on.'.format(
            multusf_entry.get()))

    try:
        if not job_window.get().isdigit() or len(job_window.get()) < 7 or job_dir == False:
            job_lbl1.config(
                text='No such job number. Please try again', fg='#FF0000')
            job_lbl1.grid(row=5, column=0, padx=8, sticky=tk.W)

        else:
            job_lbl1.config(
                text='{} returns {}'.format(job_window.get(), job_dir))
        job_lbl1.grid(row=5, column=0, sticky=tk.W)

    except ValueError as error:
        print(error)

    if pdf_type.get() == 'HR':
        with open(hr_job_path, 'rb') as new_hr:
            hirez = PyPDF2.PdfFileReader(new_hr)
            hr_copy = hirez.getPage(0)
            copier = PyPDF2.PdfFileWriter()
            copier.addPage(hr_copy)

            with open(hr_save_path, 'wb') as outputfile:
                copier.write(outputfile)
                print('High Res has been copied and saved to {}'.format(
                    multusf_entry.get()))
                pdf_lbl1.config(text='Hi Res PDF has been copied and saved to {}'.format(
                    multusf_entry.get()))
                pdf_lbl1.grid(row=7, column=0, columnspan=4,
                              sticky=tk.W, padx=8)

    elif pdf_type.get() == 'LR':
        with open(lr_job_path, 'rb') as new_lr:
            lorez = PyPDF2.PdfFileReader(new_lr)
            lr_copy = lorez.getPage(0)
            copier = PyPDF2.PdfFileWriter()
            copier.addPage(lr_copy)

            with open(lr_save_path, 'wb') as outputfile:

                copier.write(outputfile)
                print('Low Res has been copied and saved to {}'.format(
                    multusf_entry.get()))
                pdf_lbl1.config(text='Lo Res PDF has been copied and saved to {}'.format(
                    multusf_entry.get()))
                pdf_lbl1.grid(row=7, column=0, columnspan=4,
                              sticky=tk.W, padx=8)

    elif pdf_type.get() == 'RT':
        with open(rt_job_path, 'rb') as new_rt:
            raster = PyPDF2.PdfFileReader(new_rt)
            rt_copy = raster.getPage(0)
            copier = PyPDF2.PdfFileWriter()
            copier.addPage(rt_copy)

            with open(rt_save_path, 'wb') as outputfile:

                copier.write(outputfile)
                print('Raster PDF has been copied and saved to {}'.format(
                    multusf_entry.get()))
                pdf_lbl1.config(text='Raster PDF has been copied and saved to {}'.format(
                    multusf_entry.get()))
                pdf_lbl1.grid(row=7, column=0, columnspan=4,
                              sticky=tk.W, padx=8)


multus_button = tk.Button(text='Click Here',  font=('', 10),
                          command=multus, bg='#7ac141', fg='#ffffff', borderwidth=1)


multus_button.grid(row=6, column=0, sticky=tk.W, padx=8)

exit_button = tk.Button(text='Exit', font=(
    '', 10), command=root.quit, borderwidth=1)
exit_button.grid(row=6, column=1)

root.mainloop()
