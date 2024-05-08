import streamlit as st

st.title ('Trà sữa CoTAI')
col1, col2 = st. columns (2)
with col1:
  st.image('https://i.imgur.com/lEpdPsT.jpeg')

with col2:
  radio = st. radio (label='Kích cỡ', options=('Nhỏ (30K)', 'Vừa (40K)', 'Lớn (50K)'), horizontal= True)
  st.text('Thêm')
  col3, col4 = st. columns (2)
  with col3:
    check1 = st.checkbox('Sữa (5K)')
    check2 = st.checkbox('Cà phê (8K)')
  with col4:
    check3 = st.checkbox('Kem (10K)')
    check4 = st.checkbox('Trứng (15K)')

col5, col6 = st. columns (2)
with col5:
  option = st.multiselect('Topping', ['Trân châu trắng (5K)','Trân châu đen (5K)','Thạch rau câu (6K)','Vải (7K)','Nhãn (8K)','Đào (10K)'])
with col6:
  number = int(st.number_input('Số lượng',min_value=1, step=1))

textarea = st.text_area('Ghi chú')

if st.button('Đặt hàng',use_container_width= True): 
    st.subheader('Thông tin đơn hàng')
    if 'Nhỏ (30K)' in radio:
      st.write('Cỡ nhỏ')
    if 'Vừa (40K)' in radio:
      st.write('Cỡ vừa')
    if 'Lớn (50K)' in radio:
      st.write('Cỡ lớn')    
    
    st.write('Thêm:')
    bonus = 0
    if check1:
      st.write('Sữa (5K)')
      bonus += 5
    if check2:
      st.write('Cà phê (8K)')
      bonus += 8
    if check3:
      st.write('Kem (10K)')
      bonus += 10
    if check4:
      st.write('Trứng (15K)')
      bonus += 15
    
    st.write('Topping:')
    topping_money = 0  
    if "Trân châu trắng (5K)" in option:
      st.write('Trân châu trắng (5K)')
      topping_money += 5
    if "Trân châu đen (5K)" in option:
      st.write('Trân châu đen (5K)')
      topping_money += 5  
    if "Thạch rau câu (6K)" in option:
      st.write('Thạch rau câu (6K)')
      topping_money += 6
    if "Vải (7K)" in option:
      st.write('Vải (7K)')
      topping_money += 7  
    if "Nhãn (8K)" in option:
      st.write('Nhãn (8K)')
      topping_money += 8
    if "Đào (10K)" in option:
      st.write('Đào (10K)')
      topping_money += 10    

    st.write(f'Ghi chú: {textarea}')
    st.write(f'Số lượng: {number}')

    size_money=0
    if radio == "Nhỏ (30K)":
      size_money = 30
    elif radio == "Vừa (40K)":
      size_money= 40  
    elif radio == "Lớn (50K)":
      size_money = 50
    
    sum_money=(size_money + bonus + topping_money) * number
    st.write(f'Thành tiền: {sum_money}K')

