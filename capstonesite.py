import streamlit as st
import PyPDF2


import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

# Title of the app
st.title("Welcome ! Let's find score of your resume")

# File uploader widget for PDF files
st.header('upload your resume')
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Variable to store extracted text
extracted_text = ""

# Check if a PDF file is uploaded
if pdf_file is not None:
    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract text from each page
    
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        extracted_text += page.extract_text()


import re

def clean_text(input_text):
    # Remove HTML tags
    cleaned_text = re.sub('<.*?>', '', input_text)
    
    # Remove special characters (\n, \t, etc.)
    cleaned_text = re.sub(r'[\n\t]', ' ', cleaned_text)
    
    # Remove other special characters
    cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', cleaned_text)
    
    return cleaned_text

text_without_tags = clean_text(extracted_text)



import re

# Given text
text = text_without_tags 

# Remove extra spaces
text_without_extra_spaces = re.sub(' +', ' ', text)
text_without_extra_spaces = text_without_extra_spaces.lower()




# Display the extracted text
st.write("Text extracted from the PDF:")
st.text(extracted_text)

st.title('select the order of your resume')
# -------------------------------------------------------------------------------------------------

re_one = st.text_input("Enter first section :").lower()
st.write(re_one)

# ----------------------------------------------------------------------------------------------------------------


re_two = st.text_input("Enter second section :").lower()
st.write(re_two)



# ------------------------------------------------------------------------------------------------------------------

re_three = st.text_input("Enter third section :").lower()
st.write(re_three)

# ------------------------------------------------------------------------------------------------------------------

re_four = st.text_input("Enter forth section :").lower()
st.write(re_four)


# ------------------------------------------------------------------------------------------------------------------

re_five = st.text_input("Enter five section :").lower()
st.write(re_five)

# ------------------------------------------------------------------------------------------------------------------

re_six = st.text_input("Enter six section :").lower()
st.write(re_six)


# ------------------------------------------------------------------------------------------------------------------

re_seven = st.text_input("Enter seven section :").lower()
st.write(re_seven)

# ------------------------------------------------------------------------------------------------------------------

re_eight = st.text_input("Enter eight section :").lower()
st.write(re_eight)

# -------------------------------------------------------------------------------------------------------------------
def extract_text_between_sections(resume_text, section_start, section_end):
    # Use a regular expression to find the content betwesen the start and end sections
    pattern = re.compile(fr'{re.escape(section_start)}(.*?){re.escape(section_end)}', re.DOTALL)
    match = pattern.search(resume_text)

    if match:
        extracted_text = match.group(1).strip()
        return extracted_text
    else:
        return ' '

# Example usage
resume_text = text_without_extra_spaces

# Define the start and end sections you want to extract
section_start = re_one
section_end = re_two

# Extract text between the specified sections
first_section = extract_text_between_sections(resume_text, section_start, section_end)
# st.write(first_section)
# -----------------------------------------------------------------------------------------------------------------

def extract_text_between_sections(resume_text, section_start, section_end):
    # Use a regular expression to find the content between the start and end sections
    pattern = re.compile(fr'{re.escape(section_start)}(.*?){re.escape(section_end)}', re.DOTALL)
    match = pattern.search(resume_text)

    if match:
        extracted_text = match.group(1).strip()
        return extracted_text
    else:
        return ' '

# Example usage
resume_text = text_without_extra_spaces

# Define the start and end sections you want to extract
section_start = re_two
section_end = re_three

# Extract text between the specified sections
second_section = extract_text_between_sections(resume_text, section_start, section_end)
# st.write(second_section)

# ------------------------------------------------------------------------------------------------------------------

def extract_text_between_sections(resume_text, section_start, section_end):
    # Use a regular expression to find the content between the start and end sections
    pattern = re.compile(fr'{re.escape(section_start)}(.*?){re.escape(section_end)}', re.DOTALL)
    match = pattern.search(resume_text)

    if match:
        extracted_text = match.group(1).strip()
        return extracted_text
    else:
        return ' '

# Example usage
resume_text = text_without_extra_spaces

# Define the start and end sections you want to extract
section_start = re_three
section_end = re_four

# Extract text between the specified sections
third_section = extract_text_between_sections(resume_text, section_start, section_end)
# st.write(third_section)
# -----------------------------------------------------------------------------------------------------------------

def extract_text_between_sections(resume_text, section_start, section_end):
    # Use a regular expression to find the content between the start and end sections
    pattern = re.compile(fr'{re.escape(section_start)}(.*?){re.escape(section_end)}', re.DOTALL)
    match = pattern.search(resume_text)

    if match:
        extracted_text = match.group(1).strip()
        return extracted_text
    else:
        return ' '

# Example usage
resume_text = text_without_extra_spaces

# Define the start and end sections you want to extract
section_start = re_four
section_end = re_five

# Extract text between the specified sections
forth_section = extract_text_between_sections(resume_text, section_start, section_end)
# st.write(forth_section)

