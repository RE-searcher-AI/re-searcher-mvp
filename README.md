# RE:searcher
## The Office Team

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Dart](https://img.shields.io/badge/dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Firebase](https://img.shields.io/badge/firebase-%23039BE5.svg?style=for-the-badge&logo=firebase)

RE:searcher is an AI-powered app designed to assist academics by enabling them to interact with their documents and generate mind maps seamlessly. Developed during the SAIS 24-hour hackathon, it won first place for its innovative approach to academic research.

This is the original repository, unchanged, as it was submitted on the competition. We continued developing the application; more about you can see here: [https://re-searcher.web.app/](https://re-searcher.web.app/)

### Tool Features
- Question formulation
- Creating summarized content overviews
- Efficiently saving user notes

### Goal

The goal is to provide users with a simple way to search and manage documents, formulate questions, create notes, generate paragraphs, and define document topics and abstracts.

# Documentation PDF
[RE:SEARCHER - Complete documentation in Serbian](https://github.com/Serbian-AI-Society/OfficeTime/blob/main/assets/REsearcher%20Dokumentacija.pdf)

## Implementacija

Our project repository consists of two directories: **backend** and **frontend**.

### Flutter - _re_searcher_ui_

The frontend of our application uses Flutter for the user interface and is hosted on Firebase. For efficient state management, the BLOC pattern is employed. Thanks to Flutter, the application can run on all mobile and desktop platforms, as well as on the web.

### Flask - _re_searcher_api_

The backend of our application uses the Flask micro-framework, enabling efficient interaction with the chatbot through message processing, document retrieval, and authentication. It leverages AWS services, the RAG model, and Pinecone vector DB for precise data search and management, ensuring relevant information and secure communication.

## Solution Architecture and Use Case Diagram

### Solution Architecture

<image src="assets/project_architecture.jpg" alt="Arhitektura rešenja">

### Use Case Diagram

<image src="assets/UseCase.png" alt="Image description">

## Application UIUX

<image src="assets/showcase.gif" alt="Image description">

<image src="assets/Screenshot1.jpg" alt="Image description">

## Planned additional features

- Merging multiple documents
- Exporting notes to PDF format
- Grouping documents
- Image recognition
- Voice communication
- Navigating through document history

## OfficeTime team

Introducing the team behind the project **RE:searcher**!


Tara Pogančev | Vuk Čabrilo | Milan Popđurđev | Laslo Uri
--- | --- | --- | ---
<a href="https://www.github.com/tara-pogancev/"><image src="re_searcher_ui/assets/tara.jpg" height="auto" width="100" style="border-radius:0%"></a>|<a href="https://www.github.com/vukca/"><image src="re_searcher_ui/assets/vuk.jpg" height="auto" width="100" style="border-radius:0%"></a> | <a href="https://www.github.com/milanp98/"><image src="re_searcher_ui/assets/milan.jpg" height="auto" width="100" style="border-radius:0%"></a> | <a href="https://github.com/laslo-uri/"><image src="re_searcher_ui/assets/laslo.jpg" height="auto" width="100" style="border-radius:0%"></a>
<a href="https://www.linkedin.com/in/tara-pogancev/"><image src="assets/TeamMembers/TaraReal.png" height="auto" width="100" style="border-radius:0%"></a>|<a href="https://www.linkedin.com/in/vuk-%C4%8Dabrilo-63b369207/"><image src="assets/TeamMembers/VukReal.png" height="auto" width="100" style="border-radius:0%"></a> | <a href="https://www.linkedin.com/in/milan-pop%C4%91ur%C4%91ev/"><image src="assets/TeamMembers/MilanReal.png" height="auto" width="100" style="border-radius:0%"></a> | <a href="https://www.linkedin.com/in/laslo-uri/"><image src="assets/TeamMembers/LasloReal.png" height="auto" width="100" style="border-radius:0%"></a>

---
