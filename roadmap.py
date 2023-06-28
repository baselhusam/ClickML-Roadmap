import streamlit as st

def new_line(n=1):
    for i in range(n):
        st.markdown('\n')

def app():

    # Logo
    col1, col2, col3 = st.columns([0.1,1,0.1])
    col2.image("assets/logo.png")
    new_line(3)

    # Title
    st.title("🗺️ ClickML Roadmap")

    # Description
    st.markdown(
        """
        This is a roadmap for the ClickML project. It will shows the current status of the project and the future work that needs to be done.
        Please feel free to contact us if you have any questions, comments, or suggestions.
        """
    )

    # Roadmap
    st.markdown(
        """
        <br>

        ##### ☄️ Deep Learning tab →  ``` 🧪 Planning ```    
        With this tab, you will be able to train a deep learning model with your data. 
        You will be able to do all the customizations that you want, from the number of layers to the optimizer.
        
        <br>

        ##### 🍞 Hyperparameter Tuning  →  ``` 👷 development ```
        With this feature, you will be able to understand what is hyperparameter tuning of your model
        and how to do it with your data. You will see it with some  examples and a tutorial of some algorithms.
        
        <br>

        ##### 🏖️ AI tab →  ``` ✍ Studying ```
        Develop an AutoML module that automatically analyzes the dataset, selects the appropriate machine 
        learning algorithms, performs feature engineering, and optimizes hyperparameters to generate the 
        best-performing models.

        <br>

        ##### 💎 Auto Feature Selection →  ``` 🧪 Planning ```
        With this feature, you will be able to select the best features for your model automatically.
        Some of the techniques that will be used are: Filter methods, Wrapper methods, Embedded methods.

        <br>

        ##### 🎫 Data Engineering tab →  ``` ✍ Studying ```
        With this tab, you will be able to do all the data engineering that you want. Also, you will be able to 
        make data visualization for your data to put in on your Presentation.

        <br>

        ##### ⏳ Time Series tab →  ``` 🧪 Planning ```
        With this tab, you will be able to do all the time series analysis that you want. Also, you will be able
        to build a time series model with your data with the time-series techniques like Windowing, etc.

        <br>

        ##### 📜 Create a summary PDF of the process →  ``` 🧪 Planning ```
        With this feature, you will be able to create a summary PDF of the process that you have done with your data.
        This PDF will be useful for your presentation and you will be able to download it and share it with your team.

        <br>

        ##### 🐋 Create a Docker Image for ClickML →  ``` 🧪 Planning ```
        With this feature, you will be able to use the ClickML app without installing it by using Docker 
        for the ClickML Docker Image. 

        """
    , unsafe_allow_html=True)
    new_line(2)


    # Contact
    st.markdown(
        """
        ## 📩 Contact

        If you have any questions, comments, or suggestions, then please feel free to contact me.

        - [GitHub](https://github.com/baselhusam/ClickML)
        - [LinkedIn](https://www.linkedin.com/company/clickml/?viewAsMember=true)
        - [Email](baselmathar@gamil.com)

        Visit the [**ClickML**](https://clickml.streamlit.app) website for more information.
        

        ## 🗺️ ClickML Roadmap
        This is a roadmap for the ClickML project. It will shows the current status of the project and the future work that needs to be done.
        Visit the [**ClickML Roadmap**](https://clickml.streamlit.app/roadmap) for more information.
        """

    )

    # Footer
    st.markdown(
        """
        ---
        Made with ❤️ by [**Basel**](https://www.linkedin.com/in/basel-mather/)
        """

    )

    # Hide footer
    hide_footer_style = """


        <style>
        footer {visibility: hidden;}
        </style>

        """
    st.markdown(hide_footer_style, unsafe_allow_html=True)

if __name__ == "__main__":
    app()