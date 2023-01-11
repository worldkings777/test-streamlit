import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバー')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせを書く1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせを書く2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせを書く3')

# text = st.text_input('あなたの趣味を教えてください',)
# condition = st.slider('あなたの今の調子は、', 0, 100, 50)

#'あなたの趣味は、', text, ' です'
#'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('ikigai.jpg')
#     st.image(img, caption='ikigaino hon', use_column_width=True)

