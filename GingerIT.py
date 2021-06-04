import streamlit as st

from gingerit.gingerit import GingerIt

st.title('Spell Corrector and Grammar Checker')
text=st.text_input(label='Enter text')
parser = GingerIt()
res=parser.parse(text)


if st.button("Rectify"):
    st.markdown("### Result: ")
    st.write(res['result'])
 