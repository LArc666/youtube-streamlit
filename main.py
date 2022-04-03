from typing import Text
from pyparsing import condition_as_parse_action
import streamlit as st
import numpy as np
import pandas as pd
import datetime
from PIL import Image
import time

#タイトル記入
st.title("Streamlit超入門")

#文字を記入
st.write("プログレスバーの表示")
"Start!!"

#空の追加
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Interation {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"Done!!"












#2カラム
left_column,right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")

if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write('問い合わせ内容を書く')

# Text = st.text_input(
#     "あなたの趣味を教えてください。"
# )
# "あなたの好きなアーティストは", Text 

# condition = st.slider("あなたの今の調子は？",0,100,50)
# "あなたの調子は、",condition,"です"


# #チェックの有無で画像の表示
# if st.checkbox("Show Imege"):
#     #画像表示
#     img = Image.open("C:/Users/vamps/Pictures/HYDE/001-3.jpg")
#     st.image(img,caption="HYDE",use_column_width=True)















# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.07,136.02],
#     columns=["lat","lon"]
# )

# st.map(df)

# #データフレームの表示、引数がつけれる,ハイライト作れる
# st.table(df.style.highlight_max(axis=0))

# #マークダウン   Pythonのコード表示
# """
# # 章
# ## 節
# ### 項

# ```Python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


