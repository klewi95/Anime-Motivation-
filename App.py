import streamlit as st

def main():
    # Basic page configuration
    st.set_page_config(page_title="Anime Motivation", page_icon="✨")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Workout Motivation", "Mental Training"])
    
    # Main content
    if page == "Home":
        show_home()
    elif page == "Workout Motivation":
        show_workout()
    elif page == "Mental Training":
        show_mental()

def show_home():
    st.title("Anime Motivation")
    st.write("Find your inspiration through classic anime scenes")
    
    # Featured section
    st.header("Featured Scene")
    st.video("https://youtu.be/PLACEHOLDER_URL")  # Replace with actual YouTube URL
    st.write("Dragon Ball Z - Goku's First Super Saiyan Transformation")
    st.write("An iconic moment of breaking past limits when pushed to the absolute edge.")
    
    # Recent additions
    st.header("Recent Additions")
    with st.expander("View Recent Scenes"):
        st.write("• Naruto - Rock Lee vs Gaara")
        st.write("• Hajime no Ippo - Catching Leaves Training")
        st.write("• My Hero Academia - Deku's First One For All")

def show_workout():
    st.title("Workout Motivation")
    
    # Category selector
    category = st.selectbox(
        "Choose category",
        ["Training Montages", "Fight Scenes", "Sports Anime"]
    )
    
    if category == "Training Montages":
        st.subheader("Best Training Montages")
        st.video("https://youtu.be/PLACEHOLDER_URL1")
        st.write("Rocky-style training from various anime")
        
    elif category == "Fight Scenes":
        st.subheader("Epic Fight Scenes")
        st.video("https://youtu.be/PLACEHOLDER_URL2")
        st.write("Most intense anime battles")
        
    elif category == "Sports Anime":
        st.subheader("Sports Motivation")
        st.video("https://youtu.be/PLACEHOLDER_URL3")
        st.write("Best moments from sports anime")

def show_mental():
    st.title("Mental Training")
    
    # Mental training categories
    st.subheader("Choose Your Motivation")
    tab1, tab2, tab3 = st.tabs(["Never Give Up", "Overcome Fear", "Determination"])
    
    with tab1:
        st.video("https://youtu.be/PLACEHOLDER_URL4")
        st.write("Scenes about perseverance")
        
    with tab2:
        st.video("https://youtu.be/PLACEHOLDER_URL5")
        st.write("Conquering your fears")
        
    with tab3:
        st.video("https://youtu.be/PLACEHOLDER_URL6")
        st.write("Unbreakable spirit moments")

if __name__ == "__main__":
    main()
