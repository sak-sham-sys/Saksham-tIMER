import streamlit as st
import time

st.title(" Streamlit Pomodoro Gondal Timer ")

work_time=st.slider("work time(minutes)",5,90,25)
break_time=st.slider("break time(minutes)",1,30,5)

def pomodoro_timer(work_time,break_time):
    work_seconds=work_time*60
    break_seconds=break_time*60

    work_placeholder=st.empty()
    break_placeholder=st.empty()

    work_placeholder.write("work!")
    for i in range(work_seconds):
        time.sleep(1)

        work_placeholder.write(f"{work_seconds -1} seconds left")

        break_placeholder.write("Break!")
        for i in range(break_seconds):
            time.sleep(1)
            break_placeholder.write(f"{break_seconds - i} seconds left")

if st.button("Start Timer"):
            pomodoro_timer(work_time,break_time)
