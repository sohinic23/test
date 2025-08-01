import streamlit as st

import random 
a = random.randint(1,10)
st.write(a)
num = st.text_input("Hello, Please enter a number and I will print all  umbers less than it..")
num = int(num)


for i in range(0,num):
            st.write(i)




st.title("Test App")
st.header("numbers")
st.subheader("ai club")
st.write("I love AIclub")
            
