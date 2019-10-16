from nltk.chat.util import Chat,reflections
from myresponses import responses as pairs

def jarvischat():
	print("heyya! tell me what i can do?") #default message at the start    
	chat = Chat(pairs, reflections)
	chat.converse()
if __name__ == "__main__":
	jarvischat()
