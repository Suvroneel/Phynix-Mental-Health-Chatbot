from streamlit_gsheets import GSheetsConnection
import streamlit as st

from streamlit_gsheets import GSheetsConnection
import pandas as pd

# google sheets

def gsheet_insert(name, email, msg, emotion, risk, timestamp):
    conn = st.connection("gsheets", type=GSheetsConnection)
    existing_data = conn.read(worksheet="User_Messages", usecols=list(range(7)), ttl=5)
    Messages = [{
        "user_name": name,
        "user_email": email,
        "messages": msg,
        "predicted_emotions": emotion,
        "risks": risk,
        "created_at": timestamp
    }]
    # Convert Messages (list of dicts) to a DataFrame
    Messages_df = pd.DataFrame(Messages)

    # Ensure columns match in case GSheet has more columns
    Messages_df = Messages_df[existing_data.columns]

    # Concatenate
    updated_df = pd.concat([existing_data, Messages_df], ignore_index=True)
    # Update Google Sheets
    conn.update(worksheet="User_Messages", data=updated_df)

def final_response(name, email, msg, emotion, risk, timestamp,supportive_reply):
    final_response = f"""
            {timestamp}

            {name} : {msg}

            **Predicted Emotion:** {emotion}

            **Risk Level:** {risk}

            {supportive_reply}
            """

    st.session_state.messages.append({"role": "assistant", "content": final_response})

