# Importing Libraries
from gtts import gTTS
import fitz  # PyMuPDF library

# Open the PDF File
pdf_File = fitz.open('path_to_pdf_file')  # Provide the actual path to your file
textString = ""

# Extracting text from each page of the PDF
for page in pdf_File:
    try:
        textString += page.get_text()  # Extract text content from the page
    except Exception as e:
        print(f"Error processing page: {e}")  # Optional error handling

# Close the PDF File
pdf_File.close()

# Print extracted text for verification
#print(textString)

# Set language to English (en)
language = 'en'

# Convert the text to speech using gTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

# Save the audio as an MP3 file
myAudio.save("Audio.mp3")

print("Audio file has been saved successfully!")