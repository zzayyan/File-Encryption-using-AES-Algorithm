import PySimpleGUI as sg
import pyAesCrypt
import os


def encrypt():

    buffer_size = 64 * 1024
    og_filename = os.path.basename(path_to_og_file)

    if len(encryption_password) >= 1:
        try:
            pyAesCrypt.encryptFile(path_to_og_file, os.path.join(save_encrypted_file_to, og_filename + ".encryption"), encryption_password, buffer_size)
            sg.popup("File encrypted.")
        except IOError:
            sg.popup("File not found or permission denied. Please choose another directory to save the file.", title="Oh snap!")
    else:
        sg.popup("Please choose a password.", title="Oh snap!")


def decrypt():

    buffer_size = 64 * 1024
    encrypted_file_sans_path = os.path.basename(path_to_encrypted_file)
    decrypted_file = encrypted_file_sans_path.replace(".encryption", "")

    if ".encryption" in path_to_encrypted_file:
        try:
            pyAesCrypt.decryptFile(path_to_encrypted_file, os.path.join(save_decrypted_file_to, decrypted_file), decryption_password, buffer_size)
            sg.popup("File decrypted.")
        except ValueError as ve:  # Checks if the password is correct or if the file is corrupted.
            sg.popup(ve, title="Oh snap!")
        except IOError:
            sg.popup("Permission denied. Please choose another directory to save the file.", title="Oh snap!")
    else:
        sg.popup("Please choose an encrypted .encryption file.", title="Oh snap!")


# GUI theme and layout
sg.theme("DarkGrey2")

layout = [[sg.Text("Brillianta Zayyan M")],
          [sg.Text("210535614881")],
          [sg.Text("KRIPTOGRAFI")],
          [sg.Text("_"*16)],
          [sg.Text("Enkripsi")],
          [sg.Text("Pilih file yang akan dienkripsi:"), sg.In(), sg.FileBrowse()],
          [sg.Text("Simpan file di:                      "), sg.In(), sg.FolderBrowse()],
          [sg.Text("Membuat password untuk file:"), sg.InputText(), sg.Button("Encrypt")],
          [sg.Text("_"*86)],
          [sg.Text("Dekripsi")],
          [sg.Text("Pilih file yang akan didekripsi:"), sg.In(), sg.FileBrowse()],
          [sg.Text("Simpan file di:                      "), sg.In(), sg.FolderBrowse()],
          [sg.Text("Masukan password file:         "), sg.InputText(), sg.Button("Decrypt")],
          [sg.Button("Keluar")],
          [sg.Text("")]]

# Create the Window
window = sg.Window("Aplikasi Enkripsi File", layout, icon="protec.ico")

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    path_to_og_file = values[0]
    save_encrypted_file_to = values[1]
    encryption_password = values[2]
    path_to_encrypted_file = values[3]
    save_decrypted_file_to = values[4]
    decryption_password = values[5]

    if event in (None, "Quit"):  # if user closes window or clicks cancel
        break

    # Encryption
    if event == "Encrypt":
        encrypt()
    # Decryption
    if event == "Decrypt":
        decrypt()

window.close()
