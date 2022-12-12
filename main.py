from tkinter import *
from PIL import Image, ImageTk
from Speed_Class import InternetSpeed
from Twitter_Class import TwitterPost

HD_FONT = ("Helvetica", 15, "bold")
LB_FONT = ("Helvetica", 12, "bold")
TX_FONT = ("Helvetica", 13, "normal")


class TwitterInternetBot:
    def __init__(self, window):
        self.window = window
        self.window.title("Twitter Bot")
        self.window.geometry("652x575")
        # extra variables:
        self.provider_name = StringVar()

        self.head = Label(self.window, text="Tweet - If Your Internet Speed is Slower than It should Be",
                          justify="center", bd=1, highlightthickness=1, relief=RIDGE, font=HD_FONT, fg="indigo")
        self.head.place(x=5, y=5, width=642, height=60)

        twitter_image = Image.open("IMG/twitter.png")
        twitter_photo = ImageTk.PhotoImage(twitter_image)
        self.twitter_label = Label(self.window, image=twitter_photo)
        self.twitter_label.image = twitter_photo
        self.twitter_label.place(x=5, y=70, width=202, height=202)

        help_image = Image.open("IMG/help.png")
        help_photo = ImageTk.PhotoImage(help_image)
        self.help_label = Label(self.window, image=help_photo)
        self.help_label.image = help_photo
        self.help_label.place(x=220, y=93, width=212, height=152)

        speed_image = Image.open("IMG/speed.png")
        speed_photo = ImageTk.PhotoImage(speed_image)
        self.speed_label = Label(self.window, image=speed_photo)
        self.speed_label.image = speed_photo
        self.speed_label.place(x=445, y=70, width=202, height=202)

        self.center = Frame(self.window, bd=1, highlightthickness=1, relief=RIDGE, bg="beige")
        self.center.place(x=5, y=276, width=642, height=275)

        self.check_button = Button(self.center, text="Check Your Internet Speed", justify="center", font=LB_FONT,
                                   bd=1, highlightthickness=1, relief=RIDGE, wraplength=180, bg="pale green",
                                   command=self.check_method)
        self.check_button.place(x=5, y=5, width=205, height=65)

        self.download = Label(self.center, text="Download Speed", justify="center", font=LB_FONT,
                              bd=1, highlightthickness=1, relief=RIDGE)
        self.download.place(x=215, y=5, width=205, height=30)

        self.upload = Label(self.center, text="Upload Speed", justify="center", font=LB_FONT,
                            bd=1, highlightthickness=1, relief=RIDGE)
        self.upload.place(x=425, y=5, width=207, height=30)

        self.download_answer = Label(self.center, text="", justify="center", font=LB_FONT, bg="light cyan",
                                     bd=1, highlightthickness=1, relief=RIDGE)
        self.download_answer.place(x=215, y=40, width=205, height=30)

        self.upload_answer = Label(self.center, text="", justify="center", font=LB_FONT, bg="light cyan",
                                   bd=1, highlightthickness=1, relief=RIDGE)
        self.upload_answer.place(x=425, y=40, width=207, height=30)

        self.complain = Text(self.center, font=TX_FONT, bd=1, highlightthickness=1, relief=RIDGE, bg="beige")
        self.complain.place(x=5, y=80, width=628, height=100)

        self.provider = Label(self.center, text="Enter Provider Name", justify="center", font=LB_FONT,
                              bd=1, highlightthickness=1, relief=RIDGE)
        self.provider.place(x=5, y=185, width=310, height=30)

        self.provider_entry = Entry(self.center, justify="center", font=LB_FONT, bd=1, highlightthickness=1,
                                    relief=RIDGE, textvariable=self.provider_name, fg="maroon")
        self.provider_entry.place(x=323, y=185, width=310, height=31)

        self.generate_button = Button(self.center, text="Generate Text", justify="center", font=LB_FONT,
                                      bg="sandy brown", bd=1, highlightthickness=1, relief=RIDGE,
                                      command=self.generate_method)
        self.generate_button.place(x=5, y=221, width=180, height=40)

        self.tweet_button = Button(self.center, text="TWEET", justify="center", font=LB_FONT, bg="blue",
                                   fg="white smoke", bd=1, highlightthickness=1, relief=RIDGE,
                                   command=self.twitter_post_method)
        self.tweet_button.place(x=190, y=221, width=255, height=40)

        self.close_button = Button(self.center, text="Close Application", justify="center", font=LB_FONT, bg="coral",
                                   bd=1, highlightthickness=1, relief=RIDGE, command=self.close_method)
        self.close_button.place(x=451, y=221, width=180, height=40)

    # =============================== FUNCTIONALITY ==================================== #
    def close_method(self):
        self.window.destroy()

    def check_method(self):
        speed_tool = InternetSpeed()
        answer = speed_tool.get_internet_speed()
        self.download_answer.config(text=f"{answer['download']}", bg="navajo white")
        self.upload_answer.config(text=f"{answer['upload']}", bg="navajo white")

    def generate_method(self):
        self.complain.delete("1.0", END)
        complain_text = f"""Specially for {self.provider_name.get()}, 
My Internet Speed is Slower than it should be, Download Speed is {self.download_answer.cget("text")} 
and Upload Speed is {self.upload_answer.cget("text")}, I paid 125$ for it so If you don't fix it - 
I will choose another Provider.
        """
        self.complain.insert("1.0", f"{complain_text}")

    def twitter_post_method(self):
        tweet_tool = TwitterPost()
        tweet_tool.into_twitter()
        tweet_tool.twitter_post(letter=self.complain.get("1.0", END))
        self.complain.delete("1.0", END)
        self.download_answer.config(text="", bg="light gray")
        self.upload_answer.config(text="", bg="light gray")
        self.provider_name.set("")


def launch_app():
    app = Tk()
    TwitterInternetBot(app)
    app.mainloop()


if __name__ == "__main__":
    launch_app()
