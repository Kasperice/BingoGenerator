# Bingo Numbers Generator with sound

Currently working for Ubuntu:
- create virtual environment:  
  <code>python3 -m venv venv</code>  
  <code>activate venv/bin/acticate</code>  
- install sox and ffmpg  
  <code>sudo apt install sox</code>  
  <code>sudo apt install ffmpg</code>  
- install requirements from requirements.txt  
  <code>pip install -r requirements.txt</code>


How to use Bingo Numbers Generator:
- You are able to play in your native language, it is enough to pass your language code to a command from below examples:   
  <code>python main.py start --language=es</code>  
  <code>python main.py start --language=pl</code>  
  <code>python main.py start --language=\<language_code\></code>
- By default you will generate numbers which will be read in english. Then you need to run:  
  <code>python main.py start</code>
    
- In case you need help running the command just execute:  
  <code>python main.py --help</code>  
  <code>python main.py start --help</code>
  