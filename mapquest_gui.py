from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase

LabelBase.register(name = "Nunito", fn_regular= "BebasNeue-Regular.otf")
  
class MapQuest(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('main.kv')
    
    def changeMetric(self,active,val):
        print("HEllo", active.state)
    
    def calc(self,origin,destination):
        print(f"ORIGIN: {origin} DESTINATION: {destination}")
    
    def build(self):
        return self.screen
    
if __name__ == '__main__':
    MapQuest().run()