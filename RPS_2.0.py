from tkinter import*
import random
from PIL import Image, ImageTk

root=Tk()
root.title('Game Page')
root.geometry('600x500')

#had to add image path 'cuae the other way wasn't working
image_path =(r"C:\Users\HP\Desktop\Python_Codingal\Tkinter\Starting_image.jpg")
upload = Image.open(image_path)
upload = upload.resize((600, 500), Image.Resampling.LANCZOS)

image = ImageTk.PhotoImage(upload)

image_label = Label(root, image=image)
image_label.place(x=0, y=0, relwidth=1, relheight=1)


label = Label(root, text="Let's Play" ) 
label.place(relx=0.5, rely=0.1, anchor=CENTER)  #this keeps it at the center

#initiated a game counter
game_counter = 0  


#making a topwin for the game play
def topwin():
    global game_counter
    top_win = Toplevel()
    top_win.title("Pick a choice!")
    top_win.geometry('400x300')
    
    button_frame = Frame(top_win)
    button_frame.pack(expand=True)
    
    #decided to make results show on the topwin here
    result_label = Label(top_win, text="Play to see results" )
    result_label.pack(pady=10)
      
    #made use of grid here
    btn_R = Button(button_frame, text="Rock", command=lambda:play("Rock", result_label))
    btn_R.grid(row=0, column=0,padx=10, pady=20)
    
    btn_P = Button(button_frame, text="Paper", command=lambda:play("Paper",result_label))
    btn_P.grid(row=0, column=1,padx=10, pady=20)
    
    btn_S = Button(button_frame, text="Scissors", command=lambda:play("Scissors", result_label))
    btn_S.grid(row=0, column=2,padx=10, pady=20)
    
    #helped in placing the buttons the way i wanted properly
    button_frame.grid_rowconfigure(0, weight=1)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_columnconfigure(2, weight=1)
    
    
  
#added result_label here so the if, elif and else where also affected
def play(player_pick, result_label):
    global game_counter
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if (player_pick == computer_choice):
         result_label.config(text="It's a tie!", fg='orange')
        
    elif (player_pick == "Rock" and computer_choice == "Scissors") or \
         (player_pick == "Scissors" and computer_choice == "Paper") or \
         (player_pick == "Paper" and computer_choice == "Rock"): 
            result_label.config(text=f"You chose {player_pick}, Computer chose {computer_choice}. \n As a result you WINNNN!!!", fg='green') 
             
    else:
        result_label.config(text="You lose. Sorry", fg='red')
        
        #wasn't able to affect the independent color of the game counter text
    game_counter += 1
    result_label.config(text=result_label.cget('text') + f"\n Games Played: {game_counter}" ) 

btn = Button(root, text="Are you ready?", command = topwin)
btn.place(relx=0.5, rely=0.9, anchor=CENTER)           
        
root.mainloop()