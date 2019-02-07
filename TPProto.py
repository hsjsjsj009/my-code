from textblob import TextBlob,exceptions
from tkinter import *
from thesaurus import Word
from PyDictionary import PyDictionary
from tkinter.messagebox import *


class FrontApp(Frame):# class untuk satu aplikasi
    condition_synonym="all"
    def __init__(self,master): #fungis untuk halaman depan
        self.master = master
        self.master.title("English Helper!")
        Frame.__init__(self,self.master)
        self.master.geometry("300x200")
        self.pack()
        self.POS = ("Adjective","Adverb","Contradiction","Conjunction","Determiner","Interjection","Noun","Prefix","Preposition","Pronoun","Verb","Abbreviation","Phrase","Article","All")
        label1 = Label(self,height=3,text="Your Writing Company")
        label1.grid(column=0,row=0)
        self.translator = Button(self,text="Translator",command=self.Translator)
        self.translator.grid(column=0,row=1)
        label = Label(self,height=1)
        label.grid(column=0,row=2)
        self.synonym = Button(self,text="Synonym",command=self.my_synonym)
        self.synonym.grid(column=0,row=3)
        label2 = Label(self,height=1)
        label2.grid(column=0,row=4)
        dictionary = Button(self,text="Dictionary",command=self.Dictionary)
        dictionary.grid(column=0,row=5)    

    def Translator(self): #fungsi untuk halaman translate
        self.destroy()
        Frame.__init__(self,self.master)
        self.pack()
        self.master.geometry("1000x600")
        label = Label(self,text="EN-ID Translator")
        label.grid(column=0,row=0,columnspan=3)
        labelinput = Label(self,text="Input Here :")
        labelinput.grid(column=0,row=1)
        labeloutput = Label(self,text="Output Here:")
        labeloutput.grid(column=2,row=1)
        self.input = Text(self,width=60,height=20)
        self.input.grid(column=0,row=2)
        labelempty = Label(self)
        labelempty.grid(column=1,row=2)
        self.output = Text(self,width=60,height=20)
        self.output.grid(column=2,row=2)
        labelemp2= Label(self)
        labelemp2.grid(column=0,row=4,columnspan=3)
        EN_ID = Button(self,text="English to Indonesia",command=self.TranslateID)
        EN_ID.grid(column=0,row=5)
        ID_EN = Button(self,text="Indonesia to English",command=self.TranslateEN)
        ID_EN.grid(column=2,row=5)
        back = Button(self,text="Menu",command=self.Menu)
        back.grid (column=0,row=6,columnspan=3)
    
    def my_synonym(self): #fungsi untuk halaman synonym
        self.choose = StringVar(self)
        self.choose.set(self.POS[-1])
        self.destroy()
        Frame.__init__(self,self.master)
        self.master.geometry("500x600")
        self.pack()
        label = Label(self,text="EN Synonyms")
        label.grid(row=0,column=0,columnspan=4)
        label_word=Label(self,text="Word :")
        label_word.grid(row=1,column=0)
        label_PS = Label(self,text="Part Of Speech : ")
        label_PS.grid(row=2,column=0)
        self.entry_word=Entry(self)
        self.entry_word.grid(row=1,column=1)
        part_speech = OptionMenu(self,self.choose,*self.POS)
        part_speech.grid(row=2,column=1, sticky='we')
        labelemp3=Label(self)
        labelemp3.grid(row=2,column=2,rowspan=2)
        button = Button(self,text="Search",command=self.synonym_Search)
        button.grid(row=1,column=3,rowspan=2)
        self.informal =  IntVar()
        self.formal = IntVar()
        chkbox1 = Checkbutton(self,text="Informal",variable=self.informal).grid(row=3,column=0,columnspan=2)
        chkbox2 = Checkbutton(self,text="Common",variable=self.formal).grid(row=3,column=2,columnspan=2)
        labelemp=Label(self,height=1)
        labelemp.grid(row=5,column=0,columnspan=4)
        back = Button(self,text="Menu",command=self.Menu)
        back.grid(row=6,column=0,columnspan=4)
        self.entry_word.bind("<Return>",self.synonym_Search_bind)
        part_speech.bind("<Return>",self.synonym_Search_bind)

    def synonym_Search(self): #fungsi untuk mencari synonym
        if self.informal.get() and self.formal.get() : #pengecekan tipe formal atau common
            FrontApp.condition_synonym="all"
        elif self.informal.get() :
            FrontApp.condition_synonym ="informal"
        elif self.formal.get() :
            FrontApp.condition_synonym = "common"
        else :
            FrontApp.condition_synonym = "all"
        word_synonym = Synonym(self,30,25,self.entry_word.get(),row=4,column=0,columnspan=4,partspeech=self.POS.index(self.choose.get()))
        word_synonym.Search()

    def synonym_Search_bind(self,event): #fungsi untuk mencari synonym versi bind
        if self.informal.get() and self.formal.get() : #pengecekan tipe formal atau common
            FrontApp.condition_synonym="all"
        elif self.informal.get() :
            FrontApp.condition_synonym ="informal"
        elif self.formal.get() :
            FrontApp.condition_synonym = "common"
        else :
            FrontApp.condition_synonym = "all"
        word_synonym = Synonym(self,30,25,self.entry_word.get(),row=4,column=0,columnspan=4,partspeech=self.POS.index(self.choose.get()))
        word_synonym.Search()

    def meaning_search(self): #fungsi untuk mencari arti kata
        self.result.delete("1.0",END)
        process=Meaning(self.dict_word.get(),self.result)
        process.Search()

    def meaning_search_bind(self,event): #fungsi untuk mencari arti kata versi bind
        self.result.delete("1.0",END)
        process=Meaning(self.dict_word.get(),self.result)
        process.Search()

    def Menu(self): #fungsi untuk balik ke menu
        self.destroy()
        self.master.geometry("300x200")
        Frame.__init__(self,self.master)
        self.pack()
        label1 = Label(self,height=3,text="Your Writing Company")
        label1.grid(column=0,row=0)
        self.translator = Button(self,text="Translator",command=self.Translator)
        self.translator.grid(column=0,row=1)
        label = Label(self,height=1)
        label.grid(column=0,row=2)
        self.synonym = Button(self,text="Synonym",command=self.my_synonym)
        self.synonym.grid(column=0,row=3)
        label2 = Label(self,height=1)
        label2.grid(column=0,row=4)
        dictionary = Button(self,text="Dictionary",command=self.Dictionary)
        dictionary.grid(column=0,row=5)

    def TranslateID(self): #fungsi untuk translasi ke bahasa indonesia
        try :
            text = self.input.get("1.0",END)
            process = TextBlob(text)
            process = process.translate(from_lang="en",to="id")
            self.output.config(state=NORMAL)
            self.output.delete("1.0",END)
            self.output.insert("1.0",process)
            self.output.config(state=DISABLED)
        except exceptions.NotTranslated:
            self.output.config(state=NORMAL)
            self.output.delete("1.0",END)
            self.output.insert("1.0",text)
            self.output.config(state=DISABLED)
        except:
            showerror(message="No connection",title="Connection Error")    
        
    def TranslateEN(self): #fungsi untuk translasi ke bahasa inggris
        try :
            text = self.input.get("1.0",END)
            process = TextBlob(text)
            process = process.translate(from_lang="id",to="en")
            self.output.config(state=NORMAL)
            self.output.delete("1.0",END)
            self.output.insert("1.0",process)
            self.output.config(state=DISABLED)
        except exceptions.NotTranslated:
            self.output.config(state=NORMAL)
            self.output.delete("1.0",END)
            self.output.insert("1.0",text)
            self.output.config(state=DISABLED)
        except:
            showerror(message="No connection",title="Connection Error")
    def Dictionary(self):#fungsi untuk halaman kamus
        self.destroy()
        self.master.geometry("500x600")
        Frame.__init__(self,self.master)
        self.pack()
        label = Label(self,text="EN Dictionary")
        label.grid(row=0,column=0,columnspan=4)
        label_word = Label(self,text="Word : ") 
        label_word.grid(row=1,column=0)
        self.dict_word=Entry(self)
        self.dict_word.grid(row=1,column=1)
        labelemp= Label(self)
        labelemp.grid(row=1,column=2)
        search = Button(self,text="Search",command=self.meaning_search)
        search.grid(row=1,column=3)
        self.result = Text(self,width=50,height=28)
        self.result.grid(row=2,column=0,columnspan=4)
        labelemp1=Label(self)
        labelemp1.grid(row=3,column=0)
        back = Button(self,text="Menu",command=self.Menu)
        back.grid(row=4,column=0,columnspan=4)
        self.dict_word.bind("<Return>",self.meaning_search_bind)

