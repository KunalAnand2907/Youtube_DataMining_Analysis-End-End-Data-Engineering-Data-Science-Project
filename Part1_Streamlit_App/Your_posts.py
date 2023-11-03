import streamlit as st
import firebase_admin
from firebase_admin import firestore

def app():
   db = firestore.client()

   try:
      # get the posts for specific Username
      result = db.collection('Posts').document(st.session_state['username']).get()
      r = result.to_dict()
      content = r['Content']

      def delete_post(k):
         c = int(k)
         h = content[c]
         try:
            db.collection('Posts').document(st.session_state['username']).update({"Content": firestore.ArrayRemove([h])}) # remove the Content at specific index
            st.warning('Post Deleted')
         except:
            st.write('Something went Wrong..') # if post was not available
      for c in range(len(content)-1,-1,-1): # Latest  Posts -> Previous Posts
         st.text_area(label='',value=content[c]) # heading of text Box as None
         st.button('Delete Post',on_click = delete_post,args =([c]),key=c)

   except: # username is None
      if st.session_state.username == '':
         st.markdown('**Please Login first** 🔐')