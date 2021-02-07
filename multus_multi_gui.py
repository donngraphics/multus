import PyPDF2
import os
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.wm_title('Multus')

root.geometry('320x750')

root.iconbitmap(r'images\DG.ico')

header_img = ImageTk.PhotoImage(Image.open(r'images\DG_banner2.png'))
ccbutton_img = ImageTk.PhotoImage(Image.open(r'images\ccbutton-01.png'))
exitButton_img = ImageTk.PhotoImage(Image.open(r'images\exitbutton.png'))


cslogo_label = tk.Label(borderwidth=5, image=header_img)
cslogo_label.grid(row=0, column=0, columnspan=14)

multusf_label = tk.Label(
    text='Please enter the desktop folder name:')
multusf_label.grid(row=1, column=0, padx=8, columnspan=14, sticky=tk.W)

multusf_entry = tk.Entry(width=30, bg='white', borderwidth=3)
multusf_entry.grid(row=2, column=0, columnspan=14,
                   padx=8, pady=8, sticky=tk.W)
multusf_entry.insert(0, "Multus_Folder")

job_label = tk.Label(
    text='Please enter the Job Number below:')
job_label.grid(row=3, column=0, columnspan=14, padx=8, sticky=tk.W)

job_list = []

for x in reversed(range(10)):

    job_window = tk.Entry(width=30, bg='white',
                          borderwidth=3)
    job_window.grid(row=x+4, column=0, columnspan=14,
                    padx=8, pady=8, sticky=tk.W)
    job_list.append(job_window)


radPDF_lbl = tk.Label(text='Please select the PDF type:')
radPDF_lbl.grid(row=15, column=0, columnspan=14,
                padx=8, pady=8, sticky=tk.W)

pdf_type = tk.StringVar(value='LR')
rad_LR = tk.Radiobutton(text='LR', variable=pdf_type,
                        value='LR')
rad_LR.grid(row=16, column=0, padx=8, sticky=tk.W)

rad_HR = tk.Radiobutton(text='HR', variable=pdf_type,
                        value='HR', tristatevalue="x")
rad_HR.grid(row=16, column=1, sticky=tk.W)

rad_HT = tk.Radiobutton(text='RT', variable=pdf_type,
                        value='RT', tristatevalue="x")
rad_HT.grid(row=16, column=2, sticky=tk.W)


user = os.getlogin()

job_lbl1 = tk.Label(text=' ')
pdf_lbl1 = tk.Label(text=' ')


def multus():

    for jobs in job_list:
        job_listGet = ''
        job_listGet = jobs.get()

        parent_dir = r'C:\Users\{}\Desktop'.format(user)

        hr_save_path = os.path.join(
            parent_dir, multusf_entry.get(), job_listGet + '.pdf')
        lr_save_path = os.path.join(
            parent_dir, multusf_entry.get(), job_listGet + '-LR.pdf')
        rt_save_path = os.path.join(
            parent_dir, multusf_entry.get(), job_listGet + '-RT.pdf')

        job_dir = os.path.isdir(os.path.join(
            parent_dir, 'Multus', job_listGet))

        hr_job_path = os.path.abspath(
            job_listGet + '/Nexus_Files/HiRes_PDF' + '/' + job_listGet + '.pdf')

        lr_job_path = os.path.abspath(
            job_listGet + '/Nexus_Files/Softproof_PDF' + '/' + job_listGet + '-LR.pdf')

        rt_job_path = os.path.abspath(
            job_listGet + '/Nexus_Files/Raster_PDF' + '/' + job_listGet + '-RT.pdf')

        if not os.path.exists(os.path.join(parent_dir, multusf_entry.get())):
            print('The new folder {} has been created!'.format(multusf_entry.get()))
            os.makedirs(os.path.join(parent_dir, multusf_entry.get()))
        else:
            print('{} Folder already exist. Will continue on.'.format(
                multusf_entry.get()))

        try:
            if not job_listGet.isdigit() or len(job_listGet) < 7 or job_dir == False:
                job_lbl1.config(
                    text='One or more Jobs not found. Please recheck entries.', fg='#FF0000')
                job_lbl1.grid(row=19, column=0, columnspan=14,
                              padx=8, sticky=tk.W)
                continue

            else:
                job_lbl1.config(
                    text='No issues found, verify folder contents', fg='#000000')
                job_lbl1.grid(row=19, column=0, padx=8,
                              columnspan=14, sticky=tk.W)

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
                    pdf_lbl1.config(text='Hi-Res PDFs copied to {}'.format(
                        multusf_entry.get()))
                    pdf_lbl1.grid(row=20, column=0, columnspan=14,
                                  sticky=tk.W, padx=8)

        elif pdf_type.get() == 'LR':
            with open(lr_job_path, 'rb') as new_lr:
                lorez = PyPDF2.PdfFileReader(new_lr)
                lr_copy = lorez.getPage(0)
                copier = PyPDF2.PdfFileWriter()
                copier.addPage(lr_copy)

                with open(lr_save_path, 'wb') as outputfile:

                    copier.write(outputfile)
                    print('Low-Res PDFs have been copied and saved to {}'.format(
                        multusf_entry.get()))
                    pdf_lbl1.config(text='Lo-Res PDFs copied to {}'.format(
                        multusf_entry.get()))
                    pdf_lbl1.grid(row=20, column=0, columnspan=14,
                                  sticky=tk.W, padx=8)

        elif pdf_type.get() == 'RT':
            with open(rt_job_path, 'rb') as new_rt:
                raster = PyPDF2.PdfFileReader(new_rt)
                rt_copy = raster.getPage(0)
                copier = PyPDF2.PdfFileWriter()
                copier.addPage(rt_copy)

                with open(rt_save_path, 'wb') as outputfile:

                    copier.write(outputfile)
                    print('Raster PDFs have been copied and saved to {}'.format(
                        multusf_entry.get()))
                    pdf_lbl1.config(text='Raster PDFs copied to {}'.format(
                        multusf_entry.get()))
                    pdf_lbl1.grid(row=20, column=0, columnspan=14,
                                  sticky=tk.W, padx=8)


def clear():

    job_window.delete(0, tk.END)
    job_lbl1.config(text=' ')
    pdf_lbl1.config(text=' ')


multus_button = tk.Button(command=multus, image=ccbutton_img, borderwidth=0)
multus_button.grid(row=17, column=0, columnspan=14, sticky=tk.W, padx=8)

clear_button = tk.Button(command=clear, borderwidth=1, text="CLEAR")
clear_button.grid(row=17, column=2, sticky=tk.W, padx=8)

job_lbl1.grid_forget()

root.mainloop()

# CL3188
