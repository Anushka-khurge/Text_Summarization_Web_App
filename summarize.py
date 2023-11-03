import streamlit as st

#st.title("hello")
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to summarize text
def summarize_text(text):
    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Creating a frequency table to keep the score of each word
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text
    average = int(sumValues / len(sentenceValue))

    # Storing sentences into the summary
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

    return summary

#streamlit ui
st.title("Text Summarizer")

#input text
input_text = st.text_area("Enter the Text to be Summarized:")
st.subheader("Length of Text:")
length_t=len(input_text)
st.info(length_t)

if st.button('Summarize🫣') :
    if input_text:
        #summarize the input text
        summary= summarize_text(input_text)

        #displaying the summary
        st.subheader('Generated Summary:')
        st.success(summary)
        st.subheader('Length of Summary')
        length_s = len(summary)
        st.info(length_s)
        reduceper = round(length_s/length_t * 100,2)
        st.subheader("Text Reduced by (%) :")
        st.info(reduceper)

        st.balloons()
    else:
        st.error("Please enter some text!")


#information about the app
st.sidebar.markdown('## About The App')
st.sidebar.write('''📚 Introducing my text summarization app, a culmination of my dedication to NLP! 📝

🔍 This app harnesses cutting-edge NLP techniques to extract the essence of lengthy texts, saving users time and effort.

📌 It employs advanced algorithms to identify key information, condensing complex documents into concise summaries.

🎓 Ideal for students, professionals, and knowledge enthusiasts, it's a valuable tool for digesting information.

🚀 Regular updates ensure it remains at the forefront of NLP advancements.

🌟 Experience a smarter, more efficient way to consume information with my text summarization app!

📢 Try it out today and simplify your reading experience! 🚀📚📌''')

st.sidebar.write('Our Team 😉 :')
st.sidebar.write('Aditya-Anushka-Manjiri-Mokshata-Ayush')