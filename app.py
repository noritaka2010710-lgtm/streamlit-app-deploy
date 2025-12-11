from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

EXPERT_SYSTEM = {
    "キャリア相談の専門家": "あなたはキャリア相談の専門家です。相談者に寄り添い、仕事や転職に関する的確な助言を行ってください。",
    "子育て支援の専門家": "あなたは子育て支援の専門家です。保護者の不安に寄り添い、子育ての悩みに優しく回答してください。"
}

def call_expert_llm(input_text: str, selected_expert: str) -> str:
    system_prompt = EXPERT_SYSTEM[selected_expert]

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=input_text)
    ]
    result = llm.invoke(messages)
    return result.content

st.title("課題アプリ")

st.write("##### 動作モード1: キャリア相談の専門家")
st.write("##### 動作モード2: 子育て支援の専門家")
st.write("専門家を選択し、テキストを入力することで、専門家が回答します。")

expert = st.radio(
    "動作モードを選択してください。",
    ["キャリア相談の専門家", "子育て支援の専門家"]
)

text = st.text_input("質問を入力してください")

if st.button("送信"):
    if text.strip() == "":
        st.warning("質問内容を入力してください。")
    else:
        answer = call_expert_llm(text, expert)
        st.write("### 回答")
        st.write(answer)
