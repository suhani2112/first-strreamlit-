import streamlit as st
st.title(' title->hello world')
st.header('header-> namste')
st.subheader('subheader-> namste')
st.text('i am suhani hope you are good')

st.markdown('### hi')
st.markdown('## hi')
st.markdown('# hi')
st.markdown(' hi')

st.markdown('__gfg__ is great' )  #bold
st.markdown('**gfg** is great' )  #bold
st.markdown('_gfg_ is great' )    #italic
st.markdown('*gfg* is great' )    #italic
st.markdown('___gfg___ is great' )  #bold italic
st.markdown('***gfg*** is great' )   #bold italic


st.success("hey you are submitted")
st.info("info")
st.warning ("warning")
st.error("error")

st.exception(ZeroDivisionError('div not possible'))
st.help(ZeroDivisionError)

st.write("with quotes.....range(1,10)")
st.write("without quotes.....",range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.code('x=10\n'
         'for i in range(x)\n'
            '\tprint(i)')

radiobutton=st.radio('select gender:',('male','female'))
if(radiobutton=='male'):
    st.write('you are male')
if(radiobutton=='female'):
    st.write("you are female")


if(st.checkbox('kid')):
    st.write("you are a kid")
if(st.checkbox('adult')):
    st.write("you are an adult")


select=st.selectbox('state:',['select your state','rajasthan','gujrat','kerala','punjab','delhi','UP','MP'])
st.write("your state is :",select)

multiselect=st.multiselect('state:',['select your state','rajasthan','gujrat','kerala','punjab','delhi','UP','MP'])
st.write("your state is :",multiselect)

st.button ("click me")

volume=st.slider('selct volume:',1,100,1)
st.write("volume is:",volume)
if(volume>60):
    st.write("this might be harmful for your ears")

name=st.text_input("enter your Name:")
if(name):
    st.write('hi',name,'welcome')

username=st.text_input("enter your UserName:")
password=st.text_input("enter your :password:",type='password')


txt=st.text_area("write something yourself",height=300,max_chars=500,help='write only 300 words')
st.write(txt)

age=st.number_input("your age",18,50,value=30)
if(age):
    st.write('your age is:',age)

st.date_input("date")

st.time_input("time")

color=st.color_picker('select a color' ,'#DC1D07')
st.write('you select',color,'color')
