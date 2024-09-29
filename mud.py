import streamlit as st 

st.header("mud system volume calculator")
st.write("Mud system Rig 59")
st.image("p.jpg")

tank=st.selectbox("Choose Tank :", ['Sluge', 'Premix 1',"Sucation 3" 
									,'Sucation 2', 'Sucation 1',  'Inter 3', 'Inter 2' , 'Inter 1', 'Settling 2' ,
									'Settling 1' ,'Trip tank', 'Premix 2C', "Premix 2B" , 'Premix 2a', "Reserve 1",'Reserve 2', "Reserve 3","Reserve 4"])

x=st.number_input(label="enter the measument")


if x is not None :
	l=96-x
	if tank=="Sluge" :	
		volum=l*0.71
		st.write(volum)
	if tank=="Premix 1" :
		volum=l*4.44
	if tank=="Sucation 3" :
		volum=l*2.4
	if tank=="Sucation 2" :
		volum=l*2.5
	if tank=="Sucation 1" :
		volum=l*2.38
	if tank=='Inter 3':
		volum=l*2.44
	if tank=="Inter 2":
		volum=l*2.48
	if tank=="Inter 1":
		volum=l*2.34
	if tank=="Settling 2":
		volum=l*1.24
	if tank=="Settling 1" :
		volum=l*2.79
	if tank=="Trip tank":
		volum=l*0.97
	if tank=="Premix 2C":
		volum=l*1.96
	if tank=="premix 2B":
		volum=l*96
	if tank=="Premix 2a":
		volum=l*1.9
	if tank=="Reserve 1":
		volum=l*3.7
	if tank=="Reserve 2":
		volum=l*3.53
	if tank=="Reserve 3":
		volum=l*3.7
	if tank=="Reserve 4":
		volum=l*3.53
	st.write(volum)