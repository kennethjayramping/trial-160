#pip install SpeechRecogition, pip install pyaudio
from numpy import source
import speech_recognition as sr
import os

from playsound import playsound  #pip install playsound==1.2.2

from csv import DictWriter


idIdentify = str(2022)  ##mao ni siya tung string dapat na gikan sa pag identify sa ID

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #recognizer_instance.pause_threshold = 0.5
        print("Speak your ID code")
        print("Listening...")
        audio = r.listen(source)
        

        try:
            print("Confirming your ID code. Please wait... ")
            idcodeSTR = r.recognize_google(audio)
            print("Logging you in... ")
            
            if idcodeSTR == idIdentify:
                
                headersCSV = ['ID','CODE']      
                # The data assigned to the dictionary 
                dict={'ID':idcodeSTR,'CODE':idIdentify}
                
                # Pre-requisite - The CSV file should be manually closed before running this code.

                # First, open the old CSV file in append mode, hence mentioned as 'a'
                # Then, for the CSV file, create a file object
                with open('Attendance.csv', 'a', newline='') as f_object:
                    # Pass the CSV  file object to the Dictwriter() function
                    # Result - a DictWriter object
                    dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
                    # Pass the data in the dictionary as an argument into the writerow() function
                    dictwriter_object.writerow(dict)
                    # Close the file object
                    f_object.close()
                
                print("You have logged in successfully.")
                playsound('success.mp3')


            else:
                print("Your credentials do not match. Please try again.")
                playsound('error.mp3')

        
        except Exception as e:
            print("Didn't catch that. Please try again."+str(e))


if __name__ == "__main__":
    main()