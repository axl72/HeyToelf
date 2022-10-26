from gui.random_verbs import *
from core.verbs import get_verb, download_verbs, upload_verb, consult_verb
from core.scraper import get_urls, get_verb_from_web


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.bind("<Return>", lambda event: self.__submit__())
        self.geometry("800x500+300+200")
        self.verbs = [verb[0] for verb in download_verbs("cache")]
        self.title = Label(self, 18,"Random Verbs Selector")
        self.verb = Label(self, 21, get_verb(self.verbs))

        self.label1 = Label(self, 18, "Past Tense")
        self.input_past_tense = Entry(self)

        self.label2 = Label(self, 18, "Present Participle")
        self.input_present_participle = Entry(self)
        
        self.label3 = Label(self, 18, "Past Participle")
        self.input_past_participle = Entry(self)

        self.submit = Button(self, "Submit", self.__submit__)

        self.label4 = Label(self, 24, "Upload New Verb")
        self.input_download_verb = Entry(self)
        self.upload = Button(self, "Upload", self.__upload__)

    def __submit__(self):
        text_inputs = (self.input_present_participle, self.input_past_tense, self.input_past_participle)
        inputs = [button.get().lower() for button in text_inputs]
        def is_complete(inputs: list[str]) -> bool:
            lista = list(filter(lambda x: True if x != '' else False, inputs))
            return len(inputs) == len(lista) # It should there are any form to compare lists in python

        
        if not is_complete(inputs):
            return

        query = consult_verb("cache", self.verb.cget("text")).strip('\n')
        query = query.split(";")
        query.pop(0)
        if query == None:
            return
        if query != inputs:
            return
        
        new_verb = get_verb(self.verbs)
        self.verb.config(text = new_verb)
        [entry.delete('0', 'end') for entry in text_inputs]
        text_inputs[1].focus_set()

    def __upload__(self):
        urls = get_urls('www')
        url = urls[0].replace('\n', '')
        verb_string = self.input_download_verb.get()
        verb = get_verb_from_web(url, verb_string)
        upload_verb("cache", ";".join(verb) + '\n')


if __name__ == "__main__":
    main = MainWindow()
    main.mainloop()
