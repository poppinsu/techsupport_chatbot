from langchain.chat_models import ChatOpenAI
from langchain.schema import (HumanMessage, SystemMessage)
import streamlit as st


chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.1)

st.title("전자기기 에러 해결 상담사")
st.subheader("저는 당신을 위한  _:green[전자기기 에러 해결 상담사]_  tech_support입니다. 🛠️🧰")

context = """
당신은 태블릿, 노트북, 스마트폰 등 각종 전자기기의 소프트웨어 및 하드웨어에 관해 잘 알고, 
에러가 발생했을 때 해결하는 방법을 아는 능숙한 상담사입니다. 당신의 이름은 Tech_support입니다. 
당신은 사용자들이 해결해주기 원하는 각종 문제들을 파악할 수 있습니다. 
사용자들이 처한 상황에 대한 보다 자세한 정보가 필요하다면 그것을 사용자에게 질문하여 얻을 수 있습니다. 
또한 친절하고 쉽게 단계별로 기기 에러 해결 방안을 설명할 수 있습니다.
"""

messages = [SystemMessage(content=context)]
content = st.text_input("문제 상황을 알려주세요👇")
if st.button("질문하기", key="question_button"):
    user_input = content
    while user_input != "종료":
        if user_input:
            with st.spinner("해결 중..."):
                messages.append(HumanMessage(content=user_input))
                result = chat_model(messages)
                st.write("Tech_support: ", result.content)
                user_input = st.text_input("더 궁금한 점이 있으면 입력하세요 (종료하려면 '종료'를 입력하세요)", key=f"input_{len(messages)}")
                if st.button("질문하기", key="question_button"):

    st.write("상담을 종료합니다. 감사합니다.")
