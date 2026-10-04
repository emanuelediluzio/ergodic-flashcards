import streamlit as st
import os
import srs_engine
import llm_generator

st.set_page_config(page_title="Ergodic Flashcards", layout="centered")

st.title("📚 Ergodic Flashcards")
st.markdown("A private Spaced Repetition System powered by LLMs, bypassing the need for external platforms.")

# Sidebar for Navigation
page = st.sidebar.radio("Navigation", ["Study", "Generate Flashcards", "Database Stats"])

if page == "Study":
    st.header("Study Mode")
    
    due_cards = srs_engine.get_due_cards()
    
    if not due_cards:
        st.success("🎉 You're all caught up for today! No due cards.")
    else:
        st.info(f"You have {len(due_cards)} cards due for review.")
        
        # Take the first due card
        card = due_cards[0]
        
        st.markdown("---")
        st.subheader("Question:")
        st.markdown(card['question'])
        
        # State to track if answer is shown
        if "show_answer" not in st.session_state:
            st.session_state.show_answer = False
            
        if not st.session_state.show_answer:
            if st.button("Show Answer"):
                st.session_state.show_answer = True
                st.rerun()
        else:
            st.markdown("---")
            st.subheader("Answer:")
            st.markdown(card['answer'])
            
            st.markdown("---")
            st.write("How well did you remember this?")
            col1, col2, col3, col4 = st.columns(4)
            
            # Map buttons to SM-2 qualities
            # 0: Blackout, 2: Hard, 4: Good, 5: Easy
            if col1.button("0 - Blackout (Again)", use_container_width=True):
                srs_engine.update_card(card['id'], 0)
                st.session_state.show_answer = False
                st.rerun()
            if col2.button("2 - Hard", use_container_width=True):
                srs_engine.update_card(card['id'], 2)
                st.session_state.show_answer = False
                st.rerun()
            if col3.button("4 - Good", use_container_width=True):
                srs_engine.update_card(card['id'], 4)
                st.session_state.show_answer = False
                st.rerun()
            if col4.button("5 - Easy", use_container_width=True):
                srs_engine.update_card(card['id'], 5)
                st.session_state.show_answer = False
                st.rerun()

elif page == "Generate Flashcards":
    st.header("Generate from PDF (Manuscript Notes)")
    st.markdown("Upload your handwritten notes in PDF format. The LLM will extract relevant definitions and theorems into LaTeX flashcards.")
    
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    
    if uploaded_file is not None:
        if st.button("Generate Flashcards"):
            with st.spinner("Extracting content..."):
                # Save temp file
                temp_path = "temp_upload.pdf"
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                cards = llm_generator.extract_flashcards_from_pdf(temp_path)
                
                if cards:
                    srs_engine.add_multiple_flashcards(cards)
                    st.success(f"Successfully generated and added {len(cards)} flashcards!")
                    st.balloons()
                else:
                    st.error("Failed to generate flashcards.")
                    
                if os.path.exists(temp_path):
                    os.remove(temp_path)

elif page == "Database Stats":
    st.header("Database Stats")
    db = srs_engine.load_db()
    st.write(f"Total Flashcards: {len(db)}")
    
    if db:
        st.dataframe(db)
