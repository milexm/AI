# Artificial Intelligence

![AI](media/ai_icon.png)

- [1. Overview](#1-overview)
  - [1.1. Picture by AI](#11-picture-by-ai)
- [2. About the repo](#2-about-the-repo)
- [3. Preliminary steps](#3-preliminary-steps)
- [4. References](#4-references)
  - [4.1. Supporting GitHub techniques](#41-supporting-github-techniques)

## 1. Overview

 Artificial Intelligence (AI) is a branch of computer science and a
 multidisciplinary field that deals with the development of intelligent machines
 and systems capable of performing tasks that typically require human
 intelligence.

 > [!IMPORTANT] 
 > :thumbsup: AI aims to create computer programs or algorithms that can `learn`,
 `reason`, `perceive` their environment, and `make decisions` to achieve specific
 goals.

AI can be broadly categorized into two main types:

> [!NOTE]  
> **Narrow or Weak AI**. This form of AI is designed to excel in a specific task or a limited set of tasks. It is highly specialized and lacks general intelligence. Examples of narrow AI include voice assistants like Siri or Alexa, recommendation systems used by streaming platforms, and chatbots used for customer service.

> [!WARNING]  
> **General or Strong AI**. This type of AI is hypothetical and refers to machines that possess human-level intelligence. General AI would have the ability to understand, learn, and apply knowledge in a manner similar to humans across various domains. As of now, true general AI does not exist, and its development remains a subject of research and speculation.
> 
> Despite its numerous benefits, AI also raises `ethical` and `societal concerns`, such as privacy, job displacement, bias in algorithms, and potential misuse of AI technologies.

### 1.1. Picture by AI

![picture by AI](media/picture_by_ai.png)

## 2. About the repo

This repo shows practical examples on how to use [OpenaAi](https://openai.com/) API. In particular, it shows how to use the OpenAI components.

![openai_components](media/openAI_components.png)

Where

- **ChatGPT**. This is a web conversational interface that allows you to interact with ChatGPT language models.
- **DALL-E**. It allows you to create realistic images and art from the description you provide.
- **API**. It allows you to integrate OpenAI models into your apps.

> [!NOTE]
> ChatGPT stands for **Chat Generative Pre-trained Transformer**.

One of the sources of the examples shown here is the Udemy class: [ChatGPT Masterclass - Build Solutions and Apps with ChatGPT](https://www.udemy.com/course/chatgpt-build-solutions-and-apps-with-chatgpt-and-openai/).

The following figure shows the examples development environment.

![example production environment](media/chatgpt_dev_environment.png)

The user can interact with OpenAI API from the *localhost* for testing and use the [Azure Functions](https://docs.google.com/document/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub#h.ib4yzunwqg7n) in production to interact with OpenAI API in a serveless fashion.

To create and test the examples shown, you need the following tools and settings:

- OpenAI account. See [OpenAI API Login](https://docs.google.com/document/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub#h.5jazbqlah7h) and [OpenAI billing](https://docs.google.com/document/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub#h.97grw0z9k5kf).
- Visual Studio Code. See [Setup Visual Studio Code](https://docs.google.com/document/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub#h.9gpup0bkzoyl).
- Azure account. See [Setup Azure Functions](https://docs.google.com/document/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub#h.8h95unq36ppy).
- [Postman account]. See [Testing Azure function using Postman](https://docs.google.com/document/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub#h.qdyr4jg1ik0r). 

The applications we'll build have the following architecture (production environment)

![app architecture](media/chatgpt_production_environment.png)


## 3. Preliminary steps

1. [Accessing ChatGPT API](https://docs.google.com/document/u/1/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub#h.xnk73scuad4p). The first thing we want to do is to verify that we can access the ChatGPT API.
2. [Create a basic Azure function](https://docs.google.com/document/u/1/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub#h.r6ygtw61ibtg). We create a basic Azure function that we test locally. Then we’ll deploy it to the cloud and test it there.  
3. [Create a basic Azure function that uses ChatGPT API](https://docs.google.com/document/u/1/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub#h.6x9c734qltql). Now that we have the plumbing in place and tested it, we create a basic Azure function to interact with OpenAI ChatGPT API.

Find all the supporting information in the companion document [Artificial Intelligence](https://docs.google.com/document/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub) 

## 4. References

- [Artificial Intelligence](https://docs.google.com/document/d/e/2PACX-1vQJ4SRjtxJneZQ9cHzVHvgby8H7HScbznm04Q7fFn4DDjDbfgiP57De2rJgRo-yAHV19g0XtuTTadX3/pub) - Supporting information in the companion document
- [OpenaAI](https://openai.com/)
- [ChatGPT Masterclass - Build Solutions and Apps with ChatGPT](https://www.udemy.com/course/chatgpt-build-solutions-and-apps-with-chatgpt-and-openai/)

### 4.1. Supporting GitHub techniques

- [Quickstart for writing on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)
- [All-Github-Emoji-Icons](https://github.com/scotch-io/All-Github-Emoji-Icons)
- [[Markdown] An option to highlight a "Note" and "Warning" using blockquote (Beta)](https://github.com/orgs/community/discussions/16925)
