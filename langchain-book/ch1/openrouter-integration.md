---
title: LangChain
subtitle: Using OpenRouter with LangChain
headline: LangChain Integration | OpenRouter SDK Support
canonical-url: 'https://openrouter.ai/docs/community/langchain'
'og:site_name': OpenRouter Documentation
'og:title': LangChain Integration - OpenRouter SDK Support
'og:description': >-
  Integrate OpenRouter using LangChain framework. Complete guide for LangChain
  integration with OpenRouter for Python and JavaScript.
'og:image':
  type: url
  value: >-
    https://openrouter.ai/dynamic-og?title=LangChain&description=LangChain%20Integration
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary_large_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---

import { API_KEY_REF } from '../../../imports/constants';

## Using LangChain

- Using [LangChain for Python](https://github.com/langchain-ai/langchain): [github](https://github.com/alexanderatallah/openrouter-streamlit/blob/main/pages/2_Langchain_Quickstart.py)
- Using [LangChain.js](https://github.com/langchain-ai/langchainjs): [github](https://github.com/OpenRouterTeam/openrouter-examples/blob/main/examples/langchain/index.ts)
- Using [Streamlit](https://streamlit.io/): [github](https://github.com/alexanderatallah/openrouter-streamlit)

<CodeGroup>

```typescript title="TypeScript"
const chat = new ChatOpenAI(
  {
    modelName: '<model_name>',
    temperature: 0.8,
    streaming: true,
    openAIApiKey: '${API_KEY_REF}',
  },
  {
    basePath: 'https://openrouter.ai/api/v1',
    baseOptions: {
      headers: {
        'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
        'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
      },
    },
  },
);
```

```python title="Python"
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from os import getenv
from dotenv import load_dotenv

load_dotenv()

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = ChatOpenAI(
  openai_api_key=getenv("OPENROUTER_API_KEY"),
  openai_api_base=getenv("OPENROUTER_BASE_URL"),
  model_name="<model_name>",
  model_kwargs={
    "headers": {
      "HTTP-Referer": getenv("YOUR_SITE_URL"),
      "X-Title": getenv("YOUR_SITE_NAME"),
    }
  },
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

print(llm_chain.run(question))
```

</CodeGroup>
