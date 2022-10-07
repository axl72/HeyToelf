from gui.random_verbs import *
from core.verbs import get_verb, download_verbs, upload_verb
from core.scraper import get_urls, get_verb_from_web


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x500+300+200")
        self.verbs = download_verbs("cache")
        self.title = Label(self, 18,"Random Verbs Selector")
        self.verb = Label(self, 21, get_verb([verb[0] for verb in self.verbs]))

        self.label1 = Label(self, 18, "Past Tense")
        self.input = Entry(self)

        self.label2 = Label(self, 18, "Present Participle")
        self.input = Entry(self)
        
        self.label3 = Label(self, 18, "Past Participle")
        self.input = Entry(self)

        self.submit = Button(self, "Submit")

        self.label4 = Label(self, 24, "Upload New Verb")
        self.input_download_verb = Entry(self)
        self.upload = Button(self, "Upload", self.upload)


    def upload(self):
        urls = get_urls('www')
        url = urls[0].replace('\n', '')
        verb_string = self.input_download_verb.get()
        verb = get_verb_from_web(url, verb_string)
        upload_verb("cache", ";".join(verb) + '\n')


if __name__ == "__main__":
    main = MainWindow()
    main.mainloop()
