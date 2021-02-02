import PyPDF2
import os


def multus():
    u_num = int(input('How many jobs this time around?: '))
    for u_num in range(u_num):
        u_jobnum = input('Please input the Print Number: ')

        u_multus_folder = input('Name of desktop folder: ') or "Multus_Folder"

        u_file = input('Which filetype? (HR, LR, etc...): ').upper()

        user = os.getlogin()

        parent_dir = r'C:\Users\{}\Desktop'.format(user)

        #multus_dir = os.path.isdir(os.path.join(parent_dir, u_multus_folder))

        hr_save_path = os.path.join(
            parent_dir, u_multus_folder, u_jobnum + '.pdf')
        lr_save_path = os.path.join(
            parent_dir, u_multus_folder, u_jobnum + '-LR.pdf')

        job_dir = os.path.isdir(os.path.join(parent_dir, 'Multus', u_jobnum))

        hr_job_path = os.path.abspath(
            u_jobnum + '/Nexus_Files/HiRes_PDF' + '/' + u_jobnum + '.pdf')

        lr_job_path = os.path.abspath(
            u_jobnum + '/Nexus_Files/Softproof_PDF' + '/' + u_jobnum + '-LR.pdf')

        try:
            if not u_jobnum.isdigit() or len(u_jobnum) < 7 or job_dir == False:
                print('Please recheck your Print Number')
                continue
            else:
                print('{} returns {}'.format(u_jobnum, job_dir))

            if not u_file:
                print('Please enter a repsonse for the filetype.')
                continue
            elif u_file in ('HR', 'LR'):
                print('You selected {}'.format(u_file))
                pass
            else:
                print('For this test, please input \'HR\' or \'LR\'')
                continue

        except ValueError as error:
            print(error)

        if not os.path.exists(os.path.join(parent_dir, u_multus_folder)):
            print('The new folder {} has been created!'.format(u_multus_folder))
            os.makedirs(os.path.join(parent_dir, u_multus_folder))
        else:
            print('{} Folder already exist. Will continue on.'.format(u_multus_folder))

        if u_file == 'HR':
            with open(hr_job_path, 'rb') as new_hr:
                hirez = PyPDF2.PdfFileReader(new_hr)
                hr_copy = hirez.getPage(0)
                copier = PyPDF2.PdfFileWriter()
                copier.addPage(hr_copy)

                with open(hr_save_path, 'wb') as outputfile:
                    copier.write(outputfile)
                    print('High Res has been copied and saved to {}'.format(
                        u_multus_folder))

        elif u_file == 'LR':
            with open(lr_job_path, 'rb') as new_lr:
                lorez = PyPDF2.PdfFileReader(new_lr)
                lr_copy = lorez.getPage(0)
                copier = PyPDF2.PdfFileWriter()
                copier.addPage(lr_copy)

                with open(lr_save_path, 'wb') as outputfile:

                    copier.write(outputfile)
                    print('Low Res has been copied and saved to {}'.format(
                        u_multus_folder))

        else:
            print('Something went wrong...')


multus()
