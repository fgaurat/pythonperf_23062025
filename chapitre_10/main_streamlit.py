import streamlit as st
from CustomerDAO import CustomerDAO

# streamlit run main_streamlit.py
def main():

    st.set_page_config(layout="wide")

    st.write("""# Ceci est un titre de niveau 1
## Ceci est un titre de niveau 2
ceci est une liste:
- Python
- Streamlit             
- Jupyter             
""")
    
    title = st.text_input("Movie title", "Life of Brian")
    if st.button('Ok'):
        st.write("The current movie title is", title)

    dao = CustomerDAO('customers.db')
    customers = dao.find_all()
    st.table(customers)

if __name__ == '__main__':
    main()