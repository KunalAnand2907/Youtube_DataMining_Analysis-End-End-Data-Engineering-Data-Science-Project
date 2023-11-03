import streamlit as st
import firebase_admin
from firebase_admin import firestore

def app():
   if 'db' not in st.session_state:
      st.session_state.db = ""

   # Creating firestore client
   db = firestore.client()
   st.session_state.db = db

   # Part 1 -
   ph = ''
   # When user is not Logged In
   if st.session_state.username == '':
      ph = 'Login to be able to Post !!'
   else:
      ph = 'Post Your Thoughts'
   post = st.text_area(label=' :orange[+ New Post]', placeholder=ph, height=None, max_chars=500)
   if st.button('Post',use_container_width = 20):
      if post!='':
         info = db.collection('Posts').document(st.session_state.username).get() # First get the Username ~ Document
         if info.exists:
            info = info.to_dict()
            # when there exist a Post done by the user previously
            if 'Content' in info.keys():
               pos = db.collection('Posts').document(st.session_state.username)
               pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(post)])})
            else: # if there is no post that the user did previously ~ Mean Doc/Username exist but there is no Content
               data  = {"Content":[post],'Username':st.session_state.username}
               db.collection('Posts').document(st.session_state.username).set(data) #updating the Firestore Db
         else: # when info doesn't exists ~ means for the user's in Authenticatiin there Posts are not there, so adding that also
            data = {"Content": [post], 'Username': st.session_state.username}
            db.collection('Posts').document(st.session_state.username).set(data)
         st.success('Post uploaded!!')

   st.header(' :violet[Latest Posts] ')

   # Part 2 - getting the post's already posted and showing it on Home Page of the Website
   docs = db.collection('Posts').get()
   for doc in docs:
      d = doc.to_dict() # converting each object into dict
      print("d:",d)
      try:
         st.text_area(label=':green[Posted By:] '+':orange[{}]'.format(d['Username']),value = d['Content'][-1],height=20) # -1 for most recent posts
      except:
         pass







