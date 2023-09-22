import subprocess
import datetime

def colorize_word(text, target_word, background_color):
    words = text.split()
    
    result = ""
    
    background_code = {
        'yellow': '\033[43m',
    }
    
    if background_color not in background_code:
        raise ValueError("Invalid background color")
    
    for word in words:
        if word == target_word:

            colored_word = (
                background_code[background_color] +  
                word +                            
                background_code['reset']             
            )
            result += colored_word + " "  
        else:
            result += word + " " 
    
    return result.strip()  
today = datetime.date.today()
day_of_month = today.day

command = "cal"
try:
    output = subprocess.check_output(command, shell=True, text=True)
    today = str(day_of_month)
    background_color = "yellow"
    colored_sentence = colorize_word(output,today,background_color)
    print(colored_sentence)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
