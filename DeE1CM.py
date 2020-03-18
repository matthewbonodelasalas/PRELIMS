class DrumKit:
    def __init__(self):
        self.top_hat = True
        self.snare = True
class DrumKitTest:
    def play_tophat(self):
        print("ding ding di-ding")

    def play_snare(self):
        print("bang bang ba-bang")


d = DrumKitTest()
d.play_snare()
d.play_tophat()
if d.play_snare == True:
    d.play_snare = False
    
if __name__ == "__main__":
    DrumKitTest()


