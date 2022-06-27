# Write your code here
class Spotify:
    def __init__(self,sngs):
        print("Welcome to Spotify!")
        self.playlist = sngs

    def add_to_playlist(self,sng):
        self.playlist.append(sng)

    def playing_number(self,num):
        if num<=len(self.playlist):
            return f"##########################\nPlaying {num} number song for you \nSong name: {self.playlist[num-1]}"
        else:
            return f"{num} number song not found. Your playlist has {len(self.playlist)} songs only"



#========================================================

user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))
