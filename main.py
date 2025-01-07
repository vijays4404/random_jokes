#importing the kivy
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import requests
import random
#creating a app class

MOTIVATION_API="https://ron-swanson-quotes.herokuapp.com/v2/quotes"
class QuoteApp(App):
    def build(self):
        self.layout=BoxLayout(orientation='vertical',padding=20,spacing=10)


        #label to display the quote
        self.quote_label=Label(text='Click the buttom to get motivational quote',
                                halign='center',
                                valign='middle',
                                font_size=40)
    
        self.quote_label.bind(size=self.quote_label.setter('text_size'))

        #Button to fetch the quote

        self.fetch_button=Button(text='Get Quote',size_hint=(1,0.2 ),font_size=40,on_press=self.fetch_quote)
        self.layout.add_widget(self.quote_label)
        self.layout.add_widget(self.fetch_button)

        return self.layout

    def fetch_quote(self,instance):
        #Fetching a random quote from api
        response=requests.get(MOTIVATION_API)
        try:
            if response.status_code==200:
                data=response.json()
                print(data)
                quote=data[0]
               
                self.quote_label.text=quote
            else:
                self.quote_label.text='Failed to fetch quote. Please try again'
        except Exception as e:
            self.quote_label.text=f'Error:{e}'


if __name__=="__main__":
    quote=QuoteApp()
    quote.run()

            



