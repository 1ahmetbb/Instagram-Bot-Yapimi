import instaloader
import tkinter as tk
from tkinter import messagebox

def download_post():
    username = entry_userName.get()

    try:
        #nesne olustur
        bot = instaloader.Instaloader()

        #profil listesi olusturma
        profile = instaloader.Profile.from_username(bot.context, username)

        #kullanici gonderilerini al
        posts= profile.get_posts()

        #gonderileri indir
        for index,post in enumerate(posts, 1):
            bot.download_post(post, target=f'{profile.username}_{index}')

        #Basari mesaji
        messagebox.showinfo('Basarili','Gonderiler indirildi')
    except Exception as e:
        messagebox.showerror('hata', str(e))
    


root = tk.Tk()
root.title('Instagram Gonderi Indirici')
root.geometry('300x200')

label = tk.Label(root, text='Kullanici Adi:')
label.pack(pady=10)

entry_userName = tk.Entry(root)
entry_userName.pack()

download_button = tk.Button(root, text='Bilgileri Indir', command=download_post)
download_button.pack()




root.mainloop()
