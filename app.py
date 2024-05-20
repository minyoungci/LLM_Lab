from typing import List 

import nest_asyncio   # asyncico 라이브러리는 이벤트 루프와 관련된 문제를 해결할 수 있도록 돕는 유틸리티 
import streamlit as st # streamlit 라이브러리를 사용하여 웹 애플리케이션을 만들 수 있음
from phi.assistant import Assistant # phi 라이브러리의 Assistant 클래스를 사용하여 자연어 처리를 수행
from phi.document import Document # phi 라이브러리의 Document 클래스를 사용하여 문서를 처리
from phi.document.reader.pdf import PDFReader # phi 라이브러리의 PDFReader 클래스를 사용하여 PDF 문서를 읽음
from phi.document.reader.website import WebsiteReader # phi 라이브러리의 WebsiteReader 클래스를 사용하여 웹사이트를 읽음
from phi.utils.log import logger

from assistant import get_llm_os  # type: ignore

nest_asyncio.apply() # asyncio의 이벤트 루프와 관련된 문제 방지를 위해 nest_asyncio 설정 적용. 주로 Streamlit과 같은 환경에서 비동기 코드 사용할 때 필요 


st.set_page_config(
    page_title="LLM OS",
    page_icon="🤖",
)
st.title("LLM OS")
st.markdown('#### : orange_heart: LLM OS is a lightweight, open-source, and privacy-focused AI assistant for your daily needs. :orange_heart:')