class Synonym(Text): #class untuk mmengeluarkan synonym kata
    part_of_speech = ("adj","adv","contradiction","conj","determiner","interj","noun","prefix","prep","pron","verb","abb","phrase","article")
    def __init__(self,master,width,height,word,column,columnspan,row,partspeech): #inisiasi class 
        self.base_word=Word(word)
        self.master = master
        self.width = width
        self.height = height
        self.column = column
        self.row = row
        self.columnspan = columnspan
        self.partspeech = partspeech

    def Search(self): #fungsi mencari synonym kata
        if check_internet("http://google.com") : #cek koneksi internet
            temp_str = ""
            if self.partspeech != 14: #pengecekan tipe part of speech, bukan 14 menandakan tidak "all"
                if FrontApp.condition_synonym != "all" : 
                    list_synonym = self.base_word.synonyms('all',form=FrontApp.condition_synonym,partOfSpeech=Synonym.part_of_speech[self.partspeech],allowEmpty=False)
                else :
                    list_synonym = self.base_word.synonyms('all',partOfSpeech=Synonym.part_of_speech[self.partspeech],allowEmpty=False)
                if list_synonym != []: #pengecekan ketersediaan hasil
                    Text.__init__(self,self.master,width=self.width,height=self.height)
                    self.grid(row=self.row,column=self.column,columnspan=self.columnspan)
                    self.config(state=NORMAL)
                    self.delete("1.0",END)
                    for k in list_synonym:
                        for j in k:
                            temp_str += j+"\n"
                        temp_str += "\n"
                    self.insert("1.0",temp_str)
                    self.config(state=DISABLED)
                    temp_str=""
                else :
                    Text.__init__(self,self.master,width=self.width,height=self.height)
                    self.grid(row=self.row,column=self.column,columnspan=self.columnspan)
                    self.config(state=NORMAL)
                    self.delete("1.0",END)
                    self.insert("1.0","None")
                    self.config(state=DISABLED)
            else :
                if FrontApp.condition_synonym == "all": 
                    list_synonym = self.base_word.synonyms('all',allowEmpty=False)
                else :
                    list_synonym = self.base_word.synonyms('all',form=FrontApp.condition_synonym,allowEmpty=False)
                if list_synonym != [] :
                    Text.__init__(self,self.master,width=self.width,height=self.height)
                    self.grid(row=self.row,column=self.column,columnspan=self.columnspan)
                    self.config(state=NORMAL)
                    self.delete("1.0",END)
                    for k in list_synonym:
                            for j in k:
                                temp_str += j+"\n"
                            temp_str += "\n"
                    self.insert("1.0",temp_str)
                    self.config(state=DISABLED)
                    temp_str=""
                else :
                    Text.__init__(self,self.master,width=self.width,height=self.height)
                    self.grid(row=self.row,column=self.column,columnspan=self.columnspan)
                    self.config(state=NORMAL)
                    self.delete("1.0",END)
                    self.insert("1.0","None")
                    self.config(state=DISABLED)
        else :
            showerror(message="No Connection",title="Connection Error")

class Meaning(PyDictionary): #class untuk kamus
    def __init__(self,word,master_text): #inisiasi class
        PyDictionary.__init__(self)
        self.master = master_text
        self.word=word
    
    def Search(self): #fungsi untuk mencari arti kata
        if check_internet("https://google.com"): #cek koneksi internet
            try :
                temp = ""
                meaning = self.meaning(self.word)
                for i in meaning:
                    temp += i+" :\n\n"
                    for k in meaning[i] :
                        temp+=k+"\n\n"
                    temp += "\n"
                self.master.config(state=NORMAL)
                self.master.delete("1.0",END)
                self.master.insert("1.0",temp)
                self.master.config(state=DISABLED)
                temp = ""
            except : #kondisi jika tidak ada hasil
                self.master.config(state=NORMAL)
                self.master.delete("1.0",END)
                self.master.insert("1.0","None")
                self.master.config(state=DISABLED)
        else :
            showerror(message="No Connection",title="Connection Error")

def check_internet(url): #fungsi untuk mengecek koneksi
    import requests
    try :
        o = requests.get(url,timeout=3)
        return True
    except:
        return False

if __name__== "__main__": #menggunakan top levle module
    root = Tk()
    s = FrontApp(root)
    root.mainloop()