# ------------------------------------------------------------------------------------------------------------------


def extract_text_between_sections(resume_text, section_start, section_end):
    # Use a regular expression to find the content between the start and end sections
    pattern = re.compile(fr'{re.escape(section_start)}(.*?){re.escape(section_end)}', re.DOTALL)
    match = pattern.search(resume_text)

    if match:
        extracted_text = match.group(1).strip()
        return extracted_text
    else:
        return ' '

# Example usage
resume_text = text_without_extra_spaces

# Define the start and end sections you want to extract
section_start = re_five
section_end = re_six

# Extract text between the specified sections
fifth_section = extract_text_between_sections(resume_text, section_start, section_end)
# st.write(fifth_section)


# -----------------------------------------------------------------------------------------------------------------


def extract_text_between_sections(resume_text, section_start, section_end):
    # Use a regular expression to find the content between the start and end sections
    pattern = re.compile(fr'{re.escape(section_start)}(.*?){re.escape(section_end)}', re.DOTALL)
    match = pattern.search(resume_text)

    if match:
        extracted_text = match.group(1).strip()
        return extracted_text
    else:
        return ' '

# Example usage
resume_text = text_without_extra_spaces

# Define the start and end sections you want to extract
section_start = re_six
section_end = re_seven

# Extract text between the specified sections
sixth_section = extract_text_between_sections(resume_text, section_start, section_end)
# st.write(sixth_section)
# ------------------------------------------------------------------------------------------------------------------


def extract_text_between_sections(resume_text, section_start, section_end):
    # Use a regular expression to find the content between the start and end sections
    pattern = re.compile(fr'{re.escape(section_start)}(.*?){re.escape(section_end)}', re.DOTALL)
    match = pattern.search(resume_text)

    if match:
        extracted_text = match.group(1).strip()
        return extracted_text
    else:
        return ' '

# Example usage
resume_text = text_without_extra_spaces

# Define the start and end sections you want to extract
section_start = re_seven
section_end = re_eight

# Extract text between the specified sections
seventh_section = extract_text_between_sections(resume_text, section_start, section_end)
# st.write(seventh_section)


st.header("Enter text of job description")


def take_text_input():
  text = st.text_input("Enter text:")
  return text

text = take_text_input()

# ------------------------------------------------------------------------------------------------------------------


# creating a list

final_a = []
final_a.append(first_section)
final_a.append(second_section)
final_a.append(third_section)
final_a.append(forth_section)
final_a.append(fifth_section)
final_a.append(sixth_section)


# st.write(final_a)

# ------------------------------------------------------------------------------------------------------------------

def split_text_into_paragraphs(text):
      return [paragraph.strip() for paragraph in text.split('.') if paragraph.strip()]


def calculate_cosine_similarity(text1, text2):
      tfidf_vectorizer = TfidfVectorizer()
      tfidf_matrix = tfidf_vectorizer.fit_transform([text1, text2])
      cosine_similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
      return cosine_similarities[0][0]

resume_paragraphs = final_a
job_description_paragraphs = split_text_into_paragraphs(text)

st.write('YOUR JOB DESCRIPTION :    ',text)
# st.write(job_description_paragraphs)

# Add a button to the app
if st.button("find score"):
    # # Read the resume and job description text files with 'ISO-8859-1' encoding
    # with open(resume_file, 'r', encoding='ISO-8859-1') as f:
    #     resume_text = f.read()

    # with open(job_description_file, 'r', encoding='ISO-8859-1') as f:
    #     job_description_text = f.read()
    paragraph_scores = []

    for resume_paragraph in resume_paragraphs:
        paragraph_scores_for_job_desc = []
        for job_desc_paragraph in job_description_paragraphs:
            similarity = calculate_cosine_similarity(resume_paragraph, job_desc_paragraph)
            paragraph_scores_for_job_desc.append(similarity)
        max_score_for_resume_paragraph = max(paragraph_scores_for_job_desc)
        paragraph_scores.append(max_score_for_resume_paragraph)

    # displaying the max score
    top_scores = sorted(paragraph_scores, reverse=True)[:1]
    top_scores = top_scores[0]
    top_scores = np.round(top_scores*100,2)

    if top_scores>=55:
        st.write('calculating',top_scores)
        st.header('congrats! you have good resume match with this job description 🥳🎉')
        st.balloons()
        st.snow()
    elif top_scores >=35:
        st.write('calculating',top_scores)
        st.header('you have to make some changes to your resume 🤝🏻') 
        st.balloons()
        st.snow()
    else:
        st.write('calculating',top_scores)
        st.header('sorry your resume is not matching for this profile 😢')
        st.balloons()
        st.snow()
# JOB DESCRIPTION
# '''we need a data scientist who can work effectively on machine learning projects and can analyze our very well we're the company who do sentiment analysis skills. we need is Collab, Jupyter, NLP , supervised machine learning ,unsupervised machine learning expert in MYSQL query and bi tools.'''